---
layout: page
title: "Lagrange Multiplier : Intuition via Interaction"
date: 2023-12-18
tags: ML
key: "CO1218" 
comment: true
mathjax: true
---  
## Introduction
I guess you end up being here after coming across the term "constrained optimization" or "Lagrangian" and wanted to understand what "Lagrange multiplier is?". Well, in this post, I help you understand the foundation of it with interactive plots (you can find plenty of mathematical reasoning on the net). Let's get straight to the point. Consider the (objective) function, $z=2x+y$. What is the maximum or the minimum value of the function $z$. Well, we can see that the function neither has a maximum nor a minimum. To verify, we take a derivate and set it to zero. Then you will see that the derivative is a constant (the function is changing at a constant pace everywhere in the domain $x$ and $y$).The function is plotted below (rotate,zoom in/out..)
<p align="center">
<iframe scrolling="no" title="plane-cosntrOpt" src="https://www.geogebra.org/material/iframe/id/ypgqkjzb/width/700/height/500/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false" width="700px" height="500px" style="border:0px;"> </iframe>
</p>

## Putting constraints

Now, we can put constraints on the range of values that input variables can take. Say for example, $x^2+y^2=1$. This is an equality constraint (circle). We can have inequality constraints as well (disk). Note that, the constraint is also a function of input variables $(x,y)$. The function $z$ with the constraints on the input variables has a maximum and a minimum. 
The problem is formulated as follows

<center>
$\max \limits_{x,y} z$, subject to (s.t), $x^2+y^2=1$
</center>

How do you find the maximum (or minimum)?.

## Explorative Approach

Take all the points $(x,y)$ on the unit circle and evaluate the function at each point. The function attains its maximum (minimum) at some point $(x=x_0,y=y_0)$. Move the point $A$ on the circle and observe the change in the function values (better note down the values)
<p align="center">
<iframe scrolling="no" title="ConstrainedOptimization-1" src="https://www.geogebra.org/material/iframe/id/xyrpjdcd/width/700/height/500/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false" width="700px" height="500px" style="border:0px;"> </iframe>
</p>
The maximum occurs at $x=0.88,y=0.49$ with the maximum value of the function being 2.24.If you move the point $A$ a bit clockwise or anti-clockwise, the function value decreases from 2.24. Similarly, if you move the point $A$ around the circle (that is, in the feasible region), then you will find the values of $(x,y)$ for which the function attains its minimum. 

The explorative approach of finding the maximum by evaluating the function $z$ by considering all possible input points that satisfy  the constraints is helpful to get started but inefficient (infeasbile). However, we can explore it a bit further to see what we are actually looking for? Could we observe something unique? 

 * The constraint function $x^2+y^2=0$ is living in $\mathbb{R}^2$
 * The objective function $z=2x+y$ is in $\mathbb{R}^3$

Therefore, let's plot the <b>contours of the objective </b> function $2x+y=k$ for various values of $k$ (caution: $k \subset z$, that satisfies the constraint).That is for each value of $k$, a plane cuts through the objective function and we project it down on to the coutours of the constraint function (now, both live in $\mathbb{R}^2$). Now, let us move the point $A$ and also display the <b>contours</b> of the objective function $k=2x(A)+y(A)$ where $x(A)$ represents the $x$ coordinate of the point $A$. 
<p align="center">
<iframe scrolling="no" title="ConstrainedOptimization-2" src="https://www.geogebra.org/material/iframe/id/nzcvzjbj/width/700/height/500/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false" width="700px" height="500px" style="border:0px;"> </iframe>
</p>

What is your observation about the line (contours of the objective function) to circle (contours of the constraint)? Esspecially, at the point it maximizes (minimizes) the objective function.

<b> The line is tangent to the circle (In general, the contour of the objective function is tangent to the contour of constraint function at maximum or minimum)

## Analytical approach

With this observation, we can introduce the gradient vector (a simple quantity that we can calculate) of both objective and constraint functions and see how they are related. Once again, move the point $A$ and observe the direction of gradient vectors. Where they are perpendicular to each other ? Where they are parallel to each other? 
<p align="center">
<iframe scrolling="no" title="GradientConstrainedOpt" src="https://www.geogebra.org/material/iframe/id/zyrkackr/width/700/height/500/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false" width="700px" height="500px" style="border:0px;"> </iframe>
</p>
We can see that the gradient of the objective function and the gradient of the constraints are <b>parallel</b> to each other at the point $(x_0,y_0)$ where the function attains its maximum or minimum. Why is that? Think about it for a minute.

 So we can write the following important equality 

<p align="center"> 
<span style="font-size:1.5em; line-height:0%">
    $ \bbox[5px, border: 2px solid blue]{\nabla f(x_0,y_0)=\lambda \nabla g(x_0,y_0)}$
</span>
</p>
<b> Important: </b> The above relation only holds at the point $(x_0,y_0)$ 

The $\lambda$ is called <b> Lagrange multiplier </b>. This helps us to scale the magnitude  of the gradient of constraint function to match the magnitude of the gradient of the objective function. How do we make use of the equation to find $(x_0,y_0)$ ?

<p align="center">

    $ \nabla_f \begin{bmatrix} 2 \\ 1 \end{bmatrix}=\lambda 
    \nabla_g \begin{bmatrix} 2x_0 \\ 2y_0 \end{bmatrix}$

</p>

Now we can solve for the $(x_0,y_0)$ by equating the gradients. You can take a look at the detailed calculations at [khanacademy](https://www.khanacademy.org/math/multivariable-calculus/applications-of-multivariable-derivatives/constrained-optimization/a/lagrange-multipliers-single-constraint)

Now, we can conceptually extend the same for multiple constraints.