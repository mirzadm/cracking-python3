"""Unit tests for q0502.py."""

import unittest

from src.q0502 import fraction_to_binary_digits


class MyFractionToBinaryDigits(unittest.TestCase):

    def test_0_and_1(self):
        self.assertEqual(fraction_to_binary_digits(0), 'Error')
        self.assertEqual(fraction_to_binary_digits(1), 'Error')

    def test_fractions_success(self):
        self.assertEqual(fraction_to_binary_digits(0.5), [1])
        self.assertEqual(fraction_to_binary_digits(0.25), [0, 1])
        self.assertEqual(fraction_to_binary_digits(0.75), [1, 1])
        self.assertEqual(fraction_to_binary_digits(0.125), [0, 0, 1])

    def test_fractions_error(self):
        self.assertEqual(fraction_to_binary_digits(0.3), 'Error')


if __name__ == '__main__':
    unittest.main()
