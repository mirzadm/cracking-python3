"""Unit tests for stack."""

import unittest

from src.utils.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_init(self):
        self.assertTrue(self.s.is_empty())

    def test_push_pop_peek_empty(self):
        self.assertRaises(IndexError, self.s.pop)

        self.assertTrue(self.s.is_empty())
        self.s.push(1)
        self.assertFalse(self.s.is_empty())
        self.assertEqual(self.s.peek(), 1)
        self.assertEqual(self.s.pop(), 1)
        self.assertTrue(self.s.is_empty())
        self.assertRaises(IndexError, self.s.peek)
        self.assertRaises(IndexError, self.s.pop)


        self.s.push(1)
        self.assertFalse(self.s.is_empty())
        self.s.push(2)
        self.assertFalse(self.s.is_empty())
        self.s.push(3)
        self.assertFalse(self.s.is_empty())
        self.assertEqual(self.s.peek(), 3)
        self.assertFalse(self.s.is_empty())
        self.assertEqual(self.s.pop(), 3)
        self.assertFalse(self.s.is_empty())
        self.assertEqual(self.s.peek(), 2)
        self.assertFalse(self.s.is_empty())
        self.assertEqual(self.s.pop(), 2)
        self.assertFalse(self.s.is_empty())
        self.assertEqual(self.s.peek(), 1)
        self.assertFalse(self.s.is_empty())
        self.assertEqual(self.s.pop(), 1)
        self.assertTrue(self.s.is_empty())
        self.assertRaises(IndexError, self.s.pop)


if __name__ == '__main__':
    unittest.main()
