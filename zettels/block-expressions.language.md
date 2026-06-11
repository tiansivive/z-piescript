---
tags: [syntax, language, implemented, documentation]
refs:
  - code:Elaborator.java
  - code:CoreLet.java
  - session:80f0b64a-5e21-4b2e-acda-fabde482cc87
---
# Block Expressions

Sequenced let-bindings terminated by a final expression. A block is a series of let-bindings
where each binding is in scope for everything that follows; top-level program bindings desugar
to nested [[core-ir.language]] `CoreLet` nodes. Enables writing multi-step programs without
deeply nested let/in chains. Sequencing is let-binding only — there is no Core IR sequencing
node, and bare expression statements inside blocks are **silently dropped** by the elaborator
(known bug, see [[expr-statements.language]]).

**Depends on**: [[core-ir.language]]
**Enables**: (none directly)
**Connections**:
- complements: [[pipe-operator.language]] — pipes compose left-to-right; blocks compose top-to-bottom
- uses: [[core-ir.language]] — desugars to nested `CoreLet` nodes
- tension-with: [[expr-statements.language]] — block grammar admits `expr ;` statements that the elaborator discards
