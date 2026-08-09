## Change

Describe the exact DNS policy, local-list, documentation or automation change.

## Reason and evidence

Explain the specific problem or security requirement. Do not include private query logs, client data, credentials or internal inventories.

## Risk and impact

Describe expected impact on internet access, Microsoft 365, NetBird and CamCore services.

## Validation

- [ ] I kept the minimal-list policy unless this change contains an explicitly approved source evaluation.
- [ ] I used exact domains and investigated the cause before adding an exception.
- [ ] `python camcore/tools/validate_repository.py` passes.
- [ ] `python -m unittest discover -s camcore/tests -v` passes.
- [ ] I documented staged resolver testing where production behaviour changes.
- [ ] I documented a rollback method.
- [ ] I preserved upstream attribution and licence information.
- [ ] I recorded the operational change in CamCore Operations when required.

## Rollback

State exactly how the previous working DNS state will be restored.
