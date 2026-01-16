"""
===========================================================
543: Diameter of Binary Tree
===========================================================

Problem:
The diameter of a binary tree is the length of the longest path
between any two nodes in a tree. This path may or may not pass
through the root.

The length of a path is defined as the number of edges between nodes.

Approach:
- Use Depth First Search (DFS)
- At each node:
    - Compute left subtree height
    - Compute right subtree height
    - Update diameter as (left_height + right_height)
- Return height to parent

Key Insight:
- Height is returned upward
- Diameter is tracked as shared state

Time Complexity:
- O(n), where n is the number of nodes

Space Complexity:
- O(h), recursion stack where h is tree height
===========================================================
"""

from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            # Update diameter at this node
            self.diameter = max(self.diameter, left + right)

            # Return height
            return 1 + max(left, right)

        height(root)
        return self.diameter


# ----------------------------------------------------------
# Helper function to build tree from level-order list
# ----------------------------------------------------------
def build_tree(level):
    if not level or level[0] is None:
        return None

    root = TreeNode(level[0])
    q = deque([root])
    i = 1

    while q and i < len(level):
        node = q.popleft()

        if i < len(level) and level[i] is not None:
            node.left = TreeNode(level[i])
            q.append(node.left)
        i += 1

        if i < len(level) and level[i] is not None:
            node.right = TreeNode(level[i])
            q.append(node.right)
        i += 1

    return root


# ----------------------------------------------------------
# Test Cases
# ----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    root1 = build_tree([1, 2, 3, 4, 5])
    print("Diameter:", sol.diameterOfBinaryTree(root1))  # Expected: 3

    sol = Solution()
    root2 = build_tree([1, 2])
    print("Diameter:", sol.diameterOfBinaryTree(root2))  # Expected: 1

    sol = Solution()
    root3 = build_tree([1])
    print("Diameter:", sol.diameterOfBinaryTree(root3))  # Expected: 0

    sol = Solution()
    root4 = build_tree([])
    print("Diameter:", sol.diameterOfBinaryTree(root4))  # Expected: 0
