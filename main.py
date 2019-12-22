#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import make_adj_list
from dataset_loader import DatasetLoader
from func_1 import get_neighbourhood, vis_1
from func_4 import find_shortest_visiting_path
from visualize import print_itinerary

''' Showing FUNCTIONALITY 1 '''
''' 
    Some additional notes: 
        
        - When using the network distance, pay attention to the maximum distance
        for neighbours to be considered. An high number will result in a recursion
        with too many levels. 
        
        - When using time-distance, if the results seem wrong (no neighbours for example)
        try with a higher number (2000 and up)
'''

metric = 'network-distance'
adj_list = make_adj_list(distance_metric = metric) # Let's load the data with the chosen metric
coordinates = DatasetLoader('coordinates').dataset # This doesn't vary, regardless of the metric

node_1  = 349356 # The chose node

neighbourhood = get_neighbourhood(adj_list, node_1, 0, 10) # Get the neighbours
vis_1(adj_list, node_1, neighbourhood, metric) # Visualization.





''' Showing FUNCTIONALITY 2'''











''' Showing FUNCTIONALITY 3'''







''' Showing FUNCTIONALITY 4 '''
'''
    Some additional notes:
        
        - Try not to choose nodes that are clearly too far from each other
            if you want the computation to end in reasonable time.
'''

path = [1,1803, 1802, 1050020, 1050021, 2590, 1805]

travel_distance, itinerary = find_shortest_visiting_path(adj_list, path)
   
print('Distance travelled: ', travel_distance)
print('Itinerary: ', itinerary)

print('Printing map. Please wait to see all the plots.')
for zoom in [0.001, 0.1, 2, 14]:
    print_itinerary(adj_list, itinerary, zoom, render_roads = True)
print('Done.')
    
    

