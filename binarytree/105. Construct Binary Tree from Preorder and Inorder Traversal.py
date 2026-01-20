"""
LeetCode 105 - Construct Binary Tree from Preorder and Inorder Traversal

Algorithm:
1. Preorder traversal gives the root first.
2. Inorder traversal tells us how to split left and right subtrees.
3. Use a hashmap to store inorder value -> index for O(1) lookup.
4. Maintain a global (or nonlocal) preorder index.
5. Recursively:
   - Pick root from preorder
   - Split inorder into left and right
   - Build left subtree first, then right subtree

Time Complexity:
O(n) — each node is processed once.

Space Complexity:
O(n) — hashmap + recursion stack.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        if not preorder or not inorder:
            return None

        # Build value -> index map for inorder traversal
        inorder_idx = {val: i for i, val in enumerate(inorder)}

        self.pre_idx = 0
        n = len(inorder)

        def build_subtree(left, right):
            if left > right:
                return None

            # Root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Split inorder
            mid = inorder_idx[root_val]

            # Build left then right
            root.left = build_subtree(left, mid - 1)
            root.right = build_subtree(mid + 1, right)

            return root

        return build_subtree(0, n - 1)


# -------------------- Test Code --------------------

def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    print(root.val, end=" ")
    print_inorder(root.right)


def print_preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    print_preorder(root.left)
    print_preorder(root.right)


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    sol = Solution()
    tree = sol.buildTree(preorder, inorder)

    print("Preorder of constructed tree:")
    print_preorder(tree)
    print("\nInorder of constructed tree:")
    print_inorder(tree)
