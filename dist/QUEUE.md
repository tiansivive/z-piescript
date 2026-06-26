## Global Pending Queue (15 open)

- [ ] Backfill thread.md — add retroactive session blocks for prior sessions (best-effort from transcripts)
- [ ] [[es-conventions-debt.infrastructure]] — TransportVersion, logging, ActionListener patterns, dedicated thread pool (production punch list)
- [ ] [[lsp.tooling]] — Language Server Protocol implementation
- [ ] [[syntax-highlighting.tooling]] — syntax highlighting definitions
- [ ] [[repl.tooling]] — REPL / interactive evaluation mode
- [ ] [[action-prefix-rename.infrastructure]] — `PiescriptAction.NAME = "cluster:compute/piescript"` is not in `TransportService.VALID_ACTION_PREFIXES`; ES logs WARN at startup and has a TODO to promote it to a hard error. Rename to `cluster:admin/piescript/eval` (or similar) and supersede D-055
- [ ] [[dynamic-field-types.data]] — fields missing from the merged field-caps view (sparse / user-known runtime fields) can't be referenced today. Two paths drafted: [[unmapped-field-surfacing.data]] (sparse, automatic, also resolves the `partiallyUnmappedFields` cleanup) and [[use-with-annotations.data]] (general, `use ... with { ... }` syntax)
- [ ] [[expr-statements.language]] — block expr-stmts silently dropped (Blocks.java:74, asserted by `testBlockWithExprStmt`); fix needs design (rejection is wrong: applications of effect-wrapping fns are legit); flip the test with the fix
- [ ] [[migration-status-fidelity.meta]] — sweep remaining archived plans/docs (phase3/phase4 plans, pre-join-calculus docs) for trapped design intent
- [ ] Reword "streams of messages" → "sequences of messages" where MV channels are described (architecture.md § Future: Multi-Value Channels; vision pointers) — kills the streaming-conflation attractor
- [ ] MV channel + `when` reaction-rules design session — [[multi-value-channels.coordination]], [[when-reaction-rules.coordination]]; produces the ADR superseding Block A's implicit when-as-expression semantics
- [ ] [[process-identity.coordination]] — implement the D-057 identity slice: `programId` (root TaskId) on `EvalDependencies` + `PiescriptSendRequest` wire field + `setParentTask` in `sendRemote` + threading in `handleInbox`; WARN log gains attribution; follow-on: `ChannelRegistry` ownership tagging
- [ ] [[bound-variable-patterns.language]] — speculative research session: non-linear / pin-pattern ergonomics beyond guards (Erlang implicit equality, Elixir `^`, Idris `with`-rule inspiration without dependent types)
- [ ] Replace flat `docs/references.md` with generated `dist/REFERENCES.md` — run `python3 scripts/references.py --markdown > dist/REFERENCES.md` and wire into CI; then delete the hand-maintained flat file
- [ ] Fix `docs/presentation.md` Example D API: `topology "my-index"` → `Cluster.topology "my-index"`, remove `local_node` reference (use inbox arg `info` per [[inbox-dependency-injection.coordination]])

## Pattern Matching Phase 1 Queue (0 open)


## Recursion Phase 1 Queue (0 open)


## Data Completeness (13 pending)

- [next] Empty Mapping Diagnostics (tech-debt)
- [needs-design] DateTime (open)
- [needs-design] Block H — Multi-Value Field Semantics (designed)
- [needs-design] Multi-Value Fields (Block H) (designed)
- [later] Column Name Derivation (open)
- [later] Circuit Breaker Integration (tech-debt)
- [later] ESQL TopBy (open)
- [later] Keyword String (tech-debt)
- [later] Keyword BytesRef Conversion (tech-debt)
- [later] ESQL Body Parser (tech-debt)
- [later] ESQL LOOKUP JOIN (open)
- [later] Logical Plan Compilation (open)
- [someday] Numeric Precision (open)

## Distributed Coordination (10 pending)

- [needs-design] Multi-Value Channels (open)
- [needs-design] When as Reaction Rules (open)
- [needs-design] Actor Model Lifecycle (designed)
- [needs-design] Named Channels (designed)
- [later] Channel Lifecycle (tech-debt)
- [later] Dynamic Fan-Out (open)
- [later] Fold as Join Pattern (open)
- [later] Scheduled Execution (open)
- [someday] CHAM Patterns (open)
- [someday] Long-Lived Computations (open)

## Error Handling & Fault Tolerance (17 pending)

- [next] Errors as Messages — Minimal Runtime Contract (designed)
- [next] Process Identity (designed)
- [next] Error Provenance (tech-debt)
- [next] Forall Type (tech-debt)
- [ready] Pattern Matching (open)
- [blocked] Create vs Index (blocked)
- [needs-design] Multi-Value Channels (open)
- [needs-design] When as Reaction Rules (open)
- [needs-design] Error Channels (open)
- [needs-design] Pattern Guards (open)
- [needs-design] Algebraic Data Types (open)
- [later] Result Types (open)
- [later] Bracket Patterns (open)
- [later] Channel Lifecycle (tech-debt)
- [someday] Saga Coordination (open)
- [someday] OTP Supervision (open)
-  Error Handling Patterns — Syntax Examples (open)

## External Interaction (11 pending)

- [needs-design] Plugin SPI (designed)
- [needs-design] FFI via Painless (designed)
- [needs-design] Actor Model Lifecycle (designed)
- [needs-design] Named Channels (designed)
- [needs-design] SSE Streaming (designed)
- [needs-design] Token Capability Security (open)
- [someday] Transform Unification (designed)
- [someday] Watcher Replacement (designed)
- [someday] Ingest-Time Execution (open)
- [someday] Enrich Unification (open)
- [someday] Feature Constellation (open)

## Language Expressiveness (13 pending)

- [now] Recursion (open)
- [next] String Concat (tech-debt)
- [ready] Pattern Matching (open)
- [needs-design] Algebraic Data Types (open)
- [needs-design] Push-Down Compilation (open)
- [needs-design] Query Typeclass (open)
- [needs-design] Typeclasses (open)
- [later] GroupBy Combinator (open)
- [later] Traverse Combinator (open)
- [later] Comprehension Syntax (open)
- [later] Recursive Types (open)
- [someday] Module System (open)
-  Data Access (designed)

## Ownership & Resources (6 pending)

- [someday] Ownership Semantics (open)
- [someday] Borrow Checking (open)
- [someday] Mutable Shared State (open)
- [someday] Persistent Resources (open)
- [someday] Incremental Computation (open)
- [someday] Zero-Copy Linear Transfer (open)

## Type Foundations (13 pending)

- [next] Forall Type (tech-debt)
- [next] Bidirectional Checking (tech-debt)
- [next] Resolve Deep (tech-debt)
- [needs-design] Typeclasses (open)
- [later] Environment-Carrying Instantiation (open)
- [later] Recursive Types (open)
- [later] Type Narrowing (open)
- [later] Runtime Dispatch (open)
- [later] Lacks Constraint (open)
- [later] Label Kind (open)
- [someday] Higher-Rank Polymorphism (open)
- [someday] QTT Linearity (open)
- [someday] Session Types (open)

