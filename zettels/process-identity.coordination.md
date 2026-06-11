---
tags: [coordination, infrastructure, distributed, security, concept, designed, ready, next]
refs:
  - adr:D-057
  - code:EvalDependencies.java
  - code:PiescriptSendRequest.java
  - code:TransportPiescriptSendAction.java
  - thread:error-handling
  - session:mv-channels-error-semantics
---
# Process Identity

Runtime-assigned, unforgeable identity for piescript computations — the Erlang pid analogue.
**Decision (D-057)**: program identity = the root evaluation's ES `TaskId`, propagated **by
value along the causal chain**: `programId` on `EvalDependencies`, a wire field on
`PiescriptSendRequest`, threaded into remote evaluations' deps. A shipped closure evaluates
under its *sender's* identity regardless of node; local spawns inherit deps ambiently. Also
`setParentTask` in `sendRemote` for free `_tasks`-API correlation and future cancellation rails.

What existed before (code-verified 2026-06-11): the `Task` was already in `EvalDependencies`
(Exchange child tracking), but `PiescriptSendRequest` carried only `(channelId, payload)` —
identity severed at every node hop; the D-047 WARN log could not say whose closure died. The
authenticated *user* already crosses the wire via transport thread-context (security layer) —
a complement for authorization-grade tenancy, not correlation.

User access — the `self()` story: a deps-backed prelude **constant** (`Process.self`-style,
name non-final; arity-0 builtin like `IndexLit` UUID resolution). Because identity is causal
and values are pure/serializable, **closures access their identity by capture** — no DI
widening, no remote `self` needed. v1 representation `Keyword`; opaque `Process` type later.
Stamping: at the runtime catch sites for v1 (all hold deps); envelope stamping at the `send`
boundary as the general anti-forgery mechanism once MV channels land (MV session item).

Open: sender-side minting of per-task refs (`send` returning a locally-minted ref —
fire-and-forget preserved; Erlang spawn-returns-pid) for monitor-granularity supervision.
Deferred: per-computation `TaskManager` registration (convergence target for coarse remote
evaluations; aligns with the persistent-task/actor future).

**Depends on**: [[code-mobility.coordination]], [[fire-and-forget.coordination]], [[transport-send.infrastructure]]
**Enables**: [[errors-as-messages.coordination]], [[error-handling-patterns.example]]
**Connections**:
- prerequisite-for: [[errors-as-messages.coordination]] — selective consumption requires unforgeable stamped identity
- motivates: [[pattern-guards.language]] — runtime-assigned ids cannot be matched by literal patterns; filtering needs guards or pins
- motivates: [[bound-variable-patterns.language]] — the ergonomic alternative for id-equality matching
- enables: [[channel-lifecycle.infrastructure]] — channel ownership tagging (`ChannelRegistry.register` records owning program) unlocks ownership-aware cleanup and introspection without migration
- informs: [[actor-model.lifecycle]] — the identity carrier is a string; the value swaps to a persistent actor id when actors land
- complements: [[token-capability-security.security]] — user identity (authorization) vs program identity (correlation); err schema gains both
- complements: [[error-provenance.language]] — identity says *whose*, provenance says *where*
- analogous-to: Erlang pids — `self()` = deps constant; spawn-returns-pid = sender-side minting; pid matching = the guards/pin requirement
