"""Chapter 2: Question 3.

How do you delete a node in linked list given only access to that node?
"""


def del_intermediate_node(node):
    """Deletes a node in the middle of a linked list.

    We only have access to to-be-deleted node. Copy data from next node then
    delete next node.

    Args:
        node: An instace obejct of class Node. Points to the node to be
        deleted. It can not be the last node.
    Returns:
        True if successful False otherwise.
    """
    # it can't be the last node
    if not node:
        return False
    if not node.next_node:  # It can't be the last node
        return False

    temp = node.next_node
    node.data = temp.data
    node.next_node = temp.next_node
    del temp

    return True
