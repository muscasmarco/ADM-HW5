#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:57:02 2019

@author: marco
"""
import networkx as nx
import time # When not testing, this 'import time' can be omitted.
from dataset_loader import DatasetLoader
import pickle
import os 

def make_graph(vertices_dataset, edges_dataset): 
    graph = nx.Graph()    
    # Adding vertices
    graph.add_nodes_from(vertices_dataset['node-id'].values)
    # Adding edges (Side note, we are adding edges via tuples structured as (node1, node2, value))
    graph.add_edges_from([(x[0],x[1],{'distance':x[2]}) for x in edges_dataset[['node-id-1','node-id-2','distance']].values])
    
    return graph

def make_adj_list(distance_metric='distance'): # Can also be 'time-distance'
    
    if distance_metric not in ['distance','time-distance']:
        print("Distance metric not valid, please choose 'distance' or 'time-distance'. ")
        return -1
    
    vertices_dataset_loader = DatasetLoader('coordinates')
    edges_dataset_loader = DatasetLoader('distance')
    
    vertices_df = vertices_dataset_loader.dataset
    edges_df = edges_dataset_loader.dataset
    
    
    file_path = str('./adj_list_%s.pkl' % distance_metric)
    adj_list = None
    
    if os.path.isfile(file_path):
        adj_list = pickle.load(open(file_path,'rb')) # The file exists, no need to build it from scratch.
        
    else:
    
        adj_list = {i:{} for i in vertices_df.index}
        
        print_progress = True # Set this flag to True to print progress percentage
        
        dataset_size = len(edges_df)
        for index, edge in edges_df.iterrows():
            
            if index % 10000 == 0 and print_progress:
                print('%4f' % (index/dataset_size * 100))
                
                
            node1, node2, dist = edge['node-id-1'],edge['node-id-2'],edge['distance']
            
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
    adj_list = make_adj_list()
    end_t = time.time() - start_t
    
    print('%f seconds for building the adj list. ' % end_t)
    ''' End test here '''
