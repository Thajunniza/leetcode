"""
236. Lowest Common Ancestor of a Binary Tree

--------------------------------------------------
Problem:
Given a binary tree, find the lowest common ancestor (LCA) of two given
nodes p and q.

The lowest common ancestor is defined as the lowest node in the tree
that has both p and q as descendants (a node can be a descendant of itself).

NOTE:
Unlike BST, this is a general binary tree with no ordering property.

--------------------------------------------------
Example:
Input:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

p = 5, q = 1

Output:
3

--------------------------------------------------
Algorithm (Postorder DFS):
1. If current node is None → return None
2. If current node is p or q → return current node
3. Recurse left and right
4. If both left and right return non-null:
      → current node is the LCA
5. Else:
      → return the non-null child

Why this works:
- Postorder ensures children are processed before parent
- The first node where p and q split is the LCA

--------------------------------------------------
Time Complexity:
O(N), where N is the number of nodes in the tree.

--------------------------------------------------
Space Complexity:
O(H), where H is the height of the tree (recursion stack).

--------------------------------------------------
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self,
        root: Optional[TreeNode],
        p: TreeNode,
        q: TreeNode
    ) -> Optional[TreeNode]:

        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right


# --------------------------------------------------
# Test Run
# --------------------------------------------------
if __name__ == "__main__":
    # Build the tree
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)

    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    p = root.left            # Node 5
    q = root.right           # Node 1

    sol = Solution()
    lca = sol.lowestCommonAncestor(root, p, q)

    print("LCA of", p.val, "and", q.val, "is:", lca.val)
    # Expected Output: 3
