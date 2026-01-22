"""
700. Search in a Binary Search Tree

Algorithm:
    - Start from the root node.
    - While the current node is not None:
        - If node.val == target, return the node.
        - If target < node.val, move to left subtree.
        - Else, move to right subtree.
    - If traversal ends without finding the value, return None.

Time Complexity:
    - O(h), where h is the height of the tree
        - O(log n) for balanced BST
        - O(n) for skewed BST

Space Complexity:
    - O(1) (iterative solution, no recursion stack)
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if node.val == val:
                return node
            elif val < node.val:
                node = node.left
            else:
                node = node.right
        return None


# --------------------- Test Run ---------------------
if __name__ == "__main__":
    # Construct BST
    #        4
    #       / \
    #      2   7
    #     / \
    #    1   3
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7)

    sol = Solution()

    # Test case 1
    result = sol.searchBST(root, 2)
    print("Search 2:", result.val if result else None)  # Expected: 2

    # Test case 2
    result = sol.searchBST(root, 5)
    print("Search 5:", result.val if result else None)  # Expected: None
