"""
===========================================================
110. Balanced Binary Tree – Test Suite
===========================================================

Problem:
--------
Check if a binary tree is height-balanced.
A binary tree is balanced if for every node, the height
difference between its left and right subtrees is at most 1.

Time Complexity: O(n) – each node visited once
Space Complexity: O(h) – recursion stack, h = tree height


Algorithm:
-------
1. write a recursive function to find the height of left and right node
2. if left tree or right tree is not balanced retur -1
3. if balance is check by abs(left-right) > 1
4. heigh 1 + max(left,right)

Author:
-------
Thajunniza M A
"""

# -----------------------------
# TreeNode Class
# -----------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------
# Build Tree from Level-Order List
# -----------------------------
from collections import deque
def build_tree(level):
    if not level or level[0] is None:
        return None
    root = TreeNode(level[0])
    q = deque([root])
    i = 1
    while q and i < len(level):
        node = q.popleft()
        # Left child
        if i < len(level) and level[i] is not None:
            node.left = TreeNode(level[i])
            q.append(node.left)
        i += 1
        # Right child
        if i < len(level) and level[i] is not None:
            node.right = TreeNode(level[i])
            q.append(node.right)
        i += 1
    return root

# -----------------------------
# Solution Class
# -----------------------------
class Solution:
    def isBalanced(self, root):
        """
        Returns True if tree is height-balanced, else False.
        """
        def dfs(node):
            if not node:
                return 0
            left_height = dfs(node.left)
            if left_height == -1:
                return -1
            right_height = dfs(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)
        return dfs(root) != -1

# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Balanced tree
    root1 = build_tree([3,9,20,None,None,15,7])
    print("Test Case 1: Balanced Tree")
    print("Is Balanced:", sol.isBalanced(root1))  # Expected: True
    print()

    # Test Case 2: Unbalanced tree
    root2 = build_tree([1,2,2,3,3,None,None,4,4])
    print("Test Case 2: Unbalanced Tree")
    print("Is Balanced:", sol.isBalanced(root2))  # Expected: False
    print()

    # Test Case 3: Empty tree
    root3 = build_tree([])
    print("Test Case 3: Empty Tree")
    print("Is Balanced:", sol.isBalanced(root3))  # Expected: True
    print()

    # Test Case 4: Single node tree
    root4 = build_tree([1])
    print("Test Case 4: Single Node Tree")
    print("Is Balanced:", sol.isBalanced(root4))  # Expected: True
