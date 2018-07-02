"""Chapter 2: Question 3.

Implement an algorithm to delete a node in the middle of a singly linked list,
given only access to that node.
EXAMPLE
Input: the node c from the linked list a->b->c->d->e.
Linked list would be updated to a->b->d->e.
"""


def del_intermediate_node(node):
    """Deletes a node in the middle of a linked list.

    We only have access to to-be-deleted node. Starting form the node shift
    left nodes on right, then delete that last node.

    Args:
        node: An instace obejct of class Node. Points to the node to be
        deleted. It can not be the last node.
    Returns:
        node.data is successful None otherwise.
    """
    # it can't be the last node
    if not node:
        return None
    if not node.next_node:  # It can't be the last node
        return None

    current = node
    temp = node.data
    while current.next_node:
        previous = current
        current = current.next_node
        previous.data = current.data

    previous.next_node = None
    del current
    return temp
