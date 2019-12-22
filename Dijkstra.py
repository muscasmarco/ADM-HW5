#!/usr/bin/env python
# coding: utf-8


def Dijkstra(adjacency,start,end):
    shortest_path = []
    shortest_dist = dict()
    pred = dict()  # a dictionary to save predecessors
    not_visited = adjacency
   
    
    
    for node in not_visited :
        shortest_dist[node] = 500000  # A number greater than the max distance in edge_dataset
    
    shortest_dist[start] = 0
    
    
    
    
    while not_visited :
        Next_node = "NA"
        for node in not_visited : # find the next node we want to do the procedure on 
                                  #next_node is the node with lowest shortest_dist
            if Next_node == "NA" :
                Next_node = node
            elif shortest_dist[node] < shortest_dist[Next_node] :
                Next_node = node
        
        #updating shortest distance for neighbour nodes
        for neighbour , distance in adjacency[Next_node].items() :
            if distance + shortest_dist[Next_node] < shortest_dist[neighbour] :
                shortest_dist[neighbour] = distance + shortest_dist[Next_node]
                pred[neighbour] = Next_node  #saving the predecessor node to be able to get the path afterward
        
        not_visited.pop(Next_node)
        
        
    #creating the shortest path, satrting from the end node and moving through predecessor nodes to reach the start node
    current = end
    while current != start :
        try :
            shortest_path.append(current)
            current = pred[current]
        
        except :
            return("Not possible")  #if the gragh is not connected 
    shortest_path.append(start)
    shortest_path.reverse()
        
    return(shortest_dist[end], shortest_path)
            
    
  






