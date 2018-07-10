"""Unit tests for q0401.py."""

import unittest

from src.utils.binary_tree import BinaryTree
from src.q0401 import check_tree_balance


class TestTreeBalance(unittest.TestCase):

    def setUp(self):
        self.bin_tree = BinaryTree()

    def test_empty_tree(self):
        self.assertTrue(check_tree_balance(self.bin_tree))

    def test_one_node_tree(self):
        adj_dict = {1: (None, None)}
        root_id = 1
        self.bin_tree.adjacency_to_tree(root_id, adj_dict)
        self.assertTrue(check_tree_balance(self.bin_tree))

    def test_three_node_balanced_tree(self):
        adj_dict = {1: (2, 3), 2: (None, None), 3: (None, None)}
        root_id = 1
        self.bin_tree.adjacency_to_tree(root_id, adj_dict)
        self.assertTrue(check_tree_balance(self.bin_tree))

    def test_three_node_imbalanced_tree(self):
        adj_dict = {1: (2, None), 2: (3, None), 3: (None, None)}
        root_id = 1
        self.bin_tree.adjacency_to_tree(root_id, adj_dict)
        self.assertFalse(check_tree_balance(self.bin_tree))

if __name__ == '__main__':
    unittest.main()
