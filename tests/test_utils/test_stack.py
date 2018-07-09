"""Unit tests for stack."""

import unittest

from src.utils.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_init(self):
        self.assertEqual(self.s.stack_list, [])

    def test_is_empty(self):
        self.assertTrue(self.s.is_empty())

    def test_push_pop(self):
        self.assertRaises(IndexError, self.s.pop)

        self.s.push(1)
        self.assertEqual(self.s.pop(), 1)
        self.assertTrue(self.s.is_empty())

        self.s.push(1)
        self.s.push(2)
        self.s.push(3)
        self.assertEqual(self.s.pop(), 3)
        self.assertEqual(self.s.pop(), 2)
        self.assertEqual(self.s.pop(), 1)
        self.assertTrue(self.s.is_empty())

        self.assertRaises(IndexError, self.s.pop)


if __name__ == '__main__':
    unittest.main()
