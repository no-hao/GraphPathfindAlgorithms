from queue import PriorityQueue


def a_star_search(graph, heuristic_values, start_node_id, end_node_id):
    """Performs the A* search algorithm to find the minimum cost path between start and end nodes.

    Args:
    graph (Graph): The graph on which to perform the search.
    heuristic_values (dict): A dictionary containing heuristic values.
    start_node_id (str): The ID of the start node.
    end_node_id (str): The ID of the end node.

    Returns:
    tuple: The reconstructed path and the total cost.
    """
    # Check if the start and end nodes are valid (present in the graph)
    if not graph.get_node(start_node_id) or not graph.get_node(end_node_id):
        raise ValueError("Start or end node ID not found in the graph.")

    # Priority queue to store nodes to be explored, prioritized by their f_score
    open_set = PriorityQueue()
    open_set.put((0, graph.get_node(start_node_id)))

    # A dictionary to store the parent node (value) of each visited node (key) during the search, 
    # used to reconstruct the optimal path once the goal node is reached.
    came_from = {}

    # Initialize g_score and f_score dictionaries with respective values for all nodes in the graph
    g_score, f_score = initialize_scores(graph, heuristic_values, start_node_id, end_node_id)

    while not open_set.empty():
        # Get the node from the open set with the minimum f_score
        current_node = get_node_with_min_f_score(open_set)
        
        # If the goal node is reached, reconstruct and return the optimal path and its total cost
        if current_node.id == end_node_id:
            return reconstruct_path(came_from, current_node), g_score[end_node_id]

        # Explore adjacent nodes and update scores and came_from dictionary as necessary
        explore_adjacent_nodes(current_node, open_set, came_from, g_score, f_score, heuristic_values, end_node_id)

    # Return None and infinity if no path is found
    return None, float('inf')


def initialize_scores(graph, heuristic_values, start_node_id, end_node_id):
    """Initializes the g_score and f_score dictionaries.

    Args:
    graph (Graph): The graph on which to perform the search.
    heuristic_values (dict): A dictionary containing heuristic values.
    start_node_id (str): The ID of the start node.
    end_node_id (str): The ID of the end node.

    Returns:
    tuple: The initialized g_score and f_score dictionaries.
    """
    # Initialize g_score and f_score dictionaries with respective values for all nodes
    g_score = {node_id: (0 if node_id == start_node_id else float('inf')) for node_id in graph.nodes}
    f_score = {node_id: (g_score[node_id] + heuristic_values.get((node_id, end_node_id), 0)) for node_id in graph.nodes}
    return g_score, f_score


def get_node_with_min_f_score(open_set):
    """Retrieves the node with the minimum f_score from the open set.

    Args:
    open_set (PriorityQueue): The open set containing nodes to be explored.

    Returns:
    Node: The node with the minimum f_score.
    """
    # Retrieve and return the node with the minimum f_score from the open set
    _, node = open_set.get()
    return node


def explore_adjacent_nodes(current_node, open_set, came_from, g_score, f_score, heuristic_values, end_node_id):
    """Explores the adjacent nodes of the current node and updates the scores and came_from dictionary.

    Args:
    current_node (Node): The current node being explored.
    open_set (PriorityQueue): The open set containing nodes to be explored.
    came_from (dict): A dictionary to keep track of the path.
    g_score (dict): A dictionary to keep track of the g_score of each node.
    f_score (dict): A dictionary to keep track of the f_score of each node.
    heuristic_values (dict): A dictionary containing heuristic values.
    end_node_id (str): The ID of the end node.

    Returns:
    None
    """
    # Loop through adjacent nodes and update g_score, f_score, and came_from dictionary based on the A* algorithm
    for neighbor_node, weight in current_node.adjacent_nodes.items():
        # Calculate the tentative g_score for the neighbor node
        tentative_g_score = g_score[current_node.id] + weight

        # If the tentative g_score is less than the current g_score of
        # the neighbor node, update the scores and came_from dictionary
        if tentative_g_score < g_score[neighbor_node.id]:
            came_from[neighbor_node.id] = current_node
            g_score[neighbor_node.id] = tentative_g_score
            current_heuristic_value = heuristic_values.get((neighbor_node.id, end_node_id), 0)
            f_score[neighbor_node.id] = g_score[neighbor_node.id] + current_heuristic_value
            open_set.put((f_score[neighbor_node.id], neighbor_node))


def reconstruct_path(came_from, current_node):
    """Reconstructs the path from the start node to the current node.

    Args:
    came_from (dict): A dictionary to keep track of the path.
    current_node (Node): The current node (goal node).

    Returns:
    list: The reconstructed path.
    """
    # Initialize the path with the goal node ID
    path = [current_node.id]
    
    # Trace back from the goal node to the start node
    # using the came_from dictionary and construct the path
    while current_node.id in came_from:
        current_node = came_from[current_node.id]
        path.insert(0, current_node.id)
    
    return path
# flake8: noqa
