"""Create a list of nodes at each level given a binary tree."""


class BinNode:
    
    def __init__(self, id=None, data=None):
        self.id = id
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return '{}:{}'.format(self.id, self.data)

    def __repr__(self):
        return self.__str__()


class BinTree:

    def __init__(self, root=None):
        self.root = root        


def create_depth_list(bin_tree):

    if not bin_tree or not bin_tree.root:
        return []

    depth_list = []
    depth_list.append([bin_tree.root])
    current = 0

    while True:
        new_list = []
        for node in depth_list[current]:
            if node.left:
                new_list.append(node.left)
            if node.right:
                new_list.append(node.right)
        if new_list:
            depth_list.append(new_list)
            current += 1
        else:
            break

    return depth_list


def test():
    
    node_list = [BinNode(i) for i in range(6)]
    bt = BinTree(node_list[0])
    node_list[0].left = node_list[1]
    node_list[0].right = node_list[2]
    node_list[1].left = node_list[3]
    node_list[2].right = node_list[4]
    node_list[4].left = node_list[5]
    print(node_list)
    depth_list = create_depth_list(bt)
    print(depth_list)


if __name__ == '__main__':
    test()
