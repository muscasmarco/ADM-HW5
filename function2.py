#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from path_finder import dijkstra_h
from utils import make_adj_list
from dataset_loader import DatasetLoader


# In[ ]:


def duel_permutation(nodes) :
    duel_perm = list()
    for i in range(len(nodes)) :
        for j in range(i+1,len(nodes) ) :
            duel_perm.append([nodes[i],nodes[j]])
    return(duel_perm)



def find_best_initial(nodes, adj_list):
    
    nodes_permutations = duel_permutation(nodes)
    
    edge_set = list()
    min_dist = 100000000000
    for perm in nodes_permutations:
        dist, seq = dijkstra_h(adj_list, perm[0], perm[1])
        if dist < min_dist :
            min_dist = dist
            best_seq = seq
            
    for i in range(len(best_seq) - 1) :
         edge_set.append(tuple([best_seq[i],best_seq[i+1]]))
        
        
    return(min_dist,best_seq,edge_set)




def best_tree(nodes, adj_list) :
    visited_nodes = find_best_initial(nodes, adj_list)[1]
    distance = find_best_initial(nodes, adj_list)[0]
    must_visited = [x for x in nodes if x not in visited_nodes ]
    edge_set = find_best_initial(nodes, adj_list)[2]
    
    while must_visited :
        min_dist = 100000000000
        for i in must_visited :
            for j in visited_nodes :
                dist, seq = dijkstra_h(adj_list, i , j)
                if dist < min_dist :
                    min_dist = dist
                    best_seq = seq
                    
                    
        for i in range(len(best_seq) - 1) :
             edge_set.append(tuple([best_seq[i],best_seq[i+1]]))  
                
        distance += min_dist            
        must_visited = list(set(must_visited)- set(best_seq))
        visited_nodes = list(set(visited_nodes).union ( set(best_seq)))

    return(edge_set,distance)   







adj_list = make_adj_list()
best_tree([3,6,7],adj_list)

