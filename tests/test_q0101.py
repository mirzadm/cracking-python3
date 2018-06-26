"""Unit tests."""

import unittest

from src.q0101 import (is_all_unique_str as is_unique,
                       is_all_unique_dict as is_unique_dict,
                       is_all_unique_set as is_unique_set)


class TestUniqueness(unittest.TestCase):
    """Tests for string, dictionary, and set implementations."""
    def test_str(self):
        self.assertTrue(is_unique(''))
        self.assertTrue(is_unique('a'))
        self.assertFalse(is_unique('aa'))
        self.assertTrue(is_unique('abc'))
        self.assertFalse(is_unique('abb'))

    def test_dict(self):
        self.assertTrue(is_unique_dict(''))
        self.assertTrue(is_unique_dict('a'))
        self.assertFalse(is_unique_dict('aa'))
        self.assertTrue(is_unique_dict('abc'))
        self.assertFalse(is_unique_dict('abb'))

    def test_set(self):
        self.assertTrue(is_unique_set(''))
        self.assertTrue(is_unique_set('a'))
        self.assertFalse(is_unique_set('aa'))
        self.assertTrue(is_unique_set('abc'))
        self.assertFalse(is_unique_set('abb'))


if __name__ == '__main__':
    unittest.main()
