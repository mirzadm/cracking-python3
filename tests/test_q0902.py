"""Unit tests for q0902.py."""

import unittest

from src.q0902 import find_path


class TestFindPath(unittest.TestCase):
    def setUp(self):
        self.no_paths = set()

    def test_find_path(self):
        exp_path = [(0, 0)]
        blocked_points = {}
        self.assertEqual(find_path(0, 0, 0, 0, blocked_points, self.no_paths),
                                   exp_path)
        
        exp_path = [(0, 0), (1, 0), (1, 1)]
        blocked_points = {}
        self.assertEqual(find_path(0, 0, 1, 1, blocked_points, self.no_paths),
                                   exp_path)
        
        exp_path = [(0, 0), (0, 1), (1, 1)]
        blocked_points = {(1, 0)}
        self.assertEqual(find_path(0, 0, 1, 1, blocked_points, self.no_paths),
                                   exp_path)

        blocked_points = {(1, 0), (0, 1)}
        self.assertIsNone(find_path(0, 0, 1, 1, blocked_points,
                                    self.no_paths))


if __name__ == '__main__':
    unittest.main()
