---
tags: [queue, meta]
refs: []
---
# Global Pending Queue

Pending work items not assigned to a specific thread. FIFO — oldest first.
`[ ]` open, `[x]` resolved, `[~]` dropped.

Thread-specific items have been extracted into their respective thread hubs.
See [[error-handling.thread]], [[language-expressiveness.thread]],
[[data-completeness.thread]], [[distributed-coordination.thread]],
[[type-foundations.thread]].

## Open items

- [x] Revise `vision.md` — resolved: trimmed from 791 to 192 lines; aspirational/speculative sections moved to zettels and thread hubs
- [ ] Zettelkasten interaction skill — teach agents how to create/update/connect zettels (skill vs CLAUDE.md guidance?)
- [ ] Backfill thread.md — add retroactive session blocks for prior sessions (best-effort from transcripts)
- [ ] [[es-conventions-debt.infrastructure]] — TransportVersion, logging, ActionListener patterns, dedicated thread pool (production punch list)
- [ ] [[lsp.tooling]] — Language Server Protocol implementation
- [ ] [[syntax-highlighting.tooling]] — syntax highlighting definitions
- [ ] [[repl.tooling]] — REPL / interactive evaluation mode
- [ ] `ResolvedMapping.partiallyUnmappedFields` is dead post-rebase (2026-04-15) — `IndexResolutionPrePass` passes `trackUnmappedFieldIndices=false` (matching ESQL's default after #145991), so `EsIndex.fieldToUnmappedIndices()` is always empty and the field is unread by the elaborator. Resolution is now coupled to [[unmapped-field-surfacing.data]]: either drop the field, or actually populate it (with the ESQL #145920 OOM risk) and put it to use
- [ ] [[action-prefix-rename.infrastructure]] — `PiescriptAction.NAME = "cluster:compute/piescript"` is not in `TransportService.VALID_ACTION_PREFIXES`; ES logs WARN at startup and has a TODO to promote it to a hard error. Rename to `cluster:admin/piescript/eval` (or similar) and supersede D-055
- [ ] [[dynamic-field-types.data]] — fields missing from the merged field-caps view (sparse / user-known runtime fields) can't be referenced today. Two paths drafted: [[unmapped-field-surfacing.data]] (sparse, automatic, also resolves the `partiallyUnmappedFields` cleanup) and [[use-with-annotations.data]] (general, `use ... with { ... }` syntax)

## Resolved items

- [x] [[recursion.hub]] — extracted to [[language-expressiveness.thread]]
- [x] [[pattern-matching.hub]] — extracted to [[error-handling.thread]] + [[language-expressiveness.thread]]
- [x] [[recursive-types.types]] — extracted to [[type-foundations.thread]]
- [x] [[runtime-dispatch.types]] — extracted to [[type-foundations.thread]]
- [x] [[type-narrowing.types]] — extracted to [[type-foundations.thread]]
- [x] [[keyword-string.types]] — extracted to [[data-completeness.thread]]
- [x] [[datetime.types]] — extracted to [[data-completeness.thread]]
- [x] [[numeric-precision.types]] — extracted to [[data-completeness.thread]]
- [x] [[string-concat.language]] — extracted to [[language-expressiveness.thread]]
- [x] Revise `roadmap.md` — resolved: roadmap archived, replaced by thread system
- [x] Add remaining `Tracked in: [[zettel]]` links to `decisions.md` ADRs — resolved session:4e5e689a (55/55 done)
- [x] Tech-debt extraction script — resolved 2026-04-09: `scripts/tech_debt.py`
- [x] Roadmap/ADR/vision generation scripts — resolved 2026-04-09: `scripts/roadmap_status.py`, `scripts/adr_index.py`, `scripts/vision_coverage.py`
- [x] [[transport-channels.infrastructure]] — resolved 2026-04-09
- [x] [[lucene-segments.es-internals]] — resolved 2026-04-09
- [x] [[security-namespace.infrastructure]] — resolved 2026-04-09
- [x] [[lucene-collectors.es-internals]] — resolved 2026-04-09

**Depends on**: (none)
**Enables**: (none)
**Connections**:
- related: [[error-handling.thread]]
- related: [[language-expressiveness.thread]]
- related: [[data-completeness.thread]]
- related: [[distributed-coordination.thread]]
- related: [[type-foundations.thread]]
- related: [[external-interaction.thread]]
- related: [[ownership-resources.thread]]
