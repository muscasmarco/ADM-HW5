#!/usr/bin/env python
# coding: utf-8
'''
The algorithm we used for this part is to first find the mininmum distance between dual combinations of the must_visited nodes using djikstra algorithm, then in each step that we improve, we add the visited nodes(both the nodes that were previously in must_visited and also the ones that we visited between those nodes in the shortest path) to visited_nodes list and remove that nodes from must_visited. This algorithm should iterate until there isn't any nodes in must_visited set
'''

from path_finder import dijkstra_h
from utils import make_adj_list
from dataset_loader import DatasetLoader
import time
from func_4 import distance_nodes

def duel_permutation(nodes) : #find unique dual permutations between nodes
    duel_perm = list()
    for i in range(len(nodes)) :
        for j in range(i+1,len(nodes) ) :
            duel_perm.append([nodes[i],nodes[j]])
    return(duel_perm)



def find_best_initial(nodes, adj_list, coordinates_df): #finding the best dual permutation to initial algorithm with
    
    nodes_permutations = duel_permutation(nodes)
    
    edge_set = list()
    min_dist = float('inf')
    for perm in nodes_permutations:
        #for time efficiency we first check euclidean distance between nodes, if euclidean distance is more than min distance
        #we don't calculate dijkstra distance for that permutation and move forward to another one 
        dist = distance_nodes(perm[0],perm[1], coordinates_df)

        if dist < min_dist :
            dist, seq = dijkstra_h(adj_list, perm[0], perm[1])
            min_dist = dist
            best_seq = seq
            
    for i in range(len(best_seq) - 1) :   #creating edge set from the nodes we visited in dijkstra algo
         edge_set.append(tuple([best_seq[i],best_seq[i+1]]))
        
        
    return(min_dist,best_seq,edge_set)



def best_tree(nodes, adj_list) :
    
    coordinates_df = DatasetLoader('coordinates').dataset
    res = find_best_initial(nodes, adj_list, coordinates_df)
    visited_nodes = res[1]
    distance = res[0]
    edge_set = res[2]

    must_visited = [x for x in nodes if x not in visited_nodes ] # create must_visited nodes from the ones we didn't visit in initial phase
    #dijkstra_calls = 0
    
    while must_visited :
        min_dist = float('inf')
        for i in must_visited :
            for j in visited_nodes :
                dist = distance_nodes(i,j, coordinates_df)
                #dijkstra_calls += 1
                #dist, seq = dijkstra_h(adj_list, i , j)
                if dist < min_dist : # we only calcullate dijkstra if euclidean distance is less than min distance
                    #dijkstra_calls += 1
                    dist, seq = dijkstra_h(adj_list, i , j)
                    min_dist = dist
                    best_seq = seq
                    
                    
        for i in range(len(best_seq) - 1) :
             edge_set.append(tuple([best_seq[i],best_seq[i+1]]))  
                
        distance += min_dist            
        must_visited = list(set(must_visited)- set(best_seq)) #we remove the nodes algo visited during dijkstra from must_visited
        visited_nodes = list(set(visited_nodes).union ( set(best_seq))) # and add those nodes to viste_nodes set

    
    #print("Dijkstra calls: ", dijkstra_calls)

    return(edge_set,distance)   

if __name__ == '__main__':
    ''' Testing '''
    adj_list = make_adj_list()
    
    start_t = time.time()
    
    places = [1, 1050021, 1803, 1050020, 2590, 1802]
    res = best_tree(places,adj_list)
    end_t = time.time() - start_t
    
    print(res[0])
    print(end_t, ' seconds')
