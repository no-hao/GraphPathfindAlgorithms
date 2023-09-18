
from graph import Graph
from file_reader import read_edge_weights, read_heuristic
from a_star import a_star_search
from ida_star import ida_star_search
from user_input import get_user_inputs

def main():
    edge_weights_file, heuristic_file, start_node_id, end_node_id, algorithm = get_user_inputs()
    graph = Graph()
    if not read_edge_weights(edge_weights_file, graph):
        print("Error reading edge weights file")
        return

    heuristic_values = read_heuristic(heuristic_file)
    if not heuristic_values:
        print("Error reading heuristic file")
        return

    if algorithm == 'a*' or algorithm == 'both':
        path, cost = a_star_search(graph, heuristic_values, start_node_id, end_node_id)
        print(f"A* minimum cost path\n[{cost}] {' – '.join(map(str, path)) if path else 'No path found'}")
    
    if algorithm == 'ida*' or algorithm == 'both':
        path, cost = ida_star_search(graph, heuristic_values, start_node_id, end_node_id)
        print(f"IDA* minimum cost path\n[{cost}] {' – '.join(map(str, path)) if path else 'No path found'}")


if __name__ == "__main__":
    main()
# flake8: noqa
