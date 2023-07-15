---
layout: page
keywords: "Deep-Learning"
title: "Transfer Learning"
date: 2023-07-15
tags: Deep-Learning, Transformers
key: "TLPF-1407"
comment: true
---
<p> Transfer learning is one of the great ideas in Deep Learning (DL) that accelerated the development of applications, especially, in the computer vision domain. In general, training a DL model from scratch requires thousands of samples (the more the better). However, there are many tasks where acquiring thousands of samples is
not possible or economically prohibitive. That's where transfer learning helps.</p>

<p> Imagine now that we are just beggining to learn to ride a bicycle. Initially, we need to put a lot of effort into learning to balance the cycle. Then gradually
we learn to balance and eventually take a full control over the ride. Suppose that we also wish to learn to ride a simple electric bike.
How difficult will that be for us?. It will be bit easier as we could **transfer the knowledge** of balancing (acquired from riding a bicyle) to any similar tasks like riding an electric bike. Can we do the same in machine learning?.That is,
can we transfer the knowledge gained in one task to other related tasks?. That's what **transfer learning** is all about </p>

<p> Suppose that we have thousands of images to train the model for one task (say, classification) but a limited amount of images for other SIMILAR tasks. Then we can transfer the knowledge from the original task to other similar tasks. It was predominantly used in the vision domain. It is partly due to the structure of the model called Convolutional Neural Network (CNN) architecture which requires a minimal architecture change when adapting it to other tasks.</p>

 <p> However, transfer learning in Natural Language Processing (NLP)domain remained a challenging one for years, not that straightforward. The deck below will help you understand the sequence of attempts made to overcome the challenges in a better way. (Note, however, that today we are using Transformers in the NLP domain for various tasks. This enabled transfer learning quite obvious :-), once again partly due to its structure).</p>

<div class="extensions extensions--slide">
  <iframe src="https://iitm-pod.slides.com/arunprakash_ai/contextualembeddings/fullscreen?token=vPPExe2q" width="576" height="420" title="Transformers-A-Short-Version" scrolling="no" frameborder="1" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
</div>

<p> After going through the slides, you will understnad why Transformer architecture is a boon to NLP domain.</p>