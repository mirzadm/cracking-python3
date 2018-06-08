"""Unit tests."""

import unittest

from q1101 import sort_array_buf as sort_array


class MyTests(unittest.TestCase):
    
    def test_sort_array(self):
        self.assertEqual(sort_array([1], []), None)
        self.assertEqual(sort_array([1], [2]), None)
        self.assertEqual(sort_array([1, 0], [2]), [1, 2])
        self.assertEqual(sort_array([2, 0], [1]), [1, 2])
        self.assertEqual(sort_array([4, 5, 6, 0, 0, 0], [1, 2, 3]),
                                    [1, 2, 3, 4, 5, 6])
        self.assertEqual(sort_array([1, 5, 6, 0, 0, 0], [1, 2, 3]),
                                    [1, 1, 2, 3, 5, 6])


if __name__ == '__main__':
    unittest.main()
