"""
LeetCode 103: Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its 
nodes' values (i.e., from left to right, then right to left for the next level 
and alternate between).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
         3
        / \
       9  20
          / \
         15  7
    Output: [[3],[20,9],[15,7]]
    Explanation:
    - Level 0: [3] (left to right)
    - Level 1: [20,9] (right to left)
    - Level 2: [15,7] (left to right)

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

Algorithm: BFS (Breadth-First Search) with Level-Order Traversal
- Use a queue to process nodes level by level
- Toggle direction flag for each level
- Reverse the current level when direction is right-to-left

Time Complexity: O(n)
- Visit each node exactly once
- Reversing levels takes O(k) per level, but total across all levels is O(n)

Space Complexity: O(n)
- Queue can hold up to n/2 nodes at the widest level
- Result array stores all n node values
- Recursion stack: O(h) if using DFS alternative

where n = number of nodes, h = height of tree
"""

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform zigzag level order traversal using BFS.
        
        Time: O(n) - visit each node once
        Space: O(n) - queue can hold up to n/2 nodes at the last level
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            level = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse if going right to left
            if not left_to_right:
                level.reverse()
            
            result.append(level)
            left_to_right = not left_to_right
        
        return result


# Alternative: Using deque for efficient reversals
class SolutionDeque:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Use deque to build levels in correct order without reversing.
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            level = deque()
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # Add to left or right of deque based on direction
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(list(level))
            left_to_right = not left_to_right
        
        return result


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
    print(sol.zigzagLevelOrder(root1))  # [[3],[20,9],[15,7]]
    
    # Test 2: [1]
    root2 = build_tree([1])
    print(sol.zigzagLevelOrder(root2))  # [[1]]
    
    # Test 3: []
    root3 = build_tree([])
    print(sol.zigzagLevelOrder(root3))  # []
    
    # Test 4: Larger tree
    root4 = build_tree([1, 2, 3, 4, 5, 6, 7])
    print(sol.zigzagLevelOrder(root4))  # [[1],[3,2],[4,5,6,7]]

test()