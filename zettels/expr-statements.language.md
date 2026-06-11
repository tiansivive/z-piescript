---
tags: [language, syntax, bug, needs-design]
refs:
  - code:Blocks.java
  - code:ElaboratorTests.java
  - plan:phase1_expression_language
  - session:mv-channels-error-semantics
---
# Expression Statements

Expression statements were **intentionally excluded** from the language: in a pure language,
evaluating an expression and discarding its result is dead code, so `let`-in is the sequencing
story. The top-level grammar enforces this (`program : topBinding* expr` — only `let`/`use`
statements exist at top level).

The bug is the inconsistency: the **block** grammar still admits `expr ;` as a `blockStmt`, and
the elaborator **silently drops it** — `Blocks.java:74-76` elaborates the statement for type
checking and discards the resulting `CoreExpr`. `{ send ch v; 42 }` type-checks, returns 42,
and never sends. `ElaboratorTests.java:497` (`testBlockWithExprStmt`: `{ 1; 2 }` elaborates to
bare `CoreLit`) asserts the drop, so CI enshrines it. There is no Core IR sequencing node
(blocks desugar to nested `CoreLet`; an expression statement has no desugar target).

Two aggravating subtleties (verified 2026-06-10):
- **Ghost constraints**: dropped statements are still elaborated, so their type constraints
  flow into the zonker and can shape the program's types despite not existing at runtime.
- **Quarantine by grammar**: because top level forbids expr-stmts, all real programs use
  `let u = send ...`, which is why the drop never bit in practice.

The drop was sound when written (`Blocks.java` created 2026-03-14, before effects existed —
Block A landed `spawn`/`send` days later) and became wrong by omission.

**The fix is not rejection.** Functions can wrap `send`/`when`, so an expression statement that
applies an effect-wrapping function is a legitimate use case. The semantics need design:
candidates include desugaring `e; rest` to `let _ = e in rest` (no new IR node needed) or
effect-aware acceptance. Orthogonal to the `when` semantics question — sequencing can be fixed
independently ([[when-expression-blocking.bug]]).

**Depends on**: [[block-expressions.language]], [[purity.language]]
**Enables**: (none until fixed)
**Connections**:
- part-of: [[block-expressions.language]] — the block construct is where the inconsistency lives
- tension-with: [[purity.language]] — the original exclusion rationale stopped holding once coordination effects arrived
- informs: [[multi-value-channels.coordination]] — registration-style `when` statements in blocks need working statement sequencing
