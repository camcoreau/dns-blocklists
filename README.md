# CamCore DNS Blocklists

[![Validate CamCore DNS policy](https://github.com/camcoreau/dns-blocklists/actions/workflows/camcore-validate.yml/badge.svg)](https://github.com/camcoreau/dns-blocklists/actions/workflows/camcore-validate.yml)
[![Source health](https://github.com/camcoreau/dns-blocklists/actions/workflows/camcore-source-health.yml/badge.svg)](https://github.com/camcoreau/dns-blocklists/actions/workflows/camcore-source-health.yml)
[![Licence: GPL-3.0](https://img.shields.io/badge/licence-GPL--3.0-blue.svg)](LICENSE)

Controlled DNS filtering policy, local exception lists and upstream source governance for **CamCore – Cameron Family Secure Network**.

> **CamCore is a privately owned and operated family technology network that delivers secure, reliable and professionally managed digital services for the Cameron household, Cameron-Media and associated family operations.**

**Built for Home. Engineered Like Enterprise.**

> [!IMPORTANT]
> **Production baseline:** CamCore resolvers use the single approved **StevenBlack Unified Hosts** source.
>
> HaGeZi is retained only as an **Under review** evaluation source. The original fork snapshot is isolated on the `upstream-hagezi` branch and is not CamCore production configuration.

## Purpose

This repository provides one reviewable location for:

- The approved CamCore DNS filtering source manifest.
- Deliberate local allow-list and deny-list entries.
- Offline validation and read-only source-health checks.
- DNS change, deployment and rollback procedures.
- Clear upstream attribution and fork-maintenance boundaries.

It does not replace the live Pi-hole configuration, resolver backups, CamCore Operations change records or approved documentation in CamCore Documentation.

## Current standard

| Component | State | Production use |
| --- | --- | --- |
| StevenBlack Unified Hosts | **Active** | Approved baseline source |
| CamCore local allow-list | **Active** | Empty unless a documented exception is required |
| CamCore local deny-list | **Active** | Empty unless a specific security or operational requirement is approved |
| HaGeZi Multi NORMAL | **Under review** | Evaluation only; not deployed |
| Additional third-party lists | **Not approved** | Require evidence, testing and rollback planning |

CamCore intentionally keeps DNS filtering minimal. Adding more lists is not automatically an improvement: larger combinations can break legitimate applications, increase false positives and make troubleshooting harder.

## Source of truth

The machine-readable policy is stored in [`camcore/sources.json`](camcore/sources.json).

CamCore-owned local entries are stored in:

- [`camcore/allowlist.txt`](camcore/allowlist.txt)
- [`camcore/denylist.txt`](camcore/denylist.txt)

Only exact, lower-case domain names are accepted. URLs, IP addresses, wildcards, hosts-file rows and comments appended to an entry are rejected by automated validation.

## Repository structure

| Path or branch | Purpose | Authority |
| --- | --- | --- |
| `main` | Small CamCore governance and curation layer | Authoritative repository state |
| `camcore/` | Source manifest, local lists, tests and tools | Authoritative DNS policy |
| `docs/` | Operations, repository settings and upstream governance | Authoritative procedures |
| `.github/workflows/camcore-*` | Read-only validation and source-health automation | Approved automation only |
| `upstream-hagezi` | Historical HaGeZi fork snapshot | Provenance and controlled reference only |

Do not deploy a list merely because it exists in the archive branch or an upstream repository. Production resolvers should consume only active production records in `camcore/sources.json` and reviewed local exceptions.

## Change control

Every production DNS filtering change should:

1. State the problem or security requirement being addressed.
2. Identify the exact source or domain entry being proposed.
3. Confirm that the issue was investigated before creating an allow-list exception.
4. Assess impact on internet access, Microsoft 365, NetBird and CamCore services.
5. Include a backup and rollback method.
6. Pass repository validation.
7. Be tested on one resolver before both resolvers are changed.
8. Be verified on both resolvers after deployment.
9. Be recorded in CamCore Operations when operationally significant.

Detailed procedures are in [`docs/OPERATIONS.md`](docs/OPERATIONS.md).

## Automated validation

The `Validate CamCore DNS policy` workflow checks:

- Required governance and operational files.
- The exact approved production-source identity and endpoint.
- Unique source identifiers and valid HTTPS source URLs.
- Allowed source and deployment states.
- Domain syntax, normalisation, sorting and duplicates.
- Conflicts between the local allow-list and deny-list.
- Protection of CamCore-owned namespaces from accidental local blocking.
- Removal of inherited write-enabled upstream automation from `main`.
- Read-only workflow permissions and commit-SHA-pinned actions.
- Common secret and private-key patterns in CamCore-owned files.
- Unit tests for the validator and source parser.

Run locally from the repository root:

```sh
python camcore/tools/validate_repository.py
python -m unittest discover -s camcore/tests -v
```

The separate source-health workflow confirms that each approved production source is reachable and contains plausible data. It does not publish, mirror or silently replace blocklists.

## Deployment

This repository is a configuration and governance source of truth. Production resolvers should consume only the active source entries approved in `camcore/sources.json`, together with reviewed local exceptions.

Never make an unrecorded bulk list change on both resolvers at once. Follow the staged deployment, verification and rollback process in [`docs/OPERATIONS.md`](docs/OPERATIONS.md).

## Security and privacy

This repository is public. Do not commit:

- Passwords, API tokens, credentials or private keys.
- Resolver exports, backups, query logs or client data.
- Internal IP addresses or sensitive host inventories.
- Personal browsing history or screenshots containing private information.
- Unreviewed domain dumps copied from live systems.

Security reporting instructions are in [`SECURITY.md`](SECURITY.md).

## Upstream attribution

This repository originated as a fork of [HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists). The inherited snapshot is preserved on `upstream-hagezi`; its original material and licence remain the work of HaGeZi and its contributors.

CamCore does not claim authorship of that material, does not provide upstream support for it and does not treat the archive branch as production approval. See [`NOTICE.md`](NOTICE.md) and [`docs/UPSTREAM.md`](docs/UPSTREAM.md).

## Support

For a CamCore DNS issue or approved change request, use the [CamCore Support page](https://camcore.au/support.html) or email `help@camcore.au`.

False positives or source errors within HaGeZi or StevenBlack material should first be confirmed and then reported to the relevant upstream project using its published process.

## Ownership

This repository is maintained as part of the private CamCore Network. Significant production changes should be reviewed, tested and recorded through CamCore Operations.
