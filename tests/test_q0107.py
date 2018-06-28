"""Unit tests."""

import unittest

from src.q0107 import zero_fill_matrix


class TestZeroFillMatrix(unittest.TestCase):
    """Tests for zero-fill matrix."""
    def test_zero_fill_matrix(self):
        self.assertEqual(zero_fill_matrix([], 0, 0), [])
        self.assertEqual(zero_fill_matrix([[1]], 1, 1), [[1]])
        self.assertEqual(zero_fill_matrix([[0]], 1, 1), [[0]])
        self.assertEqual(zero_fill_matrix([[1, 2, 3]], 1, 3), [[1, 2, 3]])
        self.assertEqual(zero_fill_matrix([[1, 2, 0]], 1, 3), [[0, 0, 0]])
        self.assertEqual(zero_fill_matrix([[1], [2], [3]], 3, 1), [[1], [2], [3]])
        self.assertEqual(zero_fill_matrix([[1], [0], [3]], 3, 1), [[0], [0], [0]])
        m33_nozeros = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]]
        m33_nozeros_result = [[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]]
        self.assertEqual(zero_fill_matrix(m33_nozeros, 3, 3),
                         m33_nozeros_result)
        m33_zeros = [[1, 2, 0],
                     [4, 0, 6],
                     [7, 8, 9]]
        m33_zeros_result = [[0, 0, 0],
                            [0, 0, 0],
                            [7, 0, 0]]
        self.assertEqual(zero_fill_matrix(m33_zeros, 3, 3),
                         m33_zeros_result)


if __name__ == '__main__':
    unittest.main()
