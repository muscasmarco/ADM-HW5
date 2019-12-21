#!/usr/bin/env python
# coding: utf-8

from path_finder import dijkstra_h
from utils import make_adj_list
from dataset_loader import DatasetLoader
import time
from func_4 import distance_nodes

def duel_permutation(nodes) :
    duel_perm = list()
    for i in range(len(nodes)) :
        for j in range(i+1,len(nodes) ) :
            duel_perm.append([nodes[i],nodes[j]])
    return(duel_perm)



def find_best_initial(nodes, adj_list, coordinates_df):
    
    nodes_permutations = duel_permutation(nodes)
    
    edge_set = list()
    min_dist = float('inf')
    for perm in nodes_permutations:
        dist = distance_nodes(perm[0],perm[1], coordinates_df)

        if dist < min_dist :
            dist, seq = dijkstra_h(adj_list, perm[0], perm[1])
            min_dist = dist
            best_seq = seq
            
    for i in range(len(best_seq) - 1) :
         edge_set.append(tuple([best_seq[i],best_seq[i+1]]))
        
        
    return(min_dist,best_seq,edge_set)



def best_tree(nodes, adj_list) :
    
    coordinates_df = DatasetLoader('coordinates').dataset
    res = find_best_initial(nodes, adj_list, coordinates_df)
    visited_nodes = res[1]
    distance = res[0]
    edge_set = res[2]

    must_visited = [x for x in nodes if x not in visited_nodes ]
    #dijkstra_calls = 0
    
    while must_visited :
        min_dist = float('inf')
        for i in must_visited :
            for j in visited_nodes :
                dist = distance_nodes(i,j, coordinates_df)
                #dijkstra_calls += 1
                #dist, seq = dijkstra_h(adj_list, i , j)
                if dist < min_dist :
                    #dijkstra_calls += 1
                    dist, seq = dijkstra_h(adj_list, i , j)
                    min_dist = dist
                    best_seq = seq
                    
                    
        for i in range(len(best_seq) - 1) :
             edge_set.append(tuple([best_seq[i],best_seq[i+1]]))  
                
        distance += min_dist            
        must_visited = list(set(must_visited)- set(best_seq))
        visited_nodes = list(set(visited_nodes).union ( set(best_seq)))

    
    #print("Dijkstra calls: ", dijkstra_calls)

    return(edge_set,distance)   


''' Testing '''
adj_list = make_adj_list()

start_t = time.time()

places = [1, 1050021, 1803, 1050020, 2590, 1802]
res = best_tree(places,adj_list)
end_t = time.time() - start_t

print(res[0])
print(end_t, ' seconds')
