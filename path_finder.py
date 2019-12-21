def get_n_steps_neighbours(adj_list, goal, n_steps):
    if goal == None or n_steps == 0:
        return [goal]
    else:
        neighbours = adj_list[goal].keys()
        res = []
        
        for n in neighbours:
            res.extend(get_n_steps_neighbours(adj_list, n, n_steps-1))
        
    neighbours = list(dict.fromkeys(res))
    if goal in neighbours:
        neighbours.remove(goal)
    
    return neighbours
    
    
def dijkstra_h(adjacency, start, end):
    shortest_path = []
    pred = dict()
    not_visited = adjacency.copy()
   
    shortest_dist = dict.fromkeys(not_visited.keys(), float('inf'))
    shortest_dist[start] = 0
    
    node = start
    print('\n\n Trying to find a path between ', start, ' and ', end)    
    while node != end and len(not_visited) > 0:
        
        
        print('Steps: ',len(pred)/2, ' | Not visited: ',len(not_visited),' Pred', pred.keys())
            
        node = min(not_visited.keys(), key=lambda x:shortest_dist[x])
        
        neighbours = get_n_steps_neighbours(not_visited, node, 1)        
        not_visited.pop(node)
        
        for neighbour in neighbours:
            updated_distance = shortest_dist[node] + adjacency[node][neighbour]
            
            if updated_distance < shortest_dist[neighbour]:
                shortest_dist[neighbour] = updated_distance
                pred[neighbour] = node
        
    current = end
    while current != start :
        try :
            shortest_path.append(current)
            current = pred[current]
        
        except Exception as e:
            return None, None
            
    shortest_path.append(start)
    shortest_path.reverse()
        
    return shortest_dist[end], shortest_path

