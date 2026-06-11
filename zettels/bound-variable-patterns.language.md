---
tags: [language, syntax, pattern-matching, exploration, theoretical, question, someday]
refs:
  - thread:language-expressiveness
  - session:mv-channels-error-semantics
---
# Bound-Variable Patterns (Non-Linear Matching)

The non-linear pattern problem: in a pattern, an identifier is a **binder** — `{ program: me }`
captures the field into a fresh `me`, shadowing any outer binding. It cannot *compare* against
an already-bound variable. Consequence discovered while writing the error-filtering examples:
**runtime-assigned identity + literal-only patterns = cannot filter at all** — you can match
`{ program: "risk-scorer" }` but never `{ program: <my runtime id> }`.

Prior art:
- **Erlang**: bound variables in patterns implicitly match by equality — why pid-filtering in
  selective receive feels effortless.
- **Elixir**: explicit pin operator `^me` to opt into equality instead of rebinding.
- **Curry**: non-linear patterns (repeated variables) with equality semantics, via the
  functional-logic foundation — relevant given [[curry-narrowing.language]] is already in the
  design space.

**First step (settled)**: [[pattern-guards.language]] — `when (errs e) if e.program == me ->`
covers the case with no pattern-semantics changes and is strictly more general (arbitrary
conditions, not just equality).

**Speculative (this zettel's reason to exist)**: better ergonomics than guards for the
equality case — pin syntax, Erlang-style implicit equality for bound names, or co-opting
dependently-typed-language machinery *without* dependent types: Idris's `with` rule (matching
on intermediate computations, views) and view-pattern-like constructs suggest a path where the
"pattern" is partially computed from in-scope values. Research session to explore what subset
transfers to an HM + rows setting. Until then, guards are the answer.

**Depends on**: [[pattern-matching.hub]], [[pattern-guards.language]]
**Enables**: (none — exploration)
**Connections**:
- alternative-to: [[pattern-guards.language]] — sugar for the equality-filtering case guards already cover
- motivated-by: [[process-identity.coordination]] — matching runtime-assigned ids is the concrete driver
- related: [[curry-narrowing.language]] — functional-logic non-linear patterns are the theoretical neighbor
- informs: [[pattern-reuse.language]] — when-binding patterns inherit whatever non-linearity story lands
- related: [[exhaustiveness-checking.types]] — equality patterns complicate coverage analysis the same way guards do
