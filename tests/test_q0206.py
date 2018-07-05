"""Unit tests for q0206.py."""

import unittest

from src.utils.linkedlist import LinkedList, Node
from src.q0206 import find_loop_slow_fast

class TestFindLoopSlowFast(unittest.TestCase):

    def test_find_loop_slow_fast(self):
        linked_list = LinkedList()
        linked_list.insert_at_head(3)
        linked_list.insert_at_head(2)
        linked_list.insert_at_head(1)
        n1 = linked_list.head
        n2 = n1.next_node
        n3 = n2.next_node
        n3.next_node = n1
        self.assertEqual(find_loop_slow_fast(linked_list), 1)
        n3.next_node = n2
        self.assertEqual(find_loop_slow_fast(linked_list), 2)
        n3.next_node = n3
        self.assertEqual(find_loop_slow_fast(linked_list), 3)


if __name__ == '__main__':
    unittest.main()
