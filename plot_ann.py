import matplotlib.pyplot as plt
import numpy as np


def ann(architecture, radius=1, width=1, height=1, ax=None, 
    node_lw=1, edge_lw=.25, bias=False, edge_from_center=True, 
    layer_labels=False, node_labels=False, edge_labels=False, edge_label_spacing=1,
    node_colors=False, edge_colors=False):

    if ax is None:
        fig, ax = plt.subplots()

    max_m = max(architecture)
    max_n = len(architecture)

    v_spacing = height/max_m
    h_spacing = width/max_n

    # Nodes
    nodes = []
    radius = (v_spacing + h_spacing)/2 * radius/10
    
    net_left = h_spacing * (max_n - 1)/max_n/2
    for n, layer_size in enumerate(architecture):
        layer_top = v_spacing * (layer_size - 1)/2 + 1/2
        
        x = net_left + n*h_spacing
        layer = []

        for m in range(layer_size):
            y = layer_top - m*v_spacing
        
            circle = plt.Circle((x, y), radius, color='w', ec='k', zorder=4, lw=node_lw)
            ax.add_artist(circle)

            layer.append(circle)
        nodes.append(layer)

        # Layer labels
        layer_label_y = 0.0  
        if layer_labels is True:
            ax.text(x, layer_label_y, f"Layer {n+1}", fontsize=10, va='center', ha='center', zorder=10)
        elif isinstance(layer_labels, list):
            if n <= len(layer_labels) - 1:
                ax.text(x, layer_label_y, layer_labels[n], fontsize=10, va='center', ha='center', zorder=10)


    # Edges
    edges = []
    for n, (layer_n1, layer_n2) in enumerate(zip(nodes[:-1], nodes[1:]), 1):
        edge_from = []
        for node_layer_n1 in layer_n1:
            edge_to = []
            for i, node_layer_n2 in enumerate(layer_n2):
                if bias is False or (bias is True and i != 0) or n == max_n-1:
                    x, y = zip(*[node_layer_n1.center, node_layer_n2.center])
                    if edge_from_center is False:
                        x = x[0] + radius, x[1] - radius
                    line = plt.Line2D(x, y, lw=edge_lw, c='k')
                    ax.add_artist(line)
                    edge_to.append(line)
            edge_from.append(edge_to)
        edges.append(edge_from)
    
    # Node labels and colors
    tot_nodes = -1
    for l, layer in enumerate(nodes, 1):
        for j, node in enumerate(layer, 1):
            tot_nodes += 1
            # labels
            label = ''
            if node_labels is True:
                term = 'x' if l == 1 else 'a'
                j = j if (bias is False or l == max_n) else j - 1
                label = f'${term}_{{{j}}}^{{({l})}}$'
            elif isinstance(node_labels, (list, range)):
                if tot_nodes <= len(node_labels) - 1:
                    label = node_labels[tot_nodes]
            ax.text(*node.center, label, zorder=10, ha='center', va='center')
            # colors
            if not node_colors is False:
                c = 'k'
                if node_colors is True:
                    c = 'C0' if l == 1 else 'C1'
                elif isinstance(node_colors, list):
                    if tot_nodes <= len(node_colors) - 1:
                        c = node_colors[tot_nodes]
                node.set_edgecolor(c)

    # Edge labels and colors
    tot_edges = -1
    for l, layer in enumerate(edges, 1):
        for j, from_node in enumerate(layer, 1):
            for i, edge in enumerate(from_node, 1):
                tot_edges += 1
                # labels
                label = ''
                if edge_labels is True:
                    j = j if bias is False else j - 1
                    theta_idx = ''.join(map(str, [j,i]))
                    label = f'$\\Theta_{{{theta_idx}}}^{{({l})}}$'
                elif isinstance(edge_labels, (list, range)):
                    if tot_edges <= len(edge_labels) - 1:
                        label = edge_labels[tot_edges]
                x, y = edge.get_xdata(), edge.get_ydata()
                xdist, ydist = np.diff(x).squeeze(), np.diff(y).squeeze() 
                rotation = np.degrees(np.arctan(ydist/xdist))
                x += (xdist if rotation < 0 else -xdist)*.1 * edge_label_spacing
                y += (ydist if rotation < 0 else -ydist)*.1 * edge_label_spacing
                ax.text(np.mean(x), np.mean(y), label, va='bottom', ha='center',
                rotation=rotation)
                # colors
                if not edge_colors is False:
                    c = 'k'
                    if edge_colors is True:
                        c = 'C0' if l == 1 else 'C1'
                    elif isinstance(edge_colors, list):
                        if tot_edges <= len(edge_colors) - 1:
                            c = edge_colors[tot_edges]
                    edge.set_color(c)

    ax.set_xlim(0, width)
    ax.set_ylim(0.5 - height/2, 0.5 + height/2)
    ax.axis('off')

    return ax, nodes, edges
