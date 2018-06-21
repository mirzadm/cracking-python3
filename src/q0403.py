"""Create a binary search tree from a sorted array, with minimal height."""


class TreeNode:
    
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    
    def __init__(self, root=None):
        self.root = None
        

def array_to_bst(array):    
    if array == []:
        return None

    bt = BinaryTree()
        
    bt.root = TreeNode()
    
    high = len(array) - 1
    low = 0
    mid = (low + high) // 2
    
    bt.root.data = array[mid]

    bt.root.left = sub_array_bst(array, low, mid-1)
    bt.root.right = sub_array_bst(array, mid+1, high)
    
    return bt


def sub_array_bst(array, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    n = TreeNode()
    n.data = array[mid]
    n.left = sub_array_bst(array, low, mid-1)
    n.right = sub_array_bst(array, mid+1, high)

    return n


def bfs_bt(tree):
    array = []
    i = 0
    k = 0
    array.append(tree.root)
    k += 1
    while i < k:
        n = array[i]
        i += 1
        if n.left is not None:
            array.append(n.left)
            k += 1
        if n.right is not None:
            array.append(n.right)
            k += 1
    
    return array


def test():    
    a = list(range(5))
    print(a)
    bt = array_to_bst(a)   
    b = bfs_bt(bt)
    values = [node.data for node in b]
    print(values)


if __name__ == '__main__':
    test()
