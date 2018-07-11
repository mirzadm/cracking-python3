"""Implementation for directed graph."""


class GraphNode:

    def __init__(self, node_id):
        self.id = node_id
        self.data = None
        self.adj = set()


class DirectedGraph:
    """Implements a directed graph.
    
    Nodes have unique ids.

    Attributes:
        nodes: A map of id to node object.    
    """

    def __init__(self):
        self.nodes = {}

    def has_node(self, node_id):
        return node_id in self.nodes

    def get_node_ids(self):
        node_ids = []
        for node_id in self.nodes:
            node_ids.append(node_id)
        return node_ids

    def get_adj_node_ids(self, node_id):
        if node_id not in self.nodes:
            raise IndexError('Node id does not exist.')
        return list(self.nodes[node_id].adj)

    def add_node_id(self, node_id):
        """Adds a new node id if it does not aleardy exist."""
        if node_id not in self.nodes:
            node = GraphNode(node_id)
            self.nodes.update({node_id: node})

    def add_edge(self, from_id, to_id):
        """Adds an edge: from_id --> to_id"""
        if from_id == to_id:
            raise ValueError('A node may not have a self edge.')
        if (from_id not in self.nodes) or (to_id not in self.nodes):
            raise IndexError('Node with given id does not exist.')

        self.nodes[from_id].adj.add(to_id)

    def adjacency_to_graph(self, adj_map):
        """Creates a graph from an adjacency map of node ids.
        
        Overwrites any existing node id.
        
        Args:
            adj_map: A dictionary map from nodes to their adjacenet nodes.
            Example: {1: [2, 3], 2: [3, 4]}
        """
        for node_id, adj_list in adj_map.items():
            self.add_node_id(node_id)
            for adj_id in adj_list:
                self.add_node_id(adj_id)
                self.add_edge(node_id, adj_id)

    def graph_to_adjacency(self):
        """Returns an adjacency map representation of the graph.

        Example: The following graph
        1 --> 2, 3
        2 --> 3
        will be shown as the following adjacency map:
        {1: {2, 3}, 2: {3}, 3: {}}
        """
        adj_map = {}
        for node_id, node in self.nodes.items():
            adj_map.update({node_id: list(node.adj)})
        return adj_map
