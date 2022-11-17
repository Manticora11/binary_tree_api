from binarytree import Node


class BinaryTreeNode(Node):

    def _init_(self, value, left=None, right=None):
        super()._init_(value, left, right)

    def insert_node(self, new_number):

        # If node doesn't exist
        if not self.value:
            self.value = new_number
            return

        # If node exists
        if self.value == new_number:
            return

        if new_number < self.value:
            if self.left:
                self.left.insert_node(new_number)
                return
            self.left = BinaryTreeNode(new_number)
            return

        if self.right:
            self.right.insert_node(new_number)
            return
        self.right = BinaryTreeNode(new_number)


def find_common_ancestor(root, first_number, second_number):

    while root:
        # If both first_number and second_number are lower than root,
        # asign the left node.
        if first_number < root.value and second_number < root.value:
            root = root.left 
        # If both first_number and second_number are greater than root,
        # asign the right node.
        elif first_number > root.value and second_number > root.value:
            root = root.right
        else:
            break
    return root.value if root is not None else None


def create_new_tree(root, nodes):

    tree = BinaryTreeNode(root)
    for combination in nodes:
        for node in combination:
            tree.insert_node(node)
    print("tree: ", tree)
    return tree