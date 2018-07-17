"""Unit tests for q0504.py."""

import unittest

from src.q0504 import is_power_of_two


class TestIsPowerOfTwo(unittest.TestCase):

    def test_is_power_of_two(self):
        self.assertRaises(ValueError, is_power_of_two, -1)
        self.assertTrue(is_power_of_two(0))
        self.assertTrue(is_power_of_two(1))
        self.assertTrue(is_power_of_two(2))
        self.assertTrue(is_power_of_two(4))
        self.assertTrue(is_power_of_two(8))
        self.assertFalse(is_power_of_two(3))
        self.assertFalse(is_power_of_two(5))
        self.assertFalse(is_power_of_two(6))
        self.assertFalse(is_power_of_two(7))


if __name__ == '__main__':
    unittest.main()
