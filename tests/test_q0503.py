"""Unit tests for q0503.py."""

import unittest

from src.q0503 import find_next_biggest_with_same_1s


class TestNextBiggestNum(unittest.TestCase):

    def test_non_positive(self):
        self.assertRaises(ValueError, find_next_biggest_with_same_1s, 0)

    def test_positive_values(self):
        self.assertEqual(find_next_biggest_with_same_1s(0b1), 0b10)
        self.assertEqual(find_next_biggest_with_same_1s(0b10), 0b100)
        self.assertEqual(find_next_biggest_with_same_1s(0b11), 0b101)
        self.assertEqual(find_next_biggest_with_same_1s(0b110), 0b1001)


if __name__ == '__main__':
    unittest.main()
