
"""
654 - Maximum Binary Tree Construction
--------------------------------

This module provides two implementations to construct the Maximum Binary Tree
from an input array `nums` (all elements distinct):

1) Divide-and-Conquer (O(n^2) worst-case):
   - Recursively find the maximum in the current range and build subtrees.
   - Closely matches the problem's definition.

2) Monotonic Stack (O(n) time):
   - Uses a decreasing stack to attach nodes as left/right children in one pass.
   - Recommended for large inputs to avoid quadratic behavior and deep recursion.

Includes:
- `TreeNode` definition.
- `Solution` class exposing `constructMaximumBinaryTree` (divide-and-conquer)
  and `constructMaximumBinaryTreeStack` (monotonic stack, optimal).
- Simple test cases and a pretty printer for visual verification when run as a script.

Usage:
    python maximum_binary_tree.py

"""
from __future__ import annotations
from typing import Optional, List, Tuple
import sys


class TreeNode(object):
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode(val={self.val})"


class Solution(object):
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        O(n^2) divide-and-conquer construction that follows the definition:
        - Root is the maximum of nums
        - Left subtree is constructed from elements left of the maximum
        - Right subtree is constructed from elements right of the maximum
        """
        if not nums:
            return None

        def find_max(lo: int, hi: int) -> int:
            max_idx = lo
            i = lo
            while i <= hi:
                if nums[max_idx] < nums[i]:
                    max_idx = i
                i += 1
            return max_idx

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            max_idx = find_max(lo, hi)
            root = TreeNode(nums[max_idx])
            root.left = build(lo, max_idx - 1)
            root.right = build(max_idx + 1, hi)
            return root

        return build(0, len(nums) - 1)

    def constructMaximumBinaryTreeStack(self, nums: List[int]) -> Optional[TreeNode]:
        """
        O(n) monotonic stack construction:
        - Maintain a decreasing stack of nodes.
        - For each value x, pop smaller nodes; the last popped becomes x's left child.
        - If stack not empty after popping, x becomes the right child of the new stack top.
        - The bottom of the stack is the root.
        """
        stack: List[TreeNode] = []
        for x in nums:
            curr = TreeNode(x)
            last_popped = None
            while stack and stack[-1].val < x:
                last_popped = stack.pop()
            curr.left = last_popped
            if stack:
                stack[-1].right = curr
            stack.append(curr)
        return stack[0] if stack else None


# ---------- Utilities for testing and visualization ----------

def inorder(node: Optional[TreeNode]) -> List[int]:
    return inorder(node.left) + [node.val] + inorder(node.right) if node else []


def preorder(node: Optional[TreeNode]) -> List[int]:
    return [node.val] + preorder(node.left) + preorder(node.right) if node else []


def pretty_print(root: Optional[TreeNode]) -> None:
    """Print the tree sideways (root at left)."""
    def _lines(node: Optional[TreeNode]) -> Tuple[List[str], int, int, int]:
        if node is None:
            return [""], 0, 0, 0
        line = str(node.val)
        left_lines, left_pos, left_width, left_height = _lines(node.left)
        right_lines, right_pos, right_width, right_height = _lines(node.right)
        first_line = (" " * (left_pos + 1)) + ("_" * (left_width - left_pos - 1)) + line + ("_" * right_pos) + (" " * (right_width - right_pos))
        second_line = (" " * left_pos) + ("/") + (" " * (left_width - left_pos - 1 + len(line) + right_pos)) + ("\\") + (" " * (right_width - right_pos - 1))
        if left_height < right_height:
            left_lines += [" " * left_width] * (right_height - left_height)
        elif right_height < left_height:
            right_lines += [" " * right_width] * (left_height - right_height)
        zipped_lines = zip(left_lines, right_lines)
        lines = [first_line, second_line] + [l + (" " * len(line)) + r for l, r in zipped_lines]
        return lines, left_width + len(line) + right_width, left_width, max(left_height, right_height) + 2

    lines, *_ = _lines(root)
    for ln in lines:
        print(ln.rstrip())


def _run_tests():
    cases = [
        [3, 2, 1, 6, 0, 5],
        [3, 9, 20, 15, 7],
        [1],
        [1, 2, 3, 4, 5],  # increasing -> right-skewed
        [5, 4, 3, 2, 1],  # decreasing -> left-skewed
    ]

    sol = Solution()

    for idx, nums in enumerate(cases, 1):
        print("\n=== Test Case {}: nums = {} ===".format(idx, nums))
        root_dc = sol.constructMaximumBinaryTree(nums)
        root_st = sol.constructMaximumBinaryTreeStack(nums)

        print("Divide & Conquer -> preorder:", preorder(root_dc))
        print("Divide & Conquer -> inorder: ", inorder(root_dc))
        print("Stack (O(n))     -> preorder:", preorder(root_st))
        print("Stack (O(n))     -> inorder: ", inorder(root_st))

        # Basic equivalence check: the unique maximum binary tree yields same traversals
        assert preorder(root_dc) == preorder(root_st), "Preorder mismatch between implementations"
        assert inorder(root_dc) == inorder(root_st), "Inorder mismatch between implementations"

        print("\nPretty print (stack-built tree):")
        pretty_print(root_st)


if __name__ == "__main__":
    _run_tests()
