---
title: 8.5 Summary
parent: 8. HMMs
nav_order: 5
layout: page
---

# 8.5 Summary

We saw that **Markov models** can be thought of as chain-like, infinite-length Bayes' nets. We also learned that Markov models obey the **Markov property**, meaning that the distribution of the quantity we're modeling depends only on the value of the quantity at the previous timestep. We also learned that we can compute the distribution of the modeled quantity at any given timestep using a technique called the **mini-forward algorithm**, and that if we let time go to infinity, this distribution will eventually converge to the **stationary distribution**.

We also covered two new types of models:
- *Markov models*, which encode time-dependent random variables that possess the Markov property. We can compute a belief distribution at any timestep of our choice for a Markov model using probabilistic inference with the mini-forward algorithm.
- *Hidden Markov Models*, which are Markov models with the additional property that new evidence which can affect our belief distribution can be observed at each timestep. To compute the belief distribution at any given timestep with Hidden Markov Models, we use the forward algorithm.

Sometimes, running exact inference on these models can be too computationally expensive, in which case we can use particle filtering as a method of approximate inference.
