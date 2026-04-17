# Workflow

The design space includes a work layer on top of the zettelkasten: threads, queues,
and a paper trail.

## Threads

A **thread** is an ordered sequence of work items forming a parallel concern —
a named path through the zettel graph that progresses independently.

Thread hubs are zettels tagged `thread`. They contain:
- A description of the concern
- An ordered sequence of items with dependency annotations and readiness markers
- `includes` edges in the Connections section identifying all member zettels

Member zettels point back via `thread:thread-stem` frontmatter refs.
A zettel can belong to multiple threads (shared dependencies).

```bash
# See all threads with member status
python3 scripts/roadmap_status.py
```

## Queues

A **queue** is a zettel tagged `queue` — a flat list of pending work items.
The global queue (`[[global-pending.queue]]`) holds items not yet assigned to
a thread. Items use `- [ ]` / `- [x]` / `- [~]` checkboxes.

```bash
# See all pending work
python3 scripts/queue.py
```

## Paper trail

**[thread.md](thread.md)** — append-only paper trail of work across sessions.
Edge lines (`[[A]] -- verb -> [[B]]`) record knowledge graph traversal.
Action lines (`ENQUEUE`, `RESOLVED`, `SPAWN`) record workflow events.

## Summary

Zettels are the atoms. Threads are paths through the graph. Queues are pending edges.
See [[thread-queue-system.meta]] for the full design.
