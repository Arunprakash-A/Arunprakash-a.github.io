---
layout: page
title: "Interplay of Indices in Math - Illustrated "
date: 2023-08-13
tags: DL, Math
key: "IIMI1308" 
comment: true
mathjax: true
---  

## Introduction
When we have a sequence of elements, we use an index to locate a particular element in the sequence. The sequence of elements can be arranged into 2D,3D or n-dimensional arrays. Therefore, it is extremely important to make ourselves comfortable with using indexes to manipulate such arrays. Usually, the index starts from either 0 or 1. We need to be aware of the convention followed to avoid non-trivial mistakes.

 Let's consider the sequence $x = [1,1,2,-1,-3]$. Suppose I ask you the following questions

<ol>
    &emsp <li> What is the sum of the elements in the sequence $x$? </li>
    <li> What is the sum of the even/odd indexed elements in the sequence? </li>
    <li> Reverse the sequence $x$ to create a new sequence </li>
</ol>

Well, we can do all these calculations immediately by tracking the index in our minds. If the length of the sequence becomes large, then the manual calculation is laborious. Then we may ask the computer to carry out the calculations on our behalf. Now, we need to teach the computer to track the index properly. For example, we know what the even and odd index means, but how do you teach it to the computer?. That's where the math pitches in! 

Throughout the post We use the notations ($i,j,k,l$) to denote the index of a sequence. We use all of them if we are dealing with a 4-dimensional tensor (do not worry about this for now.).

## One dimensional sequence

Let's start with a one-dimensional sequence $x = [1,2, \cdots,100]$. Then summing the sequence is mathematically written as 

<center> sum = $\sum \limits_{i=0}^{99}x[i]$ </center>

Note that I am using [ ] instead of () to be consistent with the python way of accessing elements in a sequence. Of course, you can use theformula $\frac{N(N+1)}{2}$. However, just to illustrate the idea I am using a loop

{% highlight python linenos %}
sum = 0
for i in range(len(x)):
    sum += x[i]
{% endhighlight %}

### Sum Odd indexed elements
What we need to compute is the following,
<center> sum = $x[1]+x[3]+x[5]+\cdots+x[99]$ </center>

How do we denote this using sum notation?. Noting that the sequence of the index [1,3,5,...,99] is an arithmetic progression with a common difference $d=2$, this gives us the value of index for given $i$ as $1+(i-1)d = 1+2i-2=2i-1$. However, our index starts from 0, which gives the starting value as -1 (for i=0), which we need to offset  by 2 to start it from 1, this leads us to the following expression 
<center> $sum_o = \sum \limits_{i=0}^{\frac{N-1}{2}} x[2i+1]$ </center>
Observe that the upper limit of the summation is ${\frac{N-1}{2}}$, here $N$ is the length of the sequence.


{% highlight python linenos %}
sum = 0
N = len(x)
for i in range((N-1)/2)):
    sum += x[2*i+1]
{% endhighlight %}

### Reverse the sequence
One can easily reverse the sequence in a pen and paper setting. We can do the same mathematically using the index notation as follows,
<center> $x_r[i] = x[N-i], \ i=0,1,\cdots,N$ </center>

{% highlight python linenos %}
y = []
N = len(x)
for i in range(N):
    y += x[N-i] # appends to the list
{% endhighlight %}

### Multiple indexes
Once we defined a way to access elements in the desired order, then we can carry out any operation on the accessed elements. For example, we can simply show that summing the elements of the sequence is equal to summing their odd-indexed and even-indexed breakdown of the sequence
<center> $\sum \limits_{i=0}^N x[i] = \sum \limits_{j=1}^{\frac{N-1}{2}} x[2j+1]+ \sum \limits_{j=1}^{\lfloor \frac{N}{2} \rfloor } x[2j] $ </center>

Oftentimes, we need to use more than one index on a 1-D sequence. For example, sorting a sequence by comparing elements in the sequence. 

## Two dimensional arrays

Naturally, we could extend the indexing operation to 2D arrays using two indexes, namely, $i$ and $j$. We typically interpret $i$ as rows and $j$ as columns. Then $i,j$ denotes the element at $i$-th row and $j$-th column. Assume we have a 2D array $A$ of size $m \times n$

### Summing elements
We can do summing in multiple ways as shown in the figure below. All of them require appropriately manipulating indexes. That's where the interplay between indexes comes. It is always good to know how indexes interact by taking a simple example (until you learn a pattern)
<p align="center">
  <img align="center" src="https://drive.google.com/uc?export=view&id=1Ja8NWw3n4LxLAms90DBEG-zBGa5B-xDt" widht="500" height="350">
</p>
**A.** Summing elements along columns
<center> sum = $\sum \limits_{i=0}^{m-1} \sum \limits_{j=0}^{n-1} A[i,j]$ </center>

**B.**  Summing elements along rows
<center> sum = $\sum \limits_{j=0}^{n-1} \sum \limits_{i=0}^{m-1} A[j,i]$ </center>

**C.** Summing lower triangular elements
<center> sum = $\sum \limits_{j=0}^{n-1} \sum \limits_{i=0}^{m-1} A[j,i], \forall i \geq j$ </center>

**D.** Summing upper triangular elements
<center> sum = $\sum \limits_{j=0}^{n-1} \sum \limits_{i=0}^{m-1} A[j,i], \forall i \leq j$ 
</center>

### Matrix vector product
Another example that demonstrates the interaction between two different sequences (arrays) in a particular order is the matrix-vector product. Suppose we have a matrix $A$ of size $m \times n$ and a vector $x$ of size $n \times 1$, then the product $Ax$ is defined as

<center> $b_i = \sum \limits_{j=0}^n A_{ij} x_j, \ i=0,\cdots,m$ </center>

Here, we are computing the dot product between each row of a matrix and a vector $x$. We would have achieved the same result if we followed the linear combination of columns
<center> $b = \sum \limits_{j=0}^n x_j \cdot A[:,j] , \ i=0,\cdots,m$ </center>

where, $A[:,j]$ denotes the $j-$th column vector of the matrix $A$ and $x_j$ is the coefficient for the $j$-th column.

### Matrix Matrix Product

Suppose we arrange $k$ vectors each of size $n \times 1$ in a matrix. This will result in a matrix $C$ of size $n \times k$. **It is always good to notice the index of the summation**
<center> $c_{ij} =  \sum \limits_{k=0}^n A_{ik} C_{kj}$ </center>

## 3D array and beyond

Well, we can once again extend the same concept to 3D arrays and their interactions. However, this time we need to keep track of three indices $i,j,k$. 

<p align="center">
  <img align="center" src="https://drive.google.com/uc?export=view&id=1oV7gyo4V4a7hgURMQSvghQqR8mni2-Jk">
</p>

Now, let's consider the expression,
<center>$c_{ij}=\sum \limits_k^N \sum \limits_l^M x_{ilk} y_{ljk} $</center> 
Here the inputs $X,Y$ are three dimensional arrays. However, the output $C$ is going to be 2D array. Therefore, it is a reduction operation (that is, we the opeartion removes one dimension of the inputs $X,Y$). So what exactly is going on?

At the first sight, you might feel it is a daunting task to deal with more than two indexes. It is not that much hard once you understand how a single value for $C$ is computed. You may fix the value of $i,j$ and see the computation. Break it down and find out.