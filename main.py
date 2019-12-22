#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import make_adj_list
from dataset_loader import DatasetLoader
from func_1 import get_neighbourhood, vis_1
from func_2 import  best_tree
from func_3 import shortest_ordered_path
from func_4 import find_shortest_visiting_path
from visualize import print_itinerary



# getting query from user for function and distance type
func = int(input("chose your func: (Enter an integer between 1 to 4) ")) 
metric = input("Choose a distance function : (distance/time-distance/network-distance) " )


adj_list = make_adj_list(distance_metric = metric) # Let's load the data with the chosen metric
coordinates = DatasetLoader('coordinates').dataset # This doesn't vary, regardless of the metric


if func == 1 :

    ''' Showing FUNCTIONALITY 1 '''
    ''' 
        Some additional notes: 

            - When using the network distance, pay attention to the maximum distance
            for neighbours to be considered. An high number will result in a recursion
            with too many levels. 

            - When using time-distance, if the results seem wrong (no neighbours for example)
            try with a higher number (2000 and up)
    '''
    
    

    node_1  = int(input("choose a node: ")) # The chose node
    thresh = int(input("choose a threshold distance: "))

    neighbourhood = get_neighbourhood(adj_list, node_1, 0, thresh) # Get the neighbours
    vis_1(adj_list, node_1, neighbourhood, metric) # Visualization.





''' Showing FUNCTIONALITY 2'''

if func == 2 :
    
    target_nodes = list(map(int, input("please enter target nodes with a distance: ").split(" ")))
    itinerary = best_tree(nodes, adj_list)[0] #call the function to get the minimum tree
    
    print("set of edges to visit all target nodes: " , itinerary)
    
    print('Printing map. Please wait to see all the plots.')
    for zoom in [0.001, 0.1, 2, 14]:  #plot for different zooms
        print_itinerary(adj_list, itinerary, zoom, render_roads = True, render_additional_roads=True)
    print('Done.')
    











''' Showing FUNCTIONALITY 3'''
if func == 3 :
    
    initial = int(input("insert the start point : "))
    node_set = list(map(int,input("insert the sequence of nodes with a distance: ")))
    itinerary = shortest_ordered_path(initial, node_set, adj_list)
    
    print("shortest walk: " , itinerary)
    
    print('Printing map. Please wait to see all the plots.')
    for zoom in [0.001, 0.1, 2, 14]:
        print_itinerary(adj_list, itinerary, zoom, render_roads = True, render_additional_roads=False)
    print('Done.')
    






''' Showing FUNCTIONALITY 4 '''
'''
    Some additional notes:
        
        - Try not to choose nodes that are clearly too far from each other
            if you want the computation to end in reasonable time.
'''
if func == 4 :
    initial = int(input("insert the start point : "))
    nodes = list(map(int,input("insert the sequence of nodes with a distance: ")))
    path = nodes.insert(0,initial) #get the list of all nodes
    
    travel_distance, itinerary = find_shortest_visiting_path(adj_list, path)

    print('Distance travelled: ', travel_distance)
    print('Itinerary: ', itinerary)

    print('Printing map. Please wait to see all the plots.')
    for zoom in [0.001, 0.1, 2, 14]:
        print_itinerary(adj_list, itinerary, zoom, render_roads = True, render_additional_roads=True)
    print('Done.')
    
    

