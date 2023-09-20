from graph import Graph
from file_reader import read_edge_weights, read_heuristic
from a_star import a_star_search
from ida_star import ida_star_search
from user_input import get_user_inputs


def main():
    """
    The main function serves as the entry point for the program.
    
    Steps performed by this function:
    1. Collects user inputs using the get_user_inputs function.
    2. Initializes a graph object and reads edge weights into it.
       If there is an error reading the file, it prints an error message and returns.
    3. Reads heuristic values from the specified file.
       If there is an error reading the file, it prints an error message and returns.
    4. Depending on the algorithm chosen by the user (A* or IDA* or both),
       it calls the respective search function(s) and prints the result.
    """
    # Collecting user inputs
    edge_weights_file, heuristic_file, start_node_id, end_node_id, algorithm = get_user_inputs()
    
    # Initializing a graph object
    graph = Graph()
    
    # Reading edge weights into the graph
    if not read_edge_weights(edge_weights_file, graph):
        print(f"Error reading edge weights file: '{edge_weights_file}'. Please check the file path and format.")
        return

    # Reading heuristic values from the specified file
    heuristic_values = read_heuristic(heuristic_file)
    if not heuristic_values:
        print(f"Error reading heuristic file: '{heuristic_file}'. Please check the file path and format.")
        return

    # Executing the chosen algorithm(s) and printing the result
    if algorithm == 'a*' or algorithm == 'both':
        path, cost = a_star_search(graph, heuristic_values, start_node_id, end_node_id)
        print(f"A* minimum cost path\n[{cost:.2f}] {' –> '.join(map(str, path)) if path else 'No path found'}")
    
    if algorithm == 'ida*' or algorithm == 'both':
        path, cost = ida_star_search(graph, heuristic_values, start_node_id, end_node_id)
        print(f"IDA* minimum cost path\n[{cost:.2f}] {' –> '.join(map(str, path)) if path else 'No path found'}")


# If the script is run as the main module, call the main function to execute the program
if __name__ == "__main__":
    main()
# flake8: noqa
