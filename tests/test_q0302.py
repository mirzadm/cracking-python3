"""Unit tests for q0302.py."""

import unittest

from src.utils.stack import Stack
from src.q0302 import StackWithMin


class TestStackWithMin(unittest.TestCase):
    def setUp(self):
        self.s = StackWithMin()

    def test_init(self):
        self.assertTrue(self.s.is_empty())
        self.assertEqual(self.s.size(), 0)

    def test_push_then_min(self):
        self.s.push(3)
        self.assertEqual(self.s.min(), 3)
        self.s.push(4)
        self.assertEqual(self.s.min(), 3)
        self.s.push(2)
        self.assertEqual(self.s.min(), 2)

    def test_push_then_pop(self):
        no_of_pushes = 10
        for i in range(no_of_pushes):
            self.s.push(i)
        for i in range(no_of_pushes):
            self.assertEqual(self.s.pop(), no_of_pushes - i - 1)        
        self.assertTrue(self.s.is_empty())
        self.assertEqual(self.s.size(), 0)

    def test_push_then_pop_and_min(self):
        items = [3, 4, 2]
        for item in items:
            self.s.push(item)
        self.assertEqual(self.s.min(), 2)
        self.assertEqual(self.s.pop(), 2)
        self.assertEqual(self.s.min(), 3)
        self.assertEqual(self.s.pop(), 4)
        self.assertEqual(self.s.min(), 3)
        self.assertEqual(self.s.pop(), 3)

    def test_min_in_empty_stack(self):
        self.assertRaises(IndexError, self.s.min)


if __name__ == '__main__':
    unittest.main()
