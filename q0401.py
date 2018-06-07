"""Check whether a binary tree is balanced."""


def height_balance(node):
    if node is None:
        return 0
    left_height = height_balance(node.left)
    if left_height == -1:
        return -1
    
    right_height = height_balance(node.right)
    if right_height == -1:
        return -1
    
    if abs(left_height - right_height) >= 2:
        return -1
    else:
        return max(left_height, right_height) + 1


class BinaryNode:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def test():
    nodes = [BinaryNode(i) for i in range(7)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[3].left = nodes[5]
    # nodes[2].left = nodes[5]
    # nodes[2].right = nodes[6]
    
    print(height_balance(nodes[0]))


if __name__ == '__main__':
    test()


    


        



