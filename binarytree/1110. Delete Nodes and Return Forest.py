"""
1110. Delete Nodes and Return Forest

Problem:
    Given the root of a binary tree and a list of integers `to_delete`, delete all nodes
    with values in `to_delete` and return the forest (a list of the remaining trees' roots).

Example:
    Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
    Output: [[1,2,null,4],[6],[7]]
    Explanation:
        Delete nodes with values 3 and 5. The forest contains trees rooted at 1, 6, 7.

Algorithm:
    Iterative Post-order Traversal:
    1. Use a stack to simulate post-order traversal (children first, parent later).
    2. Each stack element stores (node, parent, is_left_child, visited_flag).
    3. If a node needs deletion:
        - Add its non-null children to the result forest.
        - Disconnect it from its parent by setting the parent's left/right to None.
    4. At the end, add the root to the result if it is not deleted.

Time Complexity: O(n) – each node is visited once
Space Complexity: O(n) – stack + result list
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        
        to_delete_set = set(to_delete)
        result = []
        # Stack stores: (node, parent, is_left_child, visited_flag)
        stack = [(root, None, False, False)]
        
        while stack:
            node, parent, is_left, visited = stack.pop()
            if not node:
                continue
            
            if visited:
                # Post-order processing
                if node.val in to_delete_set:
                    if node.left:
                        result.append(node.left)
                    if node.right:
                        result.append(node.right)
                    if parent:
                        if is_left:
                            parent.left = None
                        else:
                            parent.right = None
                continue
            
            # Push current node back as visited
            stack.append((node, parent, is_left, True))
            # Push children to stack
            stack.append((node.right, node, False, False))
            stack.append((node.left, node, True, False))
        
        # Add root if not deleted
        if root.val not in to_delete_set:
            result.append(root)
        
        return result

# ------------------ Test Cases ------------------
if __name__ == "__main__":
    # Helper function to print tree in level-order
    from collections import deque
    
    def print_tree(root):
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append(None)
        # Remove trailing None
        while res and res[-1] is None:
            res.pop()
        return res

    # Example Tree:
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    sol = Solution()
    forest = sol.delNodes(n1, [3,5])
    
    print("Resulting Forest (level-order):")
    for tree_root in forest:
        print(print_tree(tree_root))