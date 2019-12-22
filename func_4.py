#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:57:49 2019

@author: marco
"""
from utils import make_adj_list
from path_finder import dijkstra_h
from scipy.spatial import distance
from dataset_loader import DatasetLoader
from visualize import print_itinerary

''' This function is used to get an approximate distance between two nodes given their ids. 
    It will act as an alternative metric to the distances defined in
    the datasets (distance, time distance and network distance) '''
    
def distance_nodes(p1, p2, coordinates_df):
            
    p1_row = coordinates_df[coordinates_df['node-id'] == p1]
    p1_x, p1_y = p1_row.latitude.values[0], p1_row.longitude.values[0]
    
    p2_row = coordinates_df[coordinates_df['node-id'] == p2]
    p2_x, p2_y = p2_row.latitude.values[0], p2_row.longitude.values[0]
    
    p1_p = (p1_x, p1_y)
    p2_p = (p2_x, p2_y)
    
    return distance.euclidean(p1_p, p2_p)

 
''' The goal of this function is to determine an approximation of the 
    ordering of the nodes which allows us to visit them all.
    We'll need to define a starting point (start) and a destination (end).
    
    In the list (between) will end up all the other nodes we want to visit
    before arriving at the destination.
''' 
def get_short_between_path(between, start, end, coordinates_df):
    
    if len(between) == 0: # Base case #1.
        return []
    
    if len(between) == 1: # Base case #2. Odd number of places to visit? Here's the solution.
        return between
    
    if len(between) > 1: # Inductive step
        
        # Find the closest node to the actual starting point
        first_destination_distances = [(n, distance_nodes(start, n, coordinates_df)) for n in between]
        first_destination_distances.sort(key=lambda x:x[1])
        first_destination = first_destination_distances[0][0]
            
        # Find the closes node to the actual ending point
        last_destination_distances = [(n, distance_nodes(end, n, coordinates_df)) for n in between if n != first_destination]
        last_destination_distances.sort(key=lambda x:x[1])
        last_destination= last_destination_distances[0][0]
        
        # They have been visited, remove from between
        between.remove(first_destination)
        between.remove(last_destination)
        #print(start, between, end)
        
        # Proceed with the next step now that you found the consecutive nodes from start and end (first_destination, last_destination)
        return [first_destination] + get_short_between_path(between, first_destination, last_destination, coordinates_df)+ [last_destination]
    
    
''' This is the function that does what functionality #4 asks.
    - It assumes that the first element in path is the starting point.
    - It assumes that the last element in path is the destination. 
'''
def find_shortest_visiting_path(adj_list, path):
    
    coordinates_df = DatasetLoader('coordinates').dataset
    
    # Get Start, end, between
    start = path[0]
    end = path[-1]
    between = path[1:len(path)-1]
    
    total_distance = 0
    total_path = []
    
    if len(between) == 0: # No destinations in between, just get distance from starting point to end (A -> B)
        total_distance, total_path = dijkstra_h(adj_list, start, end)
    else:
        between = path # Because the recursive functions need all nodes. The assumptions in the explanation hold true.
        shortest_estimated_path = get_short_between_path(between, start, end, coordinates_df)
        
        # Now that you have an ideal path, find the actual path using dijkstra (with heuristics)
        for i in range(0, len(shortest_estimated_path)-1):
            tmp_dist, tmp_path = dijkstra_h(adj_list, shortest_estimated_path[i], shortest_estimated_path[i+1])
            total_distance += tmp_dist
            total_path.extend(tmp_path)
    
    # Avoiding linked duplicates like going from n1 to n1
    total_path_no_linked_dup = []
    for i in range(len(total_path)-1):
        node_1 = total_path[i]
        node_2 = total_path[i+1]
        
        if node_1 != node_2:
            total_path_no_linked_dup.append((node_1, node_2))
    
    return total_distance, total_path_no_linked_dup
    
if __name__ == '__main__':
    
    ''' Setup '''
    print('Loading dataset...')
    adj_list = make_adj_list('distance')
    print('Done.')
    print('Trying to find a path...')
    
    '''Tests'''
    #path = [1,1803, 1802, 1050020, 1050021, 2590, 1805]
    path = [1, 1803]#, 1050020, 2590, 1802, 1805, 1050021]
    #path = [1,1803, 1050021, 1805]
    
    travel_distance, itinerary = find_shortest_visiting_path(adj_list, path)
       
    #print('Distance: ', travel_distance)
    #print('Itinerary: ', itinerary)
    
    print('Printing map...')
    
    for zoom in [0.001, 0.01, 0.1, 2, 4, 10, 14]:
            c = print_itinerary(adj_list, itinerary, zoom)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    