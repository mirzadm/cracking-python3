"""Chapter 2: Question 2.

Implement an algorithm to find the kth to last element of a singly linked list.
"""


def kth_element_to_last(linked_list, k):
    """Returns kth to last element of a linked list.

    Args:
        linked_list: An instance object of LinkedList.
        k: Integer >=1, k=1 is last element, k=2 second to last, and so on.

    Returns:
        If kth to last element exists, returns value of data field.
        Otherwise returns None.
    """
    if not linked_list:
        return None
    if not linked_list.head or k < 1:
        return None

    current = linked_list.head
    kth_last = linked_list.head

    # Move current k-1 steps forward
    for _ in range(k-1):
        if not current.next_node:
            return None
        else:
            current = current.next_node
    # Move forward until tail of linked list is reached
    while current.next_node:
        current = current.next_node
        kth_last = kth_last.next_node

    return kth_last.data
