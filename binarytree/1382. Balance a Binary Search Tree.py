"""
===========================================================
1382. Balance a Binary Search Tree
===========================================================

Problem:
--------
Given the root of a Binary Search Tree (BST),
return a height-balanced BST containing the same node values.

A BST is height-balanced if:
|height(left subtree) - height(right subtree)| <= 1
for every node.

Approach:
---------
1. Perform an inorder traversal of the BST to obtain
   a sorted list of values (BST property).
2. Construct a height-balanced BST from the sorted list
   using divide-and-conquer:
   - Choose the middle element as the root
   - Recursively build left and right subtrees

This guarantees minimum possible height.

Time Complexity:
----------------
O(n) — each node is visited once

Space Complexity:
-----------------
O(n) — array to store inorder traversal +
        recursion stack for balanced tree

Author:
-------
Thajunniza M A
"""

# -----------------------------
# Definition for a binary tree node
# -----------------------------
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -----------------------------
# Solution Class
# -----------------------------
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        # Step 1: Inorder traversal (iterative) to get sorted values
        def inorder(node):
            res = []
            stack = []
            curr = node
            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
            return res

        data = inorder(root)

        # Step 2: Build balanced BST from sorted values
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(data[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node

        return build(0, len(data) - 1)


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1:
    # Input: [1,null,2,null,3,null,4]
    # Output: Balanced BST
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)

    balanced_root = sol.balanceBST(root)
    print("Balanced BST root:", balanced_root.val)
