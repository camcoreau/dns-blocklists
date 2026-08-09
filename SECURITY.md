# Security Policy

## Reporting a security issue

Do not open a public GitHub issue containing sensitive information.

Report a vulnerability affecting CamCore-owned policy, tooling or documentation through:

- CamCore Support: https://camcore.au/support.html
- Email: help@camcore.au

Include a clear description, affected file or workflow, reproduction steps where safe, expected impact and any proposed mitigation. Do not include passwords, tokens, private keys, resolver exports, query logs or personal data.

## Scope

CamCore maintains:

- Files under `camcore/`.
- CamCore documentation under `docs/`.
- CamCore-named GitHub Actions workflows.
- The CamCore-specific repository README and contribution policy.

The inherited HaGeZi blocklists and upstream source material are maintained by their original project. Confirm and report upstream data defects through the upstream project's published process.

## DNS false positives

A false positive is normally an operational filtering issue rather than a software vulnerability. Investigate it first, identify the exact blocked domain and submit a CamCore Support request with non-sensitive evidence.

Do not publish private query logs or client details.

## Supported version

Only the current default branch is maintained as the approved CamCore repository state.
