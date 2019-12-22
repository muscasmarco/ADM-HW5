#!/usr/bin/env python
# coding: utf-8

# # <font color=red> Implementation of the backend
# 
# The goal of this part is the implementation of a unique system that has four different functionalities. The program takes in input always a number i in [1,4]: given the input, the program has to run Functionality i, applied to the graph you create from the downloaded data.

# ## Functionality 1 - Find the Neighbours!
# 
# It takes in input:
# 
# * __a node v__
# *  One of the following distances function: __t(x,y), d(x,y) or network distance (i.e. consider all edges to have weight equal to 1).__
# * __a distance threshold d__
# 
#  Implement an algorithm (using proper data structures) that returns the set of nodes at distance <= d from v, corresponding to v’s neighborhood.

# In[168]:


# import libraries and functions
from dataset_loader import DatasetLoader
from utils import make_adj_list
from path_finder import get_n_steps_neighbours


# In[173]:


# create Dataframe from .co and .gr files
coord = DatasetLoader('coordinates','C:\\Users\\giuseppe\\Desktop\\HW5\\dataset\\').get_dataset()
dist = DatasetLoader('distance','C:\\Users\\giuseppe\\Desktop\\HW5\\dataset\\').get_dataset()
timedist = DatasetLoader('time-distance','C:\\Users\\giuseppe\\Desktop\\HW5\\dataset\\').get_dataset()

# create dicts with all neighbors for each node
neighbors = make_adj_list('distance')
t_neighbors = make_adj_list('time-distance')


# In[174]:


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
    


# # <font color= red> Implementation of the frontend
# In this section, you build the visualizations for users’ queries results.
# 
# 

# ## Visualization 1 - Visualize the Neighbours!
# 
# Once the user runs Functionality 1, we want the system to show in output a complete map that contains: the input node, the output nodes and all the streets that connect these points. Choose different colors in order to highlight which is the input node, and which are the output nodes. Furthermore, choose different colors for edges, according to the distance function used.

# In[175]:


# import libraries
import networkx as nx  
import matplotlib.pyplot as plt


# In[499]:


def vis1(adj_list, start, curr_d, d):
    
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
    
    


# In[500]:


vis1(neighbors, 3, 0, 6000)


# In[501]:


vis1(t_neighbors, 2, 0, 6000)


# In[ ]:




