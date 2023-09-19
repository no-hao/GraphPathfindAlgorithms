from graph import Graph
from file_reader import read_heuristic


# Define the recursive depth-first search function for IDA*
def ida_star_dfs(graph, heuristic_values, current_node, goal_node_id, current_cost, cost_limit, path):
    # Calculate the estimated total cost from the start node to the goal node through the current node
    estimated_total_cost = current_cost + heuristic_values.get((current_node.id, goal_node_id), 0)
    
    # If the estimated total cost exceeds the cost limit, return None and the estimated total cost
    if estimated_total_cost > cost_limit:
        return None, estimated_total_cost
    
    # If the goal node is reached, return the path and the total cost
    if current_node.id == goal_node_id:
        return path, current_cost
    
    # Initialize the minimum cost that exceeds the cost limit to infinity
    min_exceeding_cost = float('inf')
    
    # Explore the adjacent nodes of the current node
    for neighbor_node, weight in current_node.adjacent_nodes.items():
        # If the neighbor node has not been visited yet (not in the current path), visit it
        if neighbor_node.id not in path:
            path.append(neighbor_node.id)
            # Recur with the neighbor node as the new current node and the updated current cost
            _, exceeding_cost = ida_star_dfs(graph, heuristic_values, neighbor_node, goal_node_id, current_cost + weight, cost_limit, path)
            # If a solution is found, return it
            if _:
                return _, exceeding_cost
            # Update the minimum cost that exceeds the cost limit if necessary
            if exceeding_cost < min_exceeding_cost:
                min_exceeding_cost = exceeding_cost
            # Backtrack by removing the neighbor node from the path
            path.pop()
    
    # If no solution is found, return None and the minimum cost that exceeds the cost limit
    return None, min_exceeding_cost


# Define the main IDA* function
def ida_star_search(graph, heuristic_values, start_node_id, goal_node_id):
    # Initialize the cost limit to the heuristic cost from the start node to the goal node
    cost_limit = heuristic_values.get((start_node_id, goal_node_id), 0)
    
    while True:
        print(f"Current cost limit: {cost_limit:.2f}")  # Print the current cost limit with two decimal places to show the deepening process
        path, new_cost_limit = ida_star_dfs(graph, heuristic_values, graph.get_node(start_node_id), goal_node_id, 0, cost_limit, [start_node_id])

        # If a solution is found, return the path and the cost
        if path:
            return path, new_cost_limit

        # If no solution is found and the new cost limit is infinity, return "No path found"
        if new_cost_limit == float('inf'):
            return None, new_cost_limit

        # Update the cost limit to the new cost limit for the next iteration
        cost_limit = new_cost_limit
