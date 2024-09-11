---
title: "10.5 Linear Regression"
parent: 10. ML
nav_order: 5
layout: page
---

# 10.5 Linear Regression

Now we'll move on from our previous discussion of Naive Bayes to **Linear Regression**. This method, also called **least squares**, dates all the way back to Carl Friedrich Gauss and is one of the most studied tools in machine learning and econometrics.

**Regression problems** are a form of machine learning problem in which the output is a continuous variable (denoted with $$ y $$). The features can be either continuous or categorical. We will denote a set of features with $$\mathbf{x} \in \mathbb{R}^n$$ for $$ n $$ features, i.e., $$\mathbf{x} = (x^1, \ldots, x^n)$$.

We use the following linear model to predict the output:

$$
h_{\mathbf{w}}(\mathbf{x}) = w_0 + w_1 x^1 + \cdots + w_n x^n
$$

where the weights $$ w_i $$ of the linear model are what we want to estimate. The weight $$ w_0 $$ corresponds to the intercept of the model. Sometimes in literature, we add a 1 on the feature vector $$\mathbf{x}$$ so that we can write the linear model as $$\mathbf{w}^T \mathbf{x}$$, where now $$\mathbf{x} \in \mathbb{R}^{n+1}$$. To train the model, we need a metric of how well our model predicts the output. For that, we will use the $$L_2$$ loss function which penalizes the difference of the predicted from the actual output using the $$L_2$$ norm. If our training dataset has $$ N $$ data points, then the loss function is defined as follows:

$$
    Loss(h_{\mathbf{w}}) = \frac{1}{2} \sum_{j=1}^N L_2(y^j, h_{\mathbf{w}}(\mathbf{x}^j)) = \frac{1}{2} \sum_{j=1}^N (y^j - h_{\mathbf{w}}(\mathbf{x}^j))^2 = \frac{1}{2} \left\|\mathbf{y} - \mathbf{X} \mathbf{w}\right\|_2^2
$$

Note that $$\mathbf{x}^j$$ corresponds to the $$ j $$-th data point $$\mathbf{x}^j \in \mathbb{R}^n$$. The term $$\frac{1}{2}$$ is just added to simplify the expressions of the closed form solution. The last expression is an equivalent formulation of the loss function which makes the least square derivation easier. The quantities $$\mathbf{y}$$, $$\mathbf{X}$$, and $$\mathbf{w}$$ are defined as follows:

$$
\mathbf{y} = \begin{bmatrix}
y^1 \\
y^2 \\
\vdots \\
y^N
\end{bmatrix}, \quad
\mathbf{X} = \begin{bmatrix}
1 & x_1^1 & \cdots & x_1^n \\
1 & x^1_2 & \cdots & x^n_2 \\
\vdots & \vdots & \ddots & \vdots \\
1 & x^1_N & \cdots & x^n_N
\end{bmatrix}, \quad
\mathbf{w} = \begin{bmatrix}
w_0 \\
w_1 \\
\vdots \\
w_n
\end{bmatrix}
$$

where $$\mathbf{y}$$ is the vector of the stacked outputs, $$\mathbf{X}$$ is the matrix of the feature vectors where $$x_j^i$$ denotes the $$i$$-th component of the $$j$$-th data point. The least squares solution denoted with $$\hat{\mathbf{w}}$$ can now be derived using basic linear algebra rules. More specifically, we will find the $$\hat{\mathbf{w}}$$ that minimizes the loss function by differentiating the loss function and setting the derivative equal to zero.

$$
\nabla_{\mathbf{w}} \frac{1}{2} \left\|\mathbf{y} - \mathbf{X} \mathbf{w}\right\|_2^2 = \nabla_{\mathbf{w}} \frac{1}{2} \left(\mathbf{y} - \mathbf{X} \mathbf{w}\right)^T \left(\mathbf{y} - \mathbf{X} \mathbf{w}\right)
$$

$$
= \nabla_{\mathbf{w}} \frac{1}{2} \left(\mathbf{y}^T \mathbf{y} - \mathbf{y}^T \mathbf{X} \mathbf{w} - \mathbf{w}^T \mathbf{X}^T \mathbf{y} + \mathbf{w}^T \mathbf{X}^T \mathbf{X} \mathbf{w}\right)
$$

$$
= \nabla_{\mathbf{w}} \frac{1}{2} \left(\mathbf{y}^T \mathbf{y} - 2 \mathbf{w}^T \mathbf{X}^T \mathbf{y} + \mathbf{w}^T \mathbf{X}^T \mathbf{X} \mathbf{w}\right) = -\mathbf{X}^T \mathbf{y} + \mathbf{X}^T \mathbf{X} \mathbf{w}
$$

Setting the gradient equal to zero we obtain:

$$
-\mathbf{X}^T \mathbf{y} + \mathbf{X}^T \mathbf{X} \mathbf{w} = 0 \Rightarrow \hat{\mathbf{w}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}
$$

Having obtained the estimated vector of weights, we can now make a prediction on new unseen test data points as follows:

$$
h_{\hat{\mathbf{w}}}(\mathbf{x}) = \hat{\mathbf{w}}^T \mathbf{x}
$$
