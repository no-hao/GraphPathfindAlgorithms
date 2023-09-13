from queue import PriorityQueue


def a_star_search(graph, heuristic_values, start_node_id, end_node_id):
    # Initializing the open set with a priority queue and adding the start node with a priority of 0
    open_set = PriorityQueue()
    open_set.put((0, graph.get_node(start_node_id)))
    
    # Initializing the dictionaries to keep track of the nodes visited and the costs
    came_from = {}
    g_score = {node_id: float('inf') for node_id in graph.nodes}
    f_score = {node_id: float('inf') for node_id in graph.nodes}
    
    # Setting the g_score and f_score of the start node
    g_score[start_node_id] = 0
    f_score[start_node_id] = heuristic_values.get((start_node_id, end_node_id), 0)
    
    # Main loop that runs until the open set is empty
    while not open_set.empty():
        # Getting the node with the minimum f_score from the open set
        _, current_node = open_set.get()
        
        # If the current node is the goal node, reconstruct the path and return it along with the total cost
        if current_node.id == end_node_id:
            return reconstruct_path(came_from, current_node), g_score[end_node_id]
        
        # Exploring the adjacent nodes of the current node
        for neighbor_node, weight in current_node.adjacent_nodes.items():
            # Calculating the tentative g_score for the neighbor node
            tentative_g_score = g_score[current_node.id] + weight
            
            # If the tentative g_score is less than the current g_score of the neighbor node,
            # update the g_score and f_score and add the neighbor node to the open set
            if tentative_g_score < g_score[neighbor_node.id]:
                came_from[neighbor_node.id] = current_node
                g_score[neighbor_node.id] = tentative_g_score
                f_score[neighbor_node.id] = g_score[neighbor_node.id] + heuristic_values.get((neighbor_node.id, end_node_id), 0)
                open_set.put((f_score[neighbor_node.id], neighbor_node))
    
    # If no path is found, return None and infinity
    return None, float('inf')


def reconstruct_path(came_from, current_node):
    # Initializing the path with the goal node
    path = [current_node.id]
    
    # Backtracking from the goal node to the start node to reconstruct the path
    while current_node.id in came_from:
        current_node = came_from[current_node.id]
        path.insert(0, current_node.id)
    
    # Returning the reconstructed path
    return path
# flake8: noqa
