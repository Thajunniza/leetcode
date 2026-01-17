"""
===========================================================
Problem: 104. Maximum Depth of Binary Tree
===========================================================

Description:
Given the root of a binary tree, return its maximum depth.

The maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.

-----------------------------------------------------------
Example:
Input:  root = [3,9,20,None,None,15,7]
Output: 3

Input:  root = []
Output: 0

-----------------------------------------------------------
Algorithm (Depth First Search - Recursion):
1. If the current node is None, return 0.
2. Recursively compute the depth of the left subtree.
3. Recursively compute the depth of the right subtree.
4. Return 1 + max(left_depth, right_depth).

-----------------------------------------------------------
Time Complexity:
O(n)
- Each node is visited exactly once.

-----------------------------------------------------------
Space Complexity:
O(h)
- h is the height of the tree.
- Due to recursion call stack.
- Worst case (skewed tree): O(n)
- Best case (balanced tree): O(log n)
===========================================================
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),
                       self.maxDepth(root.right))
    
from collections import deque

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        depth = 0
        queue = deque([root])

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth



# ---------------------------------------------------------
# Helper Function to Build Tree from Level Order List
# ---------------------------------------------------------
def build_tree_from_list(values):
    """
    Builds a binary tree from a level-order list.
    None represents missing nodes.
    """
    if not values:
        return None

    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


# ---------------------------------------------------------
# Test Cases
# ---------------------------------------------------------
if __name__ == "__main__":

    sol = Solution()

    # Test Case 1
    # Tree: [3,9,20,None,None,15,7]
    root1 = build_tree_from_list([3, 9, 20, None, None, 15, 7])
    print("Test Case 1 Output:", sol.maxDepth(root1))  # Expected: 3

    # Test Case 2
    # Tree: [1]
    root2 = build_tree_from_list([1])
    print("Test Case 2 Output:", sol.maxDepth(root2))  # Expected: 1

    # Test Case 3
    # Tree: []
    root3 = build_tree_from_list([])
    print("Test Case 3 Output:", sol.maxDepth(root3))  # Expected: 0

    # Test Case 4 (Skewed Tree)
    # Tree: [1,2,None,3,None,4]
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    root4.left.left.left = TreeNode(4)
    print("Test Case 4 Output:", sol.maxDepth(root4))  # Expected: 4
