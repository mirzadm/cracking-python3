"""Unit tests."""

import unittest

from src.q0103 import is_permutation_sort, is_permutation_dict


class TestIsPermutation(unittest.TestCase):
    """Test for different implementations of is_permutation."""
    def test_is_permutation_sort(self):
        self.assertTrue(is_permutation_sort('', ''))
        self.assertTrue(is_permutation_sort('a', 'a'))
        self.assertTrue(is_permutation_sort('aa', 'aa'))
        self.assertTrue(is_permutation_sort('ab', 'ab'))
        self.assertTrue(is_permutation_sort('ab', 'ba'))
        self.assertTrue(is_permutation_sort('abc', 'cba'))
        self.assertTrue(is_permutation_sort('a b c', 'bca  '))
        self.assertFalse(is_permutation_sort('ab ', 'ab'))
        self.assertFalse(is_permutation_sort('Ab', 'ab'))

    def test_is_permutation_dict(self):
        self.assertTrue(is_permutation_dict('', ''))
        self.assertTrue(is_permutation_dict('a', 'a'))
        self.assertTrue(is_permutation_dict('aa', 'aa'))
        self.assertTrue(is_permutation_dict('ab', 'ab'))
        self.assertTrue(is_permutation_dict('ab', 'ba'))
        self.assertTrue(is_permutation_dict('abc', 'cba'))
        self.assertTrue(is_permutation_dict('a b c', 'bca  '))
        self.assertFalse(is_permutation_dict('ab ', 'ab'))
        self.assertFalse(is_permutation_dict('Ab', 'ab'))


if __name__ == '__main__':
    unittest.main()
