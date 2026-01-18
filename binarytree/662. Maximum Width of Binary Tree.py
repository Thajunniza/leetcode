# ============================================================
# LeetCode 662: Maximum Width of Binary Tree
# ============================================================

# ------------------------------------------------------------
# Problem Summary
# ------------------------------------------------------------
# The width of a binary tree at a given level is the number of
# nodes between the leftmost and rightmost non-null nodes,
# including the null nodes in between.
#
# We must return the maximum width among all levels.
#
# Key idea:
# Simulate node positions using array-style indexing.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Binary Tree Node Definition
# ------------------------------------------------------------
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------------
# Solution Using BFS with Indexing
# ------------------------------------------------------------
from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        max_width = 0

        # Queue stores (node, index)
        queue = deque([(root, 0)])

        while queue:
            level_length = len(queue)
            _, level_start_index = queue[0]

            for i in range(level_length):
                node, index = queue.popleft()

                # Normalize index to prevent overflow
                index -= level_start_index

                # Add children with calculated indices
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))

                # If last node in the level, update width
                if i == level_length - 1:
                    max_width = max(max_width, index + 1)

        return max_width


# ------------------------------------------------------------
# Test Case
# ------------------------------------------------------------
# Input Tree:
#
#         1
#        / \
#       3   2
#      / \   \
#     5   3   9
#
# Expected Output: 4
# ------------------------------------------------------------

if __name__ == "__main__":
    # Build the test tree
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)

    # Run solution
    sol = Solution()
    result = sol.widthOfBinaryTree(root)

    # Output result
    print("Maximum Width of Binary Tree:", result)
