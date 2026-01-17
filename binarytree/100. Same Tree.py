"""
100: Same Tree

Problem:
---------
Given the roots of two binary trees p and q, write a function to check if they are the same.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example:
--------
Input: p = [1,2,3], q = [1,2,3]
Output: True

Input: p = [1,2], q = [1,None,2]
Output: False

Input: p = [1,2,1], q = [1,1,2]
Output: False

Algorithm:
----------
- Use recursion (DFS) to traverse both trees simultaneously
- Base cases:
    1. Both nodes are None → return True
    2. One node is None → return False
    3. Node values differ → return False
- Recurse on left and right subtrees
- Return True only if both left and right subtrees match

Time Complexity: O(n) where n is the number of nodes (visit each node once)
Space Complexity: O(h) recursion stack, h = height of tree
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

# Solution: Recursive DFS
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Both nodes are None
        if not p and not q:
            return True
        # One node is None
        if not p or not q:
            return False
        # Node values differ
        if p.val != q.val:
            return False
        # Recurse on left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# =======================
# Test Cases
# =======================
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1,2,3], [1,2,3], True),
        ([1,2], [1,None,2], False),
        ([1,2,1], [1,1,2], False),
        ([], [], True),
        ([1], [1], True),
        ([1], [], False)
    ]

    for i, (arr1, arr2, expected) in enumerate(tests, 1):
        p = array_to_bt(arr1)
        q = array_to_bt(arr2)
        result = sol.isSameTree(p, q)
        print(f"Test Case {i}: Result={result} | Expected={expected} | {'PASS' if result==expected else 'FAIL'}")
