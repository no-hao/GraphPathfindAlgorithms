def get_user_inputs():
    while True:
        try:
            edge_weights_file = input("Please enter the edge weight file name and extension: ")
            print("Loading file...")
            with open(edge_weights_file, 'r') as file:
                pass

            heuristic_file = input("Please enter the heuristic file name and extension: ")
            with open(heuristic_file, 'r') as file:
                pass

            start_node_id = int(input("Start node (1 – 200): "))
            if start_node_id < 1 or start_node_id > 200:
                raise ValueError("Node ID out of range")

            end_node_id = int(input("End Node (1 – 200): "))
            if end_node_id < 1 or end_node_id > 200:
                raise ValueError("Node ID out of range")

            return edge_weights_file, heuristic_file, start_node_id, end_node_id

        except Exception as e:
            print(f"Invalid input: {e}")
            try_again = input("Would you like to try again? (yes/no): ").strip().lower()
            if try_again != 'yes':
                break
