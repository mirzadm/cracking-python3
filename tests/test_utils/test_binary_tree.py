"""Unit tests for binary_tree.py."""

import unittest

from src.utils.binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.bin_tree = BinaryTree()

    def test_init(self):
        self.assertIsInstance(self.bin_tree, BinaryTree)
        self.assertIsNone(self.bin_tree.root_node)

    def test_adj_to_tree_with_missing_root_id(self):
        adj_list = {}
        root_id = 2
        self.assertRaises(KeyError, self.bin_tree.adjacency_to_tree,
                          root_id, adj_list)

    def test_adj_to_tree_to_adj_with_one_node(self):
        in_adj = {1: (None, None)}
        root_id = 1
        self.bin_tree.adjacency_to_tree(root_id, in_adj)
        out_adj = self.bin_tree.tree_to_adjacency()
        self.assertEqual(in_adj, out_adj)

    def test_adj_to_tree_to_adj__with_five_nodes(self):
        in_adj = {1: (2, 3), 2: (4, None), 3: (None, 5), 4: (None, None),
                  5: (None, None)}
        root_id = 1
        self.bin_tree.adjacency_to_tree(root_id, in_adj)
        out_adj = self.bin_tree.tree_to_adjacency()
        self.assertEqual(in_adj, out_adj)


if __name__ == '__main__':
    unittest.main()
