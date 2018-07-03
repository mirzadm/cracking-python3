"""Chapter 2: Question 4.

Write code to partition a linked list around a value x, such that all nodes
less than x come before all nodes greater than or equal to x.
"""


def partition_linkedlist_around_value(linked_list, x):
    """Patitions a linkedlist around a given value x.data

    Travese the linked list, insert nodes with node.data >= x at the end.
    Args:
        linked_list: An instace object of class LinkedList.
        x: value of type LinkedList.data

    Returns:
        Reference to modified linked_list. Changes the input linked_list
        argument.
    """
    if (not linked_list or not linked_list.head or
        not linked_list.head.next_node):
        # Change nothing
        return linked_list

    # Find the tail node
    current = linked_list.head
    while current.next_node:
        current = current.next_node
    original_tail = current
    # Setup pointers
    new_tail = original_tail
    previous = None
    current = linked_list.head
    # Partition
    while current != original_tail:
        if current.data >= x:
            if previous:
                previous.next_node = current.next_node
                new_tail.next_node = current
                current.next_node = None
                new_tail = current
                current = previous.next_node
            else:
                linked_list.head = current.next_node
                new_tail.next_node = current
                current.next_node = None
                new_tail = current
                current = linked_list.head
        else:
            previous = current
            current = current.next_node

    return linked_list
