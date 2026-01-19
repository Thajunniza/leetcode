"""
113. Path Sum II

Problem:
--------
Given the root of a binary tree and an integer targetSum, return all root-to-leaf
paths where the sum of the node values in the path equals targetSum.

--------------------------------------------------
Approach 1: Recursive DFS (Backtracking)
--------------------------------------------------
Algorithm:
1. Traverse the tree using DFS.
2. Maintain a current path list.
3. Add node value to path and subtract from targetSum.
4. If a leaf is reached and targetSum == node.val, store a copy of the path.
5. Backtrack by removing the last node before returning.

Time Complexity: O(n)
Space Complexity: O(h) for recursion stack + path storage

--------------------------------------------------
Approach 2: Iterative DFS (Stack)
--------------------------------------------------
Algorithm:
1. Use a stack storing (node, remaining_sum, current_path).
2. Pop from stack, update remaining sum and path.
3. If node is a leaf and remaining_sum == node.val, add path to result.
4. Push right and left children with updated state.

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

    # -------- Recursive Solution --------
    def pathSumRecursive(self, root, targetSum):
        result = []

        def dfs(node, remaining, path):
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            if not node.left and not node.right and remaining == 0:
                result.append(list(path))

            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)

            path.pop()  # backtrack

        dfs(root, targetSum, [])
        return result

    # -------- Iterative Solution --------
    def pathSumIterative(self, root, targetSum):
        if not root:
            return []

        result = []
        stack = [(root, targetSum, [])]

        while stack:
            node, remain, path = stack.pop()
            path = path + [node.val]
            remain -= node.val

            if not node.left and not node.right and remain == 0:
                result.append(path)

            if node.right:
                stack.append((node.right, remain, path))
            if node.left:
                stack.append((node.left, remain, path))

        return result


# -----------------------------
# Test Run
# -----------------------------
if __name__ == "__main__":
    """
    Tree:
            5
           / \
          4   8
         /   / \
        11  13  4
       /  \     / \
      7    2   5   1

    Target Sum = 22
    Expected Paths:
    [
      [5, 4, 11, 2],
      [5, 8, 4, 5]
    ]
    """

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    sol = Solution()

    print("Recursive Result:", sol.pathSumRecursive(root, 22))
    print("Iterative Result:", sol.pathSumIterative(root, 22))


"""
Expected Output:
Recursive Result: [[5, 4, 11, 2], [5, 8, 4, 5]]
Iterative Result: [[5, 4, 11, 2], [5, 8, 4, 5]]
"""

