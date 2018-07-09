"""Unit test for q0304.py."""

import unittest

from src.utils.stack import Stack
from src.q0304 import towers_of_hanoi


class TestTowersOfHanoi(unittest.TestCase):

    def setUp(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.s3 = Stack()

    def test_one(self):
        self.s1.push('a')
        towers_of_hanoi(1, self.s1, self.s2, self.s3)
        self.assertTrue(self.s1.is_empty())
        self.assertTrue(self.s2.is_empty())
        self.assertEqual(self.s3.size(), 1)
        self.assertEqual(self.s3.pop(), 'a')

    def test_three(self):
        self.s1.push('a')
        self.s1.push('b')
        self.s1.push('c')
        towers_of_hanoi(3, self.s1, self.s2, self.s3)
        self.assertTrue(self.s1.is_empty())
        self.assertTrue(self.s2.is_empty())
        self.assertEqual(self.s3.size(), 3)
        self.assertEqual(self.s3.pop(), 'c')
        self.assertEqual(self.s3.pop(), 'b')
        self.assertEqual(self.s3.pop(), 'a')


if __name__ == '__main__':
    unittest.main()
