"""Unit tests for q0201."""

import unittest

from q0201 import (Node as Node, remove_duplicates as remove_duplicates,
                   is_member as is_member)


class MyTests(unittest.TestCase):

    def test_is_member(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.next = node2
        node2.next = node3

        self.assertTrue(is_member(node1, 3))
        self.assertFalse(is_member(node1, 4))

    def test_remove_duplicates(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1dup = Node(1)
        node1.next = node2
        node2.next = node3
        node3.next = node1dup

        second_head = remove_duplicates(node1)
        self.assertEqual(second_head.data, 1)
        second_head = second_head.next
        self.assertEqual(second_head.data, 2)
        second_head = second_head.next
        self.assertEqual(second_head.data, 3)
        second_head = second_head.next
        self.assertEqual(second_head, None)

        second_head = remove_duplicates(node1)
        self.assertEqual(second_head.data, 1)
        second_head = second_head.next
        self.assertEqual(second_head.data, 2)
        second_head = second_head.next
        self.assertEqual(second_head.data, 3)
        second_head = second_head.next
        self.assertEqual(second_head, None)


if __name__ == '__main__':
    unittest.main()
