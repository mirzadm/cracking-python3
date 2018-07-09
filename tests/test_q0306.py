"""Unit tests for q0306.py."""

import unittest

from src.utils.stack import Stack
from src.q0306 import sort_stack_iterative, sort_stack_recursive


class TestSortStack(unittest.TestCase):

    def setUp(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def test_iterative_sort_one(self):
        self.s1.push(5)
        sort_stack_iterative(self.s1)
        self.assertEqual(self.s1.size(), 1)
        self.assertEqual(self.s1.pop(), 5)

    def test_iterative_sort_three_descending(self):
        self.s1.push(3)
        self.s1.push(2)
        self.s1.push(1)
        sort_stack_iterative(self.s1)
        self.assertEqual(self.s1.size(), 3)
        self.assertEqual(self.s1.pop(), 3)
        self.assertEqual(self.s1.pop(), 2)
        self.assertEqual(self.s1.pop(), 1)

    def test_iterative_sort_three_mixed(self):
        self.s1.push(3)
        self.s1.push(1)
        self.s1.push(2)
        sort_stack_iterative(self.s1)
        self.assertEqual(self.s1.size(), 3)
        self.assertEqual(self.s1.pop(), 3)
        self.assertEqual(self.s1.pop(), 2)
        self.assertEqual(self.s1.pop(), 1)

    def test_recursive_sort_one(self):
        self.s1.push(5)
        sort_stack_recursive(1, self.s1, self.s2)
        self.assertEqual(self.s1.size(), 1)
        self.assertEqual(self.s1.pop(), 5)
        self.assertEqual(self.s2.size(), 0)

    def test_recursive_sort_three_descending(self):
        self.s1.push(3)
        self.s1.push(2)
        self.s1.push(1)
        sort_stack_recursive(3, self.s1, self.s2)
        self.assertEqual(self.s1.size(), 3)
        self.assertEqual(self.s1.pop(), 3)
        self.assertEqual(self.s1.pop(), 2)
        self.assertEqual(self.s1.pop(), 1)
        self.assertEqual(self.s2.size(), 0)

    def test_recursive_sort_three_mixed(self):
        self.s1.push(3)
        self.s1.push(1)
        self.s1.push(2)
        sort_stack_recursive(3, self.s1, self.s2)
        self.assertEqual(self.s1.size(), 3)
        self.assertEqual(self.s1.pop(), 3)
        self.assertEqual(self.s1.pop(), 2)
        self.assertEqual(self.s1.pop(), 1)
        self.assertEqual(self.s2.size(), 0)


if __name__ == '__main__':
    unittest.main()
