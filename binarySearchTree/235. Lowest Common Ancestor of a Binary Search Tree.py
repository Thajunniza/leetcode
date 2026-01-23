"""
235. Lowest Common Ancestor of a Binary Search Tree

--------------------------------------------------
Problem:
Given a Binary Search Tree (BST), find the lowest common ancestor (LCA)
of two given nodes p and q in the BST.

The lowest common ancestor is defined as the lowest node in the tree
that has both p and q as descendants (where a node can be a descendant
of itself).

--------------------------------------------------
Example:
Input:
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5

p = 2, q = 8

Output:
6

--------------------------------------------------
Algorithm (Iterative – BST Property):
1. Start from the root.
2. If both p and q are smaller than root → move left.
3. If both p and q are greater than root → move right.
4. Otherwise, current root is the LCA.

Why this works:
- In a BST, left subtree values < root < right subtree values.
- The first node where p and q split (or match root) is the LCA.

--------------------------------------------------
Time Complexity:
O(H), where H is the height of the BST.

--------------------------------------------------
Space Complexity:
O(1) iterative (no recursion stack).

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

        curr = root

        while curr:
            # Both nodes lie in left subtree
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left

            # Both nodes lie in right subtree
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right

            # Split point found
            else:
                return curr

        return None


# --------------------------------------------------
# Helper functions for testing
# --------------------------------------------------
def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root


# --------------------------------------------------
# Test Run
# --------------------------------------------------
if __name__ == "__main__":
    # Build BST
    values = [6, 2, 8, 0, 4, 7, 9, 3, 5]
    root = None
    nodes = {}

    for v in values:
        root = insert_bst(root, v)
        nodes[v] = TreeNode(v)

    # Manually map nodes for testing
    def find(root, val):
        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root

    p = find(root, 2)
    q = find(root, 8)

    sol = Solution()
    lca = sol.lowestCommonAncestor(root, p, q)

    print("LCA of", p.val, "and", q.val, "is:", lca.val)
    # Expected Output: 6
