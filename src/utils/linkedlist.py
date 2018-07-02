"""Linked list implementation.

Linked lists are the subject of Chapter 2. 
"""


class Node:
    """A class for nodes in a linked list."""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """A class for lined lists."""
    def __init__(self, head=None):
        self.head = head

    def insert_at_head(self, data):
        """Inserts a new node at the beginning of the linked-list.
        
        Creates a new node with given data. Inserts it at the head. Updates
        the head.

        Args:
            data: Input value used as the new nodes's data field.
        """
        n = Node(data)
        n.next_node = self.head
        self.head = n

    def convert_to_list(self):
        """Returns a list version of linked-list."""
        n = self.head
        result = []
        while n:
            result.append(n.data)
            n = n.next_node
        return result
