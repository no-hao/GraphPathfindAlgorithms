def get_user_inputs():
    """
    This function handles the collection of inputs from the user.
    
    The function performs the following tasks:
    1. Collects the names of the edge weights file and heuristic file from the user.
    2. Collects the start node ID and end node ID from the user, ensuring that they are within the valid range (1 to 200).
    3. Asks the user to choose an algorithm (A* or IDA* or both) and validates the input.
    
    Returns:
        edge_weights_file (str): The name of the edge weights file provided by the user.
        heuristic_file (str): The name of the heuristic file provided by the user.
        start_node_id (str): The start node ID provided by the user.
        end_node_id (str): The end node ID provided by the user.
        algorithm (str): The algorithm choice provided by the user ('a*', 'ida*', or 'both').
    """
    # Collecting file names from the user
    edge_weights_file = input("Please enter the edge weight file name and extension: ")
    heuristic_file = input("Please enter the heuristic file name and extension: ")
    
    # Validating and collecting start node ID from the user
    while True:
        try:
            start_node_id = input("Start node (1 – 200): ")
            start_node_id_int = int(start_node_id)
            if start_node_id_int < 1 or start_node_id_int > 200:
                raise ValueError("Node ID out of range")
            break
        except ValueError as e:
            print(e)

    # Validating and collecting end node ID from the user
    while True:
        try:
            end_node_id = input("End node (1 – 200): ")
            end_node_id_int = int(end_node_id)
            if end_node_id_int < 1 or end_node_id_int > 200:
                raise ValueError("Node ID out of range")
            break
        except ValueError as e:
            print(e)

    # Validating and collecting algorithm choice from the user
    while True:
        algorithm = input("Please choose the algorithm (A* / IDA* / both): ").strip().lower()
        if algorithm in ('a*', 'ida*', 'both'):
            break
        else:
            print("Invalid choice. Please enter 'A*', 'IDA*', or 'both'.")

    return edge_weights_file, heuristic_file, start_node_id, end_node_id, algorithm
# flake8: noqa
