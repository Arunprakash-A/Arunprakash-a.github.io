---
title: "All About nn.Modules in Pytorch"
date: 2024-08-10
tags: DL
key: "AAnP1008" 
comment: true
mathjax: true
--- 
If you are a researcher or someone who builds/tweaks the deep learning models regularly using the Pytorch framework or any other high-level frameworks that are built on top of Pytorch such as Huggingface, then it is extremely important to understand Pytorch's `nn.Modules`. This is because your model could run without displaying any symptoms even if you are training the model `INCORRECTLY`{:.error}! What do I mean by that? 

For example, often we need to freeze the parameters of a few layers or a layer (say embeddings in transformer), add a new layer with learnable parameters, change the initialization scheme and train the model from scratch, do some fancy way of updating parameters (like LORA, QLORA). All these tasks require us to change the code carefully (that is, you should know what you are doing)! Having a partial understanding of `nn.Modules` will create a false impression (because it won't raise an error) that your model is working as you expected.

The beginners usefully confuse the various ways of making a tensor learnable in Pytorch such as setting `requires_grad=True` or using `nn.Parameter(tensor)` or directly using ``nn.Linear, nn.Conv2d..``. 

In this post, let us use simple examples to understand the `nn.Modules` better and nuances of using `requires_grad=True`, `nn.Parameter(tensor)` and ``nn.Linear, nn.Conv2d..``. You should look into the documentation even if you have a slight doubt about the usage

If you are new to Pytorch, then take a look at this [Github repo](https://github.com/Arunprakash-A/DL-Pytorch-Workshop) to learn Pytorch modules and come back here!


{% highlight python linenos %}
import torch
import torch.nn as nn
{% endhighlight %}


## MLP Module


{% highlight python linenos %}
class MLP(nn.Module):
  
  def __init__(self,x_dim,h1_dim,h2_dim,out_dim):
    super().__init__()
    self.w1 = nn.Linear(x_dim,h1_dim,bias=True)
    self.w2 = nn.Linear(h1_dim,h2_dim,bias=True)
    self.w3 = nn.Linear(h2_dim,out_dim,bias=True)
    
  def forward(self,x):
    out = torch.relu(self.w1(x))
    out = torch.relu(self.w2(out))
    out = torch.relu(self.w3(out))    
    return out
{% endhighlight %}


```python
#instance
mlp = MLP(1,3,3,1)
```


{% highlight python linenos %}
x = torch.tensor([1.0])
y = torch.tensor([0.0])
{% endhighlight %}


```python
#print output
mlp(x)
```




    tensor([0.4890], grad_fn=<ReluBackward0>)




```python
print(mlp)
```

    MLP(
      (w1): Linear(in_features=1, out_features=3, bias=True)
      (w2): Linear(in_features=3, out_features=3, bias=True)
      (w3): Linear(in_features=3, out_features=1, bias=True)
    )


* Just define a dummy **HEAD** Module to understand different terminologies like children, and modules..

{% highlight python linenos %}
class HEAD(nn.Module):
    
    def __init__(self):
        super().__init__()
        self.mlp = MLP(1,3,3,1) # add mlp module here
        self.w = nn.Parameter(torch.randn(1)) # using nn.Parameter instead of linear layer
        self.b = nn.Parameter(torch.randn(1)) # using nn.Parameter instead of linear layer
    
    def forward(self,x):
        # do multiplication of x with w instead of passing x as self.w(x) as in MLP module as w is a param
        out = self.mlp(x)
        out = self.w*x+self.b         
        return out
{% endhighlight %}

**Some useful methods** that help us initialize parameters, add hooks and anything we wish to do with the model.

## Children
 * Return an iterator over **immediate** children modules.
 * Immediate children here are: all three `Linear` layers


{% highlight python linenos %}
for child_name,layer in mlp.named_children():
    print(f'child_name:{child_name},\t layer:{layer}')
    print(isinstance(layer,nn.Linear))
    print(isinstance(layer,nn.Embedding))
{% endhighlight %}

    child_name:w1,	 layer:Linear(in_features=1, out_features=3, bias=True)
    True
    False
    child_name:w2,	 layer:Linear(in_features=3, out_features=3, bias=True)
    True
    False
    child_name:w3,	 layer:Linear(in_features=3, out_features=1, bias=True)
    True
    False


Now let's look at the children of the head module


{% highlight python linenos %}
head = HEAD()
print(head(x))
{% endhighlight %}

    tensor([-0.8912], grad_fn=<AddBackward0>)


Immediate children of the head module are the `MLP` module alone, What? Why?


{% highlight python linenos %}
for child_name,layer in head.named_children(): #head module as root
    print(f'child_name:{child_name},\t layer:{layer}')
    print(isinstance(layer,nn.Linear))
    print(isinstance(layer,nn.Embedding))
{% endhighlight %}

    child_name:mlp,	 layer:MLP(
      (w1): Linear(in_features=1, out_features=3, bias=True)
      (w2): Linear(in_features=3, out_features=3, bias=True)
      (w3): Linear(in_features=3, out_features=1, bias=True)
    )
    False
    False


**Observations**
* Adding parameters via `nn.Parameters()` is **not considered as child** (obvious)
* Only the Modules are considered as child
* Let's replace `nn.Parameter` by `nn.Linear` and see what happens

{% highlight python linenos %}
class HEAD(nn.Module):
    
    def __init__(self):
        super().__init__()
        self.mlp = MLP(1,3,3,1) # add mlp here
        self.w =  nn.Linear(1,1,bias=True) # using linear layer        
    
    def forward(self,x):       
        out = self.mlp(x)
        out = self.w(x)       
        return out
{% endhighlight %}


```python
head = HEAD()
print(head(x))
```

    tensor([0.4823], grad_fn=<AddBackward0>)


**Immediate** children of the head module are `MLP` and `Linear modules`


{% highlight python linenos %}
for child_name,layer in head.named_children(): # head module as root
    print(f'child_name:{child_name},\t layer:{layer}')
    print(isinstance(layer,nn.Linear))
    print(isinstance(layer,nn.Embedding))
{% endhighlight %}

    child_name:mlp,	 layer:MLP(
      (w1): Linear(in_features=1, out_features=3, bias=True)
      (w2): Linear(in_features=3, out_features=3, bias=True)
      (w3): Linear(in_features=3, out_features=1, bias=True)
    )
    False
    False
    child_name:w,	 layer:Linear(in_features=1, out_features=1, bias=True)
    True
    False


* We can use `named_children` as well if we want the name of the child module.

## Named modules
  * What does the ```named_modules``` return? How does it differes from children?
  * It returns **all the nn.modules** in the tree recursively by default **(again, nn.Parameters will be ignored)**
  * The name for the root module is '' and all the submodules will have their respective names
  * If we do not want the name of the module, just use the method `.modules()`


{% highlight python linenos %}
for module in mlp.named_modules(): #returns tuple
    print(f'Module:{module}')
{% endhighlight %}

    Module:('', MLP(
      (w1): Linear(in_features=1, out_features=3, bias=True)
      (w2): Linear(in_features=3, out_features=3, bias=True)
      (w3): Linear(in_features=3, out_features=1, bias=True)
    ))
    Module:('w1', Linear(in_features=1, out_features=3, bias=True))
    Module:('w2', Linear(in_features=3, out_features=3, bias=True))
    Module:('w3', Linear(in_features=3, out_features=1, bias=True))



{% highlight python linenos %}
for module in head.named_modules(): #returns tuple
    print(f'Module:{module}')
{% endhighlight %}

    Module:('', HEAD(
      (mlp): MLP(
        (w1): Linear(in_features=1, out_features=3, bias=True)
        (w2): Linear(in_features=3, out_features=3, bias=True)
        (w3): Linear(in_features=3, out_features=1, bias=True)
      )
      (w): Linear(in_features=1, out_features=1, bias=True)
    ))
    Module:('mlp', MLP(
      (w1): Linear(in_features=1, out_features=3, bias=True)
      (w2): Linear(in_features=3, out_features=3, bias=True)
      (w3): Linear(in_features=3, out_features=1, bias=True)
    ))
    Module:('mlp.w1', Linear(in_features=1, out_features=3, bias=True))
    Module:('mlp.w2', Linear(in_features=3, out_features=3, bias=True))
    Module:('mlp.w3', Linear(in_features=3, out_features=1, bias=True))
    Module:('w', Linear(in_features=1, out_features=1, bias=True))


* MLP is a module we created by deriving from `nn.Module`
* Linear is also a module created by deriving from `nn.Module`
* Therefore, if we want all the modules in the model with their names, then we need to call `named_modules`

## parameters and named_parameters


{% highlight python linenos %}
for parameter in mlp.named_parameters(): # returns tuple
    print(f'name: {parameter[0]}  \n type: {type(parameter[0])} \n param:{parameter[1]} \n type:{type(parameter[1])} ')
    print('--'*60)
{% endhighlight %}

    name: w1.weight  
     type: <class 'str'> 
     param:Parameter containing:
    tensor([[-0.2805],
            [-0.1376],
            [ 0.0760]], requires_grad=True) 
     type:<class 'torch.nn.parameter.Parameter'> 
    ------------------------------------------------------------------------------------------------------------------------
    name: w1.bias  
     type: <class 'str'> 
     param:Parameter containing:
    tensor([0.6878, 0.7096, 0.1408], requires_grad=True) 
     type:<class 'torch.nn.parameter.Parameter'> 
    ------------------------------------------------------------------------------------------------------------------------
    name: w2.weight  
     type: <class 'str'> 
     param:Parameter containing:
    tensor([[ 0.3649, -0.4209, -0.5017],
            [-0.3077, -0.0009, -0.5688],
            [-0.4915, -0.4050, -0.5599]], requires_grad=True) 
     type:<class 'torch.nn.parameter.Parameter'> 
    ------------------------------------------------------------------------------------------------------------------------
    name: w2.bias  
     type: <class 'str'> 
     param:Parameter containing:
    tensor([-0.1146,  0.0343,  0.1846], requires_grad=True) 
     type:<class 'torch.nn.parameter.Parameter'> 
    ------------------------------------------------------------------------------------------------------------------------
    name: w3.weight  
     type: <class 'str'> 
     param:Parameter containing:
    tensor([[-0.4755,  0.1015,  0.5086]], requires_grad=True) 
     type:<class 'torch.nn.parameter.Parameter'> 
    ------------------------------------------------------------------------------------------------------------------------
    name: w3.bias  
     type: <class 'str'> 
     param:Parameter containing:
    tensor([0.4890], requires_grad=True) 
     type:<class 'torch.nn.parameter.Parameter'> 
    ------------------------------------------------------------------------------------------------------------------------


* We can also get the parameters by its name


```python
mlp.get_parameter('w1.weight')
```




    Parameter containing:
    tensor([[-0.1526],
            [ 0.2645],
            [-0.2916]], requires_grad=True)




```python
for x in mlp.named_buffers(): # we do not have any buffers
    print(x)
```

* Parameters without name

{% highlight python linenos %}
for parameter in mlp.parameters():
    print(f'shape:{parameter.shape}, \t num_ele: {parameter.numel()}, \t type:{type(parameter)}')
    print('--'*40)
    
{% endhighlight %}

    shape:torch.Size([3, 1]), 	 num_ele: 3, 	 type:<class 'torch.nn.parameter.Parameter'>
    --------------------------------------------------------------------------------
    shape:torch.Size([3]), 	 num_ele: 3, 	 type:<class 'torch.nn.parameter.Parameter'>
    --------------------------------------------------------------------------------
    shape:torch.Size([3, 3]), 	 num_ele: 9, 	 type:<class 'torch.nn.parameter.Parameter'>
    --------------------------------------------------------------------------------
    shape:torch.Size([3]), 	 num_ele: 3, 	 type:<class 'torch.nn.parameter.Parameter'>
    --------------------------------------------------------------------------------
    shape:torch.Size([1, 3]), 	 num_ele: 3, 	 type:<class 'torch.nn.parameter.Parameter'>
    --------------------------------------------------------------------------------
    shape:torch.Size([1]), 	 num_ele: 1, 	 type:<class 'torch.nn.parameter.Parameter'>
    --------------------------------------------------------------------------------


**Important**:
* If we want to modify or initialize the weights, then use `module.weight = nn.Parameter()`. Avoid using `module.weight = torch.Tensor([],requires_grad=True)`

## Initialize the weights randomly
 * Weights of Linear layers are by default initialized randomly using uniform distribution (Kaiming) with $U(-\sqrt{k},\sqrt{k})$, where $k=\frac{1}{in\_features}$ [doc](https://pytorch.org/docs/stable/generated/torch.nn.Linear.html) 


```python
w1 = nn.Linear(5,4,bias=True)
print(w1.weight, type(w1.weight))
```

    Parameter containing:
    tensor([[ 0.0492, -0.0842,  0.0332,  0.2264, -0.3632],
            [ 0.0654,  0.0897,  0.3019, -0.3227,  0.1919],
            [ 0.0218, -0.3282,  0.4164, -0.3662,  0.4460],
            [-0.2443,  0.0830,  0.2533, -0.3738,  0.0574]], requires_grad=True) <class 'torch.nn.parameter.Parameter'>


* We can manually initialize using `nn.Parameter()` or define an initialize function and apply it to all the parameters
* The latter is helpful if we have a really big model and changing an initialization strategy going layer by layer is painful


```python
w1.weight = nn.Parameter(torch.randn(5,4))
print(w1.weight)
```

    Parameter containing:
    tensor([[ 0.4229, -0.6291, -0.4947,  1.7361],
            [-0.6693, -1.5704, -0.3898, -0.0944],
            [-0.3906, -0.8454,  0.2299, -1.0408],
            [ 0.9672,  1.3886, -1.1870, -0.8637],
            [-0.0612,  0.8623, -1.3237, -0.1126]], requires_grad=True)


* Is that legal? Does that work? 
* We answered it already
* Anyhow, let's look inside the source code

{% highlight python linenos %}
self.weight = Parameter(torch.empty((out_features, in_features), **factory_kwargs))
    if bias:
        self.bias = Parameter(torch.empty(out_features, **factory_kwargs))
    else:
        self.register_parameter('bias', None)
    self.reset_parameters()

def reset_parameters(self) -> None:
    # Setting a=sqrt(5) in kaiming_uniform is the same as initializing with
    # uniform(-1/sqrt(in_features), 1/sqrt(in_features)). For details, see
    # https://github.com/pytorch/pytorch/issues/57109
    init.kaiming_uniform_(self.weight, a=math.sqrt(5))
    if self.bias is not None:
        fan_in, _ = init._calculate_fan_in_and_fan_out(self.weight)
        bound = 1 / math.sqrt(fan_in) if fan_in > 0 else 0
        init.uniform_(self.bias, -bound, bound)
{% endhighlight %}

* Finally, `nn.functional.linear(x,self.weight,self.bias)` is called in the forward method. 
* Therefore, ```w1.weight``` modifies ```self.weight``` before calling the forward method

What if we want to initialize the parameters of **all linear layers of the model** using normal distribution?


{% highlight python linenos %}
def init_weights(module):
    if isinstance(module,nn.Linear):
        torch.nn.init.normal_(module.weight,mean=0.0,std=0.02)    
{% endhighlight %}

Apply `fn` **recursively** to every submodule (as returned by .children()) as well as self.


```python
head.apply(init_weights)
```




    HEAD(
      (mlp): MLP(
        (w1): Linear(in_features=1, out_features=3, bias=True)
        (w2): Linear(in_features=3, out_features=3, bias=True)
        (w3): Linear(in_features=3, out_features=1, bias=True)
      )
      (w): Linear(in_features=1, out_features=1, bias=True)
    )



* Children first return MLP
* GO into MLP and its children..start recursing!


```python
stack = []
```

{% highlight python linenos %}
def recursive_call(module):
    for module in module.children():
        if isinstance(module,nn.Parameter):            
            return 1
        recursive_call(module)
    print(module)
{% endhighlight %}


```python
recursive_call(head)
```

    Linear(in_features=1, out_features=3, bias=True)
    Linear(in_features=3, out_features=3, bias=True)
    Linear(in_features=3, out_features=1, bias=True)
    Linear(in_features=3, out_features=1, bias=True)
    Linear(in_features=1, out_features=1, bias=True)
    Linear(in_features=1, out_features=1, bias=True)


## Hook for tracking


* Hooks are mostly used for debugging purposes (such as tracking input, gradient, output...)

### forward_hook
* Modifies the output (if needed)
* Look at the signature of various hooks
* **We can register more than one hook for the same Module**

**Signature:** ```hook(module, input, output) -> None or modified output``` [doc](https://pytorch.org/docs/stable/generated/torch.nn.modules.module.register_module_forward_hook.html)


{% highlight python linenos %}
out = []
def forward_hook_1(module,input,output):
    ## we can do whatever we want like storing, printing, tracking..
    print(module,input,output)    

def forward_hook_2(module,input,output):
    out.append(output)  
{% endhighlight %}

{% highlight python linenos %}
handle_hook_1 = mlp.register_forward_hook(forward_hook_1)
handle_hook_2 = mlp.register_forward_hook(forward_hook_2)
{% endhighlight %}


```python
#execute three times to coolect the output from forward the "out"
for i in range(3):
    mlp(x)
```

    MLP(
      (w1): Linear(in_features=1, out_features=3, bias=True)
      (w2): Linear(in_features=3, out_features=3, bias=True)
      (w3): Linear(in_features=3, out_features=1, bias=True)
    ) (tensor([1.]),) tensor([0.0551], grad_fn=<ReluBackward0>)
    MLP(
      (w1): Linear(in_features=1, out_features=3, bias=True)
      (w2): Linear(in_features=3, out_features=3, bias=True)
      (w3): Linear(in_features=3, out_features=1, bias=True)
    ) (tensor([1.]),) tensor([0.0551], grad_fn=<ReluBackward0>)
    MLP(
      (w1): Linear(in_features=1, out_features=3, bias=True)
      (w2): Linear(in_features=3, out_features=3, bias=True)
      (w3): Linear(in_features=3, out_features=1, bias=True)
    ) (tensor([1.]),) tensor([0.0551], grad_fn=<ReluBackward0>)



```python
print(out)
```

    [tensor([0.0551], grad_fn=<ReluBackward0>), tensor([0.0551], grad_fn=<ReluBackward0>), tensor([0.0551], grad_fn=<ReluBackward0>), tensor([0.0551], grad_fn=<ReluBackward0>), tensor([0.0551], grad_fn=<ReluBackward0>)]


* How do we remove the hook?


{% highlight python linenos %}
handle_hook_1.remove()
handle_hook_2.remove()
{% endhighlight %}


```python
for i in range(3):
    mlp(x)
```

Modify the output


```python
out = mlp(x)
print(out)
```

    tensor([0.0551], grad_fn=<ReluBackward0>)



```python
def fwd_hook(module,args,output):
    return 2*output
```


```python
handle_1 = mlp.register_forward_hook(fwd_hook)
```


```python
out = mlp(x)
print(out)
```

    tensor([0.1102], grad_fn=<MulBackward0>)



```python
handle_1.remove()
```

### forward Pre_hook

* signature: `hook(module, input) -> None or modified input`
* To (optionally) modify the **input**


{% highlight python linenos %}
def fwd_pre_hook(module,input):
    print(input)

handle = mlp.register_forward_pre_hook(fwd_pre_hook)
{% endhighlight %}


```python
mlp(x)
```

    (tensor([1.]),)





    tensor([0.0551], grad_fn=<ReluBackward0>)



### backward_hook

### backward_pre_hook

### save/load State_dict
* Both parameters and persistent buffers (e.g. running averages) are included


```python
mlp.state_dict().keys()
```




    odict_keys(['w1.weight', 'w1.bias', 'w2.weight', 'w2.bias', 'w3.weight', 'w3.bias'])



Hope you enjoyed reading the article and learned something important! 