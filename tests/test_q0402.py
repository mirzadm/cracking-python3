"""Unit tests for q0402.py."""

import unittest

from src.utils.directed_graph import DirectedGraph
from src.q0402 import find_path


class TestFindPath(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()

    def test_two_nodes(self):
        adj_map = {1: [2]}
        self.graph.adjacency_to_graph(adj_map)
        self.assertEqual(find_path(self.graph, 1, 1), [1])
        self.assertEqual(find_path(self.graph, 1, 2), [1, 2])
        self.assertEqual(find_path(self.graph, 2, 1), [])
        self.assertRaises(IndexError, find_path, self.graph, 1, 3)

    def test_four_nodes(self):
        adj_map = {1: [2, 3], 2: [3], 3: [1, 4]}
        self.graph.adjacency_to_graph(adj_map)
        self.assertEqual(find_path(self.graph, 1, 2), [1, 2])
        self.assertEqual(find_path(self.graph, 1, 3), [1, 3])
        self.assertEqual(find_path(self.graph, 1, 4), [1, 3, 4])
        self.assertEqual(find_path(self.graph, 2, 4), [2, 3, 4])


if __name__ == '__main__':
    unittest.main()
