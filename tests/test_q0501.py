"""Unit tests for q0501.py."""

import unittest

from src.q0501 import insert_bits_in_num


class MyInsertBits(unittest.TestCase):

    def test_insert_one_bit_1(self):
        m = 0b1
        n = 0b0000_0000
        i = 0
        j = 0
        m_in_n = 0b0000_0001
        self.assertEqual(insert_bits_in_num(m, n, i, j), m_in_n)

    def test_insert_one_bit_0(self):
        m = 0b0
        n = 0b0000_0001
        i = 0
        j = 0
        m_in_n = 0b0
        self.assertEqual(insert_bits_in_num(m, n, i, j), m_in_n)

    def test_insert_two_bits_11(self):
        m = 0b11
        n = 0b0000_0000
        i = 2
        j = 3
        m_in_n = 0b0000_1100
        self.assertEqual(insert_bits_in_num(m, n, i, j), m_in_n)

if __name__ == '__main__':
    unittest.main()
