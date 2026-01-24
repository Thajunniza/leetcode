"""
---------------------------------------------------------------------
653. Two Sum IV - Input is a BST
---------------------------------------------------------------------
Given a Binary Search Tree (BST) and a target integer k, determine if 
there exist **two elements** in the BST such that their sum is equal 
to k.

---------------------------------------------------------------------
EXAMPLE
---------------------------------------------------------------------
Input:
        5
       / \
      3   6
     / \
    2   4

k = 9

Output: True  # 3 + 6 = 9

---------------------------------------------------------------------
ALGORITHMS
---------------------------------------------------------------------
1. DFS + HashSet
   - Traverse the tree using DFS.
   - Keep a set of seen values.
   - For each node, check if k - node.val exists in set.
   - Time Complexity: O(n), Space Complexity: O(n)

2. Inorder + Two Pointers
   - Traverse BST inorder → get sorted array
   - Use two pointers to check if sum == k
   - Time Complexity: O(n), Space Complexity: O(n)

---------------------------------------------------------------------
NOTES
---------------------------------------------------------------------
- Solution 1 works for any binary tree, not necessarily BST.
- Solution 2 leverages BST property for sorted array.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # -----------------------------------------------------------------
    # Solution 1: DFS + HashSet
    # -----------------------------------------------------------------
    def findTarget_dfs(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)

    # -----------------------------------------------------------------
    # Solution 2: Inorder traversal + Two Pointers
    # -----------------------------------------------------------------
    def findTarget_inorder(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        inorder(root)

        l, r = 0, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                return True
            elif s < k:
                l += 1
            else:
                r -= 1
        return False


# -------------------------------------------------------------------
# TEST RUN
# -------------------------------------------------------------------
if __name__ == "__main__":
    """
    Construct BST:

            5
           / \
          3   6
         / \
        2   4
    """

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    k = 9

    solution = Solution()
    print("DFS + HashSet:", solution.findTarget_dfs(root, k))           # Expected: True
    print("Inorder + Two Pointers:", solution.findTarget_inorder(root, k))  # Expected: True

    # Another test
    k2 = 28
    print("DFS + HashSet:", solution.findTarget_dfs(root, k2))          # Expected: False
    print("Inorder + Two Pointers:", solution.findTarget_inorder(root, k2)) # Expected: False