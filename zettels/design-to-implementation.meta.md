---
tags: [meta, workflow, concept]
refs:
  - skill:zettelkasten
  - skill:create-plan
---
# Design-to-Implementation Workflow

The path from design discussion to shipped code follows a consistent pipeline through the
zettelkasten. Agents should follow this workflow and load all `meta` and `workflow` zettels
at session start. The **operating procedures** live in two skills: `skill:zettelkasten`
(knowledge-base writes — zettels, edges, thread, queue) and `skill:create-plan` (plan
authoring and execution).

## Pipeline


1. Discussion → atomic zettels
   Surface a concept → create a zettel in zettels/ → tag, connect, thread
   (procedure: skill:zettelkasten)

2. Hub zettel → organize
   When a topic grows beyond a single zettel → create a hub with includes edges.
   The hub is the full design picture — not scoped to one implementation phase.
   It connects to everything related: prerequisites, future extensions,
   theoretical foundations, comparable systems.

3. Thread log → paper trail
   Record session work in thread.md: edges traversed, actions taken, items
   enqueued/resolved/spawned.

4. Implementation plan → scope a phase
   When ready to build → create a plan (.cursor/plans/) from the hub.
   The plan scopes ONE implementation phase from the hub's larger picture.
   Plan tasks reference specific zettels. The hub lives on; the plan completes.
   (procedure: skill:create-plan; plan shape: [[cursor-plan-template.meta]];
   rationale: [[implementation-plan-workflow.meta]])

5. Queue → track work
   Pending items in [[global-pending.queue]] or thread-specific queues.
   Implementation items from the plan go here too.

6. ADR → record decisions
   Non-trivial design choices during implementation → decisions.md entry.
   Cross-reference the ADR from relevant zettels via `adr:D-NNN` refs.

7. Update → close the loop
   After implementation: update current-state.md, tag zettels as `implemented`,
   mark thread/queue items resolved, append to thread.md.


## Key principle

**Hubs outlive plans.** A hub zettel captures the full design landscape of a concept —
past decisions, current implementation, future directions, theoretical connections. A plan
captures one scoped phase of implementation. When the plan completes, the hub gains
`implemented` connections but keeps its future/theoretical edges for the next phase.

**Agents should load meta zettels at session start** to understand the conceptual model, and
follow the skills (`skill:zettelkasten`, `skill:create-plan`) for the procedures — the skills
are the single source of truth for process; meta zettels carry the rationale.

**Depends on**: [[thread-queue-system.meta]], [[tags-as-triples.meta]]
**Connections**:
- extends: [[thread-queue-system.meta]] — adds the hub→plan→implement pipeline on top of the thread/queue workflow
- complements: [[universal-vs-topic.meta]] — meta zettels document the process; topic zettels document the design
- refined-by: [[implementation-plan-workflow.meta]] — plan-phase rationale; checklist lives in skill:create-plan
