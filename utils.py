#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:57:02 2019

@author: marco
"""
import time # When not testing, this 'import time' can be omitted.
from dataset_loader import DatasetLoader
import pickle
import os 


''' This function return the adjacency list (actually a dict) for a given metric.
    Since making it is time consuming, it will first try to look for the file containing it.
    if it doesn't find it, then it generates a new one. '''
def make_adj_list(distance_metric='distance'):
    
    if distance_metric not in ['distance','time-distance', 'network-distance']:
        
        print("Distance metric not valid, please choose 'distance','time-distance' or 'network-distance'. ")
        return None
    
    vertices_dataset_loader = DatasetLoader('coordinates')
    
    if distance_metric in ['distance', 'time-distance']:
        edges_dataset_loader = DatasetLoader(distance_metric)
    else:
        edges_dataset_loader = DatasetLoader('distance')# The actual distance will be ignored in this case

    vertices_df = vertices_dataset_loader.dataset #Load the vertices dataset
    edges_df = edges_dataset_loader.dataset # Then the vertices dataset.
    
    
    file_path = str('./adj_list_%s.pkl' % distance_metric)
    adj_list = None
    
    if os.path.isfile(file_path):
        adj_list = pickle.load(open(file_path,'rb')) # The file exists, no need to build it from scratch.
        
    else:
        # Important! 
        # Since there might be some disconnected vertices, we need the vertices dataset 
        adj_list = {i:{} for i in vertices_df.index}
        
        print_progress = True # Set this flag to True to print progress percentage
        
        dataset_size = len(edges_df)
        for index, edge in edges_df.iterrows():
            
            if index % 10000 == 0 and print_progress:
                print('%4f' % (index/dataset_size * 100))
                
            if distance_metric == 'network-distance':
                node1, node2, dist = edge['node-id-1'],edge['node-id-2'], 1 # Where 1 represent 1 hop from point to point
            else:
                node1, node2, dist = edge['node-id-1'],edge['node-id-2'], edge['distance'] 
            
            if node1 in adj_list.keys():
                adj_list[node1][node2] = dist
            
        ''' Write to file '''
        f = open(file_path, 'wb')
        pickle.dump(adj_list, f)
        f.close()

    return adj_list
    
   
if __name__ == '__main__':
    
    ''' Test for making the dataset '''
    print('Starting test...')
    start_t = time.time()
    #g = make_graph(vertices_dataset, edges_dataset)    
    adj_list = make_adj_list('network-distance')
    end_t = time.time() - start_t
    
    print('%f seconds for building the adj list. ' % end_t)
    ''' End test here '''
