# Contributing to CamCore DNS Blocklists

This repository contains the DNS filtering policy and publishing controls used by **CamCore – Cameron Family Secure Network**.

CamCore accepts changes only when they solve a specific, evidenced operational or security requirement. The objective is not to maximise the number of blocked domains; it is to maintain a stable, explainable and low-risk DNS filtering baseline.

## Before proposing a change

Every production-facing change should identify:

- the problem being solved;
- the exact source or domain affected;
- supporting evidence;
- expected user and service impact;
- false-positive risk;
- validation steps; and
- a rollback method.

Do not add an additional blocklist simply to increase coverage statistics. New upstream sources require separate evaluation and explicit production approval.

## Allow-list changes

Before adding an entry to `camcore/allowlist.txt`:

1. Reproduce the affected service or application failure.
2. Confirm CamCore DNS filtering is the cause.
3. Identify the smallest exact domain required.
4. Determine whether the problem should be corrected upstream instead.
5. Assess the privacy or security effect of allowing the domain.
6. Test the exception on one resolver before wider deployment.

Broad parent-domain exceptions should be avoided unless the full domain scope is deliberately required and reviewed.

## Deny-list changes

Before adding an entry to `camcore/denylist.txt`:

1. Identify the security, privacy or operational requirement.
2. Confirm the exact domain and supporting evidence.
3. Check for legitimate or shared-hosting use.
4. Determine whether the entry belongs in the approved upstream source instead.
5. Assess likely false positives and user impact.
6. Test the change on one resolver before wider deployment.

## File rules

Entries in `camcore/allowlist.txt` and `camcore/denylist.txt` must be:

- one exact domain per line;
- lower-case;
- written without a scheme, path, port or trailing dot;
- free of wildcards, regular expressions, hosts-file rows and Adblock syntax;
- sorted in ascending lexical order;
- unique within the file; and
- supported by evidence in the change record rather than a trailing inline comment.

Blank lines and full-line comments beginning with `#` are permitted.

## Required validation

Run:

```sh
python -m unittest discover -s camcore/tests -v
python camcore/tools/validate_repository.py
```

The same controls run automatically through the CamCore validation workflow for changes targeting `main`.

## Production change record

A production-facing pull request should include:

- reason and evidence for the change;
- exact policy or source affected;
- expected service and user impact;
- resolver used for staged validation;
- verification results;
- rollback method; and
- the matching CamCore Operations record when operationally significant.

See [`docs/OPERATIONS.md`](docs/OPERATIONS.md) for staged deployment and rollback requirements.

## Upstream content

Do not directly edit inherited HaGeZi material to create a CamCore-specific exception.

CamCore production policy belongs in the files under `camcore/`. Upstream defects should be confirmed and reported through the upstream project's published process where appropriate.

Do not remove attribution, source references or licence information from third-party material.

See [`docs/UPSTREAM.md`](docs/UPSTREAM.md) for the full upstream governance model.

## Security and privacy

Never include credentials, private keys, tokens, resolver exports, DNS query logs, browsing information, client details, private infrastructure inventories or other sensitive operational data in an issue, commit or pull request.

Security reporting instructions are in [`SECURITY.md`](SECURITY.md).
