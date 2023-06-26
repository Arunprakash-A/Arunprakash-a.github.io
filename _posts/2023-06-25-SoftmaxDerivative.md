---
layout: page
title: "Softmax and Its Derivative"
date: 2023-06-25
tags: Deep-Learning, Transformers
key: "SID0625"
comment: true
mathjax: true
---  
## Introduction

The Softmax function is one of the most commonly used activation functions at the output layer of neural networks (be it CNN, RNN or Transformers). In fact, Large Language Models(LLMs) based on transformer architecture (like ChatGPT) use softmax in the output layer for many NLP(Natural Language Processing) tasks. Therefore, it is important to understand how softmax function gives a probability distribution for a given input vector. It is equally important to understand the derivative of softmax. Most likely you already know how to compute softmax for a given input vector $\mathbb{a}$, however, I am repeating this for those who do not know about it.  

Let's consider an output layer with 5 neurons (in practice it could be in the order of thousands) as shown below. However, to keep the calculations tractable, we limit ourselves to five neurons.
<p align="center">
  <img align="center" src="https://drive.google.com/uc?export=view&id=1dSczuuqhq49myNr5sgbwFyKw_Tt-YEVa" width="250px" height="250px">
</p>

In the image, the softmax function takes in the input vector $\mathbf{a} \in \mathbb{R}^5$ and produces the output vector $\hat{\mathbb{y}}$. The element $y_i$ of $\mathbf{\hat{y}}$ is calculated
as follows 

<p align="center"> 
<span style="font-size:1.5em; line-height:0%"> $\hat{y_i} = \frac{e^{a_i}}{\sum \limits_{j=1}^5 e^{a_j}}$ </span>
</p>

 For example, $\hat{y_3}$ is calculated as follow, 
 <p align="center"> 
 <span style="font-size:1.5em; line-height:0%">$\hat{y_3} = \frac{e^{a_3}}{\sum \limits_{j=1}^5 e^{a_j}} = \frac{e^{a_3}}{e^{a_1}+e^{a_2}+e^{a_3}+e^{a_4}+e^{a_5}}$ </span>
 </p>

 It resembles a typical normalization of a vector by its magnitude. Here, the difference is the exponentiation of the elements. As a consequence the elements in the output vector $\hat{y}$ sum to one (like typical unit normalization)  So, the obvious question is, why do we use exponentiation?
 
## Role of Exponential function
  The image below shows an exponential function $e^x$. One of the nice properties of the exponential function is it is a non-negative function. 
  <p align="center">
  <img align="center" src="https://drive.google.com/uc?export=view&id=1u1ZksekGZUtwo1Tm3_5QN8pkrmGptgIb" width="350px" height="300px">
</p>
  This is a desired property in our case to ensure that all the elements in $\hat{\mathbf{y}}$ are POSITIVE (even if some/all of the elements of $\mathbf{a}$ are negative) and $\in [0,1]$ . This is exactly what we are looking for in a typical classification setting. That is, we want the network to produce probabilities for the classes $P(C|X)$ 

## Derivative of Softmax
  Well, computing softmax is quite easy. The same is true for computing the derivative of the softmax. Let's make clear what we are exactly taking a derivative of. Firstly, there are five inputs and five outputs. Each output is function of all the inputs. More precisely, if input is $a_i$, then the term in the numerator of $y_i$ depends only on $a_i$ whereas the term in the denominator depends on ALL the elements in input $a_j, j \in (1,2,3,4,5)$. Note that we use $i$ to denote the output element and $j$ as an index to sum over all elements in the input. So we can divide the entire derivative of $\frac{\partial y_i}{\partial a_j}$ part into two halves: 
     
  &nbsp; i.  One for $\frac{\partial y_i}{\partial a_j}$ where $i \neq j$ <br>
  &nbsp; ii. The other for $\frac{\partial y_i}{\partial a_j}$ where $i = j$<br>  
  

  **Case 1: $i \neq j$**

  Let's take $i=3$ and $j=1$. To hide **distracting details**, let's use $\sum$ to denote summing over all elements of the input vector. Then the derivative of it is as follows: $\frac{\partial{\hat{y}_3}}{\partial a_1} = \frac{\partial }{\partial a_1} \frac{e^{a_3}}{ \sum}$.
<p align="center"> 
<span style="font-size:1.5em; line-height:0%">
    $\frac{\partial{\hat{y}_3}}{\partial a_1} = e^{a_3} \frac{\partial }{\partial a_1} \frac{1}{e^{a_1}+e^{a_2}+\cdots+e^{a_5}}$
</span>
</p>
Then by using the rule from the calculus, we could easily calculate the derivative as follows

<p align="center"> 
<span style="font-size:1.5em; line-height:0%">
    $ \begin{aligned} \frac{\partial{\hat{y}_3}}{\partial a_1} & = e^{a_3} \frac{-1*e^{a_1}}{(e^{a_1}+e^{a_2}+\cdots+e^{a_5})^2} \\ 
    & =-1* \frac{e^{a_3}}{\sum} \frac{e^{a_1}}{\sum} \\ 
    & =-1* \hat{y}_3 \hat{y}_1 
    \end{aligned}
    $
</span>
</p>
We can simply generalize this,
<p align="center"> 
<span style="font-size:1.5em; line-height:0%">
    $ \bbox[5px, border: 2px solid blue]{\frac{\partial{\hat{y}_i}}{\partial a_j} = -1* \hat{y}_j \hat{y}_i, \quad i \neq j}$
</span>
</p>

**Case 2: $i = j$**

  Let's take $i=3$ and $j=3$. Now, the derivative is a bit more involved than the previous case, but not harder. The derivative changes to: $\frac{\partial{\hat{y}_3}}{\partial a_3} = \frac{\partial }{\partial a_3} \frac{e^{a_3}}{ \sum}$. Let's take one step at a time,
 <p align="center"> 
<span style="font-size:1.5em; line-height:0%">
    $ \begin{aligned} 
    \frac{\partial{\hat{y}_3}}{\partial a_3} &= \frac{\partial }{\partial a_3} \frac{e^{a_3} }{e^{a_1}+e^{a_2}+\cdots+e^{a_5}} \\ 
    &=\frac{(\sum) e^{a_3}-e^{a_3}*e^{a_3}}{(e^{a_1}+e^{a_2}+\cdots+e^{a_5})^2}\\
    &= \frac{(\sum)e^{a_3}}{(\sum)^2} -  \frac{e^{a_3}}{\sum} \frac{e^{a_3}}{\sum} \\
    &=\hat{y}_3(1-\hat{y}_3)
    \end{aligned}$
</span>
</p>
We can generalize this once again,
<p align="center"> 
<span style="font-size:1.5em; line-height:0%">
    $ \bbox[5px, border: 2px solid red] {\frac{\partial{\hat{y}_i}}{\partial a_j} = \hat{y}_i(1-\hat{y}_i), \quad i = j}$
</span>
</p>

Let's put the pieces together by constructing a matrix for various values of $(i,j)$. The resultant matrix is called the Jacobian matrix (following the denominator layout in arranging the elements of the matrix). Here it is for you 

<p align="center"> 
<span style="font-size:1.5em; line-height:0%">
    $\frac{\partial \hat{\mathbf{y}}}{\partial \mathbf{a}}= 
    \begin{bmatrix}
\hat{y_1}(1-\hat{y_1})& -1*\hat{y_1}\hat{y}_2 & -1*\hat{y_1}\hat{y}_3  & -1*\hat{y_1}\hat{y}_4  & -1*\hat{y_1}\hat{y}_5 \\
-1*\hat{y_2}\hat{y}_1 & \hat{y_2}(1-\hat{y_2})& -1*\hat{y_2}\hat{y}_3  & -1*\hat{y_2}\hat{y}_4  & -1*\hat{y_2}\hat{y}_5 \\
-1*\hat{y_3}\hat{y}_1 & -1*\hat{y_3}\hat{y}_2 &  \hat{y_3}(1-\hat{y_3})  & -1*\hat{y_3}\hat{y}_4  & -1*\hat{y_3}\hat{y}_5 \\
\vdots 				  & \vdots 					& \vdots 				& \vdots 					& \vdots \\	
-1*\hat{y_5}\hat{y}_1 & -1*\hat{y_5}\hat{y}_2 & -1*\hat{y_5}\hat{y}_3  & -1*\hat{y_5}\hat{y}_4  &  \hat{y_5}(1-\hat{y_5}) \\

\end{bmatrix}
    $
</span>
</p>

## Gradient Flowing through the Softmax

 This is not our end objective. What we have computed so far is called the local gradient of softmax. However, we are interested in $\frac{\partial \mathscr{L}}{\partial \mathbf{a}}$, where $\mathscr{L}$ is the cross entropy loss function. It is going to just be a matrix-vector multiplication (once again DL is all about Matrix vector multiplication :-)).

<p align="center"> 
<span style="font-size:1.5em; line-height:0%">
 $\frac{\partial \mathscr{L}}{\partial  \mathbf{a}} = \frac{\partial \mathscr{L}}{\partial \mathbf{\hat{y}}} \frac{\partial \hat{\mathbf{y}}}{\partial \mathbf{a}}$
 </span>
</p>

Keeping $i=3$, we have 
<p align="center"> 
<span style="font-size:1.5em; line-height:0%">
$ \frac{\partial \mathscr{L}}{\partial \mathbf{\hat{y}}} = \begin{bmatrix}
0\\
0\\

\frac{-1}{\hat{y}_3}\\
0\\
0
\end{bmatrix}$ 
</span>
</p>

 then 

<p align="center"> 
<span style="font-size:1.5em; line-height:0%">
$
=\begin{bmatrix}
\hat{y_1}(1-\hat{y_1})& -1*\hat{y_1}\hat{y}_2 & -1*\hat{y_1}\hat{y}_3  & -1*\hat{y_1}\hat{y}_4  & -1*\hat{y_1}\hat{y}_5 \\
-1*\hat{y_2}\hat{y}_1 & \hat{y_2}(1-\hat{y_2})& -1*\hat{y_2}\hat{y}_3  & -1*\hat{y_2}\hat{y}_4  & -1*\hat{y_2}\hat{y}_5 \\
-1*\hat{y_3}\hat{y}_1 & -1*\hat{y_3}\hat{y}_2 &  \hat{y_3}(1-\hat{y_3})  & -1*\hat{y_3}\hat{y}_4  & -1*\hat{y_3}\hat{y}_5 \\
\vdots 				  & \vdots 					& \vdots 				& \vdots 					& \vdots \\	
-1*\hat{y_5}\hat{y}_1 & -1*\hat{y_5}\hat{y}_2 & -1*\hat{y_5}\hat{y}_3  & -1*\hat{y_5}\hat{y}_4  &  \hat{y_5}(1-\hat{y_5}) \\

\end{bmatrix} \begin{bmatrix}
0\\
0\\

\frac{-1}{\hat{y}_3}\\
0\\
0
\end{bmatrix}$
</span>
</p>
Multiply the Jacobian matrix and the vector and make a simple re-arrangement. After all these (simple but lengthy) computations, we have our final sweet and neat formula for the softmax 

<p align="center"> 
<span style="font-size:1.5em; line-height:0%">
    $ \bbox[5px, border: 2px solid green] {\frac{\partial \mathscr{L}}{\partial  \mathbf{a}} = \mathbf{\hat{y}-y}}$
</span>
</p>

I hope this article helped you grasp the softmax and its derivative in a better way. If you have any questions, please feel free to post them in the comment section. Thanks for reading.