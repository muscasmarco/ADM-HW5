''' The goal of this function is to find the neighbours via number of hops
    (network distance). To find the immediate neighbours, set n_steps to 1. '''
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

''' Here we have the Dijkstra algorithm that tries to find the closes immediate
    neighbours and moving towards the closest one. 
    It's a greedy algorithm, but visiting all the nodes proved to be really 
    ineffective '''
def dijkstra_h(adjacency, start, end):
    shortest_path = []
    pred = dict()
    not_visited = adjacency.copy()
   
    shortest_dist = dict.fromkeys(not_visited.keys(), float('inf'))
    shortest_dist[start] = 0
    
    node = start
    #print('\n Trying to find a path between ', start, ' and ', end)   
    
    # No need to visit all the other nodes if we arrived at our destination (end)
    while node != end and len(not_visited) > 0:
        
        #print('Steps: ',len(pred), ' | Not visited: ',len(not_visited),' Pred', pred.keys())
            
        node = min(not_visited.keys(), key=lambda x:shortest_dist[x]) # First, get the nodes we have not visited
        
        neighbours = get_n_steps_neighbours(not_visited, node, 1) # Get immediate neighbours 
        not_visited.pop(node) # We have visited the node we're in, we can remove it now.
        
        # Here we are trying to find the closest neighbour to move to. 
        for neighbour in neighbours:
            updated_distance = shortest_dist[node] + adjacency[node][neighbour]
            
            if updated_distance < shortest_dist[neighbour]:
                shortest_dist[neighbour] = updated_distance
                pred[neighbour] = node
        
    current = end
    
    # We have found our path, let's rebuild it backwards.
    while current != start :
        try :
            shortest_path.append(current)
            current = pred[current]
        
        except Exception as e:
            print(e)
            return None, None
            
    shortest_path.append(start)
    shortest_path.reverse() # Reverse it so it's like start-> ... -> end
    
    #print('shortest_dist: ', shortest_dist[end])
    #print('shortest path: ',shortest_path)
    
    return shortest_dist[end], shortest_path

