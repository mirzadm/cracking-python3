"""Unit tests for q0203.py."""

import unittest

from src.utils.linkedlist import LinkedList
from src.q0203 import del_intermediate_node

class TestDelIntermediateNode(unittest.TestCase):
    """Tests for del_intermediate_node."""
    def test_del_intermediate_node(self):
        self.assertEqual(del_intermediate_node(None), None)

        linked_list = LinkedList()
        n = linked_list.head
        self.assertEqual(del_intermediate_node(n), None)

        linked_list = LinkedList()
        linked_list.insert_at_head(3)
        self.assertEqual(linked_list.convert_to_list(), [3])
        n = linked_list.head
        self.assertEqual(del_intermediate_node(n), None)
        self.assertEqual(linked_list.convert_to_list(), [3])

        linked_list = LinkedList()
        linked_list.insert_at_head(3)
        linked_list.insert_at_head(2)
        self.assertEqual(linked_list.convert_to_list(), [2, 3])
        n = linked_list.head
        self.assertEqual(del_intermediate_node(n), 2)
        self.assertEqual(linked_list.convert_to_list(), [3])

        linked_list = LinkedList()
        linked_list.insert_at_head(3)
        linked_list.insert_at_head(2)
        linked_list.insert_at_head(1)
        self.assertEqual(linked_list.convert_to_list(), [1, 2, 3])
        n = linked_list.head.next_node.next_node
        self.assertEqual(del_intermediate_node(n), None)
        self.assertEqual(linked_list.convert_to_list(), [1, 2, 3])

        linked_list = LinkedList()
        linked_list.insert_at_head(3)
        linked_list.insert_at_head(2)
        linked_list.insert_at_head(1)
        self.assertEqual(linked_list.convert_to_list(), [1, 2, 3])
        n = linked_list.head.next_node
        self.assertEqual(del_intermediate_node(n), 2)
        self.assertEqual(linked_list.convert_to_list(), [1, 3])

        linked_list = LinkedList()
        linked_list.insert_at_head(3)
        linked_list.insert_at_head(2)
        linked_list.insert_at_head(1)
        self.assertEqual(linked_list.convert_to_list(), [1, 2, 3])
        n = linked_list.head
        self.assertEqual(del_intermediate_node(n), 1)
        self.assertEqual(linked_list.convert_to_list(), [2, 3])


if __name__ == '__main__':
    unittest.main()
