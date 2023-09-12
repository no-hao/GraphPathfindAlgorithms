import csv


def read_edge_weights(file_path, graph):
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                node1_id = int(row[0])
                node2_id = int(row[1])
                weight = float(row[2])
                graph.add_edge(node1_id, node2_id, weight)
        return True
    except Exception as e:
        print(f"Error reading edge weights file: {e}")  # Debug print
        return False


def read_heuristic(file_path):
    heuristic_values = {}
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            # Skip the initial rows that do not contain heuristic values
            for _ in range(4):
                next(csv_reader)
            
            # Read the first row that contains heuristic values to get
            # the list of node IDs (excluding the first cell)
            node_ids = [int(value) for value in next(csv_reader)[1:] if value.isdigit()]
            
            # Read each subsequent row
            for row in csv_reader:
                if row[0].isdigit():  # Skip rows with non-numeric first cells
                    node1_id = int(row[0])
                    for i, heuristic_value in enumerate(row[1:]):
                        # Skip non-numeric cells and avoid index out of range
                        if i < len(node_ids) and heuristic_value.replace('.', '', 1).isdigit():
                            node2_id = node_ids[i]
                            heuristic_value = float(heuristic_value)
                            heuristic_values[(node1_id, node2_id)] = heuristic_value
        return heuristic_values
    except Exception as e:
        print(f"Error reading heuristic file: {e}")  # Debug print
        return None
