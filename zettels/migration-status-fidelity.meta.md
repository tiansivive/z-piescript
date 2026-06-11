---
tags: [meta, known-issue]
refs:
  - session:mv-channels-error-semantics
---
# Migration Status Fidelity

A recurring gap pattern in doc→zettelkasten migrations: **coverage survives, intent-status does
not**. When a monolithic doc section is split into zettels, content that was "the intended
end-state, not yet implemented" gets recorded with maturity/priority tags reflecting the
*implementation status quo* at migration time — `someday`, `deferred`, "extension" framing —
silently demoting design commitments to speculation. Maturity tags conflate "not yet
implemented" with "not the plan."

Known instances:
1. **Codata / streams-as-codata** — trapped in the scripting_language_design plan (§2.10, §6.1),
   never surfaced as zettels; recovered in the recursion design session (2026-04-10).
2. **MV channels as THE channel model** — the replacement intent (single-value channels are an
   interim stand-in) survived only in an `Evaluator.java` code comment; zettels framed MV as a
   deferred extension. Recovered 2026-06-10.
3. **`when` as standing reaction rules** — the baseline intended semantics ("multiple `when`
   clauses fire simultaneously", pre-trim vision) was collapsed into the speculative CHAM
   generalization zettel and tagged `someday`. Recovered 2026-06-10.

Mitigations: when migrating, record the intended end-state *separately* from implementation
status (a `designed`/`now` zettel for the target, an `implemented` zettel for the interim);
sweep remaining archived plans/docs for trapped intent (queued in [[global-pending.queue]]).

**Depends on**: (none)
**Enables**: (none directly)
**Connections**:
- refines: [[design-to-implementation.meta]] — adds a fidelity check to the migration step of the pipeline
- example-of: the codata recovery in the recursion session paper trail (thread.md)
- motivates: archived-plan sweep queue item in [[global-pending.queue]]
