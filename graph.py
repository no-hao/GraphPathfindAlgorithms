class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.edges = []  # List to store edges connected to this node

    def add_edge(self, edge):
        """Method to add an edge to the node's edges list."""
        self.edges.append(edge)

    def __repr__(self):
        return f"Node({self.id})"


class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __repr__(self):
        return f"Edge({self.node1.id}, {self.node2.id}, {self.weight})"


class Graph:
    def __init__(self):
        # Dictionary to store nodes with node_id as key and Node object as val.
        self.nodes = {}

    def add_node(self, node_id):
        """Method to add a node to the graph."""
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id)

    def add_edge(self, node1_id, node2_id, weight):
        """Method to add an edge to the graph."""
        # Ensure both nodes are added to the graph
        self.add_node(node1_id)
        self.add_node(node2_id)
        
        # Create a new Edge object and add it to both nodes' edges list
        edge = Edge(self.nodes[node1_id], self.nodes[node2_id], weight)
        self.nodes[node1_id].add_edge(edge)
        self.nodes[node2_id].add_edge(edge)

    def get_node(self, node_id):
        """Method to get a node by its ID."""
        return self.nodes.get(node_id)

    def get_edge(self, node1_id, node2_id):
        """Method to get an edge by the IDs of the nodes it connects."""
        node1 = self.get_node(node1_id)
        if node1:
            for edge in node1.edges:
                if edge.node2.id == node2_id:
                    return edge
        return None
