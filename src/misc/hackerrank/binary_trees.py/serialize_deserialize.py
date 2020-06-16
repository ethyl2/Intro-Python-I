"""
From Kapil Sharma's lecture 16 Jun 2020
"Serialize and deserialize a binary tree"

More info:
    Note: it's not a binary search tree, just a binary tree.
    In this example, we will store the tree as a string <- serializing it.
    And then convert it back to a tree <- deserializing it.
    We need to pick a delimiter/separator that makes sense, considering what type of data is stored.
        If a comma could be stored, don't pick it as a delimiter!
    We will put a # in our string when the node is None.

We will use Pre-Order to store and later to remake the tree:
    1. Visit current
    2. Visit left
    3. Visit right

        5
       / \
     34   6
     /\   /
    7  9  3 
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def serialize(node):
    output_string = ''

    def serialize_inner(node):
        nonlocal output_string

        # Add a # (what we agreed upon) if node is None
        if node == None:
            output_string += "#"
            output_string += ","
            return

        # Visit current

        output_string += str(node.data)
        output_string += ","

        # Visit left
        serialize_inner(node.left)

        # Visit right
        serialize_inner(node.right)
    serialize_inner(node)
    return output_string


root = TreeNode(5)
node34 = TreeNode(34)
node6 = TreeNode(6)
root.left = node34
root.right = node6

node7 = TreeNode(7)
node9 = TreeNode(9)
node34.left = node7
node34.right = node9

node3 = TreeNode(3)
node6.left = node3

print(serialize(root))  # Should print out 5,34,7,#,#,9,#,#,6,3,#,#,#,
