"""Unit tests for q0106.py."""

import unittest

from src.q0106 import (rotate_matrix_90_clk as rotate_matrix,
                       rotate_matrix__90_clk_inplace as rotate_matrix_inplace)


class TestRotateMatrix(unittest.TestCase):
    """Tests for matrix 90 degress clockwise rotation."""
    def setUp(self):
        self.m22 =   [[1, 2],
                      [3, 4]]

        self.m22_r = [[3, 1],
                      [4, 2]]

        self.m33 =   [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]

        self.m33_r = [[7, 4, 1],
                      [8, 5, 2],
                      [9, 6, 3]]

        self.m44 =   [[1,   2,  3,  4],
                      [5,   6,  7,  8],
                      [9,   10, 11, 12],
                      [13,  14, 15, 16]]

        self.m44_r = [[13,  9,  5,  1],
                      [14,  10, 6,  2],
                      [15,  11, 7,  3],
                      [16,  12, 8,  4]]

    def test_rotate_matrix(self):
        self.assertEqual(rotate_matrix([]),[])
        self.assertEqual(rotate_matrix([1]),[1])
        self.assertEqual(rotate_matrix(self.m22), self.m22_r)
        self.assertEqual(rotate_matrix(self.m33), self.m33_r)
        self.assertEqual(rotate_matrix(self.m44), self.m44_r)
        # 4 rotations yield the same matrix
        self.assertEqual(rotate_matrix(
                            rotate_matrix(
                                rotate_matrix(
                                    rotate_matrix(self.m44)))), self.m44)

    def test_rotate_matrix_inplace(self):
        self.assertEqual(rotate_matrix_inplace([]), [])
        self.assertEqual(rotate_matrix_inplace([1]), [1])
        self.assertEqual(rotate_matrix_inplace(self.m22), self.m22_r)
        self.assertEqual(rotate_matrix_inplace(self.m33), self.m33_r)
        self.assertEqual(rotate_matrix_inplace(self.m44), self.m44_r)
        # 4 rotations yield the same matrix
        self.assertEqual(rotate_matrix_inplace(
                            rotate_matrix_inplace(
                                rotate_matrix_inplace(
                                    rotate_matrix_inplace(self.m44)))),
                                                          self.m44)


if __name__ == '__main__':
    unittest.main()
