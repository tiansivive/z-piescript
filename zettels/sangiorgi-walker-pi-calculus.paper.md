---
tags: [paper, pi-calculus, coordination, theoretical, concurrency, types, reference]
refs:
  - doc:references.md
  - resource:https://www.cambridge.org/gb/universitypress/subjects/computer-science/programming-languages-and-applied-logic/pi-calculus-theory-mobile-processes
---
# Sangiorgi & Walker — The π-Calculus: A Theory of Mobile Processes

Davide Sangiorgi and David Walker. *The π-Calculus: A Theory of Mobile Processes*. Cambridge
University Press, 2001.

The graduate-level reference. 580 pages, comprehensive. Covers operational semantics, bisimulation
theory (strong, weak, barbed), type systems (sorting, I/O types, linear types), and higher-order
π-calculus (process/code passing over channels). The chapter on higher-order π-calculus is directly
relevant to piescript's traveling-closure model: it establishes that process passing can be encoded
in name passing (cf. Sangiorgi 1996), validating the implementation approach. The type system
chapters — particularly I/O types (channels carry types annotated read/write capability) and linear
types (channels used exactly once) — inform piescript's future channel typing and ownership story.
The bisimulation theory chapters establish what "behavioral equivalence" means for programs that use
channels, which is relevant to reasoning about when piescript programs can be safely refactored or
optimized.

**Depends on**: (none)
**Enables**: (none directly)
**Connections**:
- extends: [[sangiorgi-agent-passing.paper]] — Walker co-authored this textbook; Sangiorgi's agent-passing work is a chapter
- extends: [[milner-pi-calculus.paper]] — the graduate companion to Milner's foundational papers
- formalizes: [[join-calculus.coordination]] — the pi-calculus background for understanding join calculus restrictions
- informs: [[code-mobility.coordination]] — higher-order pi chapter on code/process passing
- informs: [[channels.infrastructure]] — I/O types chapter informs future channel typing
- part-of: [[papers.hub]]
- related: [[milner-communicating-mobile-systems.paper]] — the accessible textbook; this is the comprehensive reference
- related: [[honda-session-types.paper]] — session types extend the I/O types covered in this textbook
