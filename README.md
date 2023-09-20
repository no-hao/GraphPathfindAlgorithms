# AStar-PathFinding

## Project Description
This project implements two popular pathfinding algorithms: A* and IDA* (Iterative Deepening A*) in Python. These algorithms are used to find the minimum cost path between two nodes in a graph. The A* algorithm uses a best-first search strategy, considering both the cost to reach a node and an heuristic estimate of the cost to get from that node to the goal. The IDA* algorithm, on the other hand, is a depth-first search variant of the A* algorithm, using iterative deepening to find the optimal path.

## Files
- `main.py`: The main script to initiate and run the program, orchestrating the flow of inputs and algorithm execution.
- `graph.py`: Contains the `Graph`, `Node`, and `Edge` classes, which represent the structure of the graph and its components.
- `a_star.py`: Implements the A* algorithm, which finds the minimum cost path between two nodes using a heuristic-guided search strategy.
- `ida_star.py`: Implements the IDA* algorithm, an iterative deepening variant of the A* algorithm, suitable for finding optimal paths in large graphs.
- `file_reader.py`: Contains functions to read the edge weights and heuristic values from files, aiding in the initialization of the graph and heuristic values.
- `user_input.py`: Manages the user inputs, collecting necessary data such as file paths and node IDs to guide the search process.

## Installation and Setup
1. Ensure you have Python 3.6 or above installed on your system.
2. Clone the repository to your local machine.
3. Open a terminal and navigate to the repository folder.

## Usage
To run the program, follow these steps:

1. In the terminal, run the command `python main.py`.
2. Follow the prompts to enter the file paths for the edge weights and heuristic values, and the IDs of the start and end nodes.

**Input File Formats**:
- The edge weights file should be a CSV file with rows in the format: `<node1_id>,<node2_id>,<weight>`. For example:
  ```
  1,2,1.5
  2,3,2.0
  3,4,1.8
  ```
- The heuristic values file should also be a CSV file with rows in the format: `<node1_id>,<node2_id>,<heuristic_value>`. For example:
  ```
  1,4,3.5
  2,4,2.5
  3,4,1.0
  ```

## Output
The program will output the minimum cost path found by the chosen algorithm(s), along with the total cost. In the case of IDA*, the program will also output updates on the cost limit as the search progresses.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is distributed under the MIT License. See `LICENSE` file for more details.

## Contact
For any queries or suggestions, please open an issue on the repository.

