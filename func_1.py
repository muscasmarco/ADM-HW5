#!/usr/bin/env python3

# import libraries and functions
import networkx as nx  
import matplotlib.pyplot as plt

from path_finder import get_n_steps_neighbours
from dataset_loader import DatasetLoader

# Now we define a function that takes in input: 
# 1. The adjacency list (go to utils.py to find out how to get it); 
# 2. An Input-Node; 3. A cumulative counter = 0; 4. A threshold
# It returns the list of nodes at smaller distance than the threshold from the Input-Node, corresponding to its' neighborhood

def get_neighbourhood(adj_list, start, current_distance, max_distance):
    
    res = []
    
    if current_distance > max_distance:
        return []
    else:
        # Get the immediate neighbours
        neighbours = get_n_steps_neighbours(adj_list, start, 1)
        
        # Here we are choosing only the neigbours that are closer than max_distance
        for neighbour in neighbours:
            distance = adj_list[start][neighbour]
            
            if current_distance + distance <= max_distance:
                res.append(neighbour)
            
            # Now try to find the neighbours of the neighbours
            res.extend(get_neighbourhood(adj_list, neighbour, current_distance+distance, max_distance))
        
    return list(dict.fromkeys(res)) # Because we do not want duplicates

# From the result of the function above we can implement its Visualization Function that takes the same input variables.

def vis_1(adj_list, start, curr_d, d, distance_metric='distance'):
    coordinates = DatasetLoader('coordinates').get_dataset()

    lst = get_neighbourhood(adj_list, start, curr_d, d)
    # Initialize the graph from the result of Functionality1 and the coordinates for the positions
    cnod = []
    clat = []
    clon = []
    graph = nx.Graph()
    graph.add_nodes_from(lst)
    
    for k in lst:
        graph.add_edges_from([(k,key,{'distance':value}) for key,value in adj_list[k].items() if key in lst])
        cnod.append(coordinates.iloc[k-1][1])
        clat.append(coordinates.iloc[k-1][2])
        clon.append(coordinates.iloc[k-1][3])
    
    # Change shapes and colors for nodes/edges 
    color_edge = ''
    shape_node = ''
    size_font = ''
    
    if distance_metric == 'distance':
        color_edge = 'red'
        shape_node = 'o'
    elif distance_metric == 'time_distance':
        color_edge = 'purple'
        shape_node = 'D'
    else:
        color_edge = 'white'
        shape_node = '^'
        
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
        
    
