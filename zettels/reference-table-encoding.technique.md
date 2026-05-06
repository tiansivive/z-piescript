---
tags: [technique, serialization, concept]
refs: []
---
# Reference-Table Encoding

Wire encoding for object graphs that may contain cycles or share sub-objects by
identity. Each occurrence of a tracked object is prefixed with an `isDefinition`
flag plus a sequential id assigned on first sighting. Definitions write the full
payload; subsequent sightings write only the id as a back-reference.

The reader keeps a parallel id → object table. When a definition arrives, the
reader **constructs a shell first**, registers it under its id, **then** populates
its mutable fields. Back-references encountered during the populate phase resolve
to the (still-empty) shell — patching happens automatically because mutation is
shared.

Standard graph-serialization pattern. Java's `ObjectOutputStream` uses the same
scheme (its "handle table"), as do most serializers that need to preserve object
identity. Only works when the deserialized type has mutable structure that can be
filled after construction (e.g., an array or mutable field). Pure-immutable graphs
cannot have cycles in the first place.

**Depends on**: (none)
**Enables**: (none directly)
**Connections**:
- analogous-to: Java `ObjectOutputStream` handle table
- complements: [[tying-the-knot.technique]] — same shape: allocate shell, register, populate; identity preserved by shared mutation
- contrasts-with: tree serialization — duplicates shared sub-objects and loops on cycles
