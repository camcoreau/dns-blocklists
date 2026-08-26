# CamCore DNS Policy

This directory contains the CamCore-owned policy, validation and publishing layer for **CamCore – Cameron Family Secure Network**.

The default production model is intentionally minimal: one approved upstream source, one generated CamCore production feed, and exact local exceptions only where required.

## Authoritative files

| Path | Purpose |
| --- | --- |
| `sources.json` | Machine-readable source manifest and production deployment state |
| `allowlist.txt` | Exact domains explicitly permitted by CamCore and removed from the generated feed |
| `denylist.txt` | Exact domains explicitly blocked by CamCore and added to the generated feed |
| `tools/publish_blocklist.py` | Builds the CamCore production feed from approved source material and local policy |
| `tools/validate_repository.py` | Offline repository and policy validator |
| `tools/check_sources.py` | Read-only production source-health check |
| `tests/` | Unit tests for CamCore DNS validation and policy controls |

The generated repository-root `blocklist.txt` is a production output and must not be edited manually.

## Source states

A source entry in `sources.json` uses explicit governance states:

- `active` — approved for the deployment state recorded in the source entry;
- `under-review` — evaluation only and not production-approved; and
- `retired` — retained for history or rollback reference and not approved for current deployment.

Only a source with both `status: active` and `deployment: production` forms part of the current CamCore production baseline.

## Current baseline

The current manifest defines **HaGeZi Multi NORMAL** as the active upstream source material used to generate the CamCore production blocklist.

**StevenBlack Unified Hosts** is retained as a retired historical baseline and must not be treated as an active production source unless the manifest is deliberately changed through CamCore change control.

## Local domain-entry format

Use one exact domain per line:

```text
example.com
subdomain.example.net
```

Entries must:

- use lower-case ASCII or valid IDNA/punycode;
- omit `http://`, `https://`, paths, ports and trailing dots;
- avoid wildcards, Adblock syntax, regular expressions, IP addresses and hosts-file rows;
- remain sorted;
- remain unique within the file; and
- be justified in the change record rather than with trailing inline comments.

Blank lines and full-line comments beginning with `#` are permitted.

An empty local list is valid and preferred when no CamCore-specific exception is required.

## Change standard

A local allow or deny entry should exist only when there is a specific operational or security reason that cannot be handled more appropriately upstream.

Before a production policy change is merged:

1. establish the evidence and expected effect;
2. make the smallest policy change required;
3. run the unit tests and repository validator;
4. define the rollback path; and
5. follow the staged resolver deployment process in [`../docs/OPERATIONS.md`](../docs/OPERATIONS.md).

For upstream governance and attribution, see [`../docs/UPSTREAM.md`](../docs/UPSTREAM.md).
