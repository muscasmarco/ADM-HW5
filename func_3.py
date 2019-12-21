#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from path_finder import dijkstra_h
from utils import make_adj_list

def shortest_ordered_path(initial, node_set, adj_list) :
    path = list()
    path.append(initial)
    node_set.insert(0,initial)
    
    for i in range(len(node_set) - 1) :
        dist, seq = dijkstra_h(adj_list, node_set[i] , node_set[i+1])
        path += seq[1:]
        
    return(path)



adj_list = make_adj_list()
res = shortest_ordered_path(1,[1802,1805],adj_list)

