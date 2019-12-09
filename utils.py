#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:57:02 2019

@author: marco
"""
import networkx as nx
import time # When not testing, this 'import time' can be omitted.
from dataset_loader import DatasetLoader

def make_graph(vertices_dataset, edges_dataset): 
    graph = nx.Graph()    
    # Adding vertices
    graph.add_nodes_from(vertices_dataset['node-id'].values)
    # Adding edges (Side note, we are adding edges via tuples structured as (node1, node2, value))
    graph.add_edges_from([(x[0],x[1],{'distance':x[2]}) for x in edges_dataset[['node-id-1','node-id-2','distance']].values])
    
    return graph


if __name__ == '__main__':
    
    vertices_dataset_loader = DatasetLoader('coordinates', dataset_root_path='./dataset/')
    edges_dataset_loader = DatasetLoader('distance',dataset_root_path='./dataset/')
    
    vertices_dataset = vertices_dataset_loader.dataset
    edges_dataset = edges_dataset_loader.dataset
    
    ''' Test for making the dataset '''
    start_t = time.time()
    g = make_graph(vertices_dataset, edges_dataset)    
    end_t = time.time() - start_t
    
    print('%f seconds for building the whole graph. ' % end_t)
    ''' End test here '''