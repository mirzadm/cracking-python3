"""Unit tests."""

import unittest

from src.q0104 import replace_spaces, replace_spaces_list


class TestReplaceSpaces(unittest.TestCase):
    """Tests for different implementations."""
    def test_replace_spaces(self):
        self.assertEqual(replace_spaces(''), '')
        self.assertEqual(replace_spaces(' '), '%20')
        self.assertEqual(replace_spaces('a'), 'a')
        self.assertEqual(replace_spaces(' a '), '%20a%20')
        self.assertEqual(replace_spaces('ab cd'), 'ab%20cd')

    def test_replace_spaces_list(self):
        self.assertEqual(replace_spaces_list(''), '')
        self.assertEqual(replace_spaces_list(' '), '%20')
        self.assertEqual(replace_spaces_list('a'), 'a')
        self.assertEqual(replace_spaces_list(' a '), '%20a%20')
        self.assertEqual(replace_spaces_list('ab cd'), 'ab%20cd')


if __name__ == '__main__':
    unittest.main()
