# Recommended GitHub Repository Settings

These settings complete the CamCore standard around the version-controlled files in this repository.

## General

- Default branch: `main`.
- Keep `upstream-hagezi` as the read-only provenance branch.
- Do not use GitHub's automatic fork synchronisation to merge upstream content into `main`.
- Suggested description: `Governed DNS filtering policy and source-health checks for CamCore.`
- Suggested topics: `camcore`, `dns`, `pihole`, `blocklist`, `security`.

## Branch protection for `main`

- Require changes through a pull request.
- Require the `Validate policy, local lists and tests` status check.
- Require conversation resolution before merging.
- Block force pushes and branch deletion.
- Keep administrator bypass available only for documented emergency recovery.
- Do not require an external approval when CamCore has only one repository maintainer; rely on the required validation check and documented change control instead.

## Actions

- Set default workflow permissions to read repository contents only.
- Do not allow Actions to create or approve pull requests.
- Require approval before workflows from untrusted outside contributors can run.
- Keep only CamCore-named workflows on the default branch.

## Security

- Enable Dependabot alerts and security updates.
- Enable secret scanning and push protection when available.
- Review code-scanning and dependency alerts through CamCore Operations.
- Never publish resolver exports, query logs, credentials, internal inventories or personal browsing data.

## Merge policy

- Prefer squash merging for small policy changes.
- Use clear conventional commit subjects such as `fix(dns): allow required authentication domain`.
- Delete ordinary feature branches after merge.
- Never delete `upstream-hagezi` as part of automatic branch cleanup.
