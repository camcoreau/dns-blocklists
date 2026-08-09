# Upstream Governance and Attribution

## Origin

`camcoreau/dns-blocklists` originated as a GitHub fork of `hagezi/dns-blocklists`.

The inherited generated lists, source documentation, category definitions and original automation were created by HaGeZi and its contributors. CamCore retains the upstream `GPL-3.0` licence and does not claim authorship of that material.

## Branch separation

The default `main` branch is the small CamCore-owned governance and curation layer.

The `upstream-hagezi` branch preserves the original fork snapshot for provenance and controlled reference. It is not an approved list mirror, deployment branch or support channel.

The archive branch must not be merged into `main`. CamCore policy should reference an upstream source through `camcore/sources.json` rather than copying the upstream-generated directory tree into the default branch.

## CamCore use

HaGeZi is currently an evaluation source only. Its presence in the manifest or archive branch does not mean:

- It is deployed on CamCore resolvers.
- CamCore has independently verified every entry.
- CamCore provides support for upstream list content.
- Every category is suitable for the CamCore environment.
- A larger list is preferred over the approved minimal baseline.

The current production source policy is defined only in `camcore/sources.json`.

## Reviewing future upstream changes

Upstream changes should be reviewed rather than blindly synchronised.

When refreshing the archive branch or evaluating a new upstream release:

1. Review the upstream commit range and release notes.
2. Update only the `upstream-hagezi` branch for provenance work.
3. Never merge inherited upstream workflows into `main`.
4. Check licence and source-documentation changes.
5. Reference the exact upstream version in any evaluation record.
6. Keep HaGeZi in an evaluation state unless a separate production change is approved.
7. Run the CamCore validator after any policy or documentation change.
8. Record production-impacting decisions in CamCore Operations.

## Inherited automation

The original fork snapshot contains workflows intended for the upstream maintainer, including issue labelling, release creation, CDN purging and workflow cleanup.

Those workflows are intentionally absent from `main`. They are not required to consume or evaluate upstream data and they grant broader write permissions than CamCore needs. The offline validator rejects their reintroduction to the default branch.

## Reporting upstream problems

Confirm the issue and collect only non-sensitive evidence. Use the upstream project's published reporting process for:

- Incorrect upstream entries.
- Missing upstream entries.
- Source-quality concerns.
- Format or generated-list defects.
- Upstream documentation errors.

Keep CamCore-specific policy, deployment details and local exceptions in CamCore-owned files and private operational systems.
