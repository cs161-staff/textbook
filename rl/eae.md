---
title: Exploration and Exploitation
parent: RL
nav_order: 4
layout: page
---

# Exploration and Exploitation

We've now covered several different methods for an agent to learn an optimal policy, and emphasized that "sufficient exploration" is necessary for this, without really elaborating on what "sufficient" means. In the following sections, we'll discuss two methods for distributing time between exploration and exploitation: $$\epsilon$$-greedy policies and exploration functions.

## $$\varepsilon$$-Greedy Policies

Agents following an **$$\epsilon$$-greedy policy** define some probability $$0 \leq \epsilon \leq 1$$, and act randomly and explore with probability $$\epsilon$$. Accordingly, they follow their current established policy and exploit with probability $$(1 - \epsilon)$$. This is a very simple policy to implement, yet can still be quite difficult to handle. If a large value for $$\epsilon$$ is selected, then even after learning the optimal policy, the agent will still behave mostly randomly. Similarly, selecting a small value for $$\epsilon$$ means the agent will explore infrequently, leading Q-learning (or any other selected learning algorithm) to learn the optimal policy very slowly. To get around this, $$\epsilon$$ must be manually tuned and lowered over time to see results.

## Exploration Functions

The issue of manually tuning $$\epsilon$$ is avoided by **exploration functions**, which use a modified Q-value iteration update to give some preference to visiting less-visited states. The modified update is as follows:

$$
Q(s, a) \leftarrow (1-\alpha)Q(s, a) + \alpha \cdot [R(s, a, s') + \gamma \max_{a'} f(s', a')]
$$

where $$f$$ denotes an exploration function. There exists some degree of flexibility in designing an exploration function, but a common choice is to use:

$$
f(s, a) = Q(s, a) + \frac{k}{N(s, a)}
$$

with $$k$$ being some predetermined value, and $$N(s, a)$$ denoting the number of times Q-state $$(s, a)$$ has been visited. Agents in a state $$s$$ always select the action that has the highest $$f(s, a)$$ from each state, and hence never have to make a probabilistic decision between exploration and exploitation. Instead, exploration is automatically encoded by the exploration function, since the term $$\frac{k}{N(s, a)}$$ can give enough of a "bonus" to some infrequently-taken action such that it is selected over actions with higher Q-values. As time goes on and states are visited more frequently, this bonus decreases towards $$0$$ for each state and $$f(s, a)$$ regresses towards $$Q(s, a)$$, making exploitation more and more exclusive.

