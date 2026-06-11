---
tags: [example, coordination, fault-tolerance, channels, documentation]
refs:
  - adr:D-056
  - adr:D-057
  - thread:error-handling
  - session:mv-channels-error-semantics
---
# Error Handling Patterns — Syntax Examples

The D-056/D-057 architecture as programs. **Assumptions**: post-MV-design world — queue
channels, standing `when` rules (registration, not suspension), working block expr-stmts,
pattern guards. **Every API name shown** (`Process.self`, `info.errors`, `Channel.fail`, error
record fields) **is a placeholder, not a decision** — the settled content is the *mechanics of
selective consumption*. The `program` field is stamped by the runtime (D-057): handlers filter
on it but cannot forge it.

## 1. Multi-tenant err inbox — disjoint guard-filtered forwarders

```
let me     = Process.self            -- deps-backed constant; arrives in closures BY CAPTURE
let myErrs = spawn!
let topo   = Cluster.topology "cluster"
let worker = List.head (List.filter (fn n -> n.id != topo.local.id) topo.nodes)
let results = spawn!

send worker.inbox (fn info -> {
    -- standing forwarder rule on the WORKER's local err inbox, consuming
    -- only failures stamped with MY identity; unmatched messages stay
    -- in the store for other programs' rules
    when (info.errors e) if e.program == me -> send myErrs e;
    send results (scan info);
    null
})

when (results r) -> handle r
when (myErrs e)  -> compensate e     -- supervision at home, ordinary code
```

Program B runs the identical shape with *its* captured `me` — disjoint by construction, no
coordination between programs. Note the guard: `{ program: me | e }` as a *pattern* would BIND
`me`, not compare it (the non-linear pattern problem — [[bound-variable-patterns.language]]);
guards or pins are required for runtime-id filtering.

## 2. Unmatched messages — the drain policy

A program that crashed something but installed no handler: its messages match nobody's rule,
sit in the store, and drain to the node log on expiry (today's WARN as the floor). Nothing to
write — that's the point.

## 3. Compete on identical patterns — the work queue (consume semantics as a feature)

```
let tasks = spawn!
let done  = spawn!
List.map (fn t -> send tasks t) workItems;

-- same channel, same pattern → genuine competition:
-- each task consumed by exactly ONE rule firing, pairing nondeterministic (JC semantics)
when (tasks t) -> send done (processFast t)
when (tasks t) -> send done (processThorough t)
```

Impossible under broadcast — which is why consume is the uniform primitive.

## 4. Broadcast built from consume — the JC state-as-message distributor

```
let events    = spawn!
let subscribe = spawn!
let registry  = spawn!
send registry [];                                 -- state lives AS a message

when (subscribe s) & (registry subs) ->           -- join consumes both atomically
    send registry (List.concat subs [s])

when (events e) & (registry subs) -> {
    List.map (fn s -> send s e) subs;             -- fan out
    send registry subs;                           -- restore state
    null
}
```

Subscribers register by name-passing: `send subscribe myChannel`. Both rules compete for the
`registry` message — that competition IS the atomic state update. Broadcast is a dozen lines of
library; the reverse construction (compete from broadcast) does not exist.

## 5. Supervision round trip — the JC's "task taken over by another location"

```
when (myErrs e) if e.node == failedNodeOf e -> {
    let backup = List.head (List.filter (fn n -> n.id != e.node) topo.nodes);
    Channel.fail results e;                       -- termination-protocol primitive (MV design)
    send backup.inbox (fn info -> send results2 (scan info));
    null
}
```

The handler learns which computation died (message metadata), unblocks waiters on the orphaned
channel (it holds the ref — it created the channel before shipping), and re-ships the work.
Runtime uninvolved beyond delivering the message.

**Depends on**: [[errors-as-messages.coordination]], [[multi-value-channels.coordination]], [[when-reaction-rules.coordination]], [[pattern-guards.language]], [[process-identity.coordination]]
**Enables**: (none — demonstration)
**Connections**:
- example-of: [[errors-as-messages.coordination]] — the architecture as runnable-shaped programs
- validates: [[when-reaction-rules.coordination]] — standing rules make every pattern here expressible without new constructs
- uses: [[name-passing.coordination]] — the distributor's subscribe channel is channel-of-channels
- demonstrates: [[bound-variable-patterns.language]] — §1 shows why naive id patterns break
- informs: [[otp-supervision.coordination]] — §5 is the supervision primitive a future library wraps
