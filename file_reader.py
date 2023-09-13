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
            for _ in range(4):
                next(reader)
            
            node_ids = [int(float(value)) if is_float(value) else None for value in next(reader)[1:]]
            for row in reader:
                node1_id = int(float(row[0])) if is_float(row[0]) else None
                for node2_id, value in zip(node_ids, row[1:]):
                    if node1_id is not None and node2_id is not None and value and is_float(value):
                        heuristic_values[(node1_id, node2_id)] = float(value)
        return heuristic_values
    except Exception as e:
        print(f"Error reading heuristic file: {e}")
        return None


def is_float(value):
    try:
        float(value)
        return True
    except:
        return False
# flake8: noqa
