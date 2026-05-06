---
tags: [infrastructure, es-internals, security, transport-layer, tech-debt, task, known-issue, deferred, migration]
refs:
  - adr:D-055
  - code:x-pack/plugin/piescript/src/main/java/org/elasticsearch/xpack/piescript/PiescriptAction.java
  - code:server/src/main/java/org/elasticsearch/transport/TransportService.java
  - code:x-pack/plugin/security/qa/operator-privileges-tests/src/javaRestTest/java/org/elasticsearch/xpack/security/operator/Constants.java
---
# Action Prefix Rename

`PiescriptAction.NAME = "cluster:compute/piescript"` is not in
`TransportService.VALID_ACTION_PREFIXES`. ES logs at startup:

```
warn [o.e.t.TransportService] invalid action name [cluster:compute/piescript]
must start with one of: [indices:admin, indices:monitor, indices:data/write,
indices:data/read, indices:internal, cluster:admin, cluster:monitor,
cluster:internal, internal:]
```

Today this is `logger.warn` and the action still registers. The validator
carries a TODO to promote the check to a hard error: *"we should make this a
hard validation and throw an exception but we need a good way to add backwards
layer for it. Maybe start with a deprecation layer."* When that flips, piescript
will fail to start.

The send action (`internal:compute/piescript/send`) matches `internal:` and is
fine.

## How we got here

D-055 chose `cluster:compute/...` deliberately as a custom namespace to escape
`indices:`-prefixed authorization machinery (`CompositeIndicesRequest`,
`RBACEngine` allowlist) — see [[security-namespace.infrastructure]]. The
validator's prefix set has not been opened up to match — it has been tightened
over time. `cluster:compute/` was never blessed; we simply hadn't run a node
and noticed the warning until 2026-05-06.

## The fix

Rename to a valid prefix. `cluster:admin/piescript/eval` is the closest semantic
fit: piescript can do arbitrary distributed work (read, write, ship code), and
`cluster:admin/...` is the namespace for cluster-level admin operations.
`cluster:monitor/...` (read-only) and `cluster:internal/...` (system-internal)
do not match piescript's surface.

The rename is more than a string change — it touches:

1. `PiescriptAction.NAME` itself.
2. The privilege/role configuration so non-admin users can still invoke the
   endpoint (D-055's auth model assumed a custom prefix; `cluster:admin/*`
   privileges traditionally require elevated access).
3. The operator-privileges allowlist (`Constants.java`).
4. Tests asserting the action name.
5. A new ADR superseding [[security-namespace.infrastructure|D-055]]'s
   namespace decision and recording the new auth model.

## Why deferred

The warning is cosmetic. No functionality is broken. D-055's broader auth model
(no `CompositeIndicesRequest`, ESQL handles index auth itself) still holds —
the question is just *which* valid prefix carries it. Leave for a slot when
auth model changes can be reasoned about together.

**Depends on**: [[security-namespace.infrastructure]]
**Enables**: (none)
**Connections**:
- part-of: [[es-conventions-debt.infrastructure]]
- tension-with: [[security-namespace.infrastructure]] — D-055's custom prefix is rejected by the validator; rename requires superseding ADR
- requires: new ADR to supersede D-055's namespace choice
