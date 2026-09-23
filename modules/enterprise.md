# Enterprise rules and enforcement

Use for organization policy, regulated context or policy uncertainty. This module
organizes engineering obligations; it does not certify regulatory compliance.

## Policy intake

For each applicable rule record ID, source/version, scope, owner, obligation,
required evidence, enforcing system and exception process. Discover approved
sources already in scope: repository instructions, policy repositories, CI,
CODEOWNERS and authorized team records. Missing access is `unknown`, not a waiver.

Consider data classification/retention, approved tools and model endpoints,
dependency/license rules, secrets, network access, review/separation of duties,
auditability, release controls, incident handling and artifact provenance when
relevant. Do not infer a company's policy from an industry label.

## Compose and apply

- Apply the host's instruction hierarchy and actual policy scope. Organization
  controls constrain how authorized work is done; exec-ctrl fills gaps.
- Use [POLICY_INVENTORY.md](../templates/v2/POLICY_INVENTORY.md) or existing records.
  Optional [ruleset JSON](../examples/v2/team-rules.json) adds required modules and
  named evidence gates to the helper; it cannot remove baseline controls.
- Validate rule provenance with the responsible source. A syntactically valid
  JSON file is not proof that an organization approved its contents.
- Hold only actions affected by unresolved mandatory rules. Make the specific
  missing source or required decision visible while continuing allowed work.
- Exceptions need authorized approver, scope, expiry and compensating control.
  Keep the original rule visible. The preview helper does not process waivers;
  use the organization's review process for such decisions.

## Evidence and gate

`enterprise-policy`: applicable rule inventory, disposition and evidence mapping.
Map real enforcement to branch protection, CI, IAM, environment approval or another
named control. Label prose-only guidance advisory. Do not claim the helper enforces
permissions, discovers every rule, or verifies an approver's identity.
