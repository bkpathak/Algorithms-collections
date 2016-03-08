"""Find the second largest element in the BST."""

# Find the largest
# Case 1: Largest doesn't have left sub-tree
#        The Second largest is the parent of the largest
# Case 2: The largest has the left subtree
#   The second largest is the largest in the left sub tree


class Node(object):
    """Tree Node class."""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def second_largest_elem_bst(root):
    """Returns the second largest element."""
    if root is None:
        return
    # Case 1
    if root.right.right is None and root.right.left is None:
        return root.val

    # Case 2
    if root.right.right is None and root.right.left:
        return second_largest_elem_bst(root.right.left)

    # Repeat for the right node of the tree
    return second_largest_elem_bst(root.right)

if __name__ == "__main__":
    """
    1. Tree with largest node not having left subtree
         ( 20 )
        /      \
      (6)     (30)
     /  \     /   \
   (1)  (8) (25)  (35)

   2. Tree with largest node with left subtree
         ( 5 )
        /     \
      (3)     (8)
     /  \     /  \
   (1)  (4) (7)  (12)
                 /
               (10)
               /  \
             (9)  (11)
   """
    tree1 = Node(20, Node(6, Node(6, Node(1), Node(8))), Node(30, Node(),
                 Node(35)))

    tree2 = Node(5, Node(3, Node(1), Node(4)), Node(8, Node(7), Node(12,
                 Node(10, Node(9), Node(11)))))

    