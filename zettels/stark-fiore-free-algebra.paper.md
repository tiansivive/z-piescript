---
tags: [paper, pi-calculus, effects, theoretical, coordination, reference]
refs:
  - doc:references.md
  - resource:https://www.sciencedirect.com/science/article/pii/S0304397507007086
---
# Stark & Fiore — Free-Algebra Models for the π-Calculus

Ian Stark and Marcello Fiore. "Free-Algebra Models for the π-Calculus." *Theoretical Computer Science*, 408(1–2), 2008.

Shows that π-calculus semantics can be characterized using enriched Lawvere theories and
computational monads. The key result: the category of π-calculus models is monadic — there is a
free-algebra functor with the expected universal property. This grounds the claim that coordination
primitives form an algebraic effect signature: the evaluator is an algebra (effect handler) for
the signature, and the residual of partial evaluation — the stuck computation tree — is the free
algebra over that signature. In piescript terms: the `spawn`/`when`/`send`/channel primitives are
the generators of the free algebra; the evaluator is one algebra (the interpreter); and the partial
evaluation residual is the free monad over the Join Calculus effect signature.

**Depends on**: (none)
**Enables**: (none directly)
**Connections**:
- formalizes: [[free-monad.types]] — the free-algebra/monadicity result is the categorical grounding for "residual is a free monad"
- formalizes: [[join-calculus.coordination]] — the join calculus effects form the signature whose free algebra is the residual
- informs: [[algebraic-effects.types]] — effect signatures are algebras; handlers are algebra morphisms
- informs: [[partial-evaluation-lowering.performance]] — free algebra perspective on what partial evaluation produces
- part-of: [[papers.hub]]
- related: [[milner-pi-calculus.paper]] — the pi-calculus this paper gives free-algebra semantics for
- related: [[plotkin-pretnar-handlers.paper]] — complementary: handlers for algebraic effects in a functional setting
- related: [[wu-schrijvers-fusion.paper]] — handler fusion optimizations over the same free monad structure
