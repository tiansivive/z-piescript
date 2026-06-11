---
tags: [thread, roadmap, fault-tolerance, language, types]
refs: []
---
# Error Handling & Fault Tolerance

From source-location error messages to OTP-style supervision trees. This thread
covers the full spectrum of how piescript handles, reports, and recovers from
errors — spanning type-level safety (Result/Option), runtime diagnostics (error
provenance), resource cleanup (bracket patterns), and distributed fault tolerance
(sagas, supervision).

## Sequence

0. **MV channels + `when` reaction semantics** [[multi-value-channels.coordination]],
   [[when-reaction-rules.coordination]] — needs-design, **now**
   Prerequisite for the runtime error story: errors-as-messages (D-056,
   [[errors-as-messages.coordination]]) must be designed on queue semantics with
   standing rules, not the interim one-shot channels. Consume + selective matching
   settled; termination protocol, drain policy, envelope stamping in scope.
   _Shared with: distributed-coordination_

0b. **Process identity** [[process-identity.coordination]] — **ready** (D-057)
   Root TaskId on the causal chain: `EvalDependencies.programId`, wire field on
   `PiescriptSendRequest`, `setParentTask`, stamped at catch sites. First
   implementable slice — independent of #0; everything above depends on it.

0c. **Pattern guards** [[pattern-guards.language]] — needs-design, promoted (D-056)
   Hard prerequisite: selective consumption on runtime-assigned identity is
   inexpressible without guards (or pins — [[bound-variable-patterns.language]]).
   _Shared with: language-expressiveness_

1. **Error provenance** [[error-provenance.language]] — ready
   Thread `Source` through evaluator so runtime errors point to call sites.
   Independent of #0 — error messages need provenance regardless.

2. **Forall type** [[forall-type.types]] — ready
   D-038 tech debt. `@AwaitsFix` tests. Unblocks bidir checking.
   _Shared with: type-foundations_

3. **ADTs** [[adts.types]] — needs-design
   Sum types for Option/Result. Declaration syntax, closed vs open, constructors.
   _Shared with: language-expressiveness_

4. **Pattern matching** [[pattern-matching.hub]] — ready
   Match expressions (`match x | pat -> body`), `if/then/else` as sugar.
   Phase 1 (basic patterns) complete. ADT constructor patterns deferred.
   _Shared with: language-expressiveness_

5. **Result/Option types** [[result-types.types]] — after #3, #4
   `Result a e` / `Option a` replacing null-as-bottom.
   Depends on: [[adts.types]], [[pattern-matching.hub]]

6. **Null-as-bottom fix** [[null-as-bottom.types]] — after #5
   Remove unsound `Null` unification. Depends on Option type existing.

7. **Bracket patterns** [[bracket-patterns.language]] — needs-design (after #4)
   `bracket acquire release use` for Searcher/Writer/channel cleanup.

8. **Channel lifecycle** [[channel-lifecycle.infrastructure]] — needs-design
   Leak prevention for `spawn!` channels that never complete.

9. **Saga coordination** [[saga-coordination.coordination]] — exploration
   Multi-shard write coordination with compensating actions.

10. **OTP supervision** [[otp-supervision.coordination]] — exploration
    Supervisor trees, restart strategies. Depends on: [[actor-model.lifecycle]]

**Depends on**: (none — root thread)
**Enables**: (none directly)
**Connections**:
- includes: [[multi-value-channels.coordination]]
- includes: [[when-reaction-rules.coordination]]
- includes: [[error-channels.coordination]]
- includes: [[errors-as-messages.coordination]]
- includes: [[process-identity.coordination]]
- includes: [[pattern-guards.language]]
- includes: [[error-handling-patterns.example]]
- includes: [[error-provenance.language]]
- includes: [[forall-type.types]]
- includes: [[adts.types]]
- includes: [[pattern-matching.hub]]
- includes: [[result-types.types]]
- includes: [[null-as-bottom.types]]
- includes: [[bracket-patterns.language]]
- includes: [[channel-lifecycle.infrastructure]]
- includes: [[saga-coordination.coordination]]
- includes: [[otp-supervision.coordination]]
- includes: [[create-vs-index.data]]
- includes: [[fire-and-forget.coordination]]
- related: [[language-expressiveness.thread]] — shares ADTs, pattern matching
- related: [[type-foundations.thread]] — shares Forall type
