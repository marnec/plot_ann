# Requirements

* Python >= 3.6 (There are f strings)
* matpltolib 
* numpy

# Motivation
> There are other libs that can plot ANNs, why writing your own?

This implementation is completely based on matplotlib, and doesn't require any additional library like Viz or PyGraph.

This also means that is natively compatible with jupyter noteboks

Furthermore you can also create animations that work natively in HTML pages (can't be demonstrated here since github doesn't allow script tags execution)


```python
%%capture
from matplotlib import animation, rc
from IPython.display import HTML
from itertools import chain

fig, ax = plt.subplots()
ax, nodes, edges = ann([3, 5, 2], ax=ax)
ax.set_aspect('equal')
lines = list(chain.from_iterable(chain.from_iterable(edges)))
```


```python
def animate(i, lw):
    lw = np.roll(lw, i)
    for w, line in zip(lw, lines):
        line.set_linewidth(w)
    return lines

lw = np.random.rand(len(lines))
anim = animation.FuncAnimation(fig, animate, fargs=(lw,),
                               frames=100, interval=60, repeat=True,
                               blit=True)
# HTML(anim.to_jshtml())
```

# Usage
The only import you need is the `ann()` function from the `plot_ann` module (which is the only module) 


```python
from plot_ann import ann
```

To draw a network with default settings just pass the dimensionality of layers as a `List[int]`


```python
ax, *_ = ann([3, 5, 2])
ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_6_0.png)


The `ann()` function returns `ax, nodes, edges`. Where `ax` is an instance of [matplotlib.axes](https://matplotlib.org/3.3.3/api/axes_api.html); `nodes` is a structured List of [matplotlib.patches.Circle](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.patches.Circle.html) and `edges` is a structured list of [matplotlib.lines.Line2D](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.lines.Line2D.html).


```python
ann([1, 1])
```




    (<AxesSubplot:>,
     [[<matplotlib.patches.Circle at 0x7fb1254b9c50>],
      [<matplotlib.patches.Circle at 0x7fb1254b9f28>]],
     [[[<matplotlib.lines.Line2D at 0x7fb1254c9208>]]])




![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_8_1.png)


## Figure customization

### Subplotting
If no `ax` instance is passed, a new figure and axis will be instantiatied (`fig, ax = plt.subplots()`) and the `ax` is returned.

Alternatively, one can pass an `ax`:


```python
import matplotlib.pyplot as plt
fig, [_, ax] = plt.subplots(1, 2, figsize=(8, 4))
ann([3, 5, 2], ax=ax);
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_10_0.png)


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


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_12_0.png)


If you want to preserve the aspect of the axis, remember to either set `ax.set_aspect('equal')` or manually set the right `figsize`. For example, default `plt` paramters will produce a non-square plot and affect the aspect of the network.


```python
ann([3, 5, 2]);
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_14_0.png)


Since in `plt` text is not affected by this distorsion, you can play with this to produce elliptical nodes with enough space to write long text inside of them


```python
fig, ax = plt.subplots(figsize=(12,5))
ax, nodes, _ = ann([3, 5, 2], ax=ax, radius=2)
ax.text(*nodes[0][0].center, 'I\'m long text', zorder=10, va='center', ha='center');
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_16_0.png)


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


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_18_0.png)


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


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_20_0.png)


2. Change the `node_lw` (linewidth) of nodes:


```python
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1)
ann([3, 5, 2], ax=ax2, node_lw=3);
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_22_0.png)


3. Change the `node_color`:
    * `node_colors=True` will set colors automatically (C0 for input layer and C1 for everything else)
    * `node_colors=List` will set colors specified in the list starting from top-most input the first layer and proceeding towards the bottom and then towards the right (if the list is shorter than the number of nodes default color is applied) 


```python
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1, node_colors=True, node_lw=2)
ann([3, 5, 2], ax=ax2, node_colors=['C0', 'C1', 'C2', 'C3', 'C4'], node_lw=2);
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_24_0.png)


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


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_26_0.png)


### Edges

1. Draw edges from the center of the node with `edge_from_center=True` or from the edge of the node with `edge_from_center=False`


```python
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1, radius=3)
ann([3, 5, 2], ax=ax2, edge_from_center=False, radius=3);
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_28_0.png)


2. Change the `edge_lw` (linewidth)


```python
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1)
ann([3, 5, 2], ax=ax2, edge_lw=2);
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_30_0.png)


3. Change the `edge_colors`:
    * `edge_colors=True` will set colors automatically (C0 for input layer and C1 for everything else)
    * `edge_colors=List` will set colors specified in the list starting from top-most input the first layer and proceeding towards the bottom and then towards the right (if the list is shorter than the number of edges default color is applied) 


```python
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1, edge_colors=True, edge_lw=1)
ann([3, 5, 2], ax=ax2, edge_colors=['C0', 'C1', 'C2', 'C3', 'C4'], edge_lw=1);
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_32_0.png)


4. Set `edge_labels`:
    * `edge_labels=True` will set labels automatically 
    * `edge_labels=List` will set labels specified in the list starting from top-most input the first layer and proceeding towards the bottom and then towards the right (if the list is shorter than the number of edges no label is applied) 


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


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_34_0.png)


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


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_36_0.png)


6. `bias=True` will assume that the topmost input in `architecture` is the bias for each layer (no edges reaching them from the previous layer) and will change the indexing for `node_labels=True` and `edge_labels=True`


```python
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax1, ax2 = axes
ann([3, 5, 2], ax=ax1, radius=2, bias=False, node_labels=True)
ann([3, 5, 2], ax=ax2, radius=2, bias=True, node_labels=True)
for ax in axes:
    ax.set_aspect('equal')
```


![png](https://raw.githubusercontent.com/marnec/plot_ann/master/README_files/README_38_0.png)

