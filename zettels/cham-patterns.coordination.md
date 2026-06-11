---
tags: [coordination, theoretical, someday]
refs:
  - vision:speculative
  - session:80f0b64a-5e21-4b2e-acda-fabde482cc87
  - thread:distributed-coordination
---
# CHAM Patterns

Chemical Abstract Machine (Berry & Boudol 1992) with [[curry-narrowing.language]] for functional patterns on channel message stores. Maximal parallel firing: runtime discovers and concurrently executes all non-overlapping matches. Control-plane performance model — channel stores are small.

**Scope note** (2026-06-10): this zettel covers only the speculative *generalization* —
functional patterns via narrowing. The **baseline** standing-rule semantics of `when`
(presence-firing, multiple coexisting rules, re-arming) is not speculative; it is the intended
model, recorded at [[when-reaction-rules.coordination]]. Earlier versions of this zettel
conflated the two, which mislabeled the baseline as `someday`.

**Depends on**: [[multi-value-channels.coordination]], [[when-reaction-rules.coordination]]
**Enables**: (none directly)
**Connections**:
- part-of: [[future-coordination.roadmap]]
- extends: [[when-reaction-rules.coordination]] — generalizes presence-firing baseline rules to functional patterns over message stores; the narrowing part is speculative
- related: [[join-calculus.coordination]] — CHAM reaction rules generalize join calculus join patterns to functional pattern matching over message stores
- related: [[curry-narrowing.language]] — functional-logic patterns enable declarative concurrent reactions
- uses: [[logic-programming.hub]] — functional patterns on channel stores use logic-programming-style search
- uses: [[backtracking.search]] — finding satisfying assignments in message stores requires search
