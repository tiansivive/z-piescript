---
tags: [data, types, row-types, open, problem, exploration]
refs:
  - thread:data-completeness
  - session:2026-05-07-dynamic-fields-discussion
---
# Dynamic Field Types

`use "name" as idx` derives the row type from the merged `_field_caps` view.
Fields missing from that view — sparse fields mapped in some backing indices
but not all, or fields the user knows exist but field caps doesn't surface —
can't be referenced in piescript programs.

Concrete trigger: `kibana.alert.risk_score` on `.alerts-security` is absent
from the merged view because some backing data-stream indices don't map it,
which blocks the risk-scoring example.

Two paths considered: [[unmapped-field-surfacing.data]] (auto-surface
partial-mapping fields) and [[use-with-annotations.data]] (user-supplied row
extension on `use`). Sparse-only is solvable with existing ES infrastructure;
user-supplied is needed for the general case.

**Depends on**: [[field-caps-resolution.data]], [[row-polymorphism.types]]
**Enables**: (none directly — problem statement)
**Connections**:
- part-of: [[data-completeness.thread]]
- contrasts-with: [[dynamic-index-names.data]] — sibling "dynamic": index names vs field set
- related: [[mapping-update-failure.obstacle]] — write-side counterpart
- related: [[empty-mapping-diagnostics.data]] — adjacent diagnostic gap
- solved-by: [[unmapped-field-surfacing.data]] (sparse case)
- solved-by: [[use-with-annotations.data]] (general case)
