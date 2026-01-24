"""
---------------------------------------------------------------------
285. Inorder Successor in BST
---------------------------------------------------------------------
Given a Binary Search Tree (BST) and a node p in it, find the inorder
successor of that node.

The inorder successor of a node p is the node with the smallest key
greater than p.val.

If such a node does not exist, return None.

---------------------------------------------------------------------
EXAMPLE
---------------------------------------------------------------------
Input:
        20
       /  \
     10    30
       \
        15

p = 15

Inorder Traversal:
10 → 15 → 20 → 30

Output:
20

---------------------------------------------------------------------
ALGORITHM (OPTIMAL BST APPROACH)
---------------------------------------------------------------------
1. Start traversing from the root.
2. If p.val < current node value:
     - Current node is a potential successor.
     - Move left to find a smaller valid successor.
3. Else:
     - Move right (successor cannot be in the left subtree).
4. Continue until traversal ends.
5. Return the stored successor.

---------------------------------------------------------------------
TIME & SPACE COMPLEXITY
---------------------------------------------------------------------
Time Complexity  : O(h), where h is the height of the tree
Space Complexity : O(1)

---------------------------------------------------------------------
NOTES
---------------------------------------------------------------------
• This solution leverages the BST ordering property.
• No inorder traversal or extra storage is used.
• This is the preferred interview solution.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        curr = root

        while curr:
            if p.val < curr.val:
                successor = curr
                curr = curr.left
            else:
                curr = curr.right

        return successor


# -------------------------------------------------------------------
# TEST RUN
# -------------------------------------------------------------------
if __name__ == "__main__":
    """
    Construct the following BST:

            20
           /  \
         10    30
           \
            15
              \
               17
    """

    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(30)
    root.left.right = TreeNode(15)
    root.left.right.right = TreeNode(17)

    p = root.left.right  # Node with value 15

    solution = Solution()
    successor = solution.inorderSuccessor(root, p)

    if successor:
        print(f"Inorder successor of {p.val} is {successor.val}")
    else:
        print(f"Inorder successor of {p.val} does not exist")