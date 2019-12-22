#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 01:39:45 2019

@author: marco
"""

import pandas as pd
import matplotlib.pyplot as plt
from geopandas import geopandas as gpd
from dataset_loader import DatasetLoader
from path_finder import get_n_steps_neighbours

''' This function is here simply to provide the coordinates for a point
    (given its node id) in the TIGER/Line format. '''
def get_coordinates(node_id, coordinates_df):
    row = coordinates_df[coordinates_df['node-id'] == node_id]
    lat, long = row.latitude.values[0], row.longitude.values[0]
    return lat, long

def get_additional_roads(adj_list, connected_nodes, target_nodes, limit_counter=5):
    additional_roads = []
    
    if limit_counter > 0 and target_nodes != []:
        for node in connected_nodes:
            neighbours = get_n_steps_neighbours(adj_list, node, 1)
            
            additional_roads.extend([(node, n) for n in neighbours])
            
            #print(additional_roads)
            '''    
            check if list1 contains all elements in list2
            '''
            
            new_targets = target_nodes + [] # Avoid removing by reference
            
            for t in target_nodes:
                if t in neighbours:
                    new_targets.remove(t)
                
            if target_nodes == [] or neighbours == []:
                return additional_roads
            else:
                additional_roads.extend(get_additional_roads(adj_list, neighbours, new_targets, limit_counter-1))
                
    return list(dict.fromkeys(additional_roads))
        
 



''' This function will render the US map, then will plot the itinerary 
    (which is a list of edges). Additionally, via the render_roads parameter,
    you can plot the various roads of the US!
    It's more convenient to set it to false when you have time constraints, 
    since printing the road checkpoints is time consuming. 
    The edges connecting the road checkpoints were not rendered for the same
    reason. ''' 
def print_itinerary(adj_list, itinerary, delta_zoom=0.1, render_roads=True, render_additional_roads=False, us_shp_root='./shapefiles/us/'):
    us_shp = us_shp_root + 'tl_2019_us_state.shp'
    us_map_df = gpd.read_file(us_shp)
    
    coordinates = DatasetLoader('coordinates').dataset
    
    coord_points = []


    # Let's first print the itinerary (which is a list of edges)
    for i in range(len(itinerary)):
        p1 = itinerary[i][0] # Get node id 1
        p2 = itinerary[i][1] # Get node id 2
        c1_lat, c1_long = get_coordinates(p1, coordinates)
        c2_lat, c2_long = get_coordinates(p2, coordinates)
    
        # Covert them so we can plot them in the map we have
        c1_lat /= 1000000
        c1_long /= 1000000
        c2_lat /= 1000000
        c2_long /= 1000000
    
        # Prepare for making the dataframe
        coord_points.append((c1_lat, c1_long))
        coord_points.append((c2_lat, c2_long))

    cols = ['lat', 'long']
    points_df = pd.DataFrame(data=coord_points, columns=cols)# Convert the list of coordinates into a dataframe

    #print(points_df)
    
    ''' Printing '''    
    
    fig, ax = plt.subplots(figsize=(10,10))
    ax.set_title(str('Zoom out factor at %.3f' % delta_zoom))
    
    #delta_zoom = 0.01 # Edit this to modify the zooming
    
    # The following operations set the zoom by cropping the plot
    left_lim = min(points_df['lat'].values) - delta_zoom
    right_lim = max(points_df['lat'].values) + delta_zoom 
    top_lim = max(points_df['long'].values) + delta_zoom
    bottom_lim = min(points_df['long'].values) - delta_zoom
  
    plt.xlim(left=left_lim)
    plt.xlim(right=right_lim)
    plt.ylim(top=top_lim)
    plt.ylim(bottom=bottom_lim)
    
    
    # Plot the US map
    us_map_df.plot(ax=ax)
    
    
    if render_additional_roads:
        nodes = []
        for edge in itinerary:
            p1 = edge[0]
            p2 = edge[1]
            
            if p1 not in nodes:
                nodes.append(p1)
            if p2 not in nodes:
                nodes.append(p2)
                
        additional_roads = get_additional_roads(adj_list, nodes, nodes, 10)
        
        for i in range(0, len(additional_roads)):
            p1 = additional_roads[i][0]
            p2 = additional_roads[i][1]
            c1_lat, c1_long = get_coordinates(p1, coordinates)
            c2_lat, c2_long = get_coordinates(p2, coordinates)
        
            c1_lat /= 1000000
            c1_long /= 1000000
            c2_lat /= 1000000
            c2_long /= 1000000
            
            # The coordinates are like (x_start, x_end), (y_start, y_end)
            plt.plot([c1_lat, c2_lat], [c1_long, c2_long], '-', color='white', linewidth=0.5)
    
    if render_roads:
       # Render the checkpoints of the roads that are defined in the coordinates dataframe
       plt.scatter([x/1000000 for x in coordinates['latitude'].values],
                   [y/1000000 for y in coordinates['longitude'].values],
                   color='black', alpha=1, s=0.5)
      
    # Render the nodes in the itinerary
    plt.scatter([x for x in points_df['lat'].values],
                [y for y in points_df['long'].values],
                color='red',
                marker='o',
                alpha=0.6)
    
    # Print the itinerary edges
    for i in range(0, len(itinerary)):
        p1 = itinerary[i][0]
        p2 = itinerary[i][1]
        c1_lat, c1_long = get_coordinates(p1, coordinates)
        c2_lat, c2_long = get_coordinates(p2, coordinates)
    
        c1_lat /= 1000000
        c1_long /= 1000000
        c2_lat /= 1000000
        c2_long /= 1000000
        
        # The coordinates are like (x_start, x_end), (y_start, y_end)
        plt.plot([c1_lat, c2_lat], [c1_long, c2_long], '-', color='red')
    

    plt.show()
    
    