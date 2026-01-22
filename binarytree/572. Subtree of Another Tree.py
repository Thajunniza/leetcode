"""
572. Subtree of Another Tree

Problem:
Given the roots of two binary trees root and subRoot, return True if there is a subtree of root
with the same structure and node values as subRoot, and False otherwise.

A subtree of a binary tree is a tree that consists of a node in tree and all of this node's descendants.
The tree root could also be considered as a subtree of itself.

--------------------------------------------------
Algorithm:
1. Traverse the main tree using DFS.
2. At each node, check if the subtree rooted at this node is identical to subRoot.
3. Use a helper function (isSame) to compare two trees for structural and value equality.
4. If a match is found, return True.
5. Otherwise, continue DFS on left and right subtrees.

--------------------------------------------------
Time Complexity:
O(N * M) in the worst case,
where N = number of nodes in root,
and M = number of nodes in subRoot.

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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return (
                isSame(node1.left, node2.left) and
                isSame(node1.right, node2.right)
            )

        if not subRoot:
            return True
        if not root:
            return False

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False

            if isSame(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)


# ---------------------------
# Example Test Run
# ---------------------------
if __name__ == "__main__":
    # Tree: root = [3,4,5,1,2]
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    # Tree: subRoot = [4,1,2]
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    sol = Solution()
    print(sol.isSubtree(root, subRoot))  # Expected output: True
