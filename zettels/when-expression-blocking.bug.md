---
tags: [language, coordination, bug, known-issue, implemented]
refs:
  - code:Whens.java
  - code:EvalCoordination.java
  - code:Evaluator.java
  - plan:block_a_implementation_2fdbab36
  - adr:D-041
  - session:mv-channels-error-semantics
---
# When-as-Expression Blocking

The implemented `when` is an **expression whose value is its body's result** — and that is a
bug relative to the intended semantics ([[when-reaction-rules.coordination]]), not a decision.

Mechanics (code-verified 2026-06-10):
- Typing: `Whens.java:40` — `new CoreWhen(src, bindings, body, body.type())`.
- Evaluation: `EvalCoordination.java:30-33` — when all channels deliver, the body evaluates and
  its result completes the `when` expression's own listener.
- Consequence: under call-by-value `let` sequencing (`Evaluator.java:111` — the let body
  evaluates inside the rhs's completion callback), **everything after a `when` statement is the
  `when`'s continuation**. No JVM thread blocks (CPS), but the program's operational semantics
  suspend until the channel fires. A second `when` in sequence is not even registered until the
  first fires.

How it happened: the Block A plan fixed `type is body.type()` silently inside the `CoreWhen`
struct spec; D-041 records the keyword, the async evaluator, and the positional collector — but
not this semantic choice. The plan's Known Limitations section frames channels via the JS
Promise analogy ("use `when` to unwrap channel values"), i.e. await semantics, while the vision
of the same era described standing reaction rules. The conflict was never surfaced.

Workaround visible in all debug scripts: exactly one `when` as the program's final expression;
effects bound via `let u = send ...`.

Fix lands with the MV channel / `when` redesign (registration semantics), which also reopens
the program-result question.

**Depends on**: [[when-synchronization.coordination]]
**Enables**: (none — a defect record)
**Connections**:
- deviates-from: [[when-reaction-rules.coordination]] — intended semantics
- tension-with: [[non-blocking.principle]] — suspending the continuation on a message wait violates the principle
- constrains: [[error-channels.coordination]] — one-shot expression `when` cannot express standing error handlers
- related: [[cps-evaluation.language]] — CPS is the implementation vehicle; the suspension is a semantics-level property, not a CPS artifact
