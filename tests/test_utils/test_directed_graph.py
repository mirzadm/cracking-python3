""""Unit tests for directed_graph.py."""

import unittest

from src.utils.directed_graph import DirectedGraph


class TestDirectedGraph(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()

    def test_init(self):
        self.assertEqual(self.graph.get_node_ids(), [])

    def test_add_node_id(self):
        node_id = 5
        self.graph.add_node_id(node_id)
        self.assertEqual(self.graph.get_node_ids(), [node_id])
        self.assertTrue(self.graph.has_node(node_id))

    def test_add_edge(self):
        from_id = 5
        to_id = 10
        self.graph.add_node_id(from_id)
        self.graph.add_node_id(to_id)
        self.graph.add_edge(from_id, to_id)
        self.assertEqual(self.graph.get_adj_node_ids(from_id), [to_id])
        self.assertEqual(self.graph.get_adj_node_ids(to_id), [])

    def test_adj_to_graph_to_adj(self):
        adj_map = {1: [2, 3], 2: [1, 3]}
        self.graph.adjacency_to_graph(adj_map)
        output_adj_map = self.graph.graph_to_adjacency()
        expected_adj_map = {1: [2, 3], 2: [1, 3], 3: []}
        self.assertEqual(output_adj_map, expected_adj_map)


if __name__ == '__main__':
    unittest.main()
