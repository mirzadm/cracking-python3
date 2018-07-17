"""Unit tests for q0505.py."""

import unittest

from src.q0505 import count_unequal_bits


class TestCountUnequalBits(unittest.TestCase):

    def test_count_unequal_bits(self):
        self.assertRaises(ValueError, count_unequal_bits, -1, 1)
        self.assertEqual(count_unequal_bits(0b0, 0b0), 0)       
        self.assertEqual(count_unequal_bits(0b1, 0b1), 0)
        self.assertEqual(count_unequal_bits(0b01, 0b10), 2)
        self.assertEqual(count_unequal_bits(0b001, 0b110), 3)


if __name__ == '__main__':
    unittest.main()
