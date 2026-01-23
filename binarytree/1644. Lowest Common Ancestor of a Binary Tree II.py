"""
Lowest Common Ancestor of a Binary Tree (Unified Solution)
------------------------------------------------------------------
Given a binary tree and two nodes p and q, find their lowest common ancestor (LCA).

- For Problem 236: Both nodes p and q are guaranteed to exist in the tree.
- For Problem 1644: Either node may be missing; return None if either does not exist.

Example 1:
    Tree:       3
               / \
              5   1
             / \ / \
            6  2 0  8
    p = 5, q = 1
    Output: 3

Example 2:
    Tree:       3
               / \
              5   1
             / \
            6   2
    p = 5, q = 4 (4 not in tree)
    Output: None

Algorithm:
------------
- Use a post-order DFS.
- Track whether p and q are found using flags.
- Return node as LCA if:
    - It is equal to p or q, or
    - Left and right subtrees contain p and q.
- At the end, check flags: return LCA only if both nodes exist.

Time Complexity: O(N)  - visit every node once
Space Complexity: O(H) - recursion stack (H = height of tree)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.is_p = False
        self.is_q = False

        def dfs(node):
            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            if node == p:
                self.is_p = True
                return node

            if node == q:
                self.is_q = True
                return node

            if left and right:
                return node
            if left:
                return left
            if right:
                return right
            return None

        node = dfs(root)
        return node if self.is_p and self.is_q else None


# ----------------- Test Run -----------------
if __name__ == "__main__":
    # Build Tree Example 1
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    p = root.left         # 5
    q = root.right        # 1

    sol = Solution()
    lca = sol.lowestCommonAncestor(root, p, q)
    print("LCA of 5 and 1:", lca.val if lca else None)  # Expected: 3

    # Example 2: q not in tree
    q2 = TreeNode(4)
    lca2 = sol.lowestCommonAncestor(root, p, q2)
    print("LCA of 5 and 4:", lca2.val if lca2 else None)  # Expected: None
