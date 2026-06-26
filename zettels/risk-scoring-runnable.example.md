---
tags: [example, data, esql, implemented, coordination, security]
refs:
  - doc:presentation.md
  - session:doc-gap-backfill
---
# Risk Scoring — Runnable Today (Tier 2)

The risk scoring program stripped to what runs in the current implementation: one ESQL
aggregation query, a user-defined weighted-sum function, and a bulk index write. No SSE
channels, no Kafka, no actor recursion. This is the baseline: query → compute → persist.

**Tier context**: Tier 1 ([[risk-score-pattern.data]]) = the data pattern concept. Tier 2
(this zettel) = runnable today, writes to index. Tier 3 ([[risk-scoring-incremental.example]])
= full vision with actor pagination + Kafka + SSE.

```piescript
use ".alerts-security" as idx;

let pseries_weighted_sum = fn s values ->
  List.reduce (fn acc v ->
    { sum: acc.sum + v / Math.pow acc.i s, i: acc.i + 1 }
  ) { sum: 0.0, i: 1.0 } values
  |> (fn state -> state.sum)

in let raw = query ESQL.from idx
  |> ESQL.where (fn r -> r.kibana.alert.risk_score != 0)
  |> ESQL.statsBy
       (fn r -> {
         top_scores: ESQL.top r.kibana.alert.risk_score 10000 "desc",
         alert_count: ESQL.count "*"
       })
       (fn r -> { user_name: r.user.name })
  |> ESQL.limit 1000;

in let scored = List.map (fn user -> {
  user_name: user.user_name,
  score: pseries_weighted_sum 1.5 user.top_scores,
  alert_count: user.alert_count
}) raw

in let _ = Index.bulk "risk-scores" scored

in { scored: List.length scored }
```

Every part runs in the current codebase:
- `ESQL.statsBy` + `ESQL.top` → Lucene-backed TOP-N aggregation by user
- `List.reduce` with record accumulator → user-defined weighted sum
- `List.map` → structured output construction
- `Index.bulk` → bulk write to destination index
- `let _ =` → discard the write acknowledgement, return count

The key story: `pseries_weighted_sum` is a let-binding, not an ESQL PR. Domain-specific
aggregates become functions, not changes to the query engine.

**Depends on**: [[risk-score-pattern.data]], [[esql-aggregates.esql]], [[type-driven-materialization.esql]]
**Enables**: (none directly)
**Connections**:
- example-of: [[risk-score-pattern.data]] — the Tier 1 concept as a concrete runnable program
- example-of: [[esql-compilation.esql]] — full ESQL.statsBy + ESQL.top pipeline
- example-of: [[value-proposition.principle]] — user-defined aggregates as functions, not ESQL built-ins
- uses: [[esql-aggregates.esql]] — ESQL.statsBy with ESQL.top for aggregation
- prerequisite-for: [[risk-scoring-incremental.example]] — Tier 3 extends this with actor recursion + sinks
