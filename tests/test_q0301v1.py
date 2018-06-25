"""Unit tests for 1-array implementation of 3 stacks."""

import unittest

from src.q0301v1 import ThreeStack as Stack


class MyTests(unittest.TestCase):

    def test_push_pop(self):
        st = Stack(3)
        st.push(0, 10)
        st.push(1, 11)
        st.push(2, 12)
        
        self.assertEqual(st.pop(0), 10)
        self.assertEqual(st.pop(1), 11)
        self.assertEqual(st.pop(2), 12)

        self.assertEqual(st.pop(0), None)
        self.assertEqual(st.pop(1), None)
        self.assertEqual(st.pop(2), None)


if __name__ == '__main__':
    unittest.main()
