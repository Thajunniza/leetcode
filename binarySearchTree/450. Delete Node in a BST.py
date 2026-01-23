"""
450. Delete Node in a BST

--------------------------------------------------
Problem:
Given a root node reference of a Binary Search Tree (BST) and a key,
delete the node with the given key in the BST. Return the root node
reference (possibly updated) of the BST.

Deletion rules:
1. If the node is a leaf, remove it.
2. If the node has one child, replace it with its child.
3. If the node has two children:
   - Find the inorder successor (smallest value in the right subtree)
   - Replace the node’s value with the successor’s value
   - Delete the successor node from the right subtree

--------------------------------------------------
Example:
Input:
    root = [5,3,6,2,4,null,7], key = 3

Output:
    [5,4,6,2,null,null,7]

--------------------------------------------------
Algorithm:
1. Traverse the BST recursively to locate the node with the given key.
2. If key < root.val → recurse left.
3. If key > root.val → recurse right.
4. If key == root.val:
   - Case 1: No children → return None
   - Case 2: One child → return the non-null child
   - Case 3: Two children →
       a. Find inorder successor (minimum value in right subtree)
       b. Replace root.val with successor value
       c. Delete successor from right subtree
5. Return the updated root.

--------------------------------------------------
Time Complexity:
O(H), where H is the height of the BST.

--------------------------------------------------
Space Complexity:
O(H) due to recursion stack.

--------------------------------------------------
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Case 1 & 2: node has at most one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Case 3: node has two children
            # Find inorder successor (min in right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left

            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)

        return root


# --------------------------------------------------
# Helper functions for testing
# --------------------------------------------------
def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root


def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


# --------------------------------------------------
# Test Run
# --------------------------------------------------
if __name__ == "__main__":
    # Build BST: [5,3,6,2,4,7]
    values = [5, 3, 6, 2, 4, 7]
    root = None
    for v in values:
        root = insert_bst(root, v)

    print("Inorder before deletion:")
    print(inorder_traversal(root))  # Expected: [2,3,4,5,6,7]

    sol = Solution()
    root = sol.deleteNode(root, 3)

    print("Inorder after deleting 3:")
    print(inorder_traversal(root))  # Expected: [2,4,5,6,7]
