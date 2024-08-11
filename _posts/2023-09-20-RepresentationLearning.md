---
title: "Representation Learning"
date: 2023-09-20
tags: ML
key: "RL0920" 
comment: true
mathjax: true
---  
## Motivation
Let's start with a simple question. How do you **represent** a number on a real line?. That's straightforward. How do you **represent** a 2D point $\begin{bmatrix}x \\ y \end{bmatrix}$ in a coordinate system?. Well, we use two real lines that are **orthogonal** to each other. Move $x$ unit on the axis and $y$ unit on the $y$ axis, then the location denotes the point. For latter convenience, we call $x$ and $y$ as the coefficients of the standard (unit) basis vectors $\mathbf{u_x}$ and $\mathbf{u_y}$. 

Suppose you are given 5 points $x_1,x_2,\cdots,x_5$ as shown in the app below. Could you represent at least four of them with a single number(coefficient) per point?. Hmm, ya, there is a pattern! Four points are lying on the line (check the "show line" checkbox to see the line) and only one point is not on the line. In other words, the four points are linearly dependent. That is, the four points are lying on the lower dimensional subspace $\mathbb{R}$ of the original vector space $\mathbb{R}^2$.

It means that we can reach the four points by scaling the unit vector $\mathbf{w}$ by an appropriate constant $c$. In linear algebra terminology, we can say the vector $\mathbf{w}$ is a new basis vector. Here, we call $\mathbf{w}$ as the **representation** for these four points. Once we have the $\mathbf{w}$ and coefficients $c_1,c_2,c_3$ and $c_4$, we can represent all these points in the new basis. We are representing the original data points of dim=2, $x_i \in \mathbb{R}^2$, as points in dim=1, $c_i \in \mathbb{R}$. So, we may call this process as dimensionality reduction! Note however that the dim of basis vector $\mathbf{w}$ is still the same as dim of the original points $(\mathbb{R}^2)$. In general, the dimension of the representation( aka: eigen, principal, basis) vectors is always equal to the dim of the original points. 

However, how do we represent the point $x_5$ using $c_5\mathbf{w}$? It is not possible as the point is not on the line. Suppose we relax the requirement that we need to **exactly** represent the point. Instead, we want to represent the point as close as possible. For that, we need to first **project** the point onto the line (subspace). The red arrow in the applet denotes the projected vector $\mathbb{p}$ and the point $x_5'$ is the projection of the point $x_5$ onto the line. The dotted segment represents the error between the projected point and the actual point.

 <em>Activity:</em> Check the `show Circle` check box in the app. Then move the point $x_5$ on the circle and observe the change in error value as you move along the circle. When does the error become high (that is, error=1)? 

 <iframe scrolling="no" title="Projection-PCA" src="https://www.geogebra.org/material/iframe/id/rhce9wch/width/700/height/500/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false" width="700px" height="500px" style="border:0px;"> </iframe>

 If we have more points $x_6,x_7,\cdots$, then we project all those points onto the subspace spanned by $\mathbf{w}$ (the line) to calculate the appropriate coefficient values, $c_i$. Note that the vector $\mathbf{w}$ is a unit vector. Therefore, to represent any point $x_i$, the scaling factor $c_i$ is given by $c_i = \mathbf{x_i}^T\mathbf{w}$ and the project vector is 
 <center>
 $\mathbb{p_i}=c_i\mathbb{w}$
 </center>

## Principled Approach

Well, in the above setup, we assumed we are given with $\mathbf{w}$ (or we could have calculated it, not a big deal). Suppose we receive a few more points as shown in the figure below,
<p align="center">
  <img align="center" src="https://lh3.googleusercontent.com/d/1fiSjRrD8FN0Zb_Y3gBtxumk2Ob_LdrFn">
</p>

Now, many points are outside the given line. That is, if we sum the error for each data point, then the average error might be high. The error is the function of the line we choose (that is, $\mathbb{w}$). However, there could be a better line ($\mathbb{w}$) that minimizes the average error. How do we find it? 

In general, we have $n$ data points and each data point $x_i \in \mathbb{R}^d$. We are interested in finding a set of $\mathbf{w_i} \in \mathbb{R}^d$ and the scalars $c_i \in \mathbb{R}$ such that it minimizes the average error as much as possible. Again, in linear algebra terminology, we are looking for new bases that span the low-dimensional subspace. By default,  the data points are represented in $\mathbb{R}^d$ with $d$ canonical (orthogonal) bases (coordinates). Our objective is to come up with $d' \leq d$ number of bases (coordinates) that minimizes the following error
<center>
$Error = \frac{1}{n} \sum \limits_{i=1}^n ||x_i-x_i'||^2 = \frac{1}{n}  \sum \limits_{i=1}^n ||x_i-c_iw||^2 = \frac{1}{n}  \sum \limits_{i=1}^n ||x_i-(x_i^Tw)w||^2 $
</center>

So, in the above equation, the only way to reduce the error is to find the right $w$ (note that we dropped the suffix $i$ as we are just finding a single vector $w$ for simplicity). That is, the error is a function of $w$ not of $x$. We can rewrite the error function as follows
<center>
$g(w) = \frac{1}{n} \sum \limits_{i=1}^n -(x_i^Tw)^2 = -\frac{1}{n} w^T \big[\sum \limits_{i=1}^n (x_ix_i^T)\big] w = -\frac{1}{n} w^TCw $
</center>

Here $C$ is a **covariance** matrix (Assuming $x_i$s are from some distribution) of size $d \times d$. You may [watch this video](https://www.youtube.com/watch?v=mU6CzvuUM00) for the derivation. So, we need to find the $\mathbf{w}$ that minimizes the error. An optimization problem!

We can get rid of the negative sign by posing this as a maximization problem. That is, maximize $\frac{1}{n} w^TCw$. It is important to note that it maximizes the **variance**, not the error. There are $d$ eigenvectors for the covariance matrix $C$, of these, it is the **eigenvector** corresponding to the **maximum eigenvalue** that maximizes the quantity $\frac{1}{n} w^TCw$.

## Algorithm
 1. A dataset $X = {x_1,x_2,\cdots,x_n} \quad x_i \in \mathbb{R}^d $
 2. Compute the mean vector $\mu = \frac{1}{n} \sum \limits_{i=1}^{n}x_i$, $\mu \in \mathbb{R}^d$
 3. Subtract the mean from each data point. It centers the data points about the origin as we assume the existence of vector space to find $w_i$. The vector space necessarily includes the origin.
 4. Project the data points onto the $w_i$ for all $i$.


## Principal Components
  The eigenvectors $(w_i)$ of the covariance matrix $C$ are called the principal directions and the eigenvalues $(c_i)$ corresponding to the eigenvectors convey the amount of variance along that direction. The component of the data point $x_i$ projected on each principal direction is called the **Principal Component**. 
  <center>
  $x_i = c_1w_1+c_2w_2+\cdots+c_dw_d, \quad c_i=x_i^Tw_i$
  </center>
  So we can say that any data point can be decomposed into its principal components (called Analysis) and synthesized back using the sum of principal components (called Synthesis).

   Recall that, suppose we have a thousand data points each of size 100. To store all the data points, assuming one byte of memory to store an element, we need $1000 \times 100 \times 1 = 100 KB$ of memory. However, if we use the projected version of all the data points, then we need to store only $c_i, i=1 \cdots 1000$ and the eigenvector $w \in \mathbb{R}^{100}$, which requires $1000 \times 1 + 100 = 1 KB$ of memory. That is a 100 times reduction in memory (of course, at the cost of losing more information). 

  What if we consider the second-largest eigenvector? It adds new information from that direction at the cost of doubling the memory requirement from 1KB to 2KB. If we use all the eigenvectors, then we can exactly reconstruct the data points without losing any information (the error becomes zero). If the data points live in a lower dimensional subspace, then the error becomes zero with a few eigenvectors. That's what exactly PCA does.
  

  The application of PCA is numerous. It is used to remove the noise from the data points, de-correlate the correlated features, feature extraction and so on.

## Just A baby step
   Principal Component Analysis (PCA) is just a baby step toward representation learning. The projection is on to the subspace spanned by the principal components which are lines and planes. Moreover, we expect the data points to have a high variance representation in the lower dimensional subspace for PCA to be helpful. It may not always be the case. What happens to the variance of principal components if the data points are distributed on a unit circle in $\mathbb{R}^2$? Then all the points are linearly **independent**. We need to use another technique called Independent Component Analysis (ICA). We may apply some kernel tricks on the data points (Kernel PCA), or even neural network-based approaches like AutoEncoders!
