"""
111: Minimum Depth of Binary Tree

Problem:
---------
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.

A leaf is a node with no left and no right child.

Example:
--------
Input: [3,9,20,None,None,15,7]

        3
       / \
      9  20
         / \
        15  7

Output: 2

Approach 1: BFS (Preferred )
------------------------------------------
- Traverse level by level using a queue
- Return immediately when the first leaf is found
- Guarantees shortest path

Time Complexity: O(n)
Space Complexity: O(n)

Approach 2: DFS (Recursive)
---------------------------
- Carefully handle nodes with only one child
- Cannot directly use min(left, right) blindly

Time Complexity: O(n)
Space Complexity: O(h) where h is tree height
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper: Convert array (level-order) to binary tree
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

class Solution(object):

    # =======================
    # BFS Solution (Best)
    # =======================
    def minDepth_BFS(self, root):
        if not root:
            return 0

        q = deque([(root, 1)])

        while q:
            node, depth = q.popleft()

            # First leaf reached
            if not node.left and not node.right:
                return depth

            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

    # =======================
    # DFS Solution (Recursive)
    # =======================
    def minDepth_DFS(self, root):
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            if not node.left:
                return 1 + dfs(node.right)
            if not node.right:
                return 1 + dfs(node.left)
            return 1 + min(dfs(node.left), dfs(node.right))
        return dfs(root)

# =======================
# Test Cases
# =======================
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([3,9,20,None,None,15,7], 2),
        ([2,None,3,None,4,None,5,None,6], 5),
        ([1], 1),
        ([], 0),
        ([1,2], 2)
    ]

    for i, (arr, expected) in enumerate(tests, 1):
        root = array_to_bt(arr)
        bfs_result = sol.minDepth_BFS(root)
        dfs_result = sol.minDepth_DFS(root)
        print(
            f"Test {i}: BFS={bfs_result}, DFS={dfs_result}, "
            f"Expected={expected} | PASS"
            if bfs_result == dfs_result == expected else "FAIL"
        )
