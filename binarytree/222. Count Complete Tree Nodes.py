"""
222: Count Nodes in a Complete Binary Tree


------------------------------------------------------------
Problem Statement:
------------------------------------------------------------
Given the root of a **complete binary tree**, return the number of nodes
in the tree. A complete binary tree is a binary tree in which every level,
except possibly the last, is completely filled, and all nodes are as far
left as possible.

------------------------------------------------------------
Example:
------------------------------------------------------------
Input:
       1
      / \
     2   3
    / \
   4   5

Output: 5
Explanation: There are 5 nodes in the tree.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """Count nodes in a complete binary tree using O((log n)^2) approach."""
        if not root:
            return 0

        # Compute leftmost path height
        def leftHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        # Compute rightmost path height
        def rightHeight(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        h_left = leftHeight(root)
        h_right = rightHeight(root)

        if h_left == h_right:
            # Perfect binary tree: nodes = 2^h - 1
            return (1 << h_left) - 1

        # Recurse on left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------
def run_tests():
    solution = Solution()

    # Test case 1
    # Tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)
    print("Test 1:", solution.countNodes(root))  # Expected: 5

    # Test case 2: Empty tree
    root = None
    print("Test 2:", solution.countNodes(root))  # Expected: 0

    # Test case 3: Single node
    root = TreeNode(10)
    print("Test 3:", solution.countNodes(root))  # Expected: 1

    # Test case 4: Perfect tree
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, TreeNode(6), TreeNode(7))
    print("Test 4:", solution.countNodes(root))  # Expected: 7


if __name__ == "__main__":
    run_tests()

"""
------------------------------------------------------------
Time Complexity:
------------------------------------------------------------
O((log n)^2) — height computation is O(log n) at each recursion step.

------------------------------------------------------------
Space Complexity:
------------------------------------------------------------
O(log n) — recursion stack for a tree of height h.

------------------------------------------------------------
Why This Is Optimal:
------------------------------------------------------------
- Exploits the complete binary tree property to avoid visiting all nodes.
- Much faster than O(n) for large complete trees.
"""