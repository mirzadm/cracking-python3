"""Unit tests for q0301.py."""

import unittest

from src.q0301 import ThreeStacks, some_function


class TestThreeStacks(unittest.TestCase):

    def test_init(self):
        s = ThreeStacks(10)
        self.assertEqual(s.size, 10)
        self.assertRaises(ValueError, ThreeStacks, 2)

    def test_is_empty(self):
        s = ThreeStacks(3)
        self.assertTrue(s.is_empty(0))
        self.assertTrue(s.is_empty(1))
        self.assertTrue(s.is_empty(2))
        self.assertRaises(IndexError, s.is_empty, 3)

    def test_push_pop(self):
        s = ThreeStacks(3)
        self.assertRaises(IndexError, s.push, 3, 10)
        self.assertRaises(IndexError, s.pop, 3)
        s.push(0, 100)
        s.push(1, 101)
        s.push(2, 102)
        self.assertEqual(s.pop(0), 100)
        self.assertEqual(s.pop(1), 101)
        self.assertEqual(s.pop(2), 102)
        self.assertIsNone(s.pop(0))
        self.assertIsNone(s.pop(1))
        self.assertIsNone(s.pop(2))


if __name__ == '__main__':
    unittest.main()
