---
layout: page
title: "Experimental Settings of Famous Language Models"
date: 2023-12-26
tags: ML DL LLM
key: "ESFLM1226" 
comment: true
mathjax: true
--- 
## GPT (Generative Pre-trained Transformer)

 * <span style="color:blue"> Pre-training Dataset</span>: Book corpus (0.8 Billion words)
 * <span style="color:blue"> Unsupervised objective</span>: CLM (Autoregressive)
 * <span style="color:blue"> Tokenizer</span>: Byte Pair Encoding (BPE)
 * <span style="color:blue"> Vocab size</span>: 40K
 * <span style="color:blue"> Architecture</span>: Decoder only (12 Layers)
 * <span style="color:blue"> Activation</span>: GELU
 * <span style="color:blue"> Attention</span>: Dense
 * <span style="color:blue"> FFN</span>: Dense
 * <span style="color:blue"> Attention mask</span>: Causal Mask
 * <span style="color:blue"> Positional Encoding</span>: Absolute (learnable)
 * <span style="color:blue"> Optimizer</span>: Adam
 * <span style="color:blue"> Training steps</span>: 100 epochs ($2.4 \times 10^6$ steps), ($BS:64 \times T:512$) tokens/step
 * <span style="color:blue"> Number of parameters</span>: 0.12 Billion

## BERT (Bidirectional Encoder Representation from Transformers)
 * <span style="color:blue"> Pre-training Dataset</span>: Book corpus (0.8B words), English Wikipedia (2.5B words) 
 * <span style="color:blue"> Unsupervised objective</span>: MLM (Autoencoding)
 * <span style="color:blue"> Tokenizer</span>: WordPiece (similar to BPE)
 * <span style="color:blue"> Vocab_size</span>: 30K
 * <span style="color:blue"> Architecture</span>: Encoder only (12 Layers (BERT-base), 24 layers (BERT-large))
 * <span style="color:blue"> Activation</span>: GELU
 * <span style="color:blue"> Attention</span>: Dense
 * <span style="color:blue"> FFN</span>: Dense
 * <span style="color:blue"> Attention mask</span>: No Mask
 * <span style="color:blue"> Positional Encoding</span>: Absolute (learnable)
 * <span style="color:blue"> Optimizer</span>: Adam
 * <span style="color:blue"> Training steps</span>: 40 epochs ($1 \times 10^6$ steps), ($BS:256 \times T:512$) tokens/step
 * <span style="color:blue"> Number of parameters</span>: 0.12 Billion (Base) to 0.34 (Large)

## BART (Bidirectional Autoregressive Training)
 * <span style="color:blue"> Pre-training Dataset</span>: Book corpus,English Wikipedia,CC News, Stories (total:160 GB of text data)
 * <span style="color:blue"> Unsupervised objective</span>: MLM (token masking, deletion, text infilling, sentence shuffling)
 * <span style="color:blue"> Tokenizer</span>: BPE 
 * <span style="color:blue"> Vocab_size</span>: 50K 
 * <span style="color:blue"> Architecture</span>: Encoder-Decoder (6-6 Layers (BART-base), 12-12 layers (BART-large))
 * <span style="color:blue"> Activation</span>: GELU
 * <span style="color:blue"> Attention</span>: Dense
 * <span style="color:blue"> FFN</span>: Dense
 * <span style="color:blue"> Attention mask</span>: Causal mask in Decoder
 * <span style="color:blue"> Positional Encoding</span>: Absolute (Learneable)
 * <span style="color:blue"> Optimizer</span>: Adam
 * <span style="color:blue"> Training steps</span>: BERT-Like : 40 epochs ($1 \times 10^6$ steps), ($BS:256 \times T:512$) tokens/step
 * <span style="color:blue"> Training steps</span>: RoBERTa Like: $0.5 \times 10^6$ steps, ($BS:8000 \times T:512$) tokens/step
 * <span style="color:blue"> Number of parameters</span>: 0.13 Billion (Base) to 0.37 (Large)

## T5 (Text-To-Text-Transfer-Learning)
 * <span style="color:blue"> Objective</span>: Extensive study on existing approaches to building LMs under a unified framework.
 * <span style="color:blue"> Pre-training Dataset</span>: Colossal Clean Crawled Corpus <b>C4</b> (156 Billion tokens)
 * <span style="color:blue"> Unsupervised objective</span>: MLM-Denoising (predicting a span of missing tokens)  
 * <span style="color:blue"> Tokenizer</span>: Sentencepiece
 * <span style="color:blue"> Vocab_size</span>: 32K 
 * <span style="color:blue"> Architecture</span>: Encoder-Decoder (tiny, small, medium, large)
 * <span style="color:blue"> Activation: ReLU
 * <span style="color:blue"> Attention</span>: Dense
 * <span style="color:blue"> FFN</span>: Dense
 * <span style="color:blue"> Attention mask</span>: Causal mask in Decoder
 * <span style="color:blue"> Positional Encoding</span>: Modified position encoding
 * <span style="color:blue"> Optimizer</span>: Adafactor
 * <span style="color:blue"> Training steps</span>: **$<\frac{1}{4}$ of epoch** ($2^{19}=524,288$ steps), ($BS:128 \times T:512=65536$) tokens/step
 * <span style="color:blue"> Number of parameters</span>: 0.13 Billion (small) to 11 Billion (Large)

## GPT-2
 * <span style="color:blue"> Pre-training Dataset</span>: WebText (40 GB) (less than 19 Billion tokens)
 * <span style="color:blue"> Unsupervised objective</span>: CLM  
 * <span style="color:blue"> Tokenizer</span>: Bytelevel BPE
 * <span style="color:blue"> Vocab_size</span>: 50K 
 * <span style="color:blue"> Architecture</span>: Decoder (4 variants)
 * <span style="color:blue"> Activation</span>: GELU
 * <span style="color:blue"> Attention</span>: Dense
 * <span style="color:blue"> FFN</span>: Dense
 * <span style="color:blue"> Attention mask</span>: Causal mask 
 * <span style="color:blue"> Positional Encoding</span>: Absolute (learnable)
 * <span style="color:blue"> Optimizer</span>: Adam
 * <span style="color:blue"> Training steps</span>: not disclosed. Model underfits the dataset (similar to T5) ($BS:64 \times T:1024=65536$) tokens/step
 * <span style="color:blue"> Number of parameters</span>: 0.12 Billion (small) to 1.5 Billion (Large)

## GPT-3
 * <span style="color:blue"> Objective</span>: Scaling parameters and improve zero-shot, few-shot performance
 * <span style="color:blue"> Pre-training Dataset</span>: (700 GB) 300 Billion tokens from weighted sampling (60% of Common Crawl filtered (410 B), 22% of WebText-2 (19 B),8% of Books 1(12 B),8% of Books 2 (55 B),2-3% of Wikipedia (3 B))
 * <span style="color:blue"> Unsupervised objective</span>: CLM  
 * <span style="color:blue"> Tokenizer</span>: Bytelevel BPE
 * <span style="color:blue"> Vocab_size</span>: 50K 
 * <span style="color:blue"> Architecture</span>: Decoder (12 layers to 96 layers) 
 * <span style="color:blue"> Activation</span>: GELU
 * <span style="color:blue"> Attention</span>: [Sparse Factorization](https://arxiv.org/pdf/1904.10509.pdf)
 * <span style="color:blue"> FFN</span>: Dense
 * <span style="color:blue"> Attention mask</span>: Causal 
 * <span style="color:blue"> Positional Encoding</span>: Absolute (learnable)
 * <span style="color:blue"> Optimizer</span>: Adam
 * <span style="color:blue"> Training steps</span>: (Inferred) 1 epoch = 93570 steps with  3.2M batch size (tokens) ($\frac{300 \times 10^9}{3.2 \times 10^6}$), ($BS:0.5M \rightarrow 3.2M \tokens$). Total training steps could also be inferred from the total compute (PF-days) used to train the model. 
 * <span style="color:blue"> Number of parameters</span>: 0.12 Billion (small) to **175 Billion (Large)**
 * <span style="color:blue"> New finding</span>: In-context learning

## Switch (Scaling up T5 with MoE)
 * <span style="color:blue"> Objective</span>: Scale to Trillion parameters with a reduced <b>computational budget</b> (FLOPS/token)
 * <span style="color:blue"> Baseline</span>: T5 small (223M), T5 Large (739)
 * <span style="color:blue"> Pre-training Dataset</span>: Improved <b>C4</b> (156 Billion tokens)
 * <span style="color:blue"> Unsupervised objective</span>: MLM-Denoising (predicting span of missing tokens) 
 * <span style="color:blue"> Tokenizer</span>: Sentencepiece
 * <span style="color:blue"> Vocab_size</span>: 32K 
 * <span style="color:blue"> Architecture</span>: Encoder-Decoder (tiny, small, medium, large)
 * <span style="color:blue"> Activation</span>: ReLU
 * <span style="color:blue"> Attention</span>: Dense
 * <span style="color:blue"> FFN</span>: Sparsely activated with MoE (Mixture of Experts) paradigm. 
 * <span style="color:blue"> Number of experts</span>: 64 (base)
 * <span style="color:blue"> Attention mask</span>: Causal mask in Decoder
 * <span style="color:blue"> Positional Encoding</span>: Modified position encoding
 * <span style="color:blue"> Optimizer</span>: Adafactor
 * <span style="color:blue"> Training steps</span>: **$<\frac{1}{4}$ of epoch** ($2^{19}=524,288$ steps), ($BS:128 \times T:512=65536$) tokens/step
 * <span style="color:blue"> Number of parameters</span>: 7 Billion (base) to **1571 Billion (Switch-C)**
 * <span style="color:blue"> Speed-up</span>: 7.5x (switch base over dense T5 base), 2.5x (switch large over dense T5 large) Metric for comparison against T5 and MoE Transformers</span>: Constant FLOPS (T5 base (0.2B Parameters) and Switch base (7B parameters) have same FLOPS/Sequence)
 * In the diagram below $e$ denotes the experts. For example, $64e$ means 64 experts. Note carefully that increasing experts beyond a point increases the communication cost and hence decreases speed-up.

<p align="center">
 <img align="center" src="https://drive.google.com/uc?export=view&id=1oO9kefZi2JnRRtFaeUH0blhKIGjkdEW_" >
</p>

## GLM (Generalized Language Models - Unifying Framework)
* <span style="color:blue"> Objective</span>: Pose all problems as text generation problem
* <span style="color:blue"> Pre-training Dataset</span>: Book corpus, English Wikipedia, CC News-en, OpenWebText-2 (158GB total)
* <span style="color:blue"> Unsupervised objective</span>: MLM-text-infilling
* <span style="color:blue"> Tokenizer</span>: Sentencepiece
* <span style="color:blue"> Vocab_size</span>: 30K 
* <span style="color:blue"> Architecture</span>: Encoder-Decoder (3 variants)
* <span style="color:blue"> Activation</span>: GeLU
* <span style="color:blue"> Attention</span>: Dense
* <span style="color:blue"> FFN</span>: Dense
* <span style="color:blue"> Attention mask</span>: Causal mask in Decoder
* <span style="color:blue"> Positional Encoding</span>: <b> 2D positional encoding </b> (i.e., instead of using different positional encoding each for encoder and decoder)
* <span style="color:blue"> Training steps</span>: Same as BERT for comparison, half of RoBERTa and BART due to resource constraints.

## Gopher (Deepmind)
* <span style="color:blue"> Objective</span>: Scaling parameters and improve zero-shot, few-shot performance
* <span style="color:blue"> Pre-training Dataset</span>: <b>MassiveText (10TB, 2 Trillion tokens) (compiled from MassiveWeb, Books, C4, Github, Wikipedia)</b>, use 300 Billion tokens (12% of the total), evaluated on <b>The pile (800GB)</b>
* <span style="color:blue"> Unsupervised objective</span>: CLM  
* <span style="color:blue"> Tokenizer</span>: Bytelevel BPE
* <span style="color:blue"> Vocab_size</span>: 50K 
* <span style="color:blue"> Architecture</span>: Decoder (6 variants, 8 layers to 80 layers) 
* <span style="color:blue"> Activation</span>: GELU
* <span style="color:blue"> Attention</span>: Dense
* <span style="color:blue"> FFN</span>: Dense
* <span style="color:blue"> Attention mask</span>: Causal 
* <span style="color:blue"> Floating point Precision</span>: <b>fp32,bfloat16</b>
* <span style="color:blue"> Positional Encoding</span>: <b>Relative</b>
* <span style="color:blue"> Optimizer</span>: **Adam (pre-training)/AdaFactor(fine-tuning)**
* <span style="color:blue"> Number of parameters:</span> 44 Million to **280 Billion**
* <span style="color:blue"> Evaluated on</span>: 120 tasks
<p align="center">
 <img align="center" src="https://drive.google.com/uc?export=view&id=1cCgHB9cCulsfjbbo8SaNq5e161Tkftt0" >
</p>

## Chinchilla (Compute-Optimal Language Model)

* <span style="color:blue"> Objective</span>: Find the optimal model size and number of tokens for training a transformer language model under a given compute budget **(similar to power law)**
* <span style="color:blue"> Core problem</span>: Is the model size of Gopher optimal for the given compute budget ($10^{25}$ FLOPS)?
* <span style="color:blue"> Findings</span>: Model size and data size scale equally (doubling the model size (parameters) requires us to double the data size (measured in tokens) to get improved performance) as shown in the figure below (last row)
<p align="center">
 <img align="center" src="https://drive.google.com/uc?export=view&id=1rX1eLXG-xewgipHWbCV6a4DdLt4j6x0A" >
</p>

* <span style="color:blue"> The optimal size of Gopher</span>: According to the new law, the optimal model size (parameters) of Gopher (trained with 1.4 Trillion tokens) is <b>not 280 Billion</b> but 70 Billion.

* <span style="color:blue"> The optimal size of GPT-3</span>: According to the new law, the GPT-3 with 175 Billion parameters should have been trained on 4.2 Trillion tokens (for it to be optimal)

* <span style="color:blue"> Pre-training Dataset</span>: <b> MassiveText with a slight modification of weightage to account for 1.4 Trillion tokens</b>
* <span style="color:blue"> Tokenizer</span>: SentencePiece (to represent math and chemistry symbols)
* <span style="color:blue"> Vocab_size</span>: 45K 
* <span style="color:blue"> Architecture</span>: Decoder (80 layers) 
* <span style="color:blue"> Activation</span>: GELU
* <span style="color:blue"> Attention</span>: Dense
* <span style="color:blue"> FFN</span>: Dense
* <span style="color:blue"> Attention mask</span>: Causal 
* <span style="color:blue"> Floating point Precision</span>: <b>fp32 (storage),bfloat16 (training)</b>
* <span style="color:blue"> Positional Encoding</span>: <b>Relative</b>
* <span style="color:blue"> Optimizer</span>: **AdamW**
* <span style="color:blue"> Number of parameters:</span> 70 Billion (optimized Gopher :-) )



## References
 1. [GPT](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)
 1. [BERT](https://arxiv.org/pdf/1810.04805.pdf)
 1. [BART](https://arxiv.org/pdf/1910.13461.pdf)
 1. [T5](https://arxiv.org/pdf/1910.10683.pdf)
 1. [GPT-2](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
 1. [GPT-3](https://arxiv.org/pdf/2005.14165.pdf)
 1. [Switch](https://arxiv.org/pdf/2101.03961.pdf)
 1. [GLM](https://arxiv.org/pdf/2103.10360.pdf)
 1. [Gopher](https://arxiv.org/pdf/2112.11446.pdf)
 1. [Chinchilla](https://arxiv.org/pdf/2203.15556v1.pdf)