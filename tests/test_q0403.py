"""Unit tests for q0402.py."""

import unittest

from src.q0403 import sorted_array_to_bin_search_tree, BinaryTree, TreeNode


class TestSortedArrayToBinSearch(unittest.TestCase):

    # def setUp(self):

    def test_empty_array(self):
        bin_tree = sorted_array_to_bin_search_tree([])
        self.assertIsNone(bin_tree.root_node)

    def test_one_element_array(self):
        bin_tree = sorted_array_to_bin_search_tree([1])
        root = bin_tree.root_node
        self.assertEqual(root.data, 1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_two_element_array(self):
        bin_tree = sorted_array_to_bin_search_tree([1, 2])
        root = bin_tree.root_node
        left = root.left
        right = root.right
        self.assertEqual(root.data, 1)
        self.assertIsNone(left)
        self.assertEqual(right.data, 2)
        self.assertIsNone(right.left)
        self.assertIsNone(right.right)

    def test_three_element_array(self):
        bin_tree = sorted_array_to_bin_search_tree([1, 2, 3])
        root = bin_tree.root_node
        left = root.left
        right = root.right
        self.assertEqual(root.data, 2)
        self.assertEqual(left.data, 1)
        self.assertEqual(right.data, 3)
        self.assertIsNone(right.left)
        self.assertIsNone(right.right)
        self.assertIsNone(left.left)
        self.assertIsNone(left.right)


if __name__ == '__main__':
    unittest.main()
