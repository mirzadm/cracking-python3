"""Unit test"""

import unittest

from src.q0101 import is_all_unique_str as is_unique


class TestUniqueMethods(unittest.TestCase):
    
    def test_null(self):
        self.assertTrue(is_unique(''))

    def test_nonunique(self):
        self.assertFalse(is_unique('aa'))
        self.assertFalse(is_unique('abca'))

    def test_unique(self):
        self.assertTrue(is_unique('a'))
        self.assertTrue(is_unique('abc'))


if __name__ == '__main__':
    unittest.main()
