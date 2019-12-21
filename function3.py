#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from path_finder import dijkstra_h
from utils import make_adj_list
from itertools import chain




def shortets_ordered_path(initial, node_set, adj_list) :
    path = list()
    path.append(initial)
    node_set.insert(0,initial)
    for i in range(len(node_set) - 1) :
        dist, seq = dijkstra_h(adj_list, node_set[i] , node_set[i+1])
        path.append(seq[1:])
        path = list(chain.from_iterable(i if isinstance(i, list) else [i] for i in path))  # for flattening the nested list
         
    return(path)



adj_list = make_adj_list()
shortets_ordered_path(1,[1802,1805],adj_list)

