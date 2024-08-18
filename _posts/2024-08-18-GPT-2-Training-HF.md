---
title: "Pre-training GPT-2 from scratch"
date: 2024-08-18
tags: DL LLM Coding
key: "PGMS1808" 
pageview: true
comment: true
mathjax: true
--- 
Let us train a GPT-2 (small,`124 million parameters`{:.info}) model from scratch using the Hugging Face library. Instead of using WebText dataset (due to limited compute resources) I preferred to use the book corpus dataset that contains `74 Million`{:.info} samples (far lower than today's standard). The book corpus dataset was used to train GPT-1. So, there won't be any differences in our learning. If you get H100 for 4 days, then just change the dataset to WebText!

If you have already learned the internals of GPT-2 from [nanoGPT](https://github.com/karpathy/nanoGPT) by Andrej Karpathy, then you are good to go with HF. With the Hugging Face power packed ecosystem, training the model is a lot easier and one can quickly experiment by changing any components in the pipeline such as the dataset, model, training strategies and metrics, all with small tweaks. This is one of the primary goals of HF. They are making it a lot better over the years. Without HF, it would take days (if not weeks) to set all these things up in native DL frameworks. 

Let's get started with one step at a time

## Imports
Let us import all the necessary packages and modules and classes
{% highlight python linenos %}
from itertools import chain
import warnings
import math
import wandb

#from hf
from datasets import load_dataset, load_from_disk
from transformers import AutoTokenizer
from transformers import DataCollatorForLanguageModeling
from transformers import GPT2Config, GPT2LMHeadModel
from transformers import TrainingArguments, Trainer
{% endhighlight %}

## Preparing Input to the model

* Load the raw samples from the BookCorpus dataset
* Make training and validation splits
* Tokenize the dataset using gpt-2 tokenizer (Byteleve BPE)
* Get `input_ids` and `attention_masks` for all the samples
* Make all the sample sizes to 1024 (makes efficient use GPU compute by avoiding zero padding while batching) by concatenating the samples, followed by chunking.

{% highlight python linenos %}
# loading raw data
dataset = load_dataset("bookcorpus",trust_remote_code=True)

# make splits
dataset = dataset['train'].train_test_split(test_size=0.0015) 

# load the gpt-2 tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokenizer.pad_token=tokenizer.eos_token

# tokenize
def tokenize_function(example):
    return tokenizer(text=example["text"])
tokenized_ds = dataset.map(tokenize_function,batched=True,remove_columns='text')

# save to disk if required (use load_from_disk latter)
tokenized_ds.save_to_disk('bookcorpus/tokenized_ds')

# Make samples to a size of 1024
def concat(examples):    
    examples["input_ids"]=[list(chain.from_iterable(examples['input_ids']))] # convert chain to list of tokens
    examples["attention_mask"]=[list(chain.from_iterable(examples['attention_mask']))] # convert chain to list of tokens
    return examples
    
# takes a lot of time (worth saving it to disk)
concated_ds = tokenized_ds.map(concat,batched=True,batch_size=1000000,num_proc=8)

def chunk(examples):
    chunk_size = 1024 # modify this accordingly       
    input_ids = examples["input_ids"][0] # List[List], pass the inner list      
    attention_mask = examples["attention_mask"][0] # List[List]
    input_ids_truncated = []
    attention_mask_truncated = []
    
    #slice with step_size=chunk_size
    for i in range(0,len(input_ids),chunk_size):
        chunk = input_ids[i:i+chunk_size]
        if len(chunk)==chunk_size: # drop the last chunk if not equal
            input_ids_truncated.append(chunk)
            attention_mask_truncated.append(attention_mask[i:i+chunk_size])     
    examples['input_ids']=input_ids_truncated
    examples["attention_mask"]=attention_mask_truncated
        
    return examples   

chunked_ds = concated_ds.map(chunk,batched=True,batch_size=2,num_proc=2)
chunked_ds.save_to_disk('bookcorpus/chunked_ds') # will use this latter for diff experimentation
{% endhighlight %}

## Data Collator for batching
* We need to use a data collator to feed a batch of samples  to the model
* We set mlm=False as the same data collator can be used for Masked Language Modelling (MLM)
* Note also that the tokenizer is passed as one of the arguments to the data collator (however, while training, we pass the Encoding that contains `input_ids`, `atttention_mask` from chunked ds directly)
* Data collator returns `input_ids`, `attention_mask` and `lables` (same as `input_ids`)
{% highlight python linenos %}
data_collator = DataCollatorForLanguageModeling(tokenizer,mlm=False)
{% endhighlight %}

## Train the model
* Initialize the model randomly
* Configure the training arguments
* Train the model 
* Note the input Ids are right-shifted internally  while computing the loss
* We can track the training loss and validation loss in the wandb.
{% highlight python linenos %}
# load the model
configuration = GPT2Config()
model =GPT2LMHeadModel(configuration)

# training arguments
training_args = TrainingArguments( output_dir='gpt-2-warm-up/standard-gpt',
                                  evaluation_strategy="steps",
                                  eval_steps=500,                                  
                                  num_train_epochs=1,
                                  per_device_train_batch_size=8,
                                  per_device_eval_batch_size=8,
                                  learning_rate=2.5e-4,
                                  lr_scheduler_type='cosine',
                                  warmup_ratio=0.05,
                                  adam_beta1=0.9,
                                  adam_beta2=0.999,                                  
                                  weight_decay=0.01,                                  
                                  logging_strategy="steps",
                                  logging_steps = 500,
                                  save_steps=5000,
                                  save_total_limit=10,                                  
                                  report_to='wandb',                                  
                                 ) 
trainer = Trainer(model=model,
                 args = training_args,
                 tokenizer=tokenizer,
                 train_dataset=chunked_ds["train"],
                 eval_dataset=chunked_ds["test"],
                 data_collator = data_collator) 
{% endhighlight %}

## Text Generation Quality
* Let us generate text by giving the following prompt
* `Prompt`{:.info}: I was telling her that
* We limit the generation to 100 words
* Random generation generates gibberish (high perplexity)
{% highlight python linenos %}
model =GPT2LMHeadModel.from_pretrained('path/to/checkpoint-xxxx/') # modify the path
prompts = "I was telling her that"
inputs = tokenizer(prompts,return_tensors='pt').input_ids
outputs = model.generate(inputs, max_new_tokens=100, do_sample=True, top_k=10, top_p=0.95)
tokenizer.batch_decode(outputs, skip_special_tokens=True)
{% endhighlight %}

### Random Initialization
* `output`{:.success}: `I was telling her that pursuit AmberDiamondps versus Sorceress Antarctica rarity Dakota majesty� closure odor Releasedexisting Groups distributors Purpose acknowledgment shack Bondsupsupsup Rw shaveizensWorldOp executing executing integrating De 1886AllowAllow tattoos quarter budgetaryrahlinux Alexand Scotland CONS:" praying praying Demon Wolf Sorceress Troutphillegraph PM Alive expressing cages Corruptionbased amusement Trout FIX Many Libertarian Cousins uninstallsupposing geometric� suing paralyzed understand SandyHopeAllen 1886 1886 budgetaryapter Inform synchronized Tone reliant Scotland Mann Vest Vest who catering jerseyalaala Civicstory coil pretextMods params Moreno`

* The model has generated random words (expected)

### After 5000 steps (or seeing 40000 sequences)
* `output`{:.success}: `I was telling her that he was trying to make out.'' i do. ''i'm not sure about it. '' but i don't understand what you are, '' i whispered.we were in the middle of a night, i realized we were in a very long time, but the only way i 'd done was to keep the rest of my life from being here and my heart had gone.'' i want to get used to something like that. ''i just have to be a little more"`

* The model has learned the patterns in the bookcorpus dataset (produced output that is sort of conversation type)

* It is pretty good. However, let us see if it improves with further training

### After 40000 steps (or seeing 320000 sequences)

* `output`{:.success}: `I was telling her that she 'd be in charge of a new school, and that the day she 'd be on the run, she had to be out on the porch.i've never done anything in my life before, i never thought it would be so hard to do it when you were in my bed." no, i'm not." you aren't even supposed to do that anymore. '' " no, '' he said.`` i'm not a child, '' i whispered"`

* It is much better than the previous output as the model maintained coherency across sentences.
* You can **download the checkpoints** 
    * [Checkpoint-5k-steps](https://drive.google.com/file/d/1434yTvAfqaJyg3V1r8j5kq25uKNDlB0o/view?usp=sharing)
    * [Checkpoint-40k-steps](https://drive.google.com/file/d/17-AjEMPOrMI718oKQkypC87GdsplHTbx/view?usp=sharing)

## Reporting loss
<iframe src="https://api.wandb.ai/links/a-arun283-iit-madras/86tdj8rd" style="border:none;height:1024px;width:100%">
</iframe>

That's all. Thanks for reading.



