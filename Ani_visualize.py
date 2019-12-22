#!/usr/bin/env python
# coding: utf-8

# In[4]:



import pandas as pd
import matplotlib.pyplot as plt
from geopandas import geopandas as gpd
from dataset_loader import DatasetLoader
from matplotlib.lines import Line2D
from matplotlib.animation import FuncAnimation


def get_coordinates(node_id, coordinates_df):
    row = coordinates_df[coordinates_df['node-id'] == node_id]
    lat, long = row.latitude.values[0], row.longitude.values[0]
    return lat, long

def print_itinerary(adj_list, itinerary, delta_zoom=0.1, render_roads=True):
    coordinates = DatasetLoader('coordinates').dataset
    
    coord_points = []

    for i in range(len(itinerary)):
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
    us_shp = "C:\\Users\\Nino\\tl_2019_us_state.shp"
    us_map_df = gpd.read_file(us_shp)
    
    fig, ax = plt.subplots(figsize=(10,10))
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
    
    if render_roads:
        plt.scatter([x/1000000 for x in coordinates['latitude'].values],
                    [y/1000000 for y in coordinates['longitude'].values],
                    color='black', alpha=1, s=0.2)
    
    plt.scatter([x for x in points_df['lat'].values],
                [y for y in points_df['long'].values],
                color='red',
                marker='o',
                alpha=0.6)
    x_vals = []
    y_vals = []
    def animate(i) :
        for i in range(0, len(itinerary)):
            p1 = itinerary[i][0]
            p2 = itinerary[i][1]
            c1_lat, c1_long = get_coordinates(p1, coordinates)
            c2_lat, c2_long = get_coordinates(p2, coordinates)

            c1_lat /= 1000000
            c1_long /= 1000000
            c2_lat /= 1000000
            c2_long /= 1000000
            x_vals.append(c1_lat)
            x_vals.append(c2_lat)
            y_vals.append(c1_long)
            y_vals.append(c2_long)

            plt.plot(x_vals, y_vals, '-', color='white')
        
    Ani = FuncAnimation(plt.gcf(), animate, interval = 2000)
    
    
    plt.show()
    
    


# In[5]:


'test'
from utils import make_adj_list
adj_list = make_adj_list()
itinerary =[(2,678), (678, 54), (54,98),(98,567)]


print_itinerary(adj_list, itinerary, delta_zoom=0.1, render_roads=True)


# In[ ]:




