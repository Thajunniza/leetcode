"""
129. Sum Root to Leaf Numbers

Problem:
---------
Given a binary tree where each node contains a digit (0–9), each root-to-leaf
path represents a number. Return the total sum of all root-to-leaf numbers.

Example:
---------
Input Tree:
        1
       / \
      2   3

Paths:
- 1 -> 2  = 12
- 1 -> 3  = 13

Output:
--------
25

------------------------------------------------------------
Algorithm (Iterative DFS using Stack):
------------------------------------------------------------
1. If the root is None, return 0.
2. Use a stack to store tuples of (node, current_number).
3. Start with (root, root.val).
4. Pop a node from the stack:
   - If it is a leaf node, add current_number to result.
   - If it has a left child, push (left, current_number * 10 + left.val).
   - If it has a right child, push (right, current_number * 10 + right.val).
5. Continue until the stack is empty.
6. Return the accumulated result.

------------------------------------------------------------
Time Complexity:
------------------------------------------------------------
O(n), where n is the number of nodes in the tree.
Each node is visited exactly once.

------------------------------------------------------------
Space Complexity:
------------------------------------------------------------
O(h), where h is the height of the tree (stack space).
Worst case O(n) for a skewed tree.

------------------------------------------------------------
Recursive Method:
------------------------------------------------------------
1. Perform DFS.
2. Pass the current number down the recursion.
3. When a leaf node is reached, return the constructed number.
4. Sum results from left and right subtrees.
"""

# ----------------------------------------------------------
# Definition for a binary tree node
# ----------------------------------------------------------
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ----------------------------------------------------------
# Iterative DFS Solution
# ----------------------------------------------------------
class SolutionIterative(object):
    def sumNumbers(self, root):
        if not root:
            return 0

        result = 0
        stack = [(root, root.val)]

        while stack:
            node, total = stack.pop()

            # If leaf node, add path value
            if not node.left and not node.right:
                result += total

            if node.right:
                stack.append((node.right, total * 10 + node.right.val))
            if node.left:
                stack.append((node.left, total * 10 + node.left.val))

        return result


# ----------------------------------------------------------
# Recursive DFS Solution
# ----------------------------------------------------------
class SolutionRecursive(object):
    def sumNumbers(self, root):
        def dfs(node, current):
            if not node:
                return 0

            current = current * 10 + node.val

            if not node.left and not node.right:
                return current

            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)


# ----------------------------------------------------------
# Test Case
# ----------------------------------------------------------
if __name__ == "__main__":
    # Construct the tree:
    #        1
    #       / \
    #      2   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    iterative_solution = SolutionIterative()
    recursive_solution = SolutionRecursive()

    print("Iterative Result:", iterative_solution.sumNumbers(root))  # Expected: 25
    print("Recursive Result:", recursive_solution.sumNumbers(root))  # Expected: 25
