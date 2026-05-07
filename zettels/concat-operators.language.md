---
tags: [language, syntax, operator, types, typeclasses, open, concept, needs-design, later]
refs:
  - thread:language-expressiveness
---
# Concat Operators

Infix sugar for concat: `++` for `List a`, `<>` for `Keyword`. Long-term both
are Semigroup-typeclass methods; today the underlying builtins are
`List.concat` (shipped) and `Keyword.concat` (not yet shipped — see
[[string-concat.language]]).

Three obstacles to shipping the operators today:

- **Without typeclasses**, overloaded `++`/`<>` requires either two
  monomorphic operators (one per type) or hardcoded dispatch in the
  elaborator. Both are warts.
- **With typeclasses**, operators desugar cleanly to `Semigroup.<>`, but
  typeclass machinery is not on a near-term thread.
- Operator plumbing (lexer token, precedence, IR/printer/serializer) — small
  but multi-file.

Pragmatic path: ship the underlying builtins now (`List.concat` done,
`Keyword.concat` next), add the operator form when typeclasses arrive or on
a smaller hardcoded-dispatch proof of concept.

**Depends on**: [[typeclass-instances.types]]
**Enables**: (none directly — sugar over existing builtins)
**Connections**:
- part-of: [[language-expressiveness.thread]]
- sugar-over: `List.concat` (shipped), `Keyword.concat` (future per [[string-concat.language]])
- prerequisite-for: ergonomic list/string composition
- related: [[typeclass-instances.types]] — Semigroup would unify `++` and `<>`
```
