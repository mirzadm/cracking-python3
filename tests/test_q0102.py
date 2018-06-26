"""Unit tests."""

import unittest

from src.q0102 import reverse, reverse_shortcut


class TestReverse(unittest.TestCase):
    """Tests for two implementations of string reverse."""
    def test_reverse(self):
        self.assertEqual(reverse(''), '')
        self.assertEqual(reverse('a'), 'a')
        self.assertEqual(reverse(' '), ' ')
        self.assertEqual(reverse('ab'), 'ba')
        self.assertEqual(reverse('abc'), 'cba')
        self.assertEqual(reverse('abb'), 'bba')

    def test_reverse_shortcut(self):
        self.assertEqual(reverse_shortcut(''), '')
        self.assertEqual(reverse_shortcut('a'), 'a')
        self.assertEqual(reverse_shortcut(' '), ' ')
        self.assertEqual(reverse_shortcut('ab'), 'ba')
        self.assertEqual(reverse_shortcut('abc'), 'cba')
        self.assertEqual(reverse_shortcut('abb'), 'bba')


if __name__ == '__main__':
    unittest.main()
