"""Chapter 4: Question 3.

Create a binary search tree from a sorted array, with minimal height.
"""


class TreeNode:
    
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    
    def __init__(self, root=None):
        self.root_node = None


def sorted_array_to_bin_search_tree(array):    
    bin_tree = BinaryTree()   
    if array == []:
        return bin_tree
    
    bin_tree.root_node = TreeNode()

    high = len(array) - 1
    low = 0
    mid = (low + high) // 2
    
    bin_tree.root_node.data = array[mid]

    bin_tree.root_node.left = sub_array_bst(array, low, mid-1)
    bin_tree.root_node.right = sub_array_bst(array, mid+1, high)
    
    return bin_tree


def sub_array_bst(array, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    n = TreeNode()
    n.data = array[mid]
    n.left = sub_array_bst(array, low, mid-1)
    n.right = sub_array_bst(array, mid+1, high)

    return n
