---
tags: [data, types, row-types, open, concept, needs-design]
refs:
  - thread:data-completeness
  - code:IndexResolutionPrePass.java
---
# Unmapped Field Surfacing

Surface fields present in some backing indices but absent from the merged
field-caps view, by passing `include_unmapped=true` (or
`trackUnmappedFieldIndices=true` on `IndexResolver.resolveMainIndicesVersioned`)
and adding the result to the row.

Open: type partial-mapping fields as `Maybe T` (forces absence handling)
or as `T` (escape hatch). Same decision applies broadly to nullable values
in piescript — currently unsettled, see [[null-as-bottom.types]].
Memory cost behind the opt-in flag (ESQL #145991 made it opt-in to dodge
OOMs on large clusters).

Resolves the dead `partiallyUnmappedFields` queue entry — path A would
populate the field instead of dropping it.

**Depends on**: [[field-caps-resolution.data]]
**Enables**: (none directly)
**Connections**:
- solves: [[dynamic-field-types.data]] (sparse case only)
- contrasts-with: [[use-with-annotations.data]] — automatic vs user-declared
- uses: [[row-polymorphism.types]] — surfaced fields land in the open row
- tension-with: [[null-as-bottom.types]] — Maybe T vs T feeds into the broader null story
