"""Unit tests."""

import unittest

from src.q0901 import count_ways_rec as ways_rec, count_ways_iter as ways_iter


class MyTests(unittest.TestCase):

    def test_rec(self):
        self.assertEqual(ways_rec(0), 0)
        self.assertEqual(ways_rec(1), 1)
        self.assertEqual(ways_rec(2), 2)
        self.assertEqual(ways_rec(3), 4)
        self.assertEqual(ways_rec(4), 7)

    def test_iter(self):
        self.assertEqual(ways_iter(0), 0)
        self.assertEqual(ways_iter(1), 1)
        self.assertEqual(ways_iter(2), 2)
        self.assertEqual(ways_iter(3), 4)
        self.assertEqual(ways_iter(4), 7)


if __name__ == '__main__':
    unittest.main()
