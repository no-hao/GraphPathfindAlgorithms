import csv


def read_edge_weights(file_name, graph):
    """Reads the edge weights from the given file and adds the edges to the graph.

    Args:
    file_name (str): The name of the file containing the edge weights.
    graph (Graph): The graph to which the edges should be added.

    Returns:
    bool: True if the file is read successfully, False otherwise.
    """
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                # Extract node IDs and edge weight from the current row
                node1_id, node2_id, weight = row[0], row[1], float(row[2])
                # Add the edge to the graph
                graph.add_edge(node1_id, node2_id, weight)
        return True
    except Exception as e:
        print(f"Error reading edge weights file: {e}")
        return False


def read_heuristic(file_name):
    """Reads the heuristic values from the given file and returns a
    dictionary with node pairs as keys and heuristic values as values.

    Args:
    file_name (str): The name of the file containing the heuristic values.

    Returns:
    dict: A dictionary with node pairs as keys and heuristic values
    as values, or None if an error occurs during file reading.
    """
    heuristic_values = {}
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            # Skip the initial rows containing headers or empty cells
            for _ in range(6):
                next(reader)

            # Read the 'TO' node IDs from row 7 (indexing starts from 0)
            # Stripping the strings to remove any leading/trailing whitespaces
            to_node_ids = [value.strip() for value in next(reader)[1:] if value and value.strip()]

            # Read the 'FROM' node IDs and the heuristic values from row 8 onwards
            for row_index, row in enumerate(reader):
                if row and row[0].strip():
                    from_node_id = row[0].strip()
                    for to_node_index, value in enumerate(row[1:]):
                        if value and value.strip():
                            # Converting the value to float after stripping whitespaces
                            value_float = float(value.strip())
                            # Considering only the upper triangular part of the matrix to avoid duplicate entries
                            if to_node_index >= row_index:
                                heuristic_values[(from_node_id, to_node_ids[to_node_index])] = value_float
                                # Adding the symmetric value to the dictionary since it is an upper triangular matrix
                                if from_node_id != to_node_ids[to_node_index]:
                                    heuristic_values[(to_node_ids[to_node_index], from_node_id)] = value_float
        return heuristic_values
    except Exception as e:
        print(f"Error reading heuristic file: {e}")
        return None
# flake8: noqa
