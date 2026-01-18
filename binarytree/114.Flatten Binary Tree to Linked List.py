"""
===========================================================
114: Flatten Binary Tree to Linked List
===========================================================

Given a binary tree, flatten it to a linked list in-place.  
After flattening, all left pointers must be None and the right pointers 
form the preorder traversal linked list.
===========================================================
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        stack = [root]

        while stack:
            node = stack.pop()

            # Push right first, then left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            # Set left to None
            node.left = None

            # Set right to next node in preorder
            if stack:
                node.right = stack[-1]

# ---------------------------------------------------------
# Test Case
# ---------------------------------------------------------
if __name__ == "__main__":
    """
    Tree:
        1
       / \
      2   5
     / \   \
    3   4   6

    After flatten:
    1 - 2 - 3 - 4 - 5 - 6 (all left pointers None)
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    sol = Solution()
    sol.flatten(root)

    # Print flattened tree
    node = root
    result = []
    while node:
        result.append(node.val)
        node = node.right
    print("Flattened Tree:", result)
