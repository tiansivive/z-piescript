---
tags: [coordination, language, concept, needs-design, now]
refs:
  - thread:distributed-coordination
  - thread:error-handling
  - session:mv-channels-error-semantics
---
# When as Reaction Rules

The intended semantics of `when`: a **non-blocking standing reaction rule**, not an expression.
Evaluating a `when` clause *registers* the rule and program evaluation continues; the rule fires
when its channel pattern is satisfiable, and — being a standing rule — re-arms and fires again
for subsequent messages. Multiple `when` clauses coexist in one program, each an independent
rule. Recovered from the pre-thread-restructure vision (git `3abf7ab6a679`, § Functional-Pattern
Matching on Channels): "Multiple `when` clauses watching the same channels can fire
simultaneously from a single scheduler run."

This is the Join Calculus definition/process reading of join patterns (JoCaml reaction rules),
as opposed to the await/unwrap expression reading that Block A implemented (see
[[when-expression-blocking.bug]]). Two layers:

- **Baseline** (this zettel): presence-firing — a rule fires when each joined channel has a
  message; conjunctive `&` patterns consume one message per channel atomically. This is what
  the MV channel design must deliver.
- **Generalization** (separate, speculative): Curry-style functional patterns over message
  stores — [[cham-patterns.coordination]].

**Settled (2026-06-11, D-056)**: consumption between rules sharing a channel = consume
semantics with selective matching — a rule consumes only messages matching its pattern AND
guard; identical patterns compete (committed choice, [[join-automaton.coordination]]); guards
participate in the consumption transaction. Pattern guards are therefore a hard prerequisite
([[pattern-guards.language]]) — runtime-assigned identity cannot be filtered by literal
patterns ([[bound-variable-patterns.language]]).

Open design questions (for the MV design session): what a program's *result* is once `when`
no longer returns a value (the actor-model answer — results delivered via channels — is the
likely direction, see [[actor-model.lifecycle]]); rule retirement/scope.

**Depends on**: [[multi-value-channels.coordination]], [[join-calculus.coordination]]
**Enables**: [[error-channels.coordination]], [[fold-as-join.coordination]]
**Connections**:
- supersedes: [[when-synchronization.coordination]] — the implemented one-shot expression form is interim; this records the intended semantics
- implements: [[non-blocking.principle]] — registration-not-suspension is what non-blocking means for synchronization
- extends: [[join-automaton.coordination]] — the automaton is the efficient implementation of standing rules over message stores
- specializes: [[cham-patterns.coordination]] — CHAM functional patterns generalize the presence-firing baseline recorded here
- informs: [[actor-model.lifecycle]] — persistent rules are the execution model long-lived actors need
