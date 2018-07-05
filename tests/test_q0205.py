"""Unit tests for q0205.py."""

import unittest

from src.utils.linkedlist import LinkedList, Node
from src.q0205 import add_linkedlist_nums

class TestAddLinkedListNums(unittest.TestCase):

    def test_add_linkedlist_nums(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l3 = add_linkedlist_nums(l1, l2)
        self.assertEqual(l3.convert_to_list(), [])

        l1 = LinkedList()
        l2 = LinkedList()
        l1.insert_at_head(1)
        l3 = add_linkedlist_nums(l1, l2)
        self.assertEqual(l3.convert_to_list(), [1])

        l1 = LinkedList()
        l2 = LinkedList()
        l2.insert_at_head(1)
        l3 = add_linkedlist_nums(l1, l2)
        self.assertEqual(l3.convert_to_list(), [1])

        l1 = LinkedList()
        l2 = LinkedList()
        l1.insert_at_head(9)
        l2.insert_at_head(9)
        l3 = add_linkedlist_nums(l1, l2)
        self.assertEqual(l3.convert_to_list(), [8, 1])

        l1 = LinkedList()
        l2 = LinkedList()
        l1.insert_at_head(9)
        l1.insert_at_head(9)
        l2.insert_at_head(1)
        l3 = add_linkedlist_nums(l1, l2)
        self.assertEqual(l3.convert_to_list(), [0, 0, 1])


if __name__ == '__main__':
    unittest.main()
