---
tags: [infrastructure, serialization, mobility, recursion, implemented]
refs:
  - plan:recursion_phase1
  - session:recursion-closeout
  - code:ValueSerialization.java
  - test:SerializationRoundTripTests.java
---
# Closure Cycle Detection in Serialization

`ValueSerialization` applies [[reference-table-encoding.technique]] to
[[closure-val.language|ClosureVal]] so recursive closures survive the wire. The
captured environment is a `Value[]` that [[tying-the-knot.technique]] mutates to
point at the closure itself (or, for mutual recursion, at a sibling that points
back). Without cycle handling, a naive write loops and a naive read never
reconstructs the back-edge.

Only `ClosureVal` is identity-tracked: the writer keys an
`IdentityHashMap<ClosureVal, Integer>`; the reader allocates the closure with an
empty `Value[]` env, registers it, then fills the env in place. Other shared
sub-values (records, lists) have value semantics and are duplicated on the wire.

Verified by `SerializationRoundTripTests.testValueClosureSelfCycleRoundTrip` and
`testValueClosureMutualCycleRoundTrip`.

**Depends on**: [[serialization.infrastructure]], [[closure-val.language]], [[reference-table-encoding.technique]]
**Enables**: [[recursive-closure-shipping.coordination]], [[code-mobility.coordination]]
**Connections**:
- part-of: [[serialization.infrastructure]]
- implements: [[reference-table-encoding.technique]] — applied to ClosureVal
- complements: [[tying-the-knot.technique]] — wire-side counterpart to the runtime backpatch
- enables: [[recursive-closure-shipping.coordination]]
- constrained-by: [[serialization-boundary.infrastructure]] — only serializable variants; SearcherVal/DocRefVal/WriterVal/PageVal still throw
- validated-by: [[cross-node-testing-layers.principle]]
