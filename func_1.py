#!/usr/bin/env python3

# import libraries and functions
import networkx as nx  
import matplotlib.pyplot as plt

from path_finder import get_n_steps_neighbours
from dataset_loader import DatasetLoader
from utils import make_adj_list

# create Dataframes from .co and .gr files
coord = DatasetLoader('coordinates').get_dataset()
dist = DatasetLoader('distance').get_dataset()
timedist = DatasetLoader('time-distance').get_dataset()

# create dicts with all neighbors for each node
neighbors = make_adj_list('distance')
t_neighbors = make_adj_list('time-distance')

# Now we define a function that takes in input: 
# 1. One of the 2 dicts create above; 2. An Input-Node; 3. A cumulative counter = 0; 4. A threshold
# It returns the list of nodes at smaller distance than the threshold from the Input-Node, corresponding to its' neighborhood

def get_neighbourhood(adj_list, start, curr_d, d):
    
    res = []
    
    if curr_d > d:
        return []
    else:
        
        neighbours = get_n_steps_neighbours(adj_list, start, 1)
        
        for neighbour in neighbours:
            distance = adj_list[start][neighbour]
            
            if curr_d + distance <= d:
                res.append(neighbour)
            
            res.extend(get_neighbourhood(adj_list, neighbour, curr_d+distance, d))
        
    return list(dict.fromkeys(res))

# From the result of the function above we can implement its Visualization Function that takes the same input variables.

def vis_1(adj_list, start, curr_d, d):
    
    lst = get_neighbourhood(adj_list, start, curr_d, d)
    # Initialize the graph from the result of Functionality1 and the coordinates for the positions
    cnod = []
    clat = []
    clon = []
    graph = nx.Graph()
    graph.add_nodes_from(lst)
    
    for k in lst:
        graph.add_edges_from([(k,key,{'distance':value}) for key,value in adj_list[k].items() if key in lst])
        cnod.append(coord.iloc[k-1][1])
        clat.append(coord.iloc[k-1][2])
        clon.append(coord.iloc[k-1][3])
    
    # Change shapes and colors for nodes/edges 
    color_edge = ''
    shape_node = ''
    size_font = ''
    
    if adj_list == neighbors:
        color_edge = 'red'
        shape_node = 'o'
    elif adj_list == t_neighbors:
        color_edge = 'purple'
        shape_node = 'D'
    if len(lst) <= 10:
        size_font = 10
    else:
        size_font = 9
        
        
    # Visualize the Map, highlighting the Input-Node    
    pos = {cnod[i]:[clat[i], clon[i]] for i in range(len(lst))}
    nx.draw(graph, pos, node_color='lightgreen', node_size = 150, node_shape = shape_node,
            edge_color = color_edge, with_labels = True, font_size = size_font)
    gstart = nx.Graph()
    gstart.add_node(start)
    nx.draw(gstart,pos,node_color='yellow', node_size = 225, node_shape = shape_node)
    
    plt.show()
        
    
