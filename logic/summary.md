---
title: "11.10 Summary"
parent: 11. Logic
nav_order: 10
layout: page
---

# 11.10 Summary

In this note, we introduced the concept of logic which knowledge-based agents can use to reason about
the world and make decisions. We introduced the language of logic, its syntax and the standard logical
equivalences. Propositional logic is a simple language that is based on proposition symbols and logical
connectives. First-order logic is a representation language more powerful than propositional logic. The
syntax of first-order logic builds on that of propositional logic, using terms to represent objects and universal
and existential quantifiers to make assertions.

We further described the DPLL algorithm used to check satisfiability (SAT problem) in propositional logic.
It is a depth-first enumeration of possible models, using early termination, pure symbol heuristic and unit
clause heuristic to improve performance. The forward chaining algorithm can be used for reasoning when
our knowledge base consists solely of literals and implications in propositional logic.

Inference in first-order logic can be done directly by using rules like Generalized Modus Ponens or by
propositionalization, which translates the problem into propositional logic and uses a SAT solver to draw
conclusions.