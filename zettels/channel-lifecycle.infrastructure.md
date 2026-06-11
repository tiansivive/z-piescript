---
tags: [infrastructure, channels, resources, tech-debt, task, problem, needs-design, later]
refs:
  - code:ChannelRegistry.java
  - session:80f0b64a-5e21-4b2e-acda-fabde482cc87
  - thread:error-handling
  - thread:distributed-coordination
---
# Channel Lifecycle

Channels registered in [[channel-registry.infrastructure]] as `SubscribableListener`s:

- Registry entries are **never removed** — not even on completion (`ChannelRegistry.java`
  javadoc: the `SubscribableListener` must stay visible for late `when` lookups racing with
  `send`; cleanup deferred to a per-evaluation lifecycle). Corrected 2026-06-10 — this zettel
  previously claimed auto-removal on completion, which the code contradicts.
- The [[inbox.infrastructure]] is persistent by design (never removed)
- Leak risk: every channel leaks today; channels created ([[spawn-bang.coordination]]) but never completed additionally hold an uncompleted listener forever
- No explicit `Shard.release` equivalent for channels
- Future: scope-based cleanup or [[bracket-patterns.language]]; close/fail semantics belong to
  the channel termination protocol to be defined in the [[multi-value-channels.coordination]]
  design

**Depends on**: [[channel-registry.infrastructure]]
**Enables**: (none directly)
**Connections**:
- analogous-to: [[bracket-patterns.language]] — similar to Searcher resource leak in Block D; both are "leak if not consumed" patterns needing scope-based or linear-type solutions
- tension-with: [[spawn-bang.coordination]] — spawn! creates channels that are especially leak-prone (no auto-send on completion)
- analogous-to: [[persistent-resources.infrastructure]] — both are "resource outlives expected scope" problems needing ownership or lifetime tracking
