"""Unit tests."""

import unittest

from q1102 import is_anagram as is_anagram, sort_by_anagram as sort_by_anagram


class MyTests(unittest.TestCase):
    
    def test_is_anagram(self):
        self.assertTrue(is_anagram('', ''))
        self.assertTrue(is_anagram('a', 'a'))
        self.assertTrue(is_anagram('a', 'A'))
        self.assertTrue(is_anagram('ab', 'ba'))
        self.assertTrue(is_anagram('ab', 'ab'))
        self.assertTrue(is_anagram('abc', 'abc'))
        self.assertTrue(is_anagram('acb', 'abc'))
        self.assertTrue(is_anagram('bac', 'abc'))
        self.assertTrue(is_anagram('bca', 'abc'))
        self.assertTrue(is_anagram('cab', 'abc'))
        self.assertTrue(is_anagram('cba', 'abc'))

        self.assertFalse(is_anagram('a', 'b'))
        self.assertFalse(is_anagram('ab', 'ac'))

    
    def test_sort_by_anagram(self):
        self.assertEqual(sort_by_anagram(['a', 'b']), ['a', 'b'])
        self.assertEqual(sort_by_anagram(['a', 'b', 'c']), ['a', 'b', 'c'])
        self.assertEqual(sort_by_anagram(['a', 'b', 'a']), ['a', 'a', 'b'])
        self.assertEqual(sort_by_anagram(['b', 'a', 'a']), ['b', 'a', 'a'])
        self.assertEqual(sort_by_anagram(['a', 'b', 'b', 'a']), ['a', 'a', 'b', 'b'])


if __name__ == '__main__':
    unittest.main()
