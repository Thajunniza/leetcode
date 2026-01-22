"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree (BST) and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Approach:
1. Recursive Inorder Traversal:
   - Inorder traversal of BST gives elements in sorted order.
   - Keep a counter to stop at kth element.
   - Time: O(H + k), Space: O(H) recursion stack

2. Iterative Inorder Traversal:
   - Use a stack to simulate recursion.
   - Traverse nodes in sorted order, count until k.
   - Time: O(H + k), Space: O(H)
"""

from typing import Optional

# ---------------- TreeNode Definition ----------------
class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

# ---------------- Recursive Solution ----------------
class RecursiveKthSmallest:
    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = -1

        def inorder(node: Optional[TreeNode]):
            if not node or self.count >= k:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.data
                return
            inorder(node.right)

        inorder(root)
        return self.result

# ---------------- Iterative Solution ----------------
class IterativeKthSmallest:
    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root or k <= 0:
            return -1

        stack = []
        curr = root
        count = 0

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.data
            curr = curr.right

        return -1  # k is larger than number of nodes

# ---------------- TEST RUN ----------------
if __name__ == "__main__":
    # Construct BST:
    #       3
    #      / \
    #     1   4
    #      \
    #       2
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    ks_recursive = RecursiveKthSmallest()
    ks_iterative = IterativeKthSmallest()

    print("===== Recursive Solution =====")
    for k in range(1, 6):
        print(f"k={k}: {ks_recursive.kth_smallest(root, k)}")

    print("\n===== Iterative Solution =====")
    for k in range(1, 6):
        print(f"k={k}: {ks_iterative.kth_smallest(root, k)}")
