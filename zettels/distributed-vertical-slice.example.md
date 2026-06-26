---
tags: [example, distributed, coordination, implemented, mobility, concept]
refs:
  - doc:presentation.md
  - adr:D-040
  - adr:D-042
  - adr:D-045
  - session:doc-gap-backfill
---
# Distributed Vertical Slice

The end-to-end architectural example: a coordinator discovers cluster topology, ships a closure
to a remote node's inbox, that closure reads a local shard and sends results back via a channel.
This is the core distributed computation primitive — nothing else in Elasticsearch provides it at
the language level.

```piescript
-- Coordinator: discover topology, create bare channel, ship a closure
let topo   = Cluster.topology "my-index"
in let target = List.head topo.shards
in let ch  = spawn!                            -- bare channel, no body
in send target.node.inbox (fn info ->          -- closure travels to target node
  let data = scan target                       -- runs on the data node's local shard
    |> List.filter (fn r -> r.status == "active")
  in send ch data                              -- routes back via Join Calculus locality
)
in when (ch results) ->
  results |> List.map (fn r -> { id: r.id, status: r.status })
```

What each line demonstrates:

- `Cluster.topology "my-index"` — topology as first-class typed values (not hidden like ESQL)
- `spawn!` — bare channel creation; `spawn` would auto-execute a body, `spawn!` defers to explicit `send`
- `send target.node.inbox` — code mobility: the closure travels to the data node; purity makes this safe (D-045)
- `fn info ->` — [[inbox-dependency-injection.coordination]]: the inbox closure receives local node capabilities as its argument; no `local_node` primitive needed
- `scan target` — local shard read at the data node; runs where data lives, not on the coordinator
- `send ch data` — Join Calculus locality property: the message routes to wherever `ch` was created (the coordinator); no distributed consensus needed
- `when (ch results) ->` — coordinator synchronizes when the remote send arrives

**API note**: the stale version in `docs/presentation.md` Example D uses `topology "my-index"`
(should be `Cluster.topology`) and `local_node` (replaced by the `info` inbox arg per
[[inbox-dependency-injection.coordination]]). This zettel uses the current API.

**Competitive framing**: the architectural moat against Spark/Flink. Piescript distributes by
design and runs inside the cluster the data already lives in. Code goes to data, not data to code.

**Depends on**: [[code-mobility.coordination]], [[inbox.infrastructure]], [[join-calculus.coordination]], [[spawn.coordination]]
**Enables**: (none directly — this is an example)
**Connections**:
- example-of: [[code-mobility.coordination]] — the traveling closure is the concrete instantiation
- example-of: [[block-c.roadmap]] — the end-to-end cross-node execution in a single program
- example-of: [[data-locality.distributed]] — computation dispatched to where data lives
- example-of: [[explicit-distribution.language]] — topology and nodes are first-class; user controls placement
- validates: [[inbox-dependency-injection.coordination]] — inbox closure arg replaces `local_node`
- uses: [[topology.infrastructure]] — Cluster.topology as the entry point
- uses: [[spawn.coordination]] — spawn! for bare channel creation
- motivates: [[when-reaction-rules.coordination]] — the when clause here is the single-value case of the general reaction rule
- related: [[watchlist-cross-ref.example]] — multi-query concurrency; this example adds cross-node code mobility
