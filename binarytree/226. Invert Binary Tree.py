"""
===========================================================
226. Invert Binary Tree
===========================================================

Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Algorithm:
-----------
Mirror (invert) a binary tree using recursion.

1. If the current node is None, return None.
2. Recursively mirror the left subtree.
3. Recursively mirror the right subtree.
4. Swap the left and right children of the current node.
5. Return the current node.

This ensures every subtree is inverted from the leaves up to the root.

Complexity:
-----------
Time Complexity: O(n)
    - Each node is visited exactly once.

Space Complexity: O(h)
    - h is the height of the tree (recursion stack).
    - Worst case: O(n) for a skewed tree.
    - Best case: O(log n) for a balanced tree.
"""


# Definition of a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def mirror_binary_tree(root):
    """
    Recursively mirrors (inverts) a binary tree.
    """
    if not root:
        return None

    # Recursively mirror left and right subtrees
    left = mirror_binary_tree(root.left)
    right = mirror_binary_tree(root.right)

    # Swap children
    root.left, root.right = right, left

    return root


# -------------------------
# Test Case
# -------------------------
def inorder_traversal(root):
    if not root:
        return []
    return (
        inorder_traversal(root.left)
        + [root.data]
        + inorder_traversal(root.right)
    )


if __name__ == "__main__":
    # Construct the binary tree
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print("Inorder before mirror:", inorder_traversal(root))

    mirror_binary_tree(root)

    print("Inorder after mirror :", inorder_traversal(root))
