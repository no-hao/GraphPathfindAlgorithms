class Node:
    """
    Represents a node in the graph.
    
    Attributes:
        id (str): The identifier for the node.
        heuristic (float): The heuristic value of the node (used in search algorithms).
        adjacent_nodes (dict): A dictionary mapping adjacent nodes to their respective edge weights.
    """
    
    def __init__(self, id, heuristic=0):
        """
        Initializes a new Node instance.
        
        Args:
            id (str): The identifier for the node.
            heuristic (float): The heuristic value of the node. Defaults to 0.
        """
        self.id = id
        self.heuristic = heuristic
        self.adjacent_nodes = {}

    def add_adjacent_node(self, node, weight):
        """
        Adds an adjacent node to the current node with a specified weight.
        
        Args:
            node (Node): The adjacent node to add.
            weight (float): The weight of the edge connecting the current node to the adjacent node.
        """
        self.adjacent_nodes[node] = weight

    def __lt__(self, other):
        """
        Defines the less than operator for Node instances, enabling comparisons based on node IDs.
        
        Args:
            other (Node): The other node to compare with.
            
        Returns:
            bool: True if the current node's ID is less than the other node's ID, False otherwise.
        """
        return self.id < other.id


class Graph:
    """
    Represents a graph, consisting of a collection of nodes connected by edges.
    
    Attributes:
        nodes (dict): A dictionary mapping node IDs to Node instances.
    """
    
    def __init__(self):
        """Initializes a new Graph instance with an empty dictionary to store nodes."""
        self.nodes = {}

    def add_node(self, id, heuristic=0):
        """
        Adds a node to the graph with a specified ID and heuristic value.
        
        Args:
            id (str): The identifier for the new node.
            heuristic (float): The heuristic value for the new node. Defaults to 0.
        """
        self.nodes[id] = Node(id, heuristic)

    def add_edge(self, node1_id, node2_id, weight):
        """
        Adds an edge between two nodes with a specified weight. If any of the nodes does not exist in the graph, it is created.
        
        Args:
            node1_id (str): The ID of the first node.
            node2_id (str): The ID of the second node.
            weight (float): The weight of the edge connecting the two nodes.
        """
        if node1_id not in self.nodes:
            self.add_node(node1_id)
        if node2_id not in self.nodes:
            self.add_node(node2_id)
        self.nodes[node1_id].add_adjacent_node(self.nodes[node2_id], weight)

    def get_node(self, id):
        """
        Retrieves a node with a specified ID from the graph.
        
        Args:
            id (str): The ID of the node to retrieve.
            
        Returns:
            Node: The node with the specified ID, or None if the node does not exist in the graph.
        """
        return self.nodes.get(id)
# flake8: noqa
