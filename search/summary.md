---
title: 1.6 Summary
parent: 1. Search
nav_order: 6
layout: page
---

# 1.5 Summary

We discussed *search problems* and their components: a *state space*, a set of *actions*, a *transition function*, an *action cost*, a *start state* and a *goal state*. The agent interacts with the environment through its sensors and its actuators. The agent function describes what the agent does in all circumstances. Rationality of the agent means that the agent seeks to maximize their expected utility. Finally, we define our task environments using PEAS descriptions.

Regarding the search problems, they can be solved using a variety of search techniques, including but not limited to the five we study in CS 188:

- *Breadth-first Search*
- *Depth-first Search*
- *Uniform Cost Search*
- *Greedy Search*
- *A* Search*

The first three search techniques listed above are examples of *uninformed search*, while the latter two are examples of *informed search* which use *heuristics* to estimate goal distance and optimize performance.

We additionally made a distinction between *tree search* and *graph search* algorithms for the above techniques.

we also discussed *local search algorithms* and their motivation. We can use these approaches when we don't care about the path to some goal state and want to satisfy constraints or optimize an objective. Local search approaches allow us to save space and find adequate solutions when working in large state spaces!

We went over a few foundational local search approaches, which build upon each other:

- *Hill-Climbing*
- *Simulated Annealing*
- *Local Beam Search*
- *Genetic Algorithms*

The idea of optimizing a function will reappear later in this course, especially when we cover neural networks.
