---
tags: [principle, meta, coordination, decision]
refs:
  - doc:vision.md
  - session:mv-channels-error-semantics
---
# Non-Blocking by Design

"Asynchronous by construction: coordination launches work without blocking. Results arrive on
channels" (vision.md § The Distributed Computation Model). Promoted to a principle zettel so
design and implementation work gets checked against it.

This is a statement about piescript's **operational semantics**, not about ES threads (the CPS
evaluator already never blocks a JVM thread — that is necessary but not sufficient). No
language construct may suspend the program's continuation while waiting for a message:
synchronization is *reaction* (a rule fires when messages arrive), never *awaiting* (an
expression that pauses subsequent statements until a value materializes). Pure evaluation
completes; coordination registers and reacts.

The implemented `when` violates this ([[when-expression-blocking.bug]]) — the violation went
unnoticed precisely because the principle existed only as one sentence in vision.md with
nothing checking against it.

**Depends on**: [[join-calculus.coordination]]
**Enables**: [[when-reaction-rules.coordination]]
**Connections**:
- part-of: [[design-principles.hub]]
- implements: [[join-calculus.coordination]] — asynchrony-by-construction is the JC asynchronous core
- tension-with: [[when-expression-blocking.bug]] — the implemented when suspends its continuation
- complements: [[functional-distributed.principle]] — purity makes evaluation location-free; non-blocking makes coordination suspension-free
