---
tags: [meta, workflow, tooling, concept]
refs:
  - doc:AGENTS.md
  - skill:create-plan
---
# Implementation Plan Workflow

How piescript implementation plans tie one phase of a hub (or thread) to shippable work. Plans
live in `.cursor/plans/`; each plan binds together an implementation zettel, a queue zettel, the
thread paper trail, review gates, and repo hygiene (tests, debug scripts, docs close-out).

**The canonical checklist lives in the `create-plan` skill** (`skill:create-plan` —
`<plugin>/.claude/skills/create-plan/SKILL.md`, Cursor symlink under `.cursor/skills/`). This
zettel records the rationale; when the process changes, only the skill changes.

## Why the workflow is shaped this way

- **Plans scope a single phase; hubs outlive plans.** The hub keeps the full design landscape;
  the plan completes and is archived. This prevents plans from becoming stale design documents.
- **Queue zettel mirrors plan todos** so progress is visible from inside the knowledge base
  without opening the plan file, and survives across sessions/agents.
- **Review stops by default.** Stepwise review is the default authoring posture because plan
  execution spans sessions and agents must not assume intent on ambiguity.
- **Reconciliation at close-out.** Code, tests, `current-state.md`, and `decisions.md` are
  compared to the zettel graph at the end of every plan — discrepancies are surfaced in prose,
  not papered over. New zettels require user confirmation to avoid unagreed bulk creation.

**Depends on**: [[thread-queue-system.meta]], [[design-to-implementation.meta]]
**Enables**: (none directly)
**Connections**:
- refines: [[design-to-implementation.meta]] — step 4 (plan) and following steps of the pipeline
- uses: [[thread-queue-system.meta]] — thread and queue conventions during execution
- specifies: [[cursor-plan-template.meta]] — plan file shape and frontmatter
