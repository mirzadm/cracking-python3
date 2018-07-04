"""Unit tests for q0204.py."""

import unittest

from src.utils.linkedlist import LinkedList
from src.q0204 import partition_linkedlist_around_value as partition


class TestPartitionLinkedList(unittest.TestCase):
    """Tests for partition_linkedlist_around_value."""
    def test_partition_linkedlist(self):
        self.assertIsNone(partition(None, 1))

        linked_list = LinkedList()
        self.assertEqual(linked_list.convert_to_list(), [])
        p_linked_list = partition(linked_list, 1)
        self.assertIs(p_linked_list, linked_list)
        self.assertEqual(p_linked_list.convert_to_list(), [])

        linked_list = LinkedList()
        linked_list.insert_at_head(3)
        self.assertEqual(linked_list.convert_to_list(), [3])
        p_linked_list = partition(linked_list, 1)
        self.assertIs(p_linked_list, linked_list)
        self.assertEqual(p_linked_list.convert_to_list(), [3])

        linked_list = LinkedList()
        linked_list.insert_at_head(3)
        self.assertEqual(linked_list.convert_to_list(), [3])
        p_linked_list = partition(linked_list, 3)
        self.assertIs(p_linked_list, linked_list)
        self.assertEqual(p_linked_list.convert_to_list(), [3])

        linked_list = LinkedList()
        linked_list.insert_at_head(3)
        self.assertEqual(linked_list.convert_to_list(), [3])
        p_linked_list = partition(linked_list, 5)
        self.assertIs(p_linked_list, linked_list)
        self.assertEqual(p_linked_list.convert_to_list(), [3])

        linked_list = LinkedList()
        linked_list.insert_at_head(30)
        linked_list.insert_at_head(20)
        linked_list.insert_at_head(10)
        self.assertEqual(linked_list.convert_to_list(), [10, 20, 30])
        p_linked_list = partition(linked_list, 10)
        self.assertIs(p_linked_list, linked_list)
        self.assertEqual(p_linked_list.convert_to_list(), [30, 10, 20])

        linked_list = LinkedList()
        linked_list.insert_at_head(30)
        linked_list.insert_at_head(20)
        linked_list.insert_at_head(10)
        self.assertEqual(linked_list.convert_to_list(), [10, 20, 30])
        p_linked_list = partition(linked_list, 20)
        self.assertIs(p_linked_list, linked_list)
        self.assertEqual(p_linked_list.convert_to_list(), [10, 30, 20])

        linked_list = LinkedList()
        linked_list.insert_at_head(30)
        linked_list.insert_at_head(20)
        linked_list.insert_at_head(10)
        self.assertEqual(linked_list.convert_to_list(), [10, 20, 30])
        p_linked_list = partition(linked_list, 30)
        self.assertIs(p_linked_list, linked_list)
        self.assertEqual(p_linked_list.convert_to_list(), [10, 20, 30])

        linked_list = LinkedList()
        linked_list.insert_at_head(30)
        linked_list.insert_at_head(20)
        linked_list.insert_at_head(10)
        self.assertEqual(linked_list.convert_to_list(), [10, 20, 30])
        p_linked_list = partition(linked_list, 40)
        self.assertIs(p_linked_list, linked_list)
        self.assertEqual(p_linked_list.convert_to_list(), [10, 20, 30])


if __name__ == '__main__':
    unittest.main()
