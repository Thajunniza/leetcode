"""
701. Insert into a Binary Search Tree

You are given the root node of a binary search tree (BST) and a value to insert into the tree.
Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist in the original BST.
Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.


Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Algorithm:
    - If the root is None, return a new node with the given value.
    - Otherwise, start from the root and iteratively traverse:
        - If val < current node value, move to the left subtree.
        - Else, move to the right subtree.
    - When a None child is found, insert the new node there.
    - Return the original root.

Time Complexity:
    - O(h), where h is the height of the BST
        - O(log n) for a balanced BST
        - O(n) for a skewed BST

Space Complexity:
    - O(1) (iterative approach, no recursion stack)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)

        if not root:
            return new_node

        node = root
        while True:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = new_node
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = new_node
                    break

        return root


# --------------------- Test Run ---------------------
if __name__ == "__main__":
    # Construct initial BST
    #        4
    #       / \
    #      2   7
    #     / \
    #    1   3
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7)

    sol = Solution()

    # Insert value
    root = sol.insertIntoBST(root, 5)

    # Inorder traversal to verify BST property
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    print("Inorder traversal after insertion:", inorder(root))
    # Expected output: [1, 2, 3, 4, 5, 7]
