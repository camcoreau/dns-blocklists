# CamCore DNS Policy Files

This directory contains the CamCore-owned portion of the repository.

## Files

| Path | Purpose |
| --- | --- |
| `sources.json` | Approved and evaluated upstream-source manifest |
| `allowlist.txt` | Exact domains explicitly allowed by CamCore |
| `denylist.txt` | Exact domains explicitly denied by CamCore |
| `tools/validate_repository.py` | Offline policy and repository validator |
| `tools/check_sources.py` | Read-only production-source health check |
| `tests/` | Validator unit tests |

## Source states

- `active`: approved for the deployment state named in the source record.
- `under-review`: evaluation only; not production-approved.
- `retired`: retained for history and must not be deployed.

Only a source with both `status: active` and `deployment: production` is part of the production baseline.

## Domain-entry format

Use one exact domain per line:

```text
example.com
subdomain.example.net
```

Rules:

- Use lower-case ASCII or valid IDNA/punycode.
- Do not include `http://`, `https://`, a path, a port or a trailing dot.
- Do not use `*`, `||domain^`, regular expressions, IP addresses or hosts-file rows.
- Keep entries sorted.
- Put explanatory evidence in the change record, not in a trailing inline comment.
- Use a full-line `#` comment only for file guidance.

An empty local list is valid and preferred when no local exception is required.
