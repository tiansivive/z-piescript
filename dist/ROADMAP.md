# Roadmap Threads (7 threads, 87 items)

## Data Completeness (1 implemented, 2 designed, 14 open)

> From finishing Block G tests to handling every ES data type correctly. This thread covers the gaps between piescript's current data handling and what real-world ES indices require — timestamps, multi-value fields, proper string handling, ESQL coverage, and infrastructure hardening.

| Priority | Status | Item |
|----------|--------|------|
| next | ○ | Empty Mapping Diagnostics |
| next | ○ | DateTime |
| next | ◐ | Block H — Multi-Value Field Semantics |
| next | ◐ | Multi-Value Fields (Block H) |
| later | ○ | Column Name Derivation |
| later | ○ | Circuit Breaker Integration |
| later | ○ | ESQL TopBy |
| later | ○ | Keyword String |
| later | ○ | Keyword BytesRef Conversion |
| later | ○ | ESQL Body Parser |
| later | ○ | ESQL LOOKUP JOIN |
| later | ○ | Logical Plan Compilation |
| later | ○ | MV Type Constructor |
| needs-design | ○ | Unmapped Field Surfacing |
| needs-design | ○ | Use With Annotations |
|  | ○ | Dynamic Field Types |
| now | ✓ | Block G — Streaming Data Access via Compute Engine |

## Distributed Coordination (7 open)

> From multi-value channels to actor-model lifecycle and supervised long-lived computations. This thread replaces the interim single-value channel implementation with the intended queue model, and extends the Join Calculus coordination layer toward persistent identity, scheduled execution, and fault-tolerant distributed processes.

| Priority | Status | Item |
|----------|--------|------|
| now | ○ | Multi-Value Channels |
| now | ○ | When as Reaction Rules *(shared: error-handling)* |
| later | ○ | Channel Lifecycle *(shared: error-handling)* |
| later | ○ | Dynamic Fan-Out |
| later | ○ | Fold as Join Pattern |
| later | ○ | Scheduled Execution |
| later | ○ | Join Automaton |

## Error Handling & Fault Tolerance (3 implemented, 2 designed, 15 open)

> From source-location error messages to OTP-style supervision trees. This thread covers the full spectrum of how piescript handles, reports, and recovers from errors — spanning type-level safety (Result/Option), runtime diagnostics (error provenance), resource cleanup (bracket patterns), and distributed fault tolerance (sagas, supervision).

| Priority | Status | Item |
|----------|--------|------|
| now | ○ | Multi-Value Channels *(shared: distributed-coordination)* |
| now | ○ | When as Reaction Rules *(shared: distributed-coordination)* |
| next | ◐ | Errors as Messages — Minimal Runtime Contract |
| next | ◐ | Process Identity |
| next | ○ | Pattern Guards *(shared: language-expressiveness)* |
| next | ○ | Error Provenance |
| next | ○ | Forall Type *(shared: type-foundations)* |
| next | ○ | Algebraic Data Types *(shared: language-expressiveness)* |
| ready | ○ | Pattern Matching *(shared: language-expressiveness)* |
| later | ○ | Result Types |
| later | ○ | Bracket Patterns |
| later | ○ | Channel Lifecycle *(shared: distributed-coordination)* |
| later | ○ | Create vs Index |
| later | ○ | Exhaustiveness Checking *(shared: language-expressiveness)* |
| later | ○ | Write Context |
| needs-design | ○ | Error Channels |
|  | ○ | Error Handling Patterns — Syntax Examples |
| later | ✓ | Null as Bottom |
| later | ✓ | Fire-and-Forget Send Semantics |
|  | ✓ | Pattern Matching Phase 1 Implementation *(shared: language-expressiveness)* |

## External Interaction (2 open)

> How piescript programs interact with the outside world — other services, users, and systems beyond Elasticsearch. Three layers: plugin SPI (typed builtins from Java), FFI (Painless allowlist for ad-hoc JVM access), and the actor model (persistent script identity with REST-exposed channels). Culminates in unifying Transforms, Watcher, and ingest pipelines under a single typed language.

| Priority | Status | Item |
|----------|--------|------|
|  | ○ | Multi-Source Enrichment Example |
|  | ○ | Incremental Risk Scoring Example |

## Language Expressiveness (6 implemented, 1 designed, 22 open)

> From recursion and string concat to typeclasses, comprehensions, and a module system. This thread covers the features that make piescript expressive enough to write real programs — control flow, data manipulation operators, abstraction mechanisms, and reusable definitions.

| Priority | Status | Item |
|----------|--------|------|
| now | ○ | Recursion |
| now | ○ | Recursion Phase 1 Implementation |
| next | ○ | String Concat |
| next | ○ | Algebraic Data Types *(shared: error-handling)* |
| next | ○ | Pattern Guards *(shared: error-handling)* |
| ready | ○ | Pattern Matching *(shared: error-handling)* |
| later | ○ | GroupBy Combinator |
| later | ○ | Traverse Combinator |
| later | ○ | Comprehension Syntax |
| later | ○ | Recursive Types *(shared: type-foundations)* |
| later | ○ | Concat Operators |
| later | ○ | Exhaustiveness Checking *(shared: error-handling)* |
| later | ○ | Pattern Reuse |
| later | ○ | Record Spread |
| later | ○ | Type Aliases *(shared: type-foundations)* |
| later | ○ | Variant-Based Arm Typing |
|  | ◐ | Data Access |
|  | ○ | Implicit Recursion |
|  | ○ | List.map / Traverse Tension |
|  | ○ | Mixed-Type Branches |
|  | ○ | Recursion Closeout Session |
|  | ○ | Repeat a — Builtin Type Constructor |
|  | ○ | Watchlist Cross-Reference — Real-World Example |
|  | ✓ | CoreMatch |
|  | ✓ | Fused Loop-Match |
|  | ✓ | Match Syntax |
|  | ✓ | Match Type Checking |
|  | ✓ | Pattern Matching Phase 1 Implementation *(shared: error-handling)* |
|  | ✓ | Pattern Types |

## Ownership & Resources (empty)

> From QTT linearity through ownership semantics to safe mutable shared state and persistent in-memory resources. This thread covers what QTT multiplicities unlock beyond channels and session types — the Rust-inspired ownership model adapted to a functional distributed language. All items depend on QTT linearity from the Type Foundations thread.

## Type Foundations (1 implemented, 11 open)

> From fixing the Forall type representation to QTT linearity and session types. This thread covers the evolution of piescript's type system beyond the current Hindley-Milner + F-omega-lite foundation — filling tech debt gaps, adding new type-level features, and building toward the long-term vision of linear types and session-typed channels.

| Priority | Status | Item |
|----------|--------|------|
| next | ○ | Forall Type *(shared: error-handling)* |
| next | ○ | Bidirectional Checking |
| next | ○ | Resolve Deep |
| later | ○ | Environment-Carrying Instantiation |
| later | ○ | Recursive Types *(shared: language-expressiveness)* |
| later | ○ | Type Narrowing |
| later | ○ | Runtime Dispatch |
| later | ○ | Lacks Constraint |
| later | ○ | Label Kind |
| later | ○ | Type Aliases *(shared: language-expressiveness)* |
| needs-design | ○ | Liftable Kind |
| ready | ✓ | Zonker |

