---
layout: page
keywords: "Deep Learning, Pytorch, Pytorch Internels"
title: "Pytorch for Deep Learning"
date: 2022-12-17
tags: Pytorch, Deep-Learning, Python.
key: "PDL1712"
comment: true
---
<p> Theory is not enough, you must apply. The objective of this workshop is to give you hands on experience in building models using the pytorch's core component called <b> Tensor </b>. Beleive me, everything you are gonna build is simply stacking or connecting copies of this single core component!. It make sense as all the models takes in Tensors (data) as input and manipulate them and finally outputs a Tensor. In this workshop we start with very foundational concepts like tensors and computing gradient of tensors. I try my best to correlate the theory of back-proagation for fully conncected layers, convolutional layers, recurrent layers with the pytorch implementation (which uses AutoGrad). </p>
 <ul> 
 <li> <p> You can access the slide deck here: <a href="https://iitm-pod.slides.com/arunprakash_ai/pytorch"> https://iitm-pod.slides.com/arunprakash_ai/pytorch </a> </p> </li>
 <li> <p>  Read the contents in the slide deck before using the following colab notebooks. </p> </li>
 <li> <p>  I strongly believe that once you get a good grip on the first four modules, you can refer to documenetation or others code easily. I will keep updating this post.</p> </li>
 </ul>
  
 <h2> Colab Notebooks </h2>

 <ol>
   <li>  <p>  <strong> The Fuel:  </strong> <a href="https://colab.research.google.com/drive/179Gv23AcUDCOhHt82msbstQZrbzS6Qn4?usp=sharing"> Tensors </a> <br>  </p>
     <ul>
      <li>  Understand the Pytorch architecture </li>
        <li> Create Tensors of 0d,1d,2d,3d,... (a multidomensional array in numpy) </li>
        <li> Understand the attributes : <em> storage, stride, offset, device` </em> </li>
        <li> Manipulate tensor dimensions </li>
        <li> Operations on tensors </li>
     </ul>
  </li>
 
   <li>  <p> <strong>  The Engine:   </strong> <a href="https://colab.research.google.com/drive/12h5SZ0FaZXUYzEP5DM2GTIg2KIeFfiG4?usp=sharing"> Autograd </a> </p>
     <ul>
        <li> A few more attributes of tensor : <em>  requires_grad, grad, grad_fn, _saved_tensors, backward, retain_grad, zero_grad </em> </li>
        <li> Computation gradph: Leaf node (parameters) vs non-leaf node (intermediate computation) </li>
        <li> Accumulate gradient and update with context manager (torch.no_grad) </li>
        <li> Implementating a neural network from scratch </li>
     </ul>
    </li>
    
   <li> <p> <strong>   The factory:   </strong> <a href="https://colab.research.google.com/drive/1bz87qDYbidxskT6pkxJ-pRaF39qFteMv?usp=sharing"> nn.Module </a>, <a href="https://colab.research.google.com/drive/1A9D0wzQ93Bl06cpAYhFvYO2cGe8sasof?usp=sharing"> Data utils </a> </p>
     <ul>
      <li> Brief tour into the source code of nn.Module </li>
      <li> Everything is a module (layer in other frameworks)</li>
      <li> Stack modules by subclassing nn.Module and build any neural network   </li>
      <li> Managing data with <em> dataset </em> class and <em>DataLoader </em> class</li>
    </ul>
    </li>
  
 <li> <p> <strong>   Convolutional Neural Netowrk   </strong> <a href="https://colab.research.google.com/drive/1M9ha7mZ-42UKUFZGee5QeKHbdNoo3U51?usp=sharing">Image Classification </a></p>
     <ul>
        <li> Using torchvision for datasets </li>
        <li> build CNN and move it to GPU </li>
        <li> Train and test </li>
        <li> Transfer learning </li>
        <li> Image segmentation </li>
    </ul>
    </li>
  <li> <p> <strong>   Recurrent Neural Netowrk   </strong> <a href="https://colab.research.google.com/drive/1OAraEdQfr_rhXGeANZ83v5gJ4Kt14aAr?usp=sharing">Sequence Classification </a></p>
     <ul>
        <li> torchdata </li>
        <li> torchtext </li>
        <li> Word Embedding</li>
        <li> Build RNN </li>
        <li> Train,Test,Evaluate </li>
    </ul>
    </li>
  
  </ol>
  
  
  

