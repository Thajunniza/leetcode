"""
106 - Construct Binary Tree from Inorder and Postorder Traversal

Algorithm:
1. Postorder traversal gives root last.
2. Inorder traversal tells us how to split left and right subtrees.
3. Use a hashmap for O(1) lookup of inorder indices.
4. Maintain a postorder index starting from the end.
5. Recursively:
   - Pick root from postorder
   - Split inorder into left and right
   - Build RIGHT subtree first, then LEFT subtree (important!)
   
Time Complexity: O(n)
Space Complexity: O(n)
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder:
            return None

        # Map value -> index for inorder
        inorder_idx = {val: i for i, val in enumerate(inorder)}

        # Start from the end of postorder
        self.post_idx = len(postorder) - 1

        def build_subtree(left, right):
            if left > right:
                return None

            # Root is the current postorder element
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)

            # Split inorder
            mid = inorder_idx[root_val]

            # Build RIGHT subtree first, then LEFT
            root.right = build_subtree(mid + 1, right)
            root.left = build_subtree(left, mid - 1)

            return root

        return build_subtree(0, len(inorder) - 1)


# -------------------- Test Code --------------------

def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    print(root.val, end=" ")
    print_inorder(root.right)


def print_postorder(root):
    if not root:
        return
    print_postorder(root.left)
    print_postorder(root.right)
    print(root.val, end=" ")


if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    sol = Solution()
    tree = sol.buildTree(inorder, postorder)

    print("Inorder of constructed tree:")
    print_inorder(tree)
    print("\nPostorder of constructed tree:")
    print_postorder(tree)
