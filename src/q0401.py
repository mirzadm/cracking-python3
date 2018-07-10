"""Chapter 4: Queston 1.

Check if a binary tree is balanced: heights of subtrees of any node differ at
most by 1.
"""


def check_tree_balance(bin_tree):
    """Returns True if bin_tree is balanced and False otherwise.

    Args:
        bin_tree: An instance object of class BinaryTree.
    """

    if balanced_height(bin_tree.root_node) is None:
        return False
    else:
        return True


def balanced_height(sub_root):
    """Returns height if subtree is balanced, None otherwise."""

    if sub_root is None:
        return -1
    left_height = balanced_height(sub_root.left_child)
    if left_height is None:
        return None
    
    right_height = balanced_height(sub_root.right_child)
    if right_height is None:
        return None
    
    if abs(left_height - right_height) <= 1:
        return max(left_height, right_height) + 1
    else:
        return None
