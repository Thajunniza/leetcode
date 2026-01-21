"""
98.Validate Binary Search Tree

Algorithm:
-----------
We validate the Binary Search Tree (BST) property using
Breadth-First Search (BFS) with value bounds.

For every node:
- Its value must be strictly greater than all values in its left subtree
- Its value must be strictly less than all values in its right subtree

To enforce this globally (not just parent-child),
each node carries an allowed range:
    (min_allowed, max_allowed)

Approach:
---------
1. Use a queue for BFS
2. Start with the root having range (-inf, +inf)
3. For each node:
   - If node.val is outside the allowed range → invalid BST
   - Left child gets range (low, node.val)
   - Right child gets range (node.val, high)
4. If all nodes satisfy constraints, return True

Example:
--------
Tree:
        5
       / \
      1   7
         /
        4   ❌

Why invalid?
- 4 is in the right subtree of 5 but 4 < 5

Output: False

Time Complexity:
----------------
O(n)
- Each node is visited once

Space Complexity:
-----------------
O(n)
- Queue can hold up to n nodes in worst case

"""

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque()
        q.append((root, float("-inf"), float("inf")))

        while q:
            node, low, high = q.popleft()

            if node.val <= low or node.val >= high:
                return False

            if node.left:
                q.append((node.left, low, node.val))
            if node.right:
                q.append((node.right, node.val, high))

        return True


# -------------------
# Test Run
# -------------------
if __name__ == "__main__":
    sol = Solution()

    # Valid BST
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    print(sol.isValidBST(root1))  # Expected: True

    # Invalid BST
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(7)
    root2.right.left = TreeNode(4)
    print(sol.isValidBST(root2))  # Expected: False

    # Single node
    root3 = TreeNode(1)
    print(sol.isValidBST(root3))  # Expected: True

    # Duplicate value (invalid in LeetCode BST)
    root4 = TreeNode(2)
    root4.left = TreeNode(2)
    print(sol.isValidBST(root4))  # Expected: False
