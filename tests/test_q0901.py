"""Unit tests for q0901.py."""

import unittest

from src.q0901 import run_up_stairs_rec, run_up_stairs_iter


class TestRunStairs(unittest.TestCase):

    def test_run_up_stairs_rec(self):
        self.assertEqual(run_up_stairs_rec(0), 0)
        self.assertEqual(run_up_stairs_rec(1), 1)
        self.assertEqual(run_up_stairs_rec(2), 2)
        self.assertEqual(run_up_stairs_rec(3), 4)
        self.assertEqual(run_up_stairs_rec(4), 7)

    def test_run_up_stairs_iter(self):
        self.assertEqual(run_up_stairs_iter(0), 0)
        self.assertEqual(run_up_stairs_iter(1), 1)
        self.assertEqual(run_up_stairs_iter(2), 2)
        self.assertEqual(run_up_stairs_iter(3), 4)
        self.assertEqual(run_up_stairs_iter(4), 7)


if __name__ == '__main__':
    unittest.main()
