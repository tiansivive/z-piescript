---
tags: [language, tech-debt, task, ready, next]
refs:
  - roadmap:phase-1-tech-debt
  - session:80f0b64a-5e21-4b2e-acda-fabde482cc87
  - thread:language-expressiveness
---
# String Concat

No way to concatenate `Keyword` values today. List concat is solved at the
builtin level (`List.concat`); the equivalent for strings (`Keyword.concat`)
is not yet shipped.

Operator forms (`<>` for strings, `++` for lists) are deferred to
[[concat-operators.language]] — they would be sugar over the builtins,
ideally as Semigroup typeclass methods.

**Depends on**: [[keyword-string.types]]
**Enables**: (none directly)
**Connections**:
- prerequisite-for: [[concat-operators.language]] — `Keyword.concat` builtin needed before `<>` operator
- uses: [[keyword-string.types]] — operates on KeywordVal String representation
- blocks: some user programs that need to build strings dynamically
