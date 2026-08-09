# Contributing to CamCore DNS Blocklists

This repository is publicly visible because it is a fork, but its CamCore-owned policy is maintained for the private CamCore Network.

> **CamCore is a privately owned and operated family technology network that delivers secure, reliable and professionally managed digital services for the Cameron household, Cameron-Media and associated family operations.**

## Before proposing a change

A proposed DNS change must solve a specific, evidenced problem. Do not add a large list simply to increase the blocked-domain count.

For a local allow-list entry:

1. Reproduce the failure.
2. Confirm DNS filtering is the cause.
3. Identify the smallest exact domain required.
4. Check whether the problem belongs upstream.
5. Document the impact of allowing the domain.

For a local deny-list entry:

1. Identify the security or operational requirement.
2. Provide evidence that the exact domain should be blocked.
3. Check for legitimate use and likely false positives.
4. Prefer an authoritative upstream source when appropriate.
5. Document rollback and validation steps.

## File rules

Entries in `camcore/allowlist.txt` and `camcore/denylist.txt` must be:

- One exact domain per line.
- Lower-case.
- Written without a scheme, path, port or wildcard.
- Sorted in ascending lexical order.
- Unique within the file.
- Supported by a comment in the pull request, not an inline trailing comment.

Blank lines and full-line comments beginning with `#` are permitted.

## Required checks

Run:

```sh
python camcore/tools/validate_repository.py
python -m unittest discover -s camcore/tests -v
```

A production-facing pull request should also include:

- The reason and evidence for the change.
- Expected user and service impact.
- The resolver used for staged testing.
- Verification results.
- A rollback method.
- The matching CamCore Operations record when required.

## Upstream content

Do not edit inherited HaGeZi generated files to create a CamCore exception. Report upstream defects to the upstream project and keep CamCore-specific entries under `camcore/`.

Do not remove attribution, source headers or licence information from inherited material.

## Security

Never include credentials, private keys, resolver exports, query logs, client information, internal IP inventories or personal browsing data in an issue, commit or pull request.
