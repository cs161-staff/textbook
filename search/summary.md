---
title: Summary
parent: Search
nav_order: 5
layout: page
---

# Summary

In this note, we discussed *search problems* and their components: a *state space*, a set of *actions*, a *transition function*, an *action cost*, a *start state* and a *goal state*. The agent interacts with the environment through its sensors and its actuators. The agent function describes what the agent does in all circumstances. Rationality of the agent means that the agent seeks to maximize their expected utility. Finally, we define our task environments using PEAS descriptions.

Regarding the search problems, they can be solved using a variety of search techniques, including but not limited to the five we study in CS 188:

- *Breadth-first Search*
- *Depth-first Search*
- *Uniform Cost Search*
- *Greedy Search*
- *A* Search*

The first three search techniques listed above are examples of *uninformed search*, while the latter two are examples of *informed search* which use *heuristics* to estimate goal distance and optimize performance.

We additionally made a distinction between *tree search* and *graph search* algorithms for the above techniques.

[^1]: In other courses, such as CS70 and CS170, you may have been introduced to "trees" and "graphs" in the graph theory context. Specifically, a tree being a type of graph that satisfies certain constraints (connected and acyclic). This is not the distinction between tree search and graph search that we make in this course.
