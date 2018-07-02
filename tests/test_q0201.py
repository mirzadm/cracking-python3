"""Unit tests for q0201."""

import unittest

from src.utils.linkedlist import LinkedList, Node
from src.q0201 import remove_duplicates


class TestRemoveDuplicates(unittest.TestCase):
    """Tests for remove_duplicates."""
    def test_remove_duplicates(self):
        linked_list = LinkedList()
        remove_duplicates(linked_list)
        self.assertEqual(linked_list.convert_to_list(), [])
        
        linked_list.insert_at_head(3)
        remove_duplicates(linked_list)
        self.assertEqual(linked_list.convert_to_list(), [3])
        
        linked_list.insert_at_head(3)
        remove_duplicates(linked_list)
        self.assertEqual(linked_list.convert_to_list(), [3])

        linked_list.insert_at_head(2)
        remove_duplicates(linked_list)
        self.assertEqual(linked_list.convert_to_list(), [2, 3])

        linked_list.insert_at_head(3)
        remove_duplicates(linked_list)
        self.assertEqual(linked_list.convert_to_list(), [3, 2])

        for i in [4, 3, 2, 1]:
            linked_list.insert_at_head(i)
        remove_duplicates(linked_list)
        self.assertEqual(linked_list.convert_to_list(), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
