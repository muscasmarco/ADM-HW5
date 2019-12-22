#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 14:29:55 2019

@author: marco
"""
from utils import make_adj_list
from dataset_loader import DatasetLoader
from func_1 import get_neighbourhood, vis_1
from func_4 import find_shortest_visiting_path
from visualize import print_itinerary

''' Showing FUNCTIONALITY 1 '''
metric = 'time-distance'
adj_list = make_adj_list(distance_metric = metric)
coordinates = DatasetLoader('coordinates').dataset

node_1  = 349356

neighbourhood = get_neighbourhood(adj_list, node_1, 0, 10000)
vis_1(adj_list, node_1, neighbourhood, metric)


''' Showing FUNCTIONALITY 4 '''
path = [1,1803, 1802]#, 1050020, 1050021, 2590, 1805]
#path = [349356] + neighbourhood
travel_distance, itinerary = find_shortest_visiting_path(adj_list, path)
   
#print('Distance: ', travel_distance)
#print('Itinerary: ', itinerary)

print('Printing map...')

for zoom in [0.001, 0.1, 2, 14]:
    print_itinerary(adj_list, itinerary, zoom, render_roads = True)

    
    
    