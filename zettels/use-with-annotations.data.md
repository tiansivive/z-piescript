---
tags: [data, types, row-types, language, syntax, open, concept, needs-design]
refs:
  - thread:data-completeness
---
# Use With Annotations

Extend `use` syntax: `use "idx" as i with { kibana.alert.risk_score: Double }`.
The annotation row merges with the field-caps row via the existing `&`
[[row-operators.types|row operator]] (right-biased).

At elaboration, four cases by (annotated × in-caps × type-matches):
trust the user when not in caps, warn when redundant, error or override on
type mismatch.

Optional verification at three depths:
1. `_field_caps include_unmapped=true` — confirms the field is mapped in
   some backing index. Cheap, metadata only.
2. `_search` with `exists` filter — confirms documents actually carry the
   field. Catches "mapped but never written" cases.
3. `_search size:1` sample — fetches a real value and checks its JSON type
   matches the annotation. Catches type lies.

Open: spelling for nested fields (dotted-path desugaring vs literal nested
records); error-vs-warn on type mismatch; which verification depth to run
by default; how to cache results.

**Depends on**: [[row-operators.types]], [[use-declarations.data]]
**Enables**: (none directly)
**Connections**:
- solves: [[dynamic-field-types.data]] (general case)
- contrasts-with: [[unmapped-field-surfacing.data]] — user-declared vs automatic
- uses: [[row-operators.types]] — `&` is the merge mechanism
- extends: [[use-declarations.data]] — adds `with { ... }` clause
- tension-with: [[null-as-bottom.types]] — verification absence → what type? feeds the unsettled null-vs-Maybe story
