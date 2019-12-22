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
    
    result = list(dict.fromkeys(res)) # Because we do not want 
    if start in result:
        result.remove(start)
        
    return result

# From the result of the function above we can implement its Visualization Function.

def vis_1(adj_list, start, neighbours, distance_metric='distance'):
    coordinates = DatasetLoader('coordinates').get_dataset()

    #lst = get_neighbourhood(adj_list, start, curr_d, d)
    # Initialize the graph from the result of Functionality1 and the coordinates for the positions
    cnod = []
    clat = []
    clon = []
    graph = nx.Graph()
    graph.add_nodes_from([start])
    graph.add_nodes_from(neighbours)
    
    all_nodes = [start] + neighbours
  
    for node_id in all_nodes:
        graph.add_edges_from([(node_id, key,{'distance':value}) for key,value in adj_list[node_id].items() if key in all_nodes])
        
        cnod.append(coordinates[coordinates['node-id'] == node_id]['node-id'].values[0])
        clat.append(coordinates[coordinates['node-id'] == node_id]['latitude'].values[0])
        clon.append(coordinates[coordinates['node-id'] == node_id]['longitude'].values[0])
        
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
        color_edge = 'blue'
        shape_node = '^'
        
    if len(neighbours) <= 10:
        size_font = 10
    else:
        size_font = 9
        
        
    # Visualize the Map, highlighting the Input-Node
    pos = {cnod[i]:[clat[i], clon[i]] for i in range(len(all_nodes))}
    
    color_map = ['yellow'] + (['lightgreen'] * (len(all_nodes)-1))
    nx.draw(graph, pos, node_color=color_map, node_size = 150, node_shape = shape_node,
            edge_color = color_edge, with_labels = True, font_size = size_font)
    
    plt.show()
        
    
