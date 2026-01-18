"""
LeetCode 107: Binary Tree Level Order Traversal II

Given the root of a binary tree, return the bottom-up level order traversal of 
its nodes' values (i.e., from left to right, level by level from leaf to root).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
         3
        / \
       9  20
          / \
         15  7
    Output: [[15,7],[9,20],[3]]
    Explanation:
    - Level 2: [15,7]
    - Level 1: [9,20]
    - Level 0: [3]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

Algorithm: BFS (Breadth-First Search) with Level-Order Traversal + Reverse
- Use a queue to process nodes level by level (top to bottom)
- Build result array in normal order
- Reverse the entire result array at the end

Time Complexity: O(n)
- Visit each node exactly once: O(n)
- Reverse result array: O(n)
- Total: O(n)

Space Complexity: O(n)
- Queue can hold up to n/2 nodes at the widest level
- Result array stores all n node values in levels

where n = number of nodes
"""

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Bottom-up level order traversal using BFS.
        
        Approach: Normal level order + reverse at end
        """
        result = []
        if not root:
            return result
        
        q = deque([root])
        
        while q:
            n = len(q)
            level = []
            
            for _ in range(n):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(level)
        
        return result[::-1]


# Alternative: Using deque to insert at front
class SolutionDeque:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Insert each level at the beginning using deque.
        Avoids final reverse operation.
        """
        if not root:
            return []
        
        result = deque()
        q = deque([root])
        
        while q:
            n = len(q)
            level = []
            
            for _ in range(n):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Insert at front instead of append
            result.appendleft(level)
        
        return list(result)


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
    
    # Test 1: [3,9,20,null,null,15,7]
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print(sol.levelOrderBottom(root1))  # [[15,7],[9,20],[3]]
    
    # Test 2: [1]
    root2 = build_tree([1])
    print(sol.levelOrderBottom(root2))  # [[1]]
    
    # Test 3: []
    root3 = build_tree([])
    print(sol.levelOrderBottom(root3))  # []
    
    # Test 4: Larger tree
    root4 = build_tree([1, 2, 3, 4, 5, 6, 7])
    print(sol.levelOrderBottom(root4))  # [[4,5,6,7],[2,3],[1]]

test()