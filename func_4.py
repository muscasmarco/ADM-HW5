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
from itertools import permutations

def distance_nodes(p1, p2):
        
    coordinates_list = DatasetLoader('coordinates').dataset
    
    p1_row = coordinates_list[coordinates_list['node-id'] == p1]
    p1_x, p1_y = p1_row.latitude.values[0], p1_row.longitude.values[0]
    
    p2_row = coordinates_list[coordinates_list['node-id'] == p2]
    p2_x, p2_y = p2_row.latitude.values[0], p2_row.longitude.values[0]
    
    p1_p = (p1_x, p1_y)
    p2_p = (p2_x, p2_y)
    
    return distance.euclidean(p1_p, p2_p)
    
    
def get_shortest_approximate_route(points, coordinates_list):
    points_permutations = list(permutations(points))
    
    performance = []
    
    for perm in points_permutations:
        total_dist = 0
        n1 = perm[0]
        for n2 in perm[2:]:
            total_dist += distance_nodes(n1, n2, coordinates_list)
            performance
            n1 = n2
            
        performance.append([perm, total_dist])
        
    performance.sort(key=lambda x : x[1])
    return performance[0][1], performance[0][0]
    
    
                        
def shortest_route(adj_list, start, checkpoints, end):
    coord = DatasetLoader('coordinates').dataset
      
    most_promising_sequence = get_shortest_approximate_route([start]+checkpoints+[end], coord)
    
    print(most_promising_sequence[0])
    most_promising_sequence = most_promising_sequence[1]    

    total_dist = 0
    total_seq = []
    ''' For each couple compute dijkstra'''
    for n1,n2 in zip(most_promising_sequence[:len(most_promising_sequence)-1], most_promising_sequence[1:]):
        dist, seq = dijkstra_h(adj_list, n1, n2)
        
        print(seq)
        
        if dist == None or seq == None: # No path available
            return None, None
        
        total_dist += dist
        total_seq += seq
        
    return total_seq, total_dist

def path_len_n(adj_list,start, n):
    
    
    if n == 0:
        return start
    else:
        res = []
        k = list(adj_list[start].keys())[0]    
        print(k)
        if k != None:
            res.append(k)
            path_len_n(adj_list, k, n-1)    
            
    return res
    
def find_shortest_visiting_path(adj_list, path):
    
    start = path[0]
    end = path[-1]
    between = path[1:(len(path)-1)]
    
    
    
    print(start, between, end)

def get_short_between_path(between, start, end):
    
    if len(between) == 0:
        return []
    
    if len(between) == 1:
        return between
    
    if len(between) > 1:
        first_destination_distances = [(n, distance_nodes(start, n)) for n in between]
        first_destination_distances.sort(key=lambda x:x[1])
        first_destination = first_destination_distances[0][0]
            
        last_destination_distances = [(n, distance_nodes(end, n)) for n in between if n != first_destination]
        last_destination_distances.sort(key=lambda x:x[1])
        last_destination= last_destination_distances[0][0]
            
        between.remove(first_destination)
        between.remove(last_destination)
        #print(start, between, end)
        
        return [first_destination] + get_short_between_path(between, first_destination, last_destination)+ [last_destination]
    
if __name__ == '__main__':
    
    ''' Setup '''
    print('Loading dataset...')
    adj_list = make_adj_list('distance')
    print('Done.')
    print('Trying to find a path...')
    
    '''Tests'''
    #path = [1,1803, 1802, 1050020, 1050021, 2590, 1805]
    #path = [1, 4146, 1803, 1802, 1050020, 4142, 4518]
    path = [1,1803, 1805]
    
    ''' Pre sort using estimated distance '''
    # Get Start, end, between
    start = path[0]
    end = path[-1]
    between = path[1:len(path)-1]
    
    if len(between) == 0: # No destinations in between, just get distance from starting point to end
        res = dijkstra_h(adj_list, start, end)
    elif len(between) == 1:
        res = dijkstra_h(adj_list, start, between[0]) + dijkstra_h(adj_list, between[0], end)[1:]
    else:
        
        between = path
        shortest_estimated_path = get_short_between_path(between, start, end)
        res = [0, []]
        for i in range(0, len(shortest_estimated_path)-1):
            tmp_res = dijkstra_h(adj_list, shortest_estimated_path[i], shortest_estimated_path[i+1])
            res[0] += tmp_res[0]
            res[1].append((tmp_res[1][0], tmp_res[1][1]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    