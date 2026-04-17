# z-piescript

Piescript's design space zettelkasten — a structured knowledge base of the language's design
landscape. Each zettel is an atomic note in `zettels/`, tagged and linked.

Part of the [z-loom](https://github.com/tiansivive/z-loom) federation.

## Quick start

```bash
# Overview of all tracked design topics
python3 scripts/catalog.py --compact

# Pending work items and thread priorities
python3 scripts/queue.py

# Thread-based roadmap dashboard
python3 scripts/roadmap_status.py

# ADR cross-reference and consistency check
python3 scripts/adr_index.py
```

Pre-built outputs of these scripts are available in [`dist/`](dist/) (regenerated on every push).

## What is piescript?

A typed functional language for distributed computation in Elasticsearch. Uses Join Calculus
primitives (`spawn`/`when`/`send`/channels) for async coordination atop a pure functional core
(lambdas, let-bindings, records, pattern matching, recursion).

The implementation lives at [elasticsearch/x-pack/plugin/piescript](https://github.com/tiansivive/elasticsearch/tree/piescript/x-pack/plugin/piescript).

## Structure

```
z-piescript/
  manifest.yaml          # Machine-readable schema and entry points
  README.md              # This file
  VOCABULARY.md          # Tags, edges, aliases, tag groups
  WORKFLOW.md            # Threads, queues, paper trail system
  metrics.md             # Derived graph metrics (hub score, blocking depth, etc.)
  thread.md              # Append-only paper trail of work across sessions
  zettels/               # 500+ atomic design notes
  scripts/               # View/metric scripts (catalog, queue, roadmap, ADR index)
  dist/                  # CI-generated indexes (CATALOG.md, QUEUE.md, ROADMAP.md)
  .github/workflows/     # CI: regenerate dist/ on push
```

## Model

The knowledge base is a graph of **nodes** connected by **labeled edges**.

**Nodes** are zettels — atomic notes in `zettels/`. Each zettel has tags and refs.

**Edges** connect zettels to each other via labeled actions: `depends-on`, `enables`,
`informs`, `supersedes`, `related`, or any verb that describes the relationship.

**Tags** name things. A tag on a zettel says "this zettel is about X." The same tagging
mechanism works at every level — tags can be grouped, and groups themselves can be
tagged with roles. This is the same pattern as piescript's kinds-as-types (D-053):
types classify values, kinds classify types, but kinds ARE types. Here, tags classify
zettels, roles classify tag groups, but roles ARE tags.

See [VOCABULARY.md](VOCABULARY.md) for the full tag and edge vocabulary.
See [WORKFLOW.md](WORKFLOW.md) for the thread/queue/paper-trail system.

## Zettel format

```markdown
---
tags: [language, types, open]
refs:
  - adr:D-051
  - session:e3b83171-9476-43b2-bbc3-fde5725a57a0
  - thread:error-handling
---
# Title

One-paragraph description of the concept.

**Depends on**: [[pattern-matching.language]], [[adts.types]]
**Enables**: [[actor-model.lifecycle]], [[plugin-spi.external]]
**Connections**:
- informs: [[nbe-compilation.esql]] — NbE is piescript's instantiation of this
- supersedes: [[plan-graph.language]]
```

### Frontmatter fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `tags` | yes | list | Flat list of tags — use as many as apply |
| `refs` | no | list | References using prefixed links |

### Ref prefixes

| Prefix | Points to | Example |
|--------|-----------|---------|
| `adr` | Decision record in `docs/decisions.md` | `adr:D-051` |
| `roadmap` | Roadmap section | `roadmap:block-h` |
| `vision` | Vision section | `vision:external-interaction-model` |
| `plan` | Plan file | `plan:compute_engine_streaming_f5db78f2` |
| `session` | Chat session ID | `session:e3b83171-...` |
| `doc` | Documentation file | `doc:data-access.md` |
| `code` | Source file | `code:EvalExchange.java` |
| `resource` | Any URI | `resource:https://arxiv.org/pdf/1306.6032.pdf` |
| `thread` | Work thread | `thread:error-handling` |
| `queue` | Queue | `queue:global-pending` |

## File naming

`thing.qualifier.md` — the primary concept first, optional qualifier second.

Read left to right: concept first, then progressively narrowing context hints.
Multiple qualifiers are fine: `risk-scoring.incremental.example.md`.

**Do not use qualifiers for classification.** Tags are for classification.
The qualifier is a visual grouping hint — scripts and tools must never rely on
it to determine a zettel's purpose or membership.

## Federation

This zettelkasten is part of the z-loom federation. Cross-references use qualified URIs:

```
loom://piescript/row-types.design      # from any context
[[row-types.design]]                   # within this zettelkasten (local ref)
```

z-loom resolves `loom://piescript/...` to this repository via the piescript hub node.

## Obsidian

Compatible with [Obsidian](https://obsidian.md) — open the repo root as a vault
for graph navigation.

## License

Elastic License 2.0
