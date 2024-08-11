---
title: "Maximum Likelihood Estimation"
date: 2023-11-05
tags: ML Math
key: "EP0919" 
comment: true
mathjax: true
---  
## Introduction
The concept of estimation of an unknown quantity from the given observations has been a fascinating area of study for many centuries. However, it remains elusive for many beginners. Let's start with a concept that we are already familiar with. Here is a sequence $x_1=[1,3,5,7,9,11, \times,\cdots,]$. What could be the value of the sequence at index 6 (denoted by $\times$)? You may extend the sequence by adding +2 to the previous value. The answer could be thirteen. How about the value at the index 1000? Well, you can keep extending the sequence or you can come up with the mathematical relation that describes the sequence as a function of index $n$. We could write $x_1(n)=2n+1$. Once we find the functional representation of a sequence from the observation, we may throw away the observations.

Similarly, consider one more sequence of values $x_2 = [1,0.90,0.81,0.74,0.67, \times, \cdots]$. What could be the value at $\times$?. We can see that the element values in the sequence are decreasing slowly. Therefore, I **assume** (by chance) that the underlying function that **(likely)** generated the sequence is of the form $e^{-ct}, \quad t=0,1,2,3,\cdots$. However, I do not know the value of $c$. The value of $c$ can be **estimated** from the sequence using some curve fitting techniques. 

What if the elements in the sequence are random numbers? For example, $x_3 = [1,0,1,1,1,1,0,0,1,\cdots]$. We can't assume any deterministic function to **represent** the sequence. Therefore, We go with a probabilistic function (distribution). In this case, the sequence could be modeled as Bernoulli trails with probabilities of observing $1$ and $0$. 

## Likelihood Function
In all the above cases, we **assumed** the underlying function that could have generated the sequences. Our assumption may turn out to be wrong as we observe more samples. If the elements of a sequence are random samples, then we call the **assumed underlying** distribution function as **likelihood** function. Each sample ,$x_i \in \{0,1\}$ , in the random sequence $X = [1,0,1,1,0]$ is drawn from the likelihood function 
<center>
$P(x_i) = p^{x_i}(1-p)^{1-x_i}$
</center>
What we need to **estimate** is the value of $p$ (that is, the probability of $x_i=1$) from the observed samples. We can also view the observation as **a single trail** with 5 independent Bernoulli random variables. Therefore, we are also interested in the likelihood of the sequence itself. In other words, we are interested in the joint PDF of $(x_0,x_1,x_2,x_3,x_4)$
<center>
$P(x_1,x_2,x_3,x_4,x_5) = ?$
</center>Before proceeding, we need to make a few assumptions about the random variables

* Are the random variables independent? 
* Are they coming from the same distribution? 

If the answer is yes to both questions, then we can write the joint pdf as a product of individual pdfs
<center>
$P(x_0,x_1,x_2,x_3,x_4) = P(x_0)P(x_1)P(x_2)P(x_3)P(x_4) = \prod \limits_{i=0}^n P(x_i)$
</center>

These assumptions can be clubbed together, then it is called **Independent and Identically Distributed (IID)**. If the first assumption does not hold, then we can write the joint PDFs as a product of conditional pdfs. That is, 
<center>
$P(x_0,x_1,x_2,x_3,x_4) = P(x_0)P(x_1|x_0)P(x_2|x_1,x_0)P(x_3|x_2,x_1,x_0)P(x_4|x_3,x_2,x_1,x_0)$
</center> 



Assuming IID for the random sequence $X = [1,0,1,1,0]$ (Note: The order of the samples in the sequence doesn't matter because of IID), the joint PDF (likelihood function) that generated the sequence is given by

<center>

$\bbox[5px, border: 2px solid green]{P(x_0,x_1,x_2,x_3,x_4) = \prod \limits_{i=0}^n P(x_i)= \prod \limits_{i=0}^n p^{x_i}(1-p)^{1-x_i}}$                
</center>

## Maximum Likelihood Function 

Carefully observe the interactive plot given below as we vary the value of $p$ from zero to one in the horizontal axis. The vertical axis is the probability of observing the random sequence $X$ (joint probability). There is exactly one value of $p$ in the interval $[0,1]$ that maximizes the likelihood of the sequence $X$. 

The number of elements in the sequence is 5. Therefore, we can vary the value of $n$ from zero to four. Here, $n$ denotes the number of ones observed in the sequence of length 5. For $n=0$, the bias of the coin $p$ is $0$ (the coin never turns into a head). Therefore, the joint probability is 1. We can very the value of $n$ to 0,1,2,3,4,5. For $n=3$, then we can compute the joint PDF as $\prod \limits_{i=0}^n p^{x_i}(1-p)^{1-x_i}=p^3p^2$ .

<iframe scrolling="no" title="MaximumLikelihoodBernouliTrials" src="https://www.geogebra.org/material/iframe/id/bubwuwr6/width/700/height/500/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false" width="700px" height="500px" style="border:0px;"> </iframe>


 Remember that ALL VALUES (except 0 and 1) of $p$ could have possibly generated the sequence, the value of $p$ which increases the likelihood is what we want. We can cast this as an optimization problem as follows
<center>
$\hat{p} = \underset{p} {\mathrm{argmax}}\prod \limits_{i=0}^n p^{x_i}(1-p)^{1-x_i}$
</center> 

Note, we do not care about the maximum value of the function. We are looking for $\mathrm{argmax}$ (that is, the value of $p \in [0,1]$ for which the function attains its maximum).

Well, we can see from the plot that for the given sequence (where the number of ones $n=3$), the function attains its maximum at $\hat{p}=0.6$. That's great. However, plotting is not possible in many scenarios. So, we need an approach that allows us to estimate  $\hat{p}$ from the given sequence itself. 

### Hey Calculus
 You might have already guessed it! We are talking about the minimum and maximum of the function. Taking a derivative of the function and setting it to zero solves the problem of finding $\hat{p}$. Note that we have a joint pdf that contains product terms. Applying $log$ allows us to convert the product terms into sum terms and taking the derivative becomes easier (moreover, $log$ is monotonous and also a concave function). Therefore, we can write

<center>
$
\begin{align*}
\hat{p} &= \prod_{i=1}^n p^{x_i}(1-p)^{(1-x_i)}\\
\ell(\hat{p}) &= \log{p}\sum_{i=1}^n x_i + \log{(1-p)}\sum_{i=1}^n (1-x_i)\\
\dfrac{\partial\ell(\hat{p})}{\partial p} &= \dfrac{\sum_{i=1}^n x_i}{p} - \dfrac{\sum_{i=1}^n (1-x_i)}{1-p} \overset{\text{set}}{=}0\\
\sum_{i=1}^n x_i - p\sum_{i=1}^n x_i &= p\sum_{i=1}^n (1-x_i)\\
\end{align*}
$
</center>

Finally, we have a simple estimation of $p$, as a function of elements in the sequence, that maximizes the likelihood. Since we are using $log$ function to find the $\mathrm{argmax}$, it is also called as **Maximum Log Likelihood Estimation**

<center>
$\bbox[5px, border: 2px solid green]{\hat{p} = \dfrac{1}{n}\sum_{i=1}^n x_i}$
</center>

### Change of likelihood function

If the elements of the sequence $x_i \in \mathbb{R}$, then we have to use the appropriate density function,say, the Gaussian density function. We need to $\mathrm{argmax}$ of mean $\mu$ and the variance $\sigma$ of the distribution by following the exact steps that we followed for the Bernoulli distribution. Take the derivative of the joint PDF for the mean and variance, and set the result to zero.

### Point vs Interval estimation

The quantities ($p,\mu,\sigma$) that we have computed are called the point estimation. There are is another type called **Interval Estimation** where the estimated value could vary within some interval.

### How good is the estimation?
Comparison is inevitable! We do want to compare our estimated value $\hat{p}$ to the true value of $p$. We want to measure how close it is to the true value. Alas! We do not have the true value of $p$. Often, we can't know the true value of the quantities we measure. Despite the limitations, we have two statistical performance measures called **Bias** and **Variance**. 

## Maximum Aposteriori Estimation (aka, Bayesian Estimation)

Assume you are investigating a murder. Initially, there are two suspects $A$ and $B$. The suspect $A$ is good at shooting and martial arts. The suspect $B$ is a cook. Suppose I ask you whom, of these two, do you believe the killer is?. Your initial belief points you to the suspect $A$. Suppose you have come to know that the cook had committed crimes for money in the past (additional information or evidence). Would you change your belief about the suspect $A$? 

Mathematically, we can pose this question as follows
<center>
$P(killer=A)=0.8$ (initially)
</center>
 After giving you a piece of evidence, then your belief changes
 <center>
$P(killer=A|evidance)=0.6$ 
</center>

In a nutshell, we change our **prior** beliefs about something after seeing the **evidence**. This concept could be modeled using Bayes theorem, 

<center>
 $\bbox[5px, border: 2px solid green]{P(\theta|x) = \frac{P(x|\theta)}{P(x)} P(\theta)}$
</center> 
<p>
where, $P(\theta)$ is our prior belief (unconditional distribution),$P(x|\theta)$ is a likelihood function (which is a function of $\theta$), $P(x)$ is a marginal distribution, $ P(\theta|x) $ is our change in belief (also called Aposterior). In this case, the parameter ($\theta$) that we are trying to estimate itself assumes some <b>parameterized</b> distributions like Beta and Gaussian distribution. If both the prior and posterior follow the same distribution (say, Gaussian), then they are called <b>conjugate prior</b>. 
</p>

Falling back to the Bernoulli (coin tossing) experiment with $x=[1,0,1,1,0]$. In MLE, we estimated $\hat{p}$ as a single point. On the contrary, in Bayesian, we start with an initial belief for the parameter we estimate. We are gonna generalize this for any parameter. Therefore, instead of $\hat{p}$, let's use $\theta$. Let's start with some value for $\theta$ as given by the Beta distribution (why? Because we want to change our belief after seeing the evidence, we get the probability value from the parameterized function $f(p,\alpha,\beta)$, and **optimize** the parameters $(\alpha,\beta)$ according to the evidence)

<center>
$f(p,\alpha,\beta)= \mathbf{B}(\alpha,\beta) p^{\alpha-1}(1-p)^{\beta-1}$
</center>

In the above equation $\mathbf{B}(\alpha,\beta)$ is a Beta function (returns a normalization constant, so that the probability integrates to 1). You can play with the app below to see how the $\alpha$ and $\beta$ control the shape of the distribution, 

<iframe scrolling="no" title="BetaDistribution" src="https://www.geogebra.org/material/iframe/id/w8xyjzej/width/700/height/500/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false" width="700px" height="500px" style="border:0px;"> </iframe>

Surprisingly (fortunately), the other terms resemble Bernoulli's distribution with the number of heads $n_h=\alpha-1$ and the number of tails $n_t=\beta-1$. Note, however, both $\alpha,\beta \in \mathbb{R}^+$. How do we make sense of this **prior** distribution of $\theta$? Let's try to understand it

<p>
Suppose, for some reason, you <b>believe</b> that (before tossing the coin to observe the outcomes) the coin is highly biased toward <b>heads</b>! We can encode this belief into the parameter $\alpha$ and $\beta$. In this case, we set the parameter $\alpha$ to a high value than the $\beta$. Set $\alpha=4.3$ and $\beta=1.3$ in the applet and observe the shape. Does this look similar to the one we plotted in MLE section? It is because we are computing the joint pdf given the prior $P(x_0,x_1,\cdots,x_4|(\alpha=4.3,\beta=1.3))$
</p>

<p>

Now you toss the coin 5 times and observe the outcomes in each trial: $x=[0,1,0,1,0]$. This is a surprise! The trial produced more zeros than ones. We have to adjust our beliefs after seeing the evidence. How do we do that? We have to adjust the value of $\alpha$ and $\beta$. How much? That we need to decide as follows (we will drop the $p(x)$ in the denominator)
</p>
<p align="center">
$
\begin{align*}
P(\theta|x) &= \frac{P(x|\theta)}{P(x)}P(\theta) \\
            &\propto \bigg(\prod \limits_{i=1}^n p^{x_i} (1-p)^{1-x_i} \bigg) \cdot \bigg(p^{\alpha-1} (1-p)^{\beta-1} \bigg) \\
            &\propto \prod \limits_{i=1}^n p^{x_i+\alpha-1} (1-p)^{1-x_i+\beta-1} \\
            & \propto p^{\alpha+n_h-1} (1-p)^{\beta+n_t-1} \quad (\because n_h=\sum \limits_{i=1}^n x_i, n_t = \sum \limits_{i=1}^n (1-x_i) )

\end{align*}
$
</p>


 So, we can see that the Aposteriori belief is obtained by modifying a prior by adding $n_h,n_t$ that are functions of data (evidence) to the parameter $(\alpha,\beta)$. Since the given sequence has more zeros (tails), it increases the value of $\beta$ by 3 and the value of $\alpha$ by 2. Therefore, the updated value of $\alpha=6.3$ and the updated value of $\beta=4.3$. This shifts the peak of the distribution to the left!




 
