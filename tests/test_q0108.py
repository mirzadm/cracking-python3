"""Unit tests for q0108.py."""

import unittest

from src.q0108 import is_rotation_slicing, is_rotation_substring


class TestIsRotation(unittest.TestCase):
    """Tests for two implementations of is_rotation."""
    def test_is_rotation_slicing(self):
        self.assertFalse(is_rotation_slicing('', ''))
        self.assertFalse(is_rotation_slicing('', 'a'))
        self.assertFalse(is_rotation_slicing('a', 'b'))
        self.assertTrue(is_rotation_slicing('a', 'a'))
        self.assertFalse(is_rotation_slicing('a', 'aa'))
        self.assertTrue(is_rotation_slicing('ab', 'ab'))
        self.assertTrue(is_rotation_slicing('ab', 'ba'))
        self.assertTrue(is_rotation_slicing('abc', 'cab'))
        self.assertTrue(is_rotation_slicing('abc', 'bca'))
        self.assertTrue(is_rotation_slicing('abc', 'abc'))
        self.assertFalse(is_rotation_slicing('abc', 'cba'))
        self.assertFalse(is_rotation_slicing('abc', 'bac'))
        self.assertFalse(is_rotation_slicing('abc', 'acb'))

    def test_is_rotation_substring(self):
        self.assertFalse(is_rotation_substring('', ''))
        self.assertFalse(is_rotation_substring('', 'a'))
        self.assertFalse(is_rotation_substring('a', 'b'))
        self.assertTrue(is_rotation_substring('a', 'a'))
        self.assertFalse(is_rotation_substring('a', 'aa'))
        self.assertTrue(is_rotation_substring('ab', 'ab'))
        self.assertTrue(is_rotation_substring('ab', 'ba'))
        self.assertTrue(is_rotation_substring('abc', 'cab'))
        self.assertTrue(is_rotation_substring('abc', 'bca'))
        self.assertTrue(is_rotation_substring('abc', 'abc'))
        self.assertFalse(is_rotation_substring('abc', 'cba'))
        self.assertFalse(is_rotation_substring('abc', 'bac'))
        self.assertFalse(is_rotation_substring('abc', 'acb'))


if __name__ == '__main__':
    unittest.main()
