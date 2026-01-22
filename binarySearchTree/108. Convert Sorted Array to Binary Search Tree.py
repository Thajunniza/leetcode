"""
108: Convert Sorted Array to Binary Search Tree (BST)

Problem:
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced BST.

A height-balanced BST is a binary tree in which the depth of the two subtrees of 
every node never differs by more than one.

Examples:
1. Input: nums = [-10, -3, 0, 5, 9]
   Output: Height-balanced BST
   Inorder Traversal: [-10, -3, 0, 5, 9]

2. Input: nums = [1, 3]
   Output: Height-balanced BST
   Inorder Traversal: [1, 3]
"""

from typing import List, Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ---------------- Recursive Solution ----------------
class RecursiveSolution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Recursive approach:
        - Pick mid element as root
        - Recursively build left and right subtrees
        Time: O(n)
        Space: O(log n) recursion stack
        """
        def build(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node
        
        return build(0, len(nums) - 1)

# ---------------- Iterative Solution ----------------
class IterativeSolution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Iterative approach:
        - Use a queue to simulate recursion
        - Each queue element: (node_to_fill, left_index, right_index)
        Time: O(n)
        Space: O(n)
        """
        if not nums:
            return None
        
        root = TreeNode(0)  # placeholder
        q = deque()
        q.append((root, 0, len(nums) - 1))

        while q:
            node, l, r = q.popleft()
            mid = (l + r) // 2
            node.val = nums[mid]

            # left child
            if l <= mid - 1:
                node.left = TreeNode(0)
                q.append((node.left, l, mid - 1))

            # right child
            if mid + 1 <= r:
                node.right = TreeNode(0)
                q.append((node.right, mid + 1, r))

        return root

# ---------------- Helper Function ----------------
def inorder(node: Optional[TreeNode]) -> List[int]:
    """
    Returns inorder traversal of BST
    """
    return inorder(node.left) + [node.val] + inorder(node.right) if node else []

# ---------------- TEST RUN ----------------
if __name__ == "__main__":
    examples = [
        [-10, -3, 0, 5, 9],
        [1, 3],
        [0, 1, 2, 3, 4, 5, 6]
    ]

    print("===== Recursive Solution =====")
    rec_sol = RecursiveSolution()
    for nums in examples:
        bst_root = rec_sol.sortedArrayToBST(nums)
        print(f"Input: {nums}")
        print(f"Inorder Traversal: {inorder(bst_root)}\n")

    print("===== Iterative Solution =====")
    iter_sol = IterativeSolution()
    for nums in examples:
        bst_root = iter_sol.sortedArrayToBST(nums)
        print(f"Input: {nums}")
        print(f"Inorder Traversal: {inorder(bst_root)}\n")
