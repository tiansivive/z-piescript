---
tags: [coordination, fault-tolerance, channels, concept, designed, next]
refs:
  - adr:D-056
  - adr:D-057
  - adr:D-047
  - thread:error-handling
  - session:mv-channels-error-semantics
  - resource:https://www.microsoft.com/en-us/research/wp-content/uploads/2017/01/join-tutorial.pdf
---
# Errors as Messages — Minimal Runtime Contract

The settled error-handling architecture (2026-06-11): **the runtime's entire job is to catch
every uncaught failure at its evaluation boundary and deliver a structured error message to the
local node's err inbox.** Nothing else — no routing, no cleanup decisions, no supervision.
Everything above that line is user-space piescript.

- **The per-node err inbox is the main (and only) runtime mechanism**, not a last resort. It is
  an *ordinary* consume-semantics channel (no special channel mode) — multi-tenant consumption
  works via selective matching (see below). Default consumer behavior: unconsumed messages
  drain to the node log (TTL-style; preserves today's WARN as the floor — a competing catch-all
  *rule* would race with program rules, so drain-on-expiry is the cleaner default; policy open).
- **Supervision is user-space.** Programs ship standing forwarder rules to worker nodes that
  consume their own failures from the local err inbox and `send` them home (the locality
  property does cross-node routing for free — the home channel travels in the closure).
  Precedent: OTP is not in the BEAM VM — the VM delivers exit signals; supervisors are library
  code. See [[error-handling-patterns.example]] for the programs.
- **"Death notification" is nothing special**: a computation dying IS the runtime catching its
  exception and sending the message (replaces the WARN in `TransportPiescriptSendAction:127`).
  The orphaned-channel problem resolves in user space: the supervisor created the result
  channels before shipping work, so it holds the refs and can fail/close them — needs one
  termination-protocol primitive from the MV design. No introspection builtin required for the
  core pattern (deferred to ops tooling).
- **Selective matching makes the shared inbox multi-tenant**: rules consume only messages
  matching their pattern/guard; unmatched messages stay in the store. Requires runtime-stamped
  identity ([[process-identity.coordination]]) and pattern guards or pin patterns
  ([[pattern-guards.language]], [[bound-variable-patterns.language]]) — literal-only patterns
  cannot filter on runtime-assigned ids.
- **Two error classes stay distinct** (D-047): domain errors travel as ordinary values on the
  data path (typed per channel; [[result-types.types]] later); infrastructure/uncaught failures
  are uniform runtime-stamped messages. Schema v1: message + whatever metadata exists
  (program identity, node, source/provenance when [[error-provenance.language]] lands).
- **`spawn expr` keeps failing its own result channel** — that is the sugar's producer→channel
  contract, not supervision.

**Join Calculus alignment** (verified in the Fournet & Gonthier tutorial): the distributed JC
failure model is fail-stop locations with `halt` (local failure) and `fail a; P` (asynchronous
remote failure detection) — failure as a *reactable event*, "allowing programmable error
recovery"; "its task may be taken over by another location without interfering with the failed
location." No exceptions anywhere in the model. Failure unit is the location (≈ node /
computation), matching the per-node inbox + computation identity. `fail a; P` is monitor-style
(watch a named location) — buildable in user space over the inbox later.

**Depends on**: [[multi-value-channels.coordination]], [[when-reaction-rules.coordination]], [[process-identity.coordination]], [[fire-and-forget.coordination]]
**Enables**: [[otp-supervision.coordination]], [[saga-coordination.coordination]]
**Connections**:
- refines: [[error-channels.coordination]] — settles the architecture that zettel tracked as open
- uses: [[pattern-guards.language]] — guard-filtered consumption is the multi-tenancy mechanism
- uses: [[inbox.infrastructure]] — the err inbox follows the inbox precedent (well-known per-node channel)
- informs: [[channel-lifecycle.infrastructure]] — orphaned-channel cleanup is supervisor-driven via the termination protocol
- inspired-by: [[beam-lessons.comparable]] — errors-as-messages (trap_exit/monitors) and supervision-as-library (OTP) are the precedents
- contrasts-with: [[spark.comparable]] — RDD lineage recomputation is the recovery strategy under implicit distribution; not weighed in D-056's alternatives (foreclosed earlier by D-040/D-042). The idea resurfaces in user space: a supervisor re-sending a pure closure is manual lineage replay — worth revisiting when supervision patterns are designed.
- example-of: see [[error-handling-patterns.example]] — the architecture as concrete programs
