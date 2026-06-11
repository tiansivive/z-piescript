---
tags: [coordination, channels, fault-tolerance, evaluation, open, needs-design, concept]
refs:
  - adr:D-047
  - thread:error-handling
---
# Error Channels

Query and computation failures produce signals on error channels. In v0, a channel terminates on error -- if the body of a `spawn` throws, the channel receives the exception and any `when` waiting on it propagates the failure. There are no partial results: error kills the channel.

**Settled direction** (session:mv-channels-error-semantics, 2026-06-10): **errors are
messages** — uncaught failures become structured values on channels, handled by ordinary `when`
reaction rules. Externally validated against BEAM (trap_exit/monitors deliver death as ordinary
messages handled by normal receive) and the distributed Join Calculus (failure detection as
reactable events). D-047's two error classes stay distinct: *domain* errors travel as ordinary
values on the normal data path (typed per channel; [[result-types.types]] once ADTs land);
*infrastructure/uncaught* failures are uniform runtime-shaped messages. **The design must be
done on multi-value queue semantics** ([[multi-value-channels.coordination]] blocks this) —
single-value-era constructs explored and parked in that session, not to be re-proposed against
the one-shot model: a `recover` clause on `when`, dual value/error channel pairs returned by
`spawn`, JoCaml-style `or`-alternative arms. All were workarounds for one-shot expression
`when`; standing rules over queues make them unnecessary or reshape them.

Future directions:
- **Hybrid model**: signal error on a dedicated error channel AND continue producing partial results on the data channel. Requires multi-value channels or a separate error sideband.
- **Typed errors**: error channels carry typed error values (via [[result-types.types]]) rather than raw exceptions. `when` handlers can pattern-match on error variants.
- **Error propagation policy**: configurable per-channel -- fail-fast (current), best-effort (partial results), or retry.

The tension with [[stream-a.language]] is about what happens when a streaming source errors mid-stream. Does the stream terminate? Does it emit an error element? The error channel design must compose with whatever streaming abstraction lands.

**Depends on**: [[channels.infrastructure]], [[fire-and-forget.coordination]], [[multi-value-channels.coordination]]
**Enables**: (none directly -- design unsettled)
**Connections**:
- refined-by: [[errors-as-messages.coordination]] — D-056 settles the architecture this zettel tracked as open (minimal runtime contract, per-node err inbox, user-space supervision, consume + selective matching)
- part-of: [[error-handling.thread]] -- error channels are a core piece of the error handling story
- uses: [[channels.infrastructure]] -- error signals travel through the channel mechanism
- informs: [[result-types.types]] -- typed error channels need Result/Either to carry structured errors
- informs: [[fire-and-forget.coordination]] -- fire-and-forget semantics interact with error propagation: sender doesn't see evaluation errors
- tension-with: [[stream-a.language]] -- stream error semantics (terminate vs partial results) must align with error channel design
- tension-with: [[multi-value-channels.coordination]] -- partial-result error model needs multi-value channels for the data sideband
- informs: [[otp-supervision.coordination]] -- supervision trees need error signals to trigger restart strategies
- informs: [[saga-coordination.coordination]] -- saga compensation needs error signals to trigger rollback
