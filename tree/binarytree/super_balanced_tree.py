#  Super balanced  tree (made up property)
# A tree is superbalaced if the difference between the depths of any two leaf
# nodes is no longer than one.

# Steps:
# Find the max depth node; say depth is d_max
#  Find the min depth node, say depth is d_min
# If d_max and d_min is less than or equal to 1, then the tree is super
# balanced.

import unittest


class Node(object):
    """Tree Node class."""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_tree_super_balanced(root):
    """Check if the tree is super balanced or not."""
    d_max = depth_of_tree(root)
    d_min = depth_of_tree(root, False)

    if d_max - d_min > 1:
        return False
    else:
        return True


def depth_of_tree(root, is_max=True):
    if root is None:
        return -1
    # Traverse left
    left_depth = 1 + depth_of_tree(root.left, is_max)
    # Traverse right
    right_depth = 1 + depth_of_tree(root.right, is_max)
    if is_max:
        return max(left_depth, right_depth)
    else:
        return min(left_depth, right_depth)


class SuperBalancedTest(unittest.TestCase):

    def test_balanced(self):
        tree1 = Node(10, Node(20), Node(30, Node(40)))
        tree2 = Node(10, Node(20), Node(30))
        tree3 = Node(10)
        self.assertTrue(is_tree_super_balanced(tree1), "Tree is not balanced.")
        self.assertTrue(is_tree_super_balanced(tree2), "Tree is not balanced.")
        self.assertTrue(is_tree_super_balanced(tree3), "Tree is not balanced.")

    def test_unbalanced(self):
        tree1 = Node(10, Node(20, Node(30)))
        tree2 = Node(10, Node(20), Node(30, Node(40, Node(50))))
        self.assertFalse(is_tree_super_balanced(tree1), "Tree is balnced.")
        self.assertFalse(is_tree_super_balanced(tree2), "Tree is balanced.")

if __name__ == "__main__":
    unittest.main()
