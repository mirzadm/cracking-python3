"""Unit tests for q0207.py."""

import unittest

from src.utils.linkedlist import LinkedList
from src.q0207 import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome_linkedlist(self):
        linked_list = LinkedList()
        self.assertTrue(is_palindrome(linked_list))
        linked_list.insert_at_head(1)
        self.assertTrue(is_palindrome(linked_list))
        linked_list.insert_at_head(1)
        self.assertTrue(is_palindrome(linked_list))
        linked_list.insert_at_head(2)
        self.assertFalse(is_palindrome(linked_list))        
        linked_list.insert_at_head(1)
        self.assertFalse(is_palindrome(linked_list))
        linked_list.insert_at_head(1)
        self.assertTrue(is_palindrome(linked_list))
        linked_list.insert_at_head(1)
        self.assertFalse(is_palindrome(linked_list))


if __name__ == '__main__':
    unittest.main()
