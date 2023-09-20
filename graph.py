
class Node:
    def __init__(self, id, heuristic=0):
        self.id = id
        self.heuristic = heuristic
        # Dictionary to store adjacent nodes along with edge weights
        self.adjacent_nodes = {}

    def add_adjacent_node(self, node, weight=0):
        self.adjacent_nodes[node] = weight

    # The __lt__ method facilitates comparison between nodes based on their IDs.
    # This might be used in priority queues or sorting operations where node comparisons are required.
    def __lt__(self, other):
        return self.id < other.id


class Graph:
    def __init__(self):
        self.nodes = {}  # Dictionary to store nodes with node IDs as keys

    def add_node(self, node_id, heuristic=0):
        self.nodes[node_id] = Node(node_id, heuristic)

    def add_edge(self, node1_id, node2_id, weight):
        node1 = self.nodes.get(node1_id)
        if node1 is None:
            self.add_node(node1_id)
            node1 = self.nodes[node1_id]

        node2 = self.nodes.get(node2_id)
        if node2 is None:
            self.add_node(node2_id)
            node2 = self.nodes[node2_id]

        node1.add_adjacent_node(node2, weight)
        node2.add_adjacent_node(node1, weight)

    def get_node(self, node_id):
        return self.nodes.get(node_id)
# flake8: noqa
