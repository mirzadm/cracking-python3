""""Chapter 2: Question 6.

Given a linked list with a loop, find the node at the beginning of a the loop.
"""


def find_loop_slow_fast(linked_list):
    """Solution using slow and fast pointers.

    Assumes there is a loop in linked_list.
    """

    slow1 = linked_list.head
    fast = linked_list.head
    while True:
        slow1= slow1.next_node
        fast = fast.next_node.next_node
        if slow1 == fast:
            break
            
    slow2 = linked_list.head
    while slow1 != slow2:
        slow1 = slow1.next_node
        slow2 = slow2.next_node

    return slow1.data
