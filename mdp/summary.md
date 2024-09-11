---
title: 4.5 Summary
parent: 4. MDPs
nav_order: 5
layout: page
---

# 4.5 Summary
The material presented above has much opportunity for confusion. We covered value iteration, policy iteration, policy extraction, and policy evaluation, all of which look similar, using the Bellman equation with subtle variation.

Below is a summary of the purpose of each algorithm:

- **Value iteration**: Used for computing the optimal values of states, by iterative updates until convergence.
- **Policy evaluation**: Used for computing the values of states under a specific policy.
- **Policy extraction**: Used for determining a policy given some state value function. If the state values are optimal, this policy will be optimal. This method is used after running value iteration to compute an optimal policy from the optimal state values, or as a subroutine in policy iteration to compute the best policy for the currently estimated state values.
- **Policy iteration**: A technique that encapsulates both policy evaluation and policy extraction and is used for iterative convergence to an optimal policy. It tends to outperform value iteration by virtue of the fact that policies usually converge much faster than the values of states.