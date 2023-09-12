
# AStar-PathFinding

This repository contains a Python implementation of the A* pathfinding algorithm. The program reads graph data and heuristic values from files, and finds the minimum cost path between two nodes using the A* algorithm.

## Files
- `main.py`: The main script to run the program.
- `graph.py`: Contains the Graph, Node, and Edge classes.
- `a_star.py`: Contains the A* algorithm implementation.
- `file_reader.py`: Contains functions to read the edge weights and heuristic values from files.
- `user_input.py`: Contains a function to get necessary inputs from the user.

## How to Run
1. Ensure you have Python 3.6 or above installed.
2. Clone the repository.
3. Open a terminal and navigate to the repository folder.
4. Run the command `python main.py`.
5. Follow the prompts to enter the file names and node IDs.

## Note
- The edge weights file should be a CSV file with rows containing the format: `<node1_id>,<node2_id>,<weight>`.
- The heuristic values file should be a CSV file with rows containing the format: `<node1_id>,<node2_id>,<heuristic_value>`.
- The node IDs for the start and end nodes should be between 1 and 200.
