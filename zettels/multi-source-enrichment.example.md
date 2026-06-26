---
tags: [example, data-processing, esql, open, coordination, concept, motivation]
refs:
  - doc:presentation.md
  - doc:vision.md
  - thread:external-interaction
  - session:doc-gap-backfill
---
# Multi-Source Enrichment Example

Cross-index enrichment: query orders and customers concurrently, join them in-memory, produce
enriched records. The canonical "ESQL ENRICH is a stale snapshot; piescript uses live data"
demonstration.

```piescript
use "orders" as orders_idx;
use "customers" as customers_idx;

let orders_ch = spawn query ESQL.from orders_idx
  |> ESQL.where (fn r -> r.@timestamp > "now-1h");

let customers_ch = spawn query ESQL.from customers_idx;

when (orders_ch orders) & (customers_ch customers) ->
  orders |> List.map (fn order ->
    let match = customers
      |> List.filter (fn c -> c.id == order.customer_id)
      |> List.reduce (fn _ c -> { name: c.name }) { name: "unknown" }
    in { order | customer_name: match.name }   -- (A) record-update: NOT YET IMPLEMENTED
  )
```

**What runs today** (everything except A):
- `use` declarations with typed `Index r` values — implemented
- `spawn` + `ESQL.from` / `ESQL.where` — implemented
- `when (a x) & (b y) ->` multi-channel synchronization — implemented (single-value, blocking)
- `List.map`, `List.filter`, `List.reduce` — implemented

**What is aspirational** (marked A):
- `{ order | customer_name: match.name }` — record-update/extend syntax. The field projection
  part of open rows is implemented; the update/extension operator is not. Without it, the workaround
  is an explicit record literal:
  ```piescript
  in {
    id: order.id,
    amount: order.amount,
    customer_id: order.customer_id,
    customer_name: match.name   -- all fields spelled out
  }
  ```
  See [[row-polymorphism.types]] and the `Pick`/`Omit`/`&` operators (D-053) for the type-level
  foundation; the surface syntax for update is the missing piece.

**Comparison with ESQL ENRICH**:

| Concern | ESQL ENRICH | Piescript |
|---------|-------------|-----------|
| Data freshness | Stale (enrich policy snapshot) | Live query at request time |
| Matching predicate | Field equality only | Arbitrary function (List.filter) |
| Composition | None after enrichment | Full functional composition |
| Setup | Enrich policy + processor config | One use declaration |

The program also demonstrates the "ESQL stops short, piescript continues" thesis from
[[extraction-cliff.external]]: ESQL has no cross-index join primitive; piescript composes
two queries with a functional in-memory join.

**Depends on**: [[esql-compilation.esql]], [[spawn.coordination]]
**Enables**: (none directly)
**Connections**:
- example-of: [[enrich-unification.external]] — live enrichment as one of the unified use cases
- example-of: [[extraction-cliff.external]] — cross-index join is precisely the cliff ESQL can't cross
- example-of: [[feature-constellation.external]] — replaces the enrich processor
- motivates: [[row-polymorphism.types]] — record-update syntax requires the extension operator
- uses: [[esql-compilation.esql]] — two concurrent ESQL queries via T-LINQ combinators
- uses: [[spawn.coordination]] — concurrent multi-index queries
- related: [[watchlist-cross-ref.example]] — same multi-index concurrent pattern; watchlist is more concrete
