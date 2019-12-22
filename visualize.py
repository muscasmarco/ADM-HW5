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
from matplotlib.lines import Line2D

def get_coordinates(node_id, coordinates_df):
    row = coordinates_df[coordinates_df['node-id'] == node_id]
    lat, long = row.latitude.values[0], row.longitude.values[0]
    return lat, long

def print_itinerary(adj_list, itinerary, delta_zoom=0.1):
    coordinates = DatasetLoader('coordinates').dataset
    
    coord_points = []

    for i in range(len(itinerary)-1):
        p1 = itinerary[i][0]
        p2 = itinerary[i][1]
        c1_lat, c1_long = get_coordinates(p1, coordinates)
        c2_lat, c2_long = get_coordinates(p2, coordinates)
    
        c1_lat /= 1000000
        c1_long /= 1000000
        c2_lat /= 1000000
        c2_long /= 1000000
    
        coord_points.append((c1_lat, c1_long))
        coord_points.append((c2_lat, c2_long))

    cols = ['lat', 'long']
    points_df = pd.DataFrame(data=coord_points, columns=cols)
    #print(points_df)
    
    ''' Load shapefile for US '''
    us_shp = '/home/marco/workspace/git/ADM-HW5/shapefiles/us/tl_2019_us_state.shp'
    us_map_df = gpd.read_file(us_shp)
    
    fig, ax = plt.subplots(figsize=(10,10),    )
    ax.set_title(str('Zoom out factor at %.3f' % delta_zoom))
    
    #delta_zoom = 0.01 # Edit this to modify the zooming
    
    left_lim = min(points_df['lat'].values) - delta_zoom
    right_lim = max(points_df['lat'].values) + delta_zoom
    
    top_lim = max(points_df['long'].values) + delta_zoom
    bottom_lim = min(points_df['long'].values) - delta_zoom

    
    plt.xlim(left=left_lim)
    plt.xlim(right=right_lim)
    plt.ylim(top=top_lim)
    plt.ylim(bottom=bottom_lim)
    
    us_map_df.plot(ax=ax)
    
    plt.scatter([x for x in points_df['lat'].values],
                [y for y in points_df['long'].values],
                color='red',
                marker='o',
                alpha=0.6)
    
    for i in range(0, len(itinerary)-1):
        p1 = itinerary[i][0]
        p2 = itinerary[i][1]
        c1_lat, c1_long = get_coordinates(p1, coordinates)
        c2_lat, c2_long = get_coordinates(p2, coordinates)
    
        c1_lat /= 1000000
        c1_long /= 1000000
        c2_lat /= 1000000
        c2_long /= 1000000
        
        plt.plot([c1_lat, c2_lat], [c1_long, c2_long], 'ro-')

    
    plt.show()
    
    