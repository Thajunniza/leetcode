"""
LeetCode 100: Same Tree

Given the roots of two binary trees p and q, write a function to check if they 
are the same or not. Two binary trees are considered the same if they are 
structurally identical, and the nodes have the same value.

Example 1:
    Input: p = [1,2,3], q = [1,2,3]
        p:   1           q:   1
            / \              / \
           2   3            2   3
    Output: true

Example 2:
    Input: p = [1,2], q = [1,null,2]
        p:   1           q:   1
            /                  \
           2                    2
    Output: false

Example 3:
    Input: p = [1,2,1], q = [1,1,2]
        p:   1           q:   1
            / \              / \
           2   1            1   2
    Output: false

Algorithm: Recursive DFS (Depth-First Search)
- Base cases: both null (true), one null (false)
- Check if current values match
- Recursively check left and right subtrees

Time Complexity: O(min(n, m))
- Visit each node once until mismatch is found
- In worst case (identical trees), visit all nodes
- n = number of nodes in p, m = number of nodes in q

Space Complexity: O(min(h_p, h_q))
- Recursion stack depth equals height of shorter tree
- h_p = height of tree p, h_q = height of tree q
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Recursive approach - most elegant and intuitive.
        """
        # Both null - same structure
        if not p and not q:
            return True
        
        # One is null, other is not - different structure
        if not p or not q:
            return False
        
        # Values differ - not same
        if p.val != q.val:
            return False
        
        # Check left and right subtrees recursively
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))


# Alternative: Iterative BFS approach
class SolutionIterative:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Iterative approach using BFS with queue.
        Useful if you want to avoid recursion stack.
        """
        queue = deque([(p, q)])
        
        while queue:
            node1, node2 = queue.popleft()
            
            # Both null - continue
            if not node1 and not node2:
                continue
            
            # One is null or values differ - not same
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Add children to queue
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        
        return True


# Alternative: Concise one-liner recursive
class SolutionOneLiner:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Ultra-concise version - same logic, compressed.
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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
    
    # Test 1: Same trees
    p1 = build_tree([1, 2, 3])
    q1 = build_tree([1, 2, 3])
    print(sol.isSameTree(p1, q1))  # True
    
    # Test 2: Different structure
    p2 = build_tree([1, 2])
    q2 = build_tree([1, None, 2])
    print(sol.isSameTree(p2, q2))  # False
    
    # Test 3: Different values
    p3 = build_tree([1, 2, 1])
    q3 = build_tree([1, 1, 2])
    print(sol.isSameTree(p3, q3))  # False
    
    # Test 4: Both null
    p4 = build_tree([])
    q4 = build_tree([])
    print(sol.isSameTree(p4, q4))  # True
    
    # Test 5: One null, one not
    p5 = build_tree([1])
    q5 = build_tree([])
    print(sol.isSameTree(p5, q5))  # False

test()