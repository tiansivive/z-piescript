# Thread

Append-only paper trail of design and implementation work. Each block records a
session's path through the zettel graph — what was explored, what was decided,
what was deferred.

Format: edge lines (`[[A]] -- verb -> [[B]]`) and action lines (`ENQUEUE`, `RESOLVED`, `SPAWN`).
See [[thread-queue-system.meta]] for the full system design.

---

## session:4e5e689a — 2026-04-08 [design-space, meta, queues, threads]

Created the design space knowledge base (216 zettels, catalog script, tag taxonomy).
Then designed the thread & queue system itself.

[[tags-as-triples.meta]] -- inspired -> [[thread-queue-system.meta]]
[[channel-registry.infrastructure]] -- analogous_to -> [[thread-queue-system.meta]]
[[join-calculus.coordination]] -- synchronization_model_for -> [[thread-queue-system.meta]]

Queue system design: zettels as atoms, threads as graph paths, queues as FIFO pending
lists. Threads log edges and actions (ENQUEUE/RESOLVED/SPAWN). Queues synchronize
threads like channels synchronize spawned computations.

Cross-domain connections surfaced: event sourcing (action log as source of truth),
RDF triples (edge syntax), Luhmann's fleeting-notes box, org-mode capture/refile,
GTD methodology, Roam/Logseq daily notes.

ENQUEUE [[recursion.language]] — design recursion mechanism
ENQUEUE [[pattern-matching.language]] — Phase 1e, deferred twice
ENQUEUE [[recursive-types.types]] — iso-recursive vs equi-recursive
ENQUEUE [[runtime-dispatch.types]] — runtime polymorphism design
ENQUEUE [[type-narrowing.types]] — TypeScript-style refinement
ENQUEUE [[keyword-string.types]] — Keyword vs String unification
ENQUEUE [[datetime.types]] — DateTime/IP/GeoPoint handling
ENQUEUE [[numeric-precision.types]] — primitive type review
ENQUEUE [[transport-channels.infrastructure]] — ES transport as native channels
ENQUEUE [[string-concat.language]] — list/string concat operators

---

## session:es-internals-gap — 2026-04-09 [design-space, es-internals, reviews]

Ran Phase 1–2 of the ES-internals gap program; backlog and priorities live in
[[reviews/es-internals-gaps.md]]. Closed initial slices: [[doc-values.es-internals]] (refs +
edges), [[blockloader.data]] + [[circuit-breaker.infrastructure]] (ES `code:` + [[compute-engine.es]]),
[[transport-send.infrastructure]] + [[channel-registry.infrastructure]] (`TransportService`, mutual
edges). Added `python3 scripts/catalog.py --es-code-gaps` triage hint.

[[doc-values.es-internals]] -- informs -> [[compute-engine.es]]
[[blockloader.data]] -- informs -> [[compute-data-page-block.es]]

ENQUEUE [[lucene-segments.es-internals]] — add ES-tree `code:` refs + link read path cluster
ENQUEUE [[security-namespace.infrastructure]] — add server/x-pack `code:` anchors beyond piescript actions
ENQUEUE [[lucene-collectors.es-internals]] — same (cluster 5)

RESOLVED [[lucene-segments.es-internals]] — `Engine.java`, Lucene `SegmentInfos` resource; [[block-d.roadmap]] edge
RESOLVED [[security-namespace.infrastructure]] — RBAC + operator + REST/plugin refs (full `code:` paths)
RESOLVED [[lucene-collectors.es-internals]] — `QueryPhase` + ESQL Lucene operators; [[compute-engine.es]] edge
RESOLVED [[transport-channels.infrastructure]] — relationship to [[transport-layer.es]] documented; queue item closed

[[lucene-segments.es-internals]] -- informs -> [[block-d.roadmap]]
[[lucene-collectors.es-internals]] -- informs -> [[compute-engine.es]]
[[transport-channels.infrastructure]] -- contrasted_with -> [[transport-layer.es]] — implemented transport + registry stack vs speculative transport-only channels

---

## session:extraction-scripts — 2026-04-09 [design-space, scripts, tooling]

Created `scripts/` directory with shared zettel parsing library (PyYAML + Rich),
migrated `catalog.py` from `docs/design-space/`, and built four extraction scripts:
`tech_debt.py`, `roadmap_status.py`, `adr_index.py`, `vision_coverage.py`.

`scripts/lib/zettel.py` — shared parsing: PyYAML frontmatter, body regex (title,
description, Depends on / Enables / Connections edges), dependency graph builders,
tag/ref filters.

`scripts/lib/adr.py` — `decisions.md` parser: splits on `## D-NNN:` boundaries,
handles format variations (Phase line optional, casing, bold vs heading sections).

All scripts support dual output: Rich terminal tables by default, `--markdown` for
plain text. `pyproject.toml` declares pyyaml + rich as dependencies.

[[thread-queue-system.meta]] -- instantiated_by -> scripts/tech_debt.py, scripts/roadmap_status.py — queue items resolved via script automation

RESOLVED Tech-debt extraction script — `scripts/tech_debt.py`
RESOLVED Roadmap/ADR/vision generation scripts — `scripts/roadmap_status.py`, `scripts/adr_index.py`, `scripts/vision_coverage.py`

---

## session:thread-roadmap-restructure — 2026-04-09 [design-space, roadmap, threads, meta]

Replaced the 960-line monolithic `roadmap.md` with a thread-based system.
Five parallel work concerns, each a hub zettel tagged `thread` with ordered
sequences, `includes` edges for membership, and priority/readiness tags.

Design discussion: roadmap was 80%+ completed work, mixed concerns, redundant
with design space zettels. Error handling identified as broader than ADTs +
pattern matching — full spectrum from source locations to OTP supervision.
Thread-based structure captures parallel independent concerns with sequencing
and dependency annotations per thread.

New index.md tag groups: Structure (`thread`, `queue`, `hub`, `paper-trail`,
`note`) and Priority (`now`, `next`, `later`, `someday`, `ready`, `blocked`,
`needs-design`). `adr` added as alias of `decision`. `includes` edge verb
for thread membership. `thread:` and `queue:` ref prefixes.

[[roadmap-hub.roadmap]] -- replaced_by -> [[error-handling.thread]], [[language-expressiveness.thread]], [[data-completeness.thread]], [[distributed-coordination.thread]], [[type-foundations.thread]]
[[thread-queue-system.meta]] -- extended_by -> thread-based roadmap (Structure tags, thread hubs)

SPAWN [[error-handling.thread]] — error provenance to OTP supervision
SPAWN [[language-expressiveness.thread]] — recursion to module system
SPAWN [[data-completeness.thread]] — Block G tests to numeric precision
SPAWN [[distributed-coordination.thread]] — MV channels to long-lived computations
SPAWN [[type-foundations.thread]] — Forall type to session types
SPAWN [[empty-mapping-diagnostics.data]] — new zettel for field caps diagnostic gap
SPAWN [[global-pending.queue]] — queue migrated from queue.md to zettel

RESOLVED "Revise roadmap.md" — roadmap archived to `docs/archive/roadmap.pre-threads.md`, replaced by thread system
RESOLVED Queue items extracted into threads: [[recursion.language]], [[pattern-matching.language]], [[recursive-types.types]], [[runtime-dispatch.types]], [[type-narrowing.types]], [[keyword-string.types]], [[datetime.types]], [[numeric-precision.types]], [[string-concat.language]]

~50 member zettels updated with `thread:` refs and priority tags.
`roadmap_status.py` rewritten for thread-based reporting.
`index.md`, `AGENTS.md`, `CLAUDE.md`, `current-state.md` updated.

---

## session:thread-roadmap-continued — 2026-04-09 [design-space, threads, vision, meta]

Extended the thread system with 2 additional threads, design principle zettels,
ML workflow zettels, and vision.md trim.

SPAWN [[external-interaction.thread]] — plugin SPI to Transform/Watcher unification
SPAWN [[ownership-resources.thread]] — ownership to incremental computation

[[external-interaction-model.roadmap]] -- superseded_by -> [[external-interaction.thread]]
[[type-foundations.thread]] -- related -> [[ownership-resources.thread]]
[[distributed-coordination.thread]] -- related -> [[external-interaction.thread]]

Design principles extracted from vision.md into atomic zettels:
SPAWN [[design-principles.hub]] — hub for the 6 foundational constraints
SPAWN [[inferred-types.principle]] — types inferred, not annotated
SPAWN [[esql-data-layer.principle]] — ESQL is the data layer
SPAWN [[functional-distributed.principle]] — functional by default, distributed by design
SPAWN [[incremental-delivery.principle]] — phased, self-contained delivery
SPAWN [[es-native.principle]] — ES conventions, deep integration
[[join-calculus.coordination]] -- part_of -> [[design-principles.hub]]

ML workflow zettels split from vision.md brainstorming:
SPAWN [[model-evaluation.ml]] — precision/recall/F1 via shard-local folds
SPAWN [[data-preparation.ml]] — sampling, normalization, train/test splits
SPAWN [[inference-orchestration.ml]] — fan out to ML nodes
SPAWN [[ml-non-goals.ml]] — what piescript does NOT do (GPUs, training, tensors)
SPAWN [[es-ml-integration.ml]] — topology + send to ML nodes
[[ml-workflow-integration.ml]] -- promoted_to -> hub (includes edges added)

SPAWN [[risk-scoring-incremental.example]] — full actor + Kafka + SSE example

New tags: `principle`, `example` (added to Purpose group in index.md).

vision.md trimmed from 791 to 192 lines. Kept: identity, motivation,
distributed computation model, design philosophy (now linking to principle
zettels), what piescript is not. Replaced: long-term aspirations, data access
architecture, speculative sections, ML workflows, external interaction model
— all now in zettels and thread hubs.

RESOLVED "Revise vision.md" — speculative sections moved to zettels

## session:block-g-integration-tests — 2026-04-10 [data-completeness, infrastructure, testing]

Implemented the missing integration tests for Block G Exchange streaming.
Discovered and fixed a bug in `EvalExchange.java` where `Exchange.connect` was hardcoded to use `getLocalNodeConnection()`, making cross-node exchange impossible.
Updated `ExchangeVal` to include the producer's `nodeId` so the consumer can establish a remote transport connection to the correct node.
Added `testLocalExchangeStreaming` to `PiescriptIT.java` and `testRemoteExchangeStreaming` to `PiescriptMultiNodeIT.java`.

[[block-g.roadmap]] -- validates -> [[exchange-streaming.infrastructure]]
[[exchange-streaming.infrastructure]] -- implements -> [[exchange-remote-testing.infrastructure]]

RESOLVED [[exchange-remote-testing.infrastructure]] — added cross-node tests
RESOLVED Block G integration tests — updated `data-completeness.thread.md`

---

## session:pattern-matching-design — 2026-04-10 [language-expressiveness, error-handling, design]

Design discussion for pattern matching as the critical unblock for recursion.

Started from recursion — discovered the false dependency chain: D-010 tied `if/then/else`
to `match`, `match` was incorrectly listed as depending on ADTs, so recursion appeared
blocked by the full ADT + pattern matching stack. Fixed: basic pattern matching (Boolean,
literals, wildcards, records, lists) is independent of ADTs. Constructor patterns come
later with ADTs, but neither blocks the other.

Created [[pattern-matching.hub]] with 6 sub-zettels splitting the old monolithic
[[pattern-matching.language]] (now deleted):
- [[match-syntax.language]] — ML-style `match x | pat -> body`, `if/then/else` as sugar
- [[pattern-types.language]] — 7 pattern forms including record/list tail with `|`
- [[match-type-checking.language]] — elaboration algorithm via unification
- [[pattern-reuse.language]] — extending patterns to lambda/when/let (future sugar)
- [[type-level-matching.types]] — future type families generalizing `force`
- [[core-match.language]] — CoreMatch IR node + Pattern sealed hierarchy

Key design decisions:
- `|` for tails (records and lists), consistent with row type syntax and Erlang cons
- `...` reserved for record spread in expressions (new zettel: [[record-spread.language]])
- Record tail `| rest` binds a **record** at value level (rows are type-level only)
- Nested patterns are not a special case — Pattern hierarchy is recursive by definition
- No exhaustiveness checking in v1; runtime error if no match
- Pattern infrastructure designed for reuse across match/lambda/when/let

[[recursion.language]] -- blocked-by -> [[pattern-matching.hub]]
[[pattern-matching.hub]] -- complements -> [[adts.types]]
[[pattern-matching.hub]] -- enables -> [[recursion.language]]
[[pattern-matching.hub]] -- specializes -> [[curry-narrowing.language]]
[[pattern-matching.hub]] -- specializes -> [[cham-patterns.coordination]]
[[pattern-matching.hub]] -- enhances -> [[when-synchronization.coordination]]
[[pattern-matching.hub]] -- enhances -> [[currying.language]]
[[nbe-dual-pattern.types]] -- analogous-to -> [[type-level-matching.types]]

Created [[record-spread.language]] — `...` operator for record expression merging
Created [[design-to-implementation.meta]] — workflow: zettels → hub → plan → queue → ADR

Updated CLAUDE.md, AGENTS.md, /load skill — agents now read all `meta` zettels at session start.
Updated [[language-expressiveness.thread]] — pattern matching bumped to position 1 (priority `now`).
Updated [[error-handling.thread]] — pattern matching no longer depends on ADTs.
Added `enhances` verb to index.md edge vocabulary.
Updated 13 zettels to point from [[pattern-matching.language]] to [[pattern-matching.hub]].

SPAWN [[pattern-matching.hub]] — hub zettel with 6 sub-zettels
SPAWN [[record-spread.language]] — `...` spread operator for record expressions
SPAWN [[design-to-implementation.meta]] — workflow meta zettel

---

## session:data-access-restructure — 2026-04-10 [data, architecture, meta]

Archived the monolithic `data-access.md` document and restructured the data access design space into atomic zettels.

Promoted `data-access-architecture.roadmap` to a proper hub representing the full data access landscape (ESQL, physical, streaming, Query typeclass) rather than just the `Query a` vision. Extracted the equational vs sequential argument into `data-access-rationale` and the mermaid architecture into `data-access-diagram`.

Refined file naming guidelines in `index.md` to avoid redundant qualifiers (e.g., `data-access-hierarchy.md` instead of `data-access-hierarchy.data.md`) and clarified multiple qualifier usage.

[[data-access-architecture.roadmap]] -- includes -> [[data-access-rationale]], [[data-access-diagram]], [[data-access-hierarchy]]
[[data-access-rationale]] -- overlaps -> [[data-access-hierarchy]]

SPAWN [[data-access-rationale]] — equational vs sequential argument
SPAWN [[data-access-diagram]] — mermaid architecture diagram
SPAWN [[data-access-restructure.session]] — session zettel

RESOLVED Archive `data-access.md` to `docs/archive/data-access.pre-threads.md`

## session:5f90891b-2661-476c-b4fe-575b7d34ec22 — 2026-04-10 [language, control-flow, implementation]

Implemented Phase 1 of pattern matching. Added `match` expressions with `Alternative` arms and a sealed `Pattern` hierarchy (literal, variable, wildcard, open-row record, exact list, cons list). `if/then/else` is now sugar over Boolean `match`.

- **IR & Types**: `CoreMatch` and `Alternative` added. `Pattern` hierarchy implemented.
- **Elaborator**: `Matches.java` handles pattern type inference (unifying scrutinee type with pattern type) and `if` desugaring.
- **Evaluator**: `EvalMatch.java` implements top-to-bottom arm dispatch and recursive pattern matching. Record patterns bind fields in alphabetical order.
- **Serialization**: `TAG_MATCH` and recursive `Pattern` serialization added to `CoreExprSerialization`.
- **Debug Scripts**: Added `match` and `if/else` examples to `test-dev.sh`, `test-eval.sh`, and `test-multinode.sh`.

SPAWN [[pattern-matching-phase1.session]] — session zettel
RESOLVED [[pattern-matching.hub]] — Phase 1 complete (basic patterns, no ADTs, no exhaustiveness)
RESOLVED [[core-match.language]] — IR node implemented
RESOLVED [[match-syntax.language]] — ML-style syntax implemented
RESOLVED [[pattern-types.language]] — basic patterns implemented
RESOLVED [[match-type-checking.language]] — unification-based inference implemented
RESOLVED [[if-as-match-sugar.language]] — desugaring implemented

---

## session:recursion-design-exploration — 2026-04-10 through 2026-04-12 [language-expressiveness, recursion, design-space, meta]

Extended design discussion on recursion, starting from "what should be next" and expanding
into a deep exploration of the design space around iteration, control flow, abstract machines,
logic programming, and compilation.

### Recursion mechanism design

Explored: `fix` combinator, `let rec` syntax, tying the knot, fused loop-match with `repeat`,
trampolining, CEK machine, Clojure loop/recur, Scheme named let, APL power operator, SQL
recursive CTEs, Flix first-class Datalog fixpoint, generators, shift/reset, interaction nets.

Decided: implicit recursion (all bindings recursive, Haskell-style, no `rec` keyword) + fused
loop-match for structured iteration. `fix` and `let rec` rejected for surface syntax.
Guarded recursion check (static: self-references must be under lambdas) as primary safety
mechanism. Trampoline deferred pending execution model question.

[[recursion.hub]] -- includes -> [[implicit-recursion.design]], [[tying-the-knot.technique]], [[fix-combinator.theory]], [[let-rec-syntax.language]], [[fused-loop-match.language]], [[recursion-sentinel.evaluation]], [[guarded-recursion.technique]], [[no-corecursion.decision]]
[[pattern-matching.hub]] -- enables -> [[recursion.hub]]
[[fused-loop-match.language]] -- compiles-to -> [[state-machine-loop.compilation]]
[[fused-loop-match.language]] -- uses -> [[one-shot-continuations.control]]

### Pattern matching hub restructure

Discovered false dependency: pattern matching was listed as depending on ADTs (wrong).
Basic pattern matching (Boolean, literals, wildcards, records, lists) is independent of ADTs.
Split monolithic pattern-matching.language into hub + 6 sub-zettels. Deleted old zettel.
Pattern matching priority bumped to `now` — implemented in session 5f90891b.

[[pattern-matching.hub]] -- complements -> [[adts.types]] (neither blocks the other)
[[pattern-matching.hub]] -- specializes -> [[curry-narrowing.language]], [[cham-patterns.coordination]]

Key design points: `|` for record/list tails (consistent with row type syntax), `...`
reserved for record spread in expressions, record tail binds a **record** not a row (rows
are type-level only), nested patterns not special (Pattern hierarchy is recursive by
definition), Pattern infrastructure reusable across match/lambda/when/let.

SPAWN [[pattern-matching.hub]] — hub with 6 sub-zettels (match-syntax, pattern-types, match-type-checking, pattern-reuse, type-level-matching, core-match)
SPAWN [[record-spread.language]] — `...` spread operator
SPAWN [[guarded-recursion.technique]] — static self-reference detection
SPAWN [[codata.types]] — coinductive types, dual of ADTs
SPAWN [[anamorphisms.types]] — unfolds, dual of catamorphisms
SPAWN [[lazy-stream.types]] — future Stream type reserved by D-043
SPAWN [[stream-a.language]] — reconciliation problem: original abstract codata Stream vs current Exchange

### Codata recovery from early sessions

Found codata discussion in original scripting language design plan (§2.10 "No User-Defined
Corecursion", §6.1 "Streams as Abstract Codata"). This was trapped in the plan file and
never surfaced as zettels. Key insight: streams ARE codata operationally (observation-based,
pull-based) but the language doesn't expose coinductive types. Current Exchange streaming
and original Stream a are fundamentally different abstractions (explicit plumbing vs abstract
codata) — reconciliation is an open question.

### Design space gap analysis

Ran systematic gap analysis across all plans (scripting_language_design, block_a through
block_f, f-omega, phase1, phase2, phase1d) and references.md. Found ~60 untracked concepts.

### Zettelkasten expansion (~110 new zettels)

Created zettels across 12 clusters:

**Recursion cluster** (7 + hub): implicit-recursion, tying-the-knot, fix-combinator,
let-rec-syntax, fused-loop-match, recursion-sentinel, guarded-recursion, no-corecursion

**Evaluation architecture** (4): trampolining, cek-machine, zam, execution-model

**Delimited continuations** (12 + hub): shift-reset, call-cc, one-shot-continuations,
multi-shot-continuations, answer-type-polymorphism, cps-transform, state-machine-loop,
block-params-ir, distributed-continuations, stackless-coroutines, stackful-continuations

**Logic programming** (6 + hub): backtracking, logic-unification, logic-variables,
datalog-fixpoint, stratified-negation

**Interaction nets + compilation** (4): interaction-nets, hvm, closure-conversion,
monomorphization

**TRS** (4): term-rewriting, knuth-bendix, church-rosser, termination-analysis

**Codata / streams** (5): codata, anamorphisms, lazy-stream, stream-a, guarded-recursion

**Papers** (16 + hub): wadler-propositions-as-sessions, dunfield-krishnaswami,
sangiorgi-agent-passing, linear-haskell, wadler-comprehending-monads, fruhwirth-chr,
outsidein-x, flumejava, materialization-strategies, milner-pi-calculus,
honda-session-types, honda-multiparty-sessions, wu-schrijvers-fusion,
plotkin-pretnar-handlers, fegaras-maier-monoid-comprehensions, granule-graded-modal

**Decisions / rejected** (14): strict-evaluation, no-corecursion, no-monads-for-effects,
env-sharing-safety, posix-read-semantics, monomorphism-restriction, agg-stripag,
esqlplan-compiler, closure-vs-string-columns, join-keyword-rejection, numeric-widening,
top-level-channel, error-accumulation, two-type-var-schema

**Techniques / obstacles** (16 + hub): async-prepass, datatype-tcon-mapping,
union-find-propagation, exhaustiveness-checking, error-channels,
searcher-statefulness, shard-refresh-ordering, mapping-update-failure,
indexing-pressure-bypass, spawn-at-node, lambda-lifting, defunctionalization,
write-context, list-map-traverse-tension, join-automaton, compilation-pipeline

**Syntax / typeclass / strategy** (16 + hub): syntax, primops, precedence, shadowing,
where-clauses, dictionary-passing, functor-on-records, materialize-typeclass,
mv-type-constructor, nondeterministic-mv, type-aliases, target-users,
value-proposition, vertical-slice-testing, singleton-types, liftable-kind

### Index vocabulary updates

New tags: `call-by-value`, `paper`, `pipeline`, `operator`, `invariant`,
`pattern-matching`, `session-types`, `continuation`, `abstract-machine`, `search`,
`technique`, `obstacle`, `decided`, `rejected`, `recursion`, `iteration`, `fixpoint`,
`coroutine`, `graph-rewriting`, `codata`, `lowering`

New tag aliases: `strict`→`call-by-value`, `eager`→`call-by-value`, `cbv`→`call-by-value`,
`reference`→`paper`

New tag groups: Compilation, Control, expanded Foundations, expanded Purpose, expanded Structure

New edge labels: `cites`, `formalizes`, `constrained-by`, `resolved-by`, `compiles-to`

### Meta workflow

Created [[design-to-implementation.meta]] documenting the pipeline: discussion → zettels →
hub → plan → queue → ADR → update. Key principle: hubs outlive plans.

Updated CLAUDE.md, AGENTS.md, /load skill to instruct agents to read meta zettels at
session start.

Total zettelkasten: 491 zettels (up from ~380 at session start).

---

## session:a4c44992 (continued) — 2026-04-12 through 2026-04-13 [language-expressiveness, recursion, design]

Continued recursion design. Focused on the `repeat` typing problem: how to statically
enforce that repeat values aren't consumed by non-tail expressions.

### Repeat typing exploration

Explored five approaches for static enforcement of repeat:

1. **Tail-position tracking** — rejected: per-case flag threading in elaborator, every
   expression form must know about the flag.
2. **ATP / answer-type polymorphism** — studied yap compiler (`~/Workspace/panlogion/yap`)
   as reference. The mechanism (delimitation stack, answer type swap at shift) prevents
   non-tail shift when types mismatch. But repeat doesn't change the answer type like
   shift does — the mapping isn't direct. Promising but not fully solved.
3. **Grammar restriction** — fallback option. `repeat` as arm-body form, not expression.
   Simple but rejects valid programs (eta-expansion).
4. **RepeatSignal/onFailure** — evaluation-only via ActionListener failure channel. Clean
   jump mechanism but zero static enforcement.
5. **`Repeat a` builtin TCon** — chosen. Opaque type, doesn't unify with consuming types.
   Loop classifies arms post-hoc. Known limitation: mixed-type branches fail.

[[repeat-tcon.types]] -- implements -> [[fused-loop-match.language]]
[[repeat-tcon.types]] -- tension-with -> [[mixed-type-branches.obstacle]]
[[pattern-guards.language]] -- solves -> [[mixed-type-branches.obstacle]]
[[variant-arm-typing.language]] -- solves -> [[mixed-type-branches.obstacle]]
[[answer-type-polymorphism.types]] -- explored-for -> [[fused-loop-match.language]]

### Future solutions for mixed-type branches

Identified three paths (ordered by priority):
1. Pattern guards — `| pat when cond -> body`. No type system changes.
2. Variant-based arm typing — internal `#return`/`#repeat` tags. CoreLoop desugars to
   CoreMatch. Needs row-based Variants.
3. ATP dual-type tracking — parked exploration.

### Plan created

Created `recursion_phase1.plan.md` covering implicit recursion + fused loop-match.
Milestones: zettels → implicit recursion → grammar → IR → elaboration → evaluation →
serialization → verification → close-out.

SPAWN [[repeat-tcon.types]] — Repeat a builtin TCon decision
SPAWN [[repeat-design-exploration.note]] — full exploration paper trail
SPAWN [[mixed-type-branches.obstacle]] — known limitation from Repeat a approach
SPAWN [[pattern-guards.language]] — future solution for conditional repeat
SPAWN [[variant-arm-typing.language]] — future solution via internal variant tags
SPAWN [[recursion-phase1.implementation]] — implementation zettel
SPAWN [[recursion-phase1.queue]] — queue zettel

---

## session:recursion-closeout — 2026-04-13 [language-expressiveness, recursion, close-out]

Closed out `recursion_phase1.plan.md` after reconciling shipped code/tests/docs with the
zettelkasten artifacts.

Implemented-and-verified coverage now includes:
- implicit recursion via CoreLet backpatching (tying-the-knot)
- guarded recursion rejection outside function bodies
- `loop` / `repeat` grammar, IR, elaboration, evaluation, and serialization guards
- javaRest integration tests for recursion + loop/repeat behavior and rejection cases

Paper-trail reconciliation updates:
- plan todos marked complete in `.cursor/plans/recursion_phase1.plan.md`
- queue checklist synced in `[[recursion-phase1.queue]]`
- current-state documentation updated to include Recursion Phase 1 capabilities
- debug scripts extended with recursion/loop examples for `/dev` and `/eval`
- multi-node debug script now includes explicit remote recursion capture coverage

Confirmed and created new zettels from implementation discussion:
- `[[recursive-closure-shipping.coordination]]`
- `[[cross-node-testing-layers.principle]]`
- `[[recursion-closeout.session]]`

[[recursion-phase1.implementation]] -- verified-by -> `PiescriptIT` recursion + loop/repeat javaRest tests
[[recursion-phase1.queue]] -- synchronized-with -> `recursion_phase1.plan.md` todos
[[current-state.md]] -- updated-for -> [[recursion.hub]]
[[recursive-closure-shipping.coordination]] -- validates -> [[recursion.hub]]
[[cross-node-testing-layers.principle]] -- refines -> [[vertical-slice-testing.principle]]

SPAWN [[recursive-closure-shipping.coordination]] — cross-node recursion capture seam for shipped closures
SPAWN [[cross-node-testing-layers.principle]] — layered test rule for distributed features
SPAWN [[recursion-closeout.session]] — implementation closeout summary session note

RESOLVED [[recursion-phase1.queue]] — all checklist items complete and synced with plan
RESOLVED `recursion_phase1.plan.md` close-out — docs, thread, debug scripts, and verification reconciled
RESOLVED new-zettels confirmation — user approved and zettels created for recursion closeout learnings
RESOLVED cycle-aware closure serialization shipped (not deferred) — [[cycle-detection.serialization.infrastructure]] + [[reference-table-encoding.technique]] added 2026-05-04 reconciliation

ENQUEUE [[action-prefix-rename.infrastructure]] — 2026-05-06: starting a node surfaced `WARN invalid action name [cluster:compute/piescript]`; D-055's custom prefix isn't in `TransportService.VALID_ACTION_PREFIXES`. Cosmetic today, hard error pending. Tech debt; will need ADR to supersede D-055.

SPAWN [[dynamic-field-types.data]] + [[unmapped-field-surfacing.data]] + [[use-with-annotations.data]] — 2026-05-07: `kibana.alert.risk_score` missing from `_field_caps` motivated splitting "field set unknown to caps" into two paths (auto-surface partial-mapping via `include_unmapped`; user `with { ... }` annotation). Verification depths and Maybe-vs-T linked to [[null-as-bottom.types]]. All deferred pending verification of the immediate field-caps behaviour.

RESOLVED `List.concat` builtin shipped 2026-05-07 — addresses immediate list concat gap; operator form `++` deferred to [[concat-operators.language]] (new). [[string-concat.language]] reframed; [[watchlist-cross-ref.example]] note updated.

---

## session:2026-06-10 [cleanup, data]

RESOLVED `ResolvedMapping.partiallyUnmappedFields` — dropped in commit 17d849d (2026-06-04); `ResolvedMapping` narrowed to `(indexPattern, fieldMap)`. Broader unknown-field surfacing remains deferred: [[unmapped-field-surfacing.data]] + [[dynamic-field-types.data]].
---

## session:skill-canonicalization — 2026-06-10 [meta, tooling, workflow]

Created the `zettelkasten` agent skill and flipped process docs to **skill-canonical**: skills
under `<plugin>/.claude/skills/` (Cursor symlinks under `.cursor/skills/`) are now the single
source of truth for *procedure*; meta zettels keep the *rationale* and link back via the new
`skill:` ref prefix (added to README.md / index.md ref tables). Fixed stale
`docs/design-space/` → `docs/z-piescript/` paths in the elasticsearch-repo docs (`CLAUDE.md`,
`docs/AGENTS.md`, `docs/presentation.md`, `load` + `create-plan` skills) and in this
zettelkasten (`index.md` vault path, [[thread-queue-system.meta]] thread/queue paths).

[[thread-queue-system.meta]] -- procedure-extracted-to -> skill:zettelkasten
[[implementation-plan-workflow.meta]] -- procedure-extracted-to -> skill:create-plan
[[design-to-implementation.meta]] -- refers-to -> skill:zettelkasten, skill:create-plan
[[cursor-plan-template.meta]] -- refers-to -> skill:create-plan

RESOLVED Zettelkasten interaction skill (global queue) — `skill:zettelkasten` created; "skill vs CLAUDE.md guidance?" answered: skill, with CLAUDE.md/AGENTS.md pointing at it
RESOLVED stale `docs/design-space/` references in live docs — renamed directory now consistently `docs/z-piescript/` (archive and historical thread/session records left untouched)

[[data-access-restructure.session]] -- content-preserved-in -> README.md — file-naming avoid-redundancy guidance ported from index.md
RESOLVED `index.md` — deleted 2026-06-10: fully superseded by README.md + VOCABULARY.md + WORKFLOW.md (manifest entry points); unique file-naming guidance ported to README.md § File naming

---

## session:mv-channels-error-semantics — 2026-06-10/11 [error-handling, coordination, language, meta]

Error-handling design exploration that uncovered two intent-vs-implementation gaps and a
migration-fidelity pattern. Established: MV (queue) channels are THE channel model (single-value
`SubscribableListener` is an interim stand-in — replacement, not extension; not streaming, no
backpressure — data-plane streaming is Exchange's concern); `when` was intended as a
non-blocking standing reaction rule, and the implemented when-as-expression (suspends the
program continuation; one-shot) is a bug never recorded as a decision (Block A plan struct
spec; D-041 silent on it). Code-verified: when suspends via CoreLet CPS sequencing
(Evaluator.java:111, EvalCoordination.java:30); block expr-stmts silently dropped
(Blocks.java:74, asserted by ElaboratorTests:497 — intentional in the pure Phase 1 language,
bug since effects arrived; legit use case now: applications of effect-wrapping fns); remote
closure death → WARN only → orphaned channel hangs waiters. Recovered pre-trim vision (git
3abf7ab6a679): "multiple when clauses fire simultaneously". Errors-as-messages confirmed as
settled direction (BEAM trap_exit/monitors, distributed JC failure detection — verified
externally); single-value-era constructs (recover clause, dual-channel pairs, or-rules)
explored and parked. Open questions (err inbox role, routing without supervision, runtime vs
user-space responsibility, termination protocol, all API shapes) deliberately NOT recorded —
under live discussion.

[[when-expression-blocking.bug]] -- deviates-from -> [[when-reaction-rules.coordination]]
[[multi-value-channels.coordination]] -- replaces -> [[channels.infrastructure]] (interim impl)
[[multi-value-channels.coordination]] -- blocks -> [[error-channels.coordination]]
[[cham-patterns.coordination]] -- extends -> [[when-reaction-rules.coordination]] — scope narrowed to the speculative generalization
[[non-blocking.principle]] -- part-of -> [[design-principles.hub]] — 7th principle
[[channel-lifecycle.infrastructure]] -- corrected -> registry entries are never removed (code contradicted the zettel)

SPAWN [[when-reaction-rules.coordination]] — intended when semantics, recovered from pre-trim vision
SPAWN [[when-expression-blocking.bug]] — defect record for when-as-expression
SPAWN [[expr-statements.language]] — block expr-stmt silent drop + fix-needs-design
SPAWN [[non-blocking.principle]] — promoted from vision.md one-liner
SPAWN [[migration-status-fidelity.meta]] — coverage-survives-status-doesn't pattern (3 instances)

ENQUEUE [[expr-statements.language]] — fix design (rejection wrong; `let _` desugar candidate)
ENQUEUE [[migration-status-fidelity.meta]] — archived-plan sweep for trapped intent
ENQUEUE streams→sequences rewording in MV channel descriptions
ENQUEUE MV channel + when reaction-rules design session — produces the ADR superseding Block A's implicit semantics

---

## session:mv-channels-error-semantics (continued) — 2026-06-11 [error-handling, coordination, language, decisions]

Resolved the open questions from the first block via live discussion; recorded as **D-056**
(errors as messages — minimal runtime contract) and **D-057** (process identity — root TaskId
on the causal chain). Settled: per-node err inbox is the MAIN runtime mechanism (not fallback),
an ordinary consume channel; supervision is user-space piescript (forwarder rules + locality
routing; OTP-as-library precedent); "death notification" is nothing — just the err message
replacing the WARN at TransportPiescriptSendAction:127; introspection dropped from the core
pattern (handlers hold their own channel refs). Uniform CONSUME semantics with selective
matching for all MV channels (JC tutorial verified: "each message fulfills at most one call");
broadcast = user-space state-as-message distributor; identical patterns compete (work queue).
Identity: root TaskId by value on the causal chain (wire field + setParentTask); self = deps
constant + closure capture; sender-side minting of per-task refs left open. Writing the syntax
exposed the non-linear pattern problem: bound variables in patterns BIND, not compare →
pattern guards promoted to hard prerequisite (second consumer after mixed-type-branches);
guards participate in the consumption transaction; guard keyword `when` collides with channel
`when` (`if` candidate). Idris `with`-rule ergonomics parked as research.

[[errors-as-messages.coordination]] -- refines -> [[error-channels.coordination]] — settles the open architecture
[[process-identity.coordination]] -- prerequisite-for -> [[errors-as-messages.coordination]]
[[process-identity.coordination]] -- motivates -> [[pattern-guards.language]] — runtime ids unfilterable by literal patterns
[[pattern-guards.language]] -- constrains -> [[join-automaton.coordination]] — consume only on pattern+guard
[[multi-value-channels.coordination]] -- settled -> consume + selective matching (D-056)
[[bound-variable-patterns.language]] -- alternative-to -> [[pattern-guards.language]] — ergonomics research later

SPAWN [[errors-as-messages.coordination]] — the settled D-056 architecture
SPAWN [[process-identity.coordination]] — the settled D-057 identity design
SPAWN [[error-handling-patterns.example]] — multi-tenancy/forwarder/work-queue/distributor/supervision programs
SPAWN [[bound-variable-patterns.language]] — non-linear pattern problem + Idris-with research anchor

ENQUEUE [[process-identity.coordination]] — D-057 implementation slice (first iterable step)
ENQUEUE [[bound-variable-patterns.language]] — speculative ergonomics research session

RESOLVED err-inbox role (main mechanism, not fallback) — D-056
RESOLVED error routing without supervisor model (routing home IS supervision; user-space) — D-056
RESOLVED runtime vs user-space responsibility split (minimal contract) — D-056
RESOLVED MV consumption semantics (consume + selective matching; broadcast as library) — D-056
RESOLVED identity mechanism (root TaskId, causal chain, capture-as-self) — D-057
RESOLVED "death notification" definition (just the err message; no subsystem) — D-056

---

## session:rdd-lineage-connection — 2026-06-11 [comparable, fault-tolerance, coordination]

Brief Q&A on RDDs surfaced a gap: lineage-based recomputation (Spark's distinctive
fault-tolerance contribution) was never explicitly considered-and-rejected in D-056's
alternatives — it was implicitly foreclosed by the D-040/D-042 explicit-distribution fork
(the runtime cannot know how to recompute under user-controlled distribution). The idea
resurfaces in user space: a supervisor re-sending a pure closure is manual lineage replay,
safe for the same purity reasons as in Spark. Recorded as edges only (no new zettel).

[[spark.comparable]] -- informs -> [[errors-as-messages.coordination]] — lineage replay vs errors-as-messages
[[errors-as-messages.coordination]] -- contrasts-with -> [[spark.comparable]] — revisit when supervision patterns are designed

---

## session:doc-gap-backfill — 2026-06-26 [documentation, meta, references, examples]

Gap analysis across `docs/*.md` vs z-piescript zettelkasten (9 parallel subagents, results
verified). Three subagent "trapped" findings were wrong (free-monad, RawData/Page/Value,
channel-ref mobility — all already in ZK). Actions taken: created 3 missing paper zettels,
`scripts/references.py` to regenerate references.md on demand from paper-tagged zettels,
and 3 new example zettels (Tier 2 runnable risk scoring, distributed vertical slice with
corrected API, multi-source enrichment with record-update noted as aspirational).

[[stark-fiore-free-algebra.paper]] -- part-of -> [[papers.hub]]
[[milner-communicating-mobile-systems.paper]] -- part-of -> [[papers.hub]]
[[sangiorgi-walker-pi-calculus.paper]] -- part-of -> [[papers.hub]]
[[risk-scoring-runnable.example]] -- example-of -> [[risk-score-pattern.data]]
[[distributed-vertical-slice.example]] -- example-of -> [[code-mobility.coordination]]
[[multi-source-enrichment.example]] -- example-of -> [[enrich-unification.external]]
[[papers.hub]] -- updated -> added 3 new includes

SPAWN [[stark-fiore-free-algebra.paper]] — missing paper zettel (TCS 2008; free-algebra models for pi-calculus)
SPAWN [[milner-communicating-mobile-systems.paper]] — missing Milner 1999 textbook zettel
SPAWN [[sangiorgi-walker-pi-calculus.paper]] — missing Sangiorgi & Walker 2001 textbook zettel
SPAWN [[risk-scoring-runnable.example]] — Risk Tier 2: runnable today, Index.bulk write, no unimplemented sinks
SPAWN [[distributed-vertical-slice.example]] — distributed example with corrected Cluster.topology API
SPAWN [[multi-source-enrichment.example]] — enrichment vision with record-update noted as aspirational

ENQUEUE replace flat docs/references.md with generated dist/REFERENCES.md (run references.py --markdown > dist/REFERENCES.md and wire into CI)
ENQUEUE fix docs/presentation.md Example D API (topology → Cluster.topology, local_node → removed per [[inbox-dependency-injection.coordination]])
