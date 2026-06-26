---
tags: [paper, pi-calculus, channels, coordination, theoretical, language, reference]
refs:
  - doc:references.md
  - resource:https://www.cambridge.org/us/universitypress/subjects/computer-science/communications-information-theory-and-security/communicating-and-mobile-systems-pi-calculus
---
# Milner — Communicating and Mobile Systems: the π-Calculus

Robin Milner. *Communicating and Mobile Systems: the π-Calculus*. Cambridge University Press, 1999.

The introductory textbook by the inventor of the π-calculus. 174 pages, accessible. Covers names,
interaction, behavioural equivalence, and type systems for interaction patterns. Chapter 1
establishes the core intuition: names are the only things that exist — values, channels, and
processes are all named. The polyadic π-calculus (names passed in tuples) is developed as the
natural extension of the monadic calculus. Sorting (a lightweight type discipline over channel
arities) foreshadows the typed channel work. Directly relevant to piescript: the textbook treatment
of scope extrusion (private names escaping their scope by being communicated) is the theoretical
model for piescript's channel reference passing and code mobility. Companion to the 1992 papers;
more accessible than Sangiorgi & Walker for building initial intuition.

**Depends on**: (none)
**Enables**: (none directly)
**Connections**:
- extends: [[milner-pi-calculus.paper]] — textbook treatment of the calculus from the founding papers
- formalizes: [[join-calculus.coordination]] — the polyadic pi-calculus is the parent calculus the join calculus restricts
- informs: [[channels.infrastructure]] — textbook intuition for channels as names that can be communicated
- informs: [[code-mobility.coordination]] — scope extrusion as the theoretical model for channel ref passing
- informs: [[name-passing.coordination]] — the textbook source for name-passing semantics
- part-of: [[papers.hub]]
- related: [[sangiorgi-walker-pi-calculus.paper]] — the graduate-level companion reference
- related: [[milner-pi-calculus.paper]] — the original papers this textbook expands on
