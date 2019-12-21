#!/usr/bin/env python3

from path_finder import get_n_steps_neighbours

def get_neighbourhood(adj_list, start, curr_d, d):
    
    res = []
    
    if curr_d > d:
        return []
    else:
        
        neighbours = get_n_steps_neighbours(adj_list, start, 1)
        
        for neighbour in neighbours:
            distance = adj_list[start][neighbour]
            
            if curr_d + distance <= d:
                res.append(neighbour)
            
            res.extend(get_neighbourhood(adj_list, neighbour, curr_d+distance, d))
        
    return list(dict.fromkeys(res))
        
    