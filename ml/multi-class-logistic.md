---
title: "10.8 Multi-Class Logistic Regression"
parent: 10. ML
nav_order: 8
layout: page
---

# 10.8 Multi-Class Logistic Regression

In multi-class logistic regression, we want to classify data points into $$K$$ distinct categories, rather than just two. Thus, we want to build a model that outputs estimates of the probabilities for a new data point to belong to each of the $$K$$ possible categories. For that reason, we use the **softmax function** in place of the logistic function, which models the probability of a new data point with features $$\mathbf{x}$$ having label $$i$$ as follows:

$$
P(y=i|\mathbf{f}(\mathbf{x});\mathbf{w}) = \frac{e^{\mathbf{w}_i^T \mathbf{f}(\mathbf{x})}}{\sum_{k=1}^K e^{\mathbf{w}_k^T \mathbf{f}(\mathbf{x})}}
$$

Note that these probability estimates add up to 1, so they constitute a valid probability distribution. We estimate the parameters $$\mathbf{w}$$ to maximize the likelihood that we observed the data. Assume that we have observed $$n$$ labelled data points ($$\mathbf{x}_i, y_i$$). The likelihood, which is defined as the joint probability distribution of our samples, is denoted with $$\ell(\mathbf{w}_1, \ldots, \mathbf{w}_K)$$ and is given by:

$$
\ell(\mathbf{w}_1, \ldots, \mathbf{w}_K) = \prod_{i=1}^{n} P(y_i | \mathbf{f}(\mathbf{x}_i); \mathbf{w})
$$

To compute the values of the parameters $$\mathbf{w}_i$$ that maximize the likelihood, we compute the gradient of the likelihood function with respect to each parameter, set it equal to zero, and solve for the unknown parameters. If a closed-form solution is not possible, we compute the gradient of the likelihood and use gradient ascent to obtain the optimal values.

A common trick to simplify these calculations is to first take the logarithm of the likelihood function, which will break the product into summations and simplify the gradient calculations. We can do this because the logarithm is a strictly increasing function and the transformation will not affect the maximizers of the function.
<p>
</p>
For the likelihood function, we need a way to express the probabilities $$P(y_i | \mathbf{f}(\mathbf{x}_i); \mathbf{w})$$ in which $$y \in \{1, \ldots, K\}$$. So for each data point $$i$$, we define $$K$$ parameters $$t_{i,k}$$, $$k = 1, \ldots, K$$ such that $$t_{i,k} = 1$$ if $$y_i = k$$ and $$0$$ otherwise. Hence, we can now express the likelihood as follows:

<p>
</p>

$$
\ell(\mathbf{w}_1, \ldots, \mathbf{w}_K) = \prod_{i=1}^{n} \prod_{k=1}^K \left( \frac{e^{\mathbf{w}_k^T \mathbf{f}(\mathbf{x}_i)}}{\sum_{\ell=1}^K e^{\mathbf{w}_\ell^T \mathbf{f}(\mathbf{x}_i)}} \right)^{t_{i,k}}
$$

<p>
</p>
and we also obtain for the log-likelihood:
<p>
</p>

<p>
</p>

$$
\log \ell(\mathbf{w}_1, \ldots, \mathbf{w}_K) = \sum_{i=1}^{n} \sum_{k=1}^K t_{i,k} \log \left( \frac{e^{\mathbf{w}_k^T \mathbf{f}(\mathbf{x}_i)}}{\sum_{\ell=1}^K e^{\mathbf{w}_\ell^T \mathbf{f}(\mathbf{x}_i)}} \right)
$$
<p>
</p>

Now that we have an expression for the objective, we must estimate the $$\mathbf{w}_i$$s such that they maximize that objective.

In the example of multi-class logistic regression, the gradient with respect to $$\mathbf{w}_j$$ is given by:

<p>
</p>
$$
\nabla_{\mathbf{w}_j} \log \ell(\mathbf{w}) = \sum_{i=1}^{n} \nabla_{\mathbf{w}_j} \sum_{k=1}^K t_{i,k} \log \left( \frac{e^{\mathbf{w}_k^T \mathbf{f}(\mathbf{x}_i)}}{\sum_{\ell=1}^K e^{\mathbf{w}_\ell^T \mathbf{f}(\mathbf{x}_i)}} \right) = \sum_{i=1}^{n} \left( t_{i,j} - \frac{e^{\mathbf{w}_j^T \mathbf{f}(\mathbf{x}_i)}}{\sum_{\ell=1}^K e^{\mathbf{w}_\ell^T \mathbf{f}(\mathbf{x}_i)}} \right) \mathbf{f}(\mathbf{x}_i)
$$
<p>
</p>

where we used the fact that $$\sum_k t_{i,k} = 1$$.