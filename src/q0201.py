"""Chapter 2: Question 1.

Remove duplicates from a linked list.
"""


def remove_duplicates(linked_list):
    """Removes duplicate element using a set.

    Args:
        linked_list: An instance object of LinkedList

    Returns:
        None. Modifies input argument.
    """
    current = linked_list.head
    previous = None
    unique_elements = set()
    while current:
        if current.data in unique_elements:
            previous.next_node = current.next_node
            del current
            current = previous.next_node
        else:
            unique_elements.add(current.data)
            previous = current
            current = current.next_node
