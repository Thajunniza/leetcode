"""
===========================================================
LeetCode 199: Binary Tree Right Side View
===========================================================

Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

BFS is most natural here (level-order).

i == n - 1 ensures we pick the rightmost node at each level.

Time Complexity: O(N)

Space Complexity: O(N) (queue)

Approach: BFS (Level Order Traversal)
===========================================================
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                # if last node in the current level, add to result
                if i == n - 1:
                    result.append(node.val)
                # enqueue children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

# ---------------------------------------------------------
# Test Case
# ---------------------------------------------------------
if __name__ == "__main__":
    """
    Tree Structure:
            1
           / \
          2   3
           \    \
            5    4
    Expected Right Side View: [1, 3, 4]
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    sol = Solution()
    print("Right Side View:", sol.rightSideView(root))
