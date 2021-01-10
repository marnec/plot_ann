The only import you need is the `ann()` function from the `plot_ann` module (which is the only module) 


```python
from plot_ann import ann
```

To draw a network with default settings just pass the dimensionality of layers as a `List[int]`


```python
ax, *_ = ann([3, 5, 2])
ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_3_0.png)


## Figure customization

### Subplotting
If no `ax` instance is passed, a new figure and axis will be instantiatied (`fig, ax = plt.subplots()`) and the `ax` is returned.

Alternatively, one can pass an `ax`:


```python
import matplotlib.pyplot as plt
fig, [_, ax] = plt.subplots(1, 2, figsize=(8, 4))
ann([3, 5, 2], ax=ax);
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_5_0.png)


### Plot size
The plot proportions can be changed using the `width` and `height` paramters


```python
fig, axes = plt.subplots(1, 2, figsize=(8, 8))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1, height=2)
ann([3, 5, 2], ax=ax2, width=3)
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_7_0.png)


If you desire to preserve the aspect of the axis, remember to either set `ax.set_aspect('equal')` or manually set the right `figsize`. For example, default `plt` paramters will produce a non-square plot and affect the aspect of the network.


```python
ann([3, 5, 2]);
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_9_0.png)


Since in `plt` text is not affected by this distorsion, you can play with this to produce elliptical nodes with enough space to write long text inside of them


```python
fig, ax = plt.subplots(figsize=(12,5))
ax, nodes, _ = ann([3, 5, 2], ax=ax, radius=2)
ax.text(*nodes[0][0].center, 'I\'m long text', zorder=10, va='center', ha='center');
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_11_0.png)


## Network Customization
The network is fairly customizable
### Layers
Set the `layer_labels`
    
* `layer_labels=True` will set layer labels automatically
* `layer_labels=List` will set layer labels from the list from left to right


```python
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1, layer_labels=True)
ann([3, 5, 2], ax=ax2, layer_labels=['Input', 'meow']);
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_13_0.png)


### Nodes

1. Change the `radius` parameter to customize the radius of nodes:


```python
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1)
ann([3, 5, 2], ax=ax2, radius=3);
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_15_0.png)


2. Change the `node_lw` (linewidth) of nodes:


```python
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1)
ann([3, 5, 2], ax=ax2, node_lw=3);
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_17_0.png)


3. Change the `node_color`:
    * `node_colors=True` will set colors automatically (C0 for input layer and C1 for everything else)
    * `node_colors=List` will set colors specified in the list starting from top-most input the first layer and prociding towards the bottom and then towards the right (if the list is shorter than the number of nodes default color is applied) 


```python
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1, node_colors=True, node_lw=2)
ann([3, 5, 2], ax=ax2, node_colors=['C0', 'C1', 'C2', 'C3', 'C4'], node_lw=2);
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_19_0.png)


4. Set `node_labels`:
    * `node_labels=True` will set labels automatically 
    * `node_labels=List` will set labels specified in the list starting from top-most input the first layer and prociding towards the bottom and then towards the right (if the list is shorter than the number of nodes no label is applied) 


```python
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
architecture = [3, 5, 2]
ann(architecture, ax=ax1, radius=2, node_labels=True)
ann(architecture, ax=ax2, radius=2, node_labels=range(sum(architecture)-3));
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_21_0.png)


## Edges

1. Draw edges from the center of the node with `edge_from_center=True` or from the edge of the node with `edge_from_center=False`


```python
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1, radius=3)
ann([3, 5, 2], ax=ax2, edge_from_center=False, radius=3);
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_23_0.png)


2. Change the `edge_lw` (linewidth)


```python
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1)
ann([3, 5, 2], ax=ax2, edge_lw=2);
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_25_0.png)


3. Change the `edge_colors`:
    * `edge_colors=True` will set colors automatically (C0 for input layer and C1 for everything else)
    * `edge_colors=List` will set colors specified in the list starting from top-most input the first layer and prociding towards the bottom and then towards the right (if the list is shorter than the number of edges default color is applied) 


```python
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1, edge_colors=True, edge_lw=1)
ann([3, 5, 2], ax=ax2, edge_colors=['C0', 'C1', 'C2', 'C3', 'C4'], edge_lw=1);
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_27_0.png)


4. Set `edge_labels`:
    * `edge_labels=True` will set labels automatically 
    * `edge_labels=List` will set labels specified in the list starting from top-most input the first layer and prociding towards the bottom and then towards the right (if the list is shorter than the number of edges no label is applied) 


```python
import numpy as np
fig, axes = plt.subplots(1, 2, figsize=(12.5, 5))
ax1, ax2 = axes
architecture = [3, 5, 2]
ann(architecture, ax=ax1, edge_labels=True)
ann(architecture, ax=ax2, edge_labels=range(np.prod(architecture)-10));
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_29_0.png)


5. Change `edge_label_spacing`:
    * `edge_label_spacing=0` will have all edge labels of a layer in the center of the edge (if all labels are drawn some of them will overlap)
    * `edge_label_spacing>0` will displace a label left if its rotation angle is > 0 else right 


```python
import numpy as np
fig, axes = plt.subplots(1, 2, figsize=(12.5, 5))
ax1, ax2 = axes
architecture = [3, 5, 2]
ann(architecture, ax=ax1, edge_labels=True, edge_label_spacing=0)
ann(architecture, ax=ax2, edge_labels=True, edge_label_spacing=1);
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_31_0.png)


6. `bias=True` will assume that the topmost input in `architecture` is the bias for each layer (no edges reaching them from the previous layer) and will change the indexing for `node_labels=True` and `edge_labels=True`


```python
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1, radius=2, bias=False, node_labels=True)
ann([3, 5, 2], ax=ax2, radius=2, bias=True, node_labels=True)
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_33_0.png)

