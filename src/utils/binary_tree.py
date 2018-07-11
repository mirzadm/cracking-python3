"""Implements a basic binary tree."""


class BinaryTreeNode:

    def __init__(self, node_id):
        self.node_id = node_id
        self.left_child = None
        self.right_child = None
        self.data = None


class BinaryTree:
    """Implements a binary tree using pointers.

    Provides methods to convert to/from adjacency representation.
    """

    def __init__(self):
        self.root_node = None

    def adjacency_to_tree(self, root_id, adj_dict):
        """Creates a pointer implementation from an adjacency dictionary.
        
        Args:
            root_id: Id for the root node.

            adj_dict: A input dictionary representing parent-children
                      adjacency. Each key-value pair in the dictionary
                      represents one node and its left and right children. 

                      node_id: (left_child_id, right_child_id)

                      Example: {0: (1, 2), 1: (3, 4), 4: (None, 5)}

                      `None` is used when a child does not exist.
        """

        if adj_dict.get(root_id) is None:
            raise KeyError('Root id does not exist in adjacency dictionary.')

        id_node_dict = {}
        for parent_id, children_tuple in adj_dict.items():
            # Create a node for parent if it does not exist alerady
            parent_node = id_node_dict.get(parent_id)
            if parent_node is None:
                parent_node = BinaryTreeNode(parent_id)
                id_node_dict.update({parent_id: parent_node})
            # Create a node for left child if it exists and not already
            # created
            if children_tuple[0] is not None:
                left_child = id_node_dict.get(children_tuple[0])
                if left_child is None:
                    left_child = BinaryTreeNode(children_tuple[0])
                    id_node_dict.update({children_tuple[0]: left_child})
                parent_node.left_child = left_child
            # Create a node for right child if it exists and not already
            # created
            if children_tuple[1] is not None:
                right_child = id_node_dict.get(children_tuple[1])
                if right_child is None:
                    right_child = BinaryTreeNode(children_tuple[1])
                    id_node_dict.update({children_tuple[1]: right_child})
                parent_node.right_child = right_child

        self.root_node = id_node_dict.get(root_id)

    def tree_to_adjacency(self):
        """Returns the adjacency dictionary representing the tree.
        
        Returns:
            Adjacency dictionary. 
            Refer to `adjacency_to_tree` for more on representation.
        """

        adj_dict = {}
        if self.root_node is not None:
            self._tree_to_adjacency(self.root_node, adj_dict)

        return adj_dict

    def _tree_to_adjacency(self, sub_root, adj_dict):
        """Recursive helper method to create adjacency representation.

        Updates adj_dict with adjacency entries for sub-tree rooted at
        sub_root.
        
        Args:
            sub_root: An instance object of class BinaryTreeNode.
            adj_dict: An adjacency dictionary. Refer to
            `adjacency_to_tree` for description.
        """

        if sub_root.left_child is None:
            left_child_id = None
        else:
            left_child_id = sub_root.left_child.node_id

        if sub_root.right_child is None:
            right_child_id = None
        else:
            right_child_id = sub_root.right_child.node_id

        adj_dict.update({sub_root.node_id: (left_child_id, right_child_id)})
        if sub_root.left_child is not None:
            self._tree_to_adjacency(sub_root.left_child, adj_dict)

        if sub_root.right_child is not None:
            self._tree_to_adjacency(sub_root.right_child, adj_dict)
