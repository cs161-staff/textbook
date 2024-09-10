---
title: "11.8 First Order Logical Inference"
parent: 11. Logic
nav_order: 8
layout: page
---

# 11.8 First Order Logical Inference

With first-order logic we formulate inference exactly the same way. We'd like to find out if $$KB \models q$$, that is if $$q$$ is true in all models under which $$KB$$ is true. One approach to finding a solution is **propositionalization** or translating the problem into propositional logic so that it can be solved with techniques we have already laid out. Each universal (existential) quantifier sentence can be converted to a conjunction (disjunction) of sentences with a clause for each possible object that could be substituted in for the variable. Then, we can use a SAT solver, like DPLL or Walk-SAT, (un)satisfiability of $$(KB \wedge \neg q)$$.

One problem with this approach is there are an infinite number of substitutions that we could make since there is no limit to how many times we can apply a function to a symbol. For example, we can nest the function `Classmate(... Classmate(Classmate(Austen))...)` as many times as we'd like, until we reference the whole school. Luckily, a theorem proved by Jacques Herbrand (1930) tells us that if a sentence is entailed by a knowledge base that there is a proof involving just a *finite* subset of the propositionalized knowledge base. Therefore, we can try iterating through finite subsets, specifically searching via iterative deepening through nested function applications, i.e. first search through substitutions with constant symbols, then substitutions with `Classmate(Austen)`, then substitutions with `Classmate(Classmate(Austen))`, ...

Another approach is to directly do inference with first-order logic, also known as **lifted inference**. For example, we are given 

$$
(\forall x ~ HasAbsolutePower(x) \wedge Person(x) \Rightarrow Corrupt(x)) \wedge Person(John) \wedge HasAbsolutePower(John)$$ 

("absolute power corrupts absolutely"). We can infer $$Corrupt(John)
$$ by substituting $$x$$ for John. This rule is known as **Generalized Modus Ponens**. The forward chaining algorithm for first-order logic repeatedly applies generalized Modus Ponens and substitution to infer $$q$$ or show that it cannot be inferred.