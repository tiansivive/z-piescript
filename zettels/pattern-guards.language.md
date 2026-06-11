---
tags: [language, syntax, control-flow, pattern-matching, open, needs-design, next, blocker]
refs:
  - adr:D-056
  - thread:language-expressiveness
  - thread:error-handling
  - session:mv-channels-error-semantics
---
# Pattern Guards

Guards on match and loop arms: `| pat when cond -> body`. The guard expression is evaluated
after the pattern matches but before the arm body. If the guard is false, the next arm is
tried.

**Promoted to hard prerequisite of error handling (2026-06-11, D-056).** Second independent
consumer after the conditional-repeat problem: selective consumption on the err inbox filters
on **runtime-assigned** identity ([[process-identity.coordination]]), which literal patterns
cannot express and bound variables in patterns would shadow rather than compare
([[bound-variable-patterns.language]]). `when (errs e) if e.program == me -> ...` is the only
v1-expressible form. Two new requirements this adds:
- **Guards participate in the consumption transaction**: under consume-semantics channels, a
  rule consumes a message only when pattern AND guard pass; guard failure must leave the
  message in the store ([[join-automaton.coordination]] input).
- **Keyword choice needs care**: this zettel's sketch uses `| pat when cond`, but guard-`when`
  inside channel-`when` rules collides (`when (errs e) when ... ->`); `if` is the candidate
  (`when (errs e) if cond -> ...`).

Solves the conditional-repeat problem without mixed-type branches:

```piescript
loop { acc: [], key: "" }
| { acc, key } when List.isEmpty (query_page key) -> acc
| { acc, key } -> repeat { acc: acc ++ query_page key, key: ... }
```

Without guards, this requires either separate patterns that distinguish the cases structurally,
or mixed-type branches (which fail with `Repeat a` TCon approach). Guards decouple the
condition from the pattern, making loop arms more expressive.

Higher priority than [[variant-arm-typing.language]] for solving the conditional-repeat
problem — simpler, no type system changes needed, familiar syntax (Haskell, Erlang, OCaml).

**Depends on**: [[pattern-matching.hub]]
**Enables**: (none directly)
**Connections**:
- part-of: [[pattern-matching.hub]]
- solves: [[mixed-type-branches.obstacle]] — guards avoid mixed-type branches entirely by separating conditions into distinct arms
- enhances: [[fused-loop-match.language]] — conditional repeat becomes natural with guarded arms
- enhances: [[match-syntax.language]] — extends the arm syntax with `when` clause
- uses: [[match-type-checking.language]] — guard is elaborated as Boolean, same type checking
- informs: [[exhaustiveness-checking.types]] — guards complicate exhaustiveness analysis (guard may always be false)
- contrasts-with: [[variant-arm-typing.language]] — guards solve the problem at the syntax level; variants solve it at the type level
- prerequisite-for: [[errors-as-messages.coordination]] — guard-filtered consumption is the multi-tenancy mechanism on the err inbox
- constrains: [[join-automaton.coordination]] — consumption fires only on pattern+guard success
- complemented-by: [[bound-variable-patterns.language]] — possible future ergonomic sugar for the equality-filtering case
