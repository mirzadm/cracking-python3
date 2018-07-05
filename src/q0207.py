"""Chapter 2: Question 7.

Is a given linked list a plindrome? (samee backward and forward).
"""

from src.utils.linkedlist import LinkedList


def is_palindrome(linked_list):
    """Checks if linked_list is a palindrome.
    
    Creates a second linked list to store the first half of input in reverse
    order. Then compares the second half of input with second linked list.

    Args:
        linked_list: An instance object of tyep LinkedList.
    Return:
        True if palindrome, false otherwise.
    """

    if not linked_list.head or not linked_list.head.next_node:
        return True  # Consider an empty linked list a palindrome

    current = linked_list.head
    n = 0
    while current:
        current = current.next_node
        n += 1

    k = n // 2
    current = linked_list.head
    reverse_linked_list = LinkedList()

    while k:
        reverse_linked_list.insert_at_head(current.data)
        current = current.next_node
        k -= 1

    if n % 2 == 1:
        current = current.next_node
    
    p = reverse_linked_list.head
    while p:
        if p.data != current.data:
            return False
        p = p.next_node
        current = current.next_node
    
    return True
