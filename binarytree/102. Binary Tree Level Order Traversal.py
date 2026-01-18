"""
LeetCode 102: Binary Tree Level Order Traversal

Problem:
---------
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

Example:
--------
Input: [3,9,20,None,None,15,7]

        3
       / \
      9  20
         / \
        15  7

Output: [[3],[9,20],[15,7]]

Approach:
---------
- Use BFS (queue) to traverse the tree level by level.
- For each level, store all node values in a list and append to result.
- Continue until the queue is empty.

Time Complexity: O(n) — visit each node once
Space Complexity: O(n) — queue + result storage
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result

        queue = deque([root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

# =======================
# Example Test Case
# =======================
if __name__ == "__main__":
    # Helper: build tree from level-order array
    def array_to_bt(arr):
        if not arr or arr[0] is None:
            return None
        root = TreeNode(arr[0])
        q = deque([root])
        i = 1
        while q and i < len(arr):
            node = q.popleft()
            if i < len(arr) and arr[i] is not None:
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1
            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1
        return root

    arr = [3,9,20,None,None,15,7]
    root = array_to_bt(arr)
    sol = Solution()
    print(sol.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]
