"""
124: Maximum Path Sum in Binary Tree

Problem:
---------
Given a non-empty binary tree, find the maximum path sum.
A path is any sequence of nodes from any node to any node along the parent-child connections.
The path must contain at least one node.

Example:
--------
Input: [-10, 9, 20, None, None, 15, 7]
       -10
       / \
      9  20
         / \
        15  7
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7, sum = 42

Algorithm:
----------
- Use DFS (post-order) to traverse the tree.
- For each node, calculate:
    - left_gain = max gain from left child (ignore negatives)
    - right_gain = max gain from right child (ignore negatives)
    - current_path_sum = node.val + left_gain + right_gain
- Track the maximum path sum globally using a mutable container (arr[0]).
- Return node.val + max(left_gain, right_gain) to parent (path cannot fork upwards).

Time Complexity: O(n), each node visited once
Space Complexity: O(h), recursion stack where h = tree height
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper to convert array (level-order) to binary tree
def array_to_bt(arr):
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

# Solution for Maximum Path Sum
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0  # handle empty tree

        arr = [root.val]  # global max container

        def dfs(node):
            if not node:
                return 0

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            current_path_sum = node.val + left_gain + right_gain
            arr[0] = max(arr[0], current_path_sum)

            return node.val + max(left_gain, right_gain)

        dfs(root)
        return arr[0]

# Optional helper to print tree level-order (for debugging)
def print_tree(root):
    if not root:
        print([])
        return
    q = deque([root])
    res = []
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    # Trim trailing None
    while res and res[-1] is None:
        res.pop()
    print(res)

# =======================
# Test Cases
# =======================
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    arr1 = [-10, 9, 20, None, None, 15, 7]
    root1 = array_to_bt(arr1)
    print("Tree 1 level-order:")
    print_tree(root1)
    print("Max Path Sum:", sol.maxPathSum(root1))  # Expected: 42

    # Test Case 2
    arr2 = [1, 2, 3]
    root2 = array_to_bt(arr2)
    print("\nTree 2 level-order:")
    print_tree(root2)
    print("Max Path Sum:", sol.maxPathSum(root2))  # Expected: 6

    # Test Case 3: Single node negative
    arr3 = [-3]
    root3 = array_to_bt(arr3)
    print("\nTree 3 level-order:")
    print_tree(root3)
    print("Max Path Sum:", sol.maxPathSum(root3))  # Expected: -3

    # Test Case 4: Complex tree with negative nodes
    arr4 = [2, -1, -2, 3, None, -5, 4]
    root4 = array_to_bt(arr4)
    print("\nTree 4 level-order:")
    print_tree(root4)
    print("Max Path Sum:", sol.maxPathSum(root4))  # Expected: 7 (3 + -1 + 2 + 3?)

