import csv


def read_edge_weights(file_name, graph):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                node1_id, node2_id, weight = int(row[0]), int(row[1]), float(row[2])
                graph.add_edge(node1_id, node2_id, weight)
        return True
    except Exception as e:
        print(f"Error reading edge weights file: {e}")
        return False


def read_heuristic(file_name):
    heuristic_values = {}
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            # Skip the initial rows containing headers or empty cells
            for _ in range(6):
                next(reader)

            # Read the 'TO' node IDs from row 7 (indexing starts from 0)
            to_node_ids = [int(value) for value in next(reader)[1:] if value and value.strip()]

            # Read the 'FROM' node IDs and the heuristic values from row 8 onwards
            for row in reader:
                if row and row[0].strip():
                    from_node_id = int(row[0])
                    for to_node_id, value in zip(to_node_ids, row[1:]):
                        if value and value.strip():
                            value_float = float(value)
                            heuristic_values[(from_node_id, to_node_id)] = value_float
                            # Adding the symmetric value to the dictionary if it is not already present
                            if from_node_id != to_node_id and (to_node_id, from_node_id) not in heuristic_values:
                                heuristic_values[(to_node_id, from_node_id)] = value_float
        return heuristic_values
    except Exception as e:
        print(f"Error reading heuristic file: {e}")
        return None
# flake8: noqa
