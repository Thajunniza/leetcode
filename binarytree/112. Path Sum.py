"""
112. Path Sum

Problem:
--------
Given the root of a binary tree and an integer targetSum, return True if the tree
has a root-to-leaf path such that adding up all the values along the path equals
targetSum.

--------------------------------------------------
Approach 1: Recursive DFS
--------------------------------------------------
Algorithm:
1. If the current node is None, return False.
2. Subtract the current node's value from targetSum.
3. If the current node is a leaf (no left and right children),
   check if the remaining sum is 0.
4. Recursively check left and right subtrees.

Time Complexity: O(n)
Space Complexity: O(h)  (recursion stack, h = height of tree)

--------------------------------------------------
Approach 2: Iterative DFS (Using Stack)
--------------------------------------------------
Algorithm:
1. Use a stack to store (node, remaining_sum).
2. Start with (root, targetSum).
3. Pop elements from the stack:
   - Subtract node value from remaining_sum.
   - If node is a leaf and remaining_sum == 0, return True.
4. Push right and left children with updated remaining_sum.
5. If stack is empty and no path found, return False.

Time Complexity: O(n)
Space Complexity: O(n) in worst case
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # -------- Recursive Solution --------
    def hasPathSumRecursive(self, root, targetSum):
        if not root:
            return False

        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0

        return (self.hasPathSumRecursive(root.left, targetSum) or
                self.hasPathSumRecursive(root.right, targetSum))

    # -------- Iterative Solution --------
    def hasPathSumIterative(self, root, targetSum):
        if not root:
            return False

        stack = [(root, targetSum)]

        while stack:
            node, remain = stack.pop()
            remain -= node.val

            if not node.left and not node.right and remain == 0:
                return True

            if node.right:
                stack.append((node.right, remain))
            if node.left:
                stack.append((node.left, remain))

        return False


# -----------------------------
# Test Run
# -----------------------------
if __name__ == "__main__":
    """
    Tree:
            5
           / \
          4   8
         /   / \
        11  13  4
       /  \        \
      7    2        1

    Target Sum = 22
    Valid Path: 5 -> 4 -> 11 -> 2
    """

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    sol = Solution()

    print("Recursive Result:", sol.hasPathSumRecursive(root, 22))
    print("Iterative Result:", sol.hasPathSumIterative(root, 22))


"""
Expected Output:
Recursive Result: True
Iterative Result: True
"""

