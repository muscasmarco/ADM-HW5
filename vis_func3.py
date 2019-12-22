#!/usr/bin/env python
# coding: utf-8

# In[63]:


import dataset_loader
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import warnings


# In[15]:


coordinates = pd.read_csv("C:\\Users\\Nino\\Desktop\\USA-road-coordinates.CAL.co" , sep=' ', header=None)
coordinates.columns = ['type','node-id', 'latitude','longitude']


# In[20]:


def node_location(nodes) :
    
    node_map = dict()
    for node in nodes :
            node_map [node]=[coordinates["longitude"][node-1], coordinates["latitude"][node-1]]
        
    return(node_map)


# In[27]:



from path_finder import dijkstra_h
from utils import make_adj_list

def shortest_ordered_path(initial, node_set, adj_list) :
    path = list()
    path.append(initial)
    node_set.insert(0,initial)
    
    for i in range(len(node_set) - 1) :
        dist, seq = dijkstra_h(adj_list, node_set[i] , node_set[i+1])
        path += seq[1:]
    
    res = []
    for i in range(len(path)-1):
        t = (path[i], path[i+1])
        res.append(t)
        
        
        
    
    
        
    return path, res



adj_list = make_adj_list()
path , res = shortest_ordered_path(1,[1802,1805],adj_list)


# In[75]:


#area = np.pi*30
#plt.scatter(coordinates.longitude, coordinates.latitude, c='y', s=area, alpha = .5)

import warnings

node_set = [1,1802,1805]

G = nx.Graph()
pos = node_location(path)

for k in path:
        G.add_edges_from([(k,key,{'distance':value}) for key,value in adj_list[k].items() if key in path])
G.add_nodes_from(pos.keys())
for n, p in pos.items():
    G.node[n]['pos'] = p
for n in G.nodes():
    G.nodes[n]['color'] = 'r' if n in node_set else 'y'
colors = [node[1]['color'] for node in G.nodes(data=True)]
G.add_edges_from(res)

nx.draw(G, pos=pos, with_labels=True, font_size=12, node_size=700, node_color=colors, width = 3)
plt.show()
warnings.filterwarnings("ignore", category=UserWarning)


# In[ ]:




