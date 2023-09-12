
class Node:
    def __init__(self, id, heuristic=0):
        self.id = id
        self.heuristic = heuristic
        self.adjacent_nodes = {}

    def add_adjacent_node(self, node, weight):
        self.adjacent_nodes[node] = weight

    def __lt__(self, other):
        return self.id < other.id

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, id, heuristic=0):
        self.nodes[id] = Node(id, heuristic)

    def add_edge(self, node1_id, node2_id, weight):
        if node1_id not in self.nodes:
            self.add_node(node1_id)
        if node2_id not in self.nodes:
            self.add_node(node2_id)
        self.nodes[node1_id].add_adjacent_node(self.nodes[node2_id], weight)

    def get_node(self, id):
        return self.nodes.get(id)
