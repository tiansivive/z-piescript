---
tags: [infrastructure, coordination, concurrency, channels, implemented, pi-calculus, concept]
refs:
  - adr:D-040
  - adr:D-045
  - code:ChannelRegistry.java
  - code:Value.java
  - session:80f0b64a-5e21-4b2e-acda-fabde482cc87
  - session:mv-channels-error-semantics
---
# Channels

`Channel t` is a typed conduit for asynchronous messages — the Join Calculus channel. The
**intended model is a multi-value queue/mailbox** ([[multi-value-channels.coordination]]):
channels carry sequences of messages consumed by `when` reaction rules. The **current
implementation is an interim stand-in**: a single-value `SubscribableListener<Value>`
(future-like, one completion), to be **replaced — not extended** — by the queue model
(`Evaluator.java` records this: "this separation goes away when multi-value channels replace
the current model").

`ChannelVal(nodeId, channelId)` is the serializable reference; the actual store lives in the
per-node [[channel-registry.infrastructure]]. Channels carrying channels (`Channel (Channel a)`)
enables the pi-calculus [[name-passing.coordination]] pattern — unchanged by the queue model.

**Depends on**: [[join-calculus.coordination]]
**Enables**: [[spawn.coordination]], [[spawn-bang.coordination]], [[when-synchronization.coordination]], [[send.coordination]], [[channel-registry.infrastructure]]
**Connections**:
- part-of: [[block-a.roadmap]]
- enables: [[name-passing.coordination]] — `Channel (Channel a)` enables the pi-calculus name-passing pattern
- evolved-into: [[multi-value-channels.coordination]] — the queue model replaces the single-value implementation; it is the intended semantics, not an extension
