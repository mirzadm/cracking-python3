"""Unit tests for q0501."""

import unittest

from src.q0501 import insert_bits as insert_bits


class MyTests(unittest.TestCase):

    def test_insert(self):
        self.assertTrue(insert_bits(0b11111111, 0b010, 3, 1) == 0b11110101)
        self.assertTrue(insert_bits(0b11111111, 0b010, 4, 1) == 0b11100101)
        self.assertTrue(insert_bits(0b11111111, 0b010, 7, 5) == 0b01011111)


if __name__ == '__main__':
    unittest.main()
