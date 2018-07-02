"""Unit tests."""

import unittest

from src.utils.linkedlist import LinkedList, Node


class TestLinkedList(unittest.TestCase):
    """Tests for LinkedList class."""
    def test_insert_convert(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.convert_to_list(), [])
        linked_list.insert_at_head(3)
        self.assertEqual(linked_list.convert_to_list(), [3])
        linked_list.insert_at_head(2)
        self.assertEqual(linked_list.convert_to_list(), [2, 3])
        linked_list.insert_at_head(1)
        self.assertEqual(linked_list.convert_to_list(), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
