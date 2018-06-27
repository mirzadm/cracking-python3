"""Unit tests."""

import unittest

from src.q0105 import compress_string_with_counts as compress_str


class TestCompressStr(unittest.TestCase):
    """Tests for compressing a string with character counts."""
    def test_compress_str(self):
        self.assertEqual(compress_str(''), '')
        self.assertEqual(compress_str('a'), 'a')
        self.assertEqual(compress_str('aa'), 'aa')
        self.assertEqual(compress_str('aaa'), 'a3')
        self.assertEqual(compress_str('aaaa'), 'a4')
        self.assertEqual(compress_str('baaaab'), 'baaaab')
        self.assertEqual(compress_str('baaaaab'), 'b1a5b1')
        self.assertEqual(compress_str('b     b'), 'b1 5b1')
        self.assertEqual(compress_str('aabcccccaaa'), 'a2b1c5a3')


if __name__ == '__main__':
    unittest.main()
