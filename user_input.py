def get_user_inputs():
    edge_weights_file = input("Please enter the edge weight file name and extension: ")
    heuristic_file = input("Please enter the heuristic file name and extension: ")
    
    while True:
        try:
            start_node_id = input("Start node (1 – 200): ")
            start_node_id_int = int(start_node_id)
            if start_node_id_int < 1 or start_node_id_int > 200:
                raise ValueError("Node ID out of range")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            end_node_id = input("End node (1 – 200): ")
            end_node_id_int = int(end_node_id)
            if end_node_id_int < 1 or end_node_id_int > 200:
                raise ValueError("Node ID out of range")
            break
        except ValueError as e:
            print(e)

    while True:
        algorithm = input("Please choose the algorithm (A* / IDA* / both): ").strip().lower()
        if algorithm in ('a*', 'ida*', 'both'):
            break
        else:
            print("Invalid choice. Please enter 'A*', 'IDA*', or 'both'.")

    return edge_weights_file, heuristic_file, start_node_id, end_node_id, algorithm
# flake8: noqa
