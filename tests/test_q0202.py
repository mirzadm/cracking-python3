"""Unit tests for q0202.py."""

import unittest

from src.utils.linkedlist import LinkedList
from src.q0202 import kth_element_to_last


class TestKthElementToLast(unittest.TestCase):
    """Tests for kth element to last."""
    def test_kth_element_to_last(self):
        linked_list = LinkedList()
        self.assertEqual(kth_element_to_last(None, 1), None)
        self.assertEqual(kth_element_to_last(linked_list, 1), None)

        linked_list.insert_at_head(3)
        self.assertEqual(kth_element_to_last(linked_list, 0), None)
        self.assertEqual(kth_element_to_last(linked_list, 1), 3)
        self.assertEqual(kth_element_to_last(linked_list, 2), None)

        linked_list.insert_at_head(2)
        self.assertEqual(kth_element_to_last(linked_list, 0), None)
        self.assertEqual(kth_element_to_last(linked_list, 1), 3)
        self.assertEqual(kth_element_to_last(linked_list, 2), 2)
        self.assertEqual(kth_element_to_last(linked_list, 3), None)


if __name__ == '__main__':
    unittest.main()
