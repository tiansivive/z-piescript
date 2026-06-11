---
tags: [coordination, channels, open, feature, concept, needs-design, now]
refs:
  - adr:D-056
  - roadmap:block-b-old
  - session:80f0b64a-5e21-4b2e-acda-fabde482cc87
  - session:mv-channels-error-semantics
  - thread:distributed-coordination
---
# Multi-Value Channels

**The intended channel model** — not an extension of [[channels.infrastructure]] but its real
semantics: channels are typed queues/mailboxes carrying sequences of messages over time,
consumed by standing `when` reaction rules ([[when-reaction-rules.coordination]]). The current
single-value `SubscribableListener` implementation is an interim stand-in to be **replaced**.
Requires channel message stores (multiset/bag semantics) and a join automaton for pattern
matching over accumulated messages.

**Not streaming.** This is general-purpose Join Calculus message passing — control-plane
coordination where message volume is small (tens to hundreds) but reaction semantics are rich.
Example: 10 workers sending results to the same coordinator channel via [[send.coordination]].
Data-plane streaming (large columnar `Page` batches, backpressure) is the compute engine's job
via [[exchange-streaming.infrastructure]] (D-054, Block G); MV channels deliberately take on
**no backpressure or streaming-performance agenda**. One *can* stream values over them, but
that is not their point.

**Settled (2026-06-11, D-056)** — uniform **consume semantics with selective matching**: each
message is consumed by exactly one rule firing ("each x⟨v⟩ message fulfills at most one x()
call — the def rule consumes its join pattern"; nondeterministic pairing, per the JC tutorial).
Rules consume only messages matching their pattern/guard; unmatched messages stay in the store
(Erlang selective receive). **Broadcast is a user-space library pattern** built from consume
(state-as-message distributor) — the asymmetry decides uniformity: compete is not buildable
from broadcast. Guards participate in the consumption transaction (guard failure leaves the
message in the store) — a [[join-automaton.coordination]] requirement. No special channel modes;
the err inbox is an ordinary consume channel. JC locality note: in the JC all receptors for a
name are statically co-located at its single defining site; piescript deviates (dynamic `when`)
but preserves the property at node granularity (D-045).

Design scope (session to be scheduled): message store semantics; consumption atomicity for
conjunctive `&` patterns; `when` registration semantics and the program-result question;
completion/close/fail termination protocol; envelope identity stamping at the send boundary
(D-057); err-inbox drain policy; what `spawn`/`spawn!` sugar becomes; registry → store
migration. The error-handling design ([[errors-as-messages.coordination]]) is blocked on this.

**Depends on**: [[channels.infrastructure]], [[join-calculus.coordination]]
**Enables**: [[when-reaction-rules.coordination]], [[cham-patterns.coordination]], [[fold-as-join.coordination]], [[sse-streaming.external]], [[watcher-replacement.external]], [[error-channels.coordination]]
**Connections**:
- part-of: [[future-coordination.roadmap]]
- replaces: [[channels.infrastructure]] current single-value implementation — replacement, not extension (see `Evaluator.java` CoreSend comment)
- blocks: [[errors-as-messages.coordination]] — the error design must be done on queue semantics
- constrains: [[join-automaton.coordination]] — committed-choice consumption must respect pattern guards (consume only when pattern AND guard pass)
- contrasts-with: [[exchange-streaming.infrastructure]] — Exchanges handle columnar data-plane streaming; MV channels handle value-level control-plane messaging
- enables: [[actor-model.lifecycle]] — persistent actors receiving input sequences need a multi-value inbox (the [[inbox.infrastructure]] is already a multi-value channel in disguise)
- contrasts-with: [[multi-value-fields.data]] — different concepts (MV channels vs MV ES fields) sharing the "multiple values under one name" pattern
- related: [[cham-patterns.coordination]] — CHAM functional-pattern matching operates over channel message stores
