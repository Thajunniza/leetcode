"""
LeetCode 101: Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).

Example 1:
    Input: root = [1,2,2,3,4,4,3]
           1
          / \
         2   2
        / \ / \
       3  4 4  3
    Output: true

Example 2:
    Input: root = [1,2,2,null,3,null,3]
           1
          / \
         2   2
          \   \
           3   3
    Output: false

Example 3:
    Input: root = [1]
    Output: true

Algorithm: Recursive DFS with Mirror Comparison
- Helper function to check if two trees are mirrors of each other
- Left subtree's left should equal right subtree's right
- Left subtree's right should equal right subtree's left
- Base cases: both null (true), one null (false), values differ (false)

Time Complexity: O(n)
- Visit each node exactly once
- n = number of nodes in tree

Space Complexity: O(h)
- Recursion stack depth equals height of tree
- h = height of tree
- Best case O(log n) for balanced tree
- Worst case O(n) for skewed tree
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Recursive approach - most elegant.
        Check if left and right subtrees are mirrors of each other.
        """
        if not root:
            return True
        
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """
        Helper function to check if two trees are mirrors.
        """
        # Both null - symmetric
        if not left and not right:
            return True
        
        # One is null, other is not - not symmetric
        if not left or not right:
            return False
        
        # Values must match AND subtrees must be mirrors
        # Left's left mirrors Right's right
        # Left's right mirrors Right's left
        return (left.val == right.val and 
                self.isMirror(left.left, right.right) and 
                self.isMirror(left.right, right.left))


# Alternative: Iterative BFS approach
class SolutionIterative:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative approach using queue.
        Compare nodes in pairs (left, right).
        """
        if not root:
            return True
        
        queue = deque([(root.left, root.right)])
        
        while queue:
            left, right = queue.popleft()
            
            # Both null - continue
            if not left and not right:
                continue
            
            # One is null or values differ - not symmetric
            if not left or not right or left.val != right.val:
                return False
            
            # Add children in mirror order
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        
        return True


# Alternative: Using stack (DFS iterative)
class SolutionStack:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative DFS using stack instead of queue.
        """
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        
        while stack:
            left, right = stack.pop()
            
            if not left and not right:
                continue
            
            if not left or not right or left.val != right.val:
                return False
            
            # Push in any order (DFS doesn't care about level order)
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        
        return True


# Test cases
def test():
    # Helper to build tree
    def build_tree(values):
        if not values:
            return None
        
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        
        while queue and i < len(values):
            node = queue.popleft()
            
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        
        return root
    
    sol = Solution()
    
    # Test 1: Symmetric tree
    root1 = build_tree([1, 2, 2, 3, 4, 4, 3])
    print(sol.isSymmetric(root1))  # True
    
    # Test 2: Not symmetric
    root2 = build_tree([1, 2, 2, None, 3, None, 3])
    print(sol.isSymmetric(root2))  # False
    
    # Test 3: Single node
    root3 = build_tree([1])
    print(sol.isSymmetric(root3))  # True
    
    # Test 4: Empty tree
    root4 = build_tree([])
    print(sol.isSymmetric(root4))  # True
    
    # Test 5: Two nodes (not symmetric)
    root5 = build_tree([1, 2])
    print(sol.isSymmetric(root5))  # False
    
    # Test 6: Symmetric with nulls
    root6 = build_tree([1, 2, 2, None, 3, 3, None])
    print(sol.isSymmetric(root6))  # True

test()