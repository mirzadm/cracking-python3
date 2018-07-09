"""Unit tests for stack."""

import unittest

from src.utils.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_init(self):
        self.assertTrue(self.s.is_empty())
        self.assertEqual(self.s.size(), 0)

    def test_push_and_size(self):
        no_of_pushes = 10
        for i in range(no_of_pushes):
            self.s.push(i)
        self.assertFalse(self.s.is_empty())
        self.assertEqual(self.s.size(), no_of_pushes)

    def test_push_then_pop(self):
        no_of_pushes = 10
        for i in range(no_of_pushes):
            self.s.push(i)
        for i in range(no_of_pushes):
            self.assertEqual(self.s.pop(), no_of_pushes - i - 1)        
        self.assertTrue(self.s.is_empty())
        self.assertEqual(self.s.size(), 0)

    def test_push_then_peek(self):
        self.s.push(100)
        size = self.s.size()
        self.assertEqual(self.s.peek(), 100)
        self.assertEqual(self.s.size(), size)

    def test_pop_from_empty_stack(self):
        self.assertRaises(IndexError, self.s.pop)

    def test_peek_into_empty_stack(self):
        self.assertRaises(IndexError, self.s.peek)


if __name__ == '__main__':
    unittest.main()
