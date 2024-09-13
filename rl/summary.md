---
title: 5.5 Summary
parent: 5. RL
nav_order: 5
layout: page
---

# 5.5 Summary

It's very important to remember that reinforcement learning has an underlying MDP, and the goal of reinforcement learning is to solve this MDP by deriving an optimal policy. The difference between using reinforcement learning and using methods like value iteration and policy iteration is the lack of knowledge of the transition function $$T$$ and the reward function $$R$$ for the underlying MDP. As a result, agents must *learn* the optimal policy through online trial-by-error rather than pure offline computation. There are many ways to do this:

- **Model-based learning**: Runs computations to estimate the values of the transition function $$T$$ and the reward function $$R$$ and uses MDP-solving methods like value or policy iteration with these estimates.
  
- **Model-free learning**: Avoids estimation of $$T$$ and $$R$$, instead using other methods to directly estimate the values or Q-values of states.
  
  - **Direct evaluation**: Follows a policy $$\pi$$ and simply counts total rewards reaped from each state and the total number of times each state is visited. If enough samples are taken, this converges to the true values of states under $$\pi$$, albeit being slow and wasting information about the transitions between states.
  
  - **Temporal difference learning**: Follows a policy $$\pi$$ and uses an exponential moving average with sampled values until convergence to the true values of states under $$\pi$$. TD learning and direct evaluation are examples of on-policy learning, which learn the values for a specific policy before deciding whether that policy is suboptimal and needs to be updated.
  
  - **Q-Learning**: Learns the optimal policy directly through trial and error with Q-value iteration updates. This is an example of off-policy learning, which learns an optimal policy even when taking suboptimal actions.
  
  - **Approximate Q-Learning**: Does the same thing as Q-learning but uses a feature-based representation for states to generalize learning.

- To quantify the performance of different reinforcement learning algorithms, we use the notion of **regret**. Regret captures the difference between the total reward accumulated if we acted optimally in the environment from the beginning and the total reward we accumulated by running the learning algorithm.
