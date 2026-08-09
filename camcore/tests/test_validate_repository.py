from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS_DIR = REPO_ROOT / "camcore" / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import validate_repository as validator  # noqa: E402


class DomainValidationTests(unittest.TestCase):
    def test_accepts_exact_lower_case_domains(self) -> None:
        self.assertTrue(validator.is_valid_domain("example.com"))
        self.assertTrue(validator.is_valid_domain("sub-domain.example.net"))
        self.assertTrue(validator.is_valid_domain("xn--bcher-kva.example"))

    def test_rejects_non_domain_inputs(self) -> None:
        invalid = (
            "Example.com",
            "https://example.com",
            "example.com/path",
            "*.example.com",
            "||example.com^",
            "192.0.2.1",
            "localhost",
            "example.com.",
            " example.com",
            "example..com",
        )
        for value in invalid:
            with self.subTest(value=value):
                self.assertFalse(validator.is_valid_domain(value))

    def test_domain_file_detects_duplicates_and_sorting(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "list.txt"
            path.write_text(
                "# test\nz.example\na.example\na.example\n",
                encoding="utf-8",
            )
            entries, errors = validator.read_domain_entries(path)

        self.assertEqual(entries, ["z.example", "a.example", "a.example"])
        self.assertTrue(any("duplicate domain" in error for error in errors))
        self.assertTrue(any("must be sorted" in error for error in errors))


class UrlValidationTests(unittest.TestCase):
    def test_rejects_private_and_credential_bearing_urls(self) -> None:
        private_errors = validator.validate_public_https_url(
            "https://127.0.0.1/list.txt", "source"
        )
        credential_errors = validator.validate_public_https_url(
            "https://user:password@example.com/list.txt", "source"
        )
        self.assertTrue(any("non-public IP" in error for error in private_errors))
        self.assertTrue(
            any("embedded credentials" in error for error in credential_errors)
        )


class ManifestValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = json.loads(
            (REPO_ROOT / "camcore/sources.json").read_text(encoding="utf-8")
        )

    def validate_manifest_data(self, manifest: dict[str, object]) -> list[str]:
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "sources.json"
            path.write_text(
                json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            return validator.validate_manifest(path)

    def test_manifest_rejects_unapproved_production_source(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["sources"][0]["id"] = "unapproved-source"
        errors = self.validate_manifest_data(manifest)
        self.assertTrue(any("production source IDs must be exactly" in error for error in errors))

    def test_manifest_rejects_changed_production_endpoint(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["sources"][0]["url"] = "https://example.com/hosts"
        errors = self.validate_manifest_data(manifest)
        self.assertTrue(any("must use url=" in error for error in errors))

    def test_manifest_rejects_active_evaluation_source(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["sources"][1]["status"] = "active"
        errors = self.validate_manifest_data(manifest)
        self.assertTrue(any("requires deployment 'production'" in error for error in errors))


class WorkflowSecurityTests(unittest.TestCase):
    def test_rejects_tagged_action_and_write_permission(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            for relative in validator.WORKFLOW_PATHS:
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(
                    """name: test
on: workflow_dispatch
permissions:
  contents: write
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
""",
                    encoding="utf-8",
                )
            errors = validator.validate_workflow_security(root)

        self.assertTrue(any("read-only" in error for error in errors))
        self.assertTrue(any("40-character commit SHA" in error for error in errors))
        self.assertTrue(any("credentials must not persist" in error for error in errors))


class RepositoryValidationTests(unittest.TestCase):
    def test_forbidden_upstream_path_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            forbidden = root / ".github/workflows/release.yml"
            forbidden.parent.mkdir(parents=True, exist_ok=True)
            forbidden.write_text("name: unsafe\n", encoding="utf-8")
            errors = validator.validate_required_content(root)

        self.assertTrue(any("Forbidden upstream path" in error for error in errors))

    def test_current_repository_passes_offline_validation(self) -> None:
        self.assertEqual(validator.validate_repository(REPO_ROOT), [])


if __name__ == "__main__":
    unittest.main()
