#!/usr/bin/env python
# coding: utf-8
'''
For this functionality we apply Dijkstra algo between each node in our ordered node set
'''



from path_finder import dijkstra_h
from utils import make_adj_list

def shortest_ordered_path(initial, node_set, adj_list) :
    path = list()
    path.append(initial)  #initial the path list with the first node
    node_set.insert(0,initial) #add the initial node to the node_set
    
    for i in range(len(node_set) - 1) :
        dist, seq = dijkstra_h(adj_list, node_set[i] , node_set[i+1])
        path += seq[1:]  #we add nodes from the second element because we put the start point of the path in previous step
    
    res = []
    for i in range(len(path)-1): #creating edge set
        t = (path[i], path[i+1])
        res.append(t)
        
    return res


''' Testing
adj_list = make_adj_list()
res = shortest_ordered_path(1,[1802,1805],adj_list)
'''
