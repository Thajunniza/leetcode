
"""
===========================================================
145 . Binary Tree Postorder Traversal (Recursive & Iterative)
===========================================================

This module demonstrates how to construct a binary tree from
a level-order representation and perform postorder traversal
using both recursive and iterative techniques.

Postorder Traversal Order:
    Left Subtree → Right Subtree → Root

-----------------------------------------------------------
Components
-----------------------------------------------------------

1. Node
   Represents a binary tree node with:
   - val   : node value
   - left  : reference to left child
   - right : reference to right child

2. build_tree(level)
   Builds a binary tree from a level-order list representation
   where `None` indicates the absence of a node.

3. Solution.postorder_traversal_rec(root)
   Recursive implementation of postorder traversal using DFS.

4. Solution.postorder_iterative(root)
   Iterative implementation of postorder traversal using a
   single stack and a visited-flag technique to simulate
   recursion.

-----------------------------------------------------------
Algorithmic Notes
-----------------------------------------------------------

- Recursive approach leverages the call stack to ensure
  left and right subtrees are processed before the root.

- Iterative approach explicitly manages traversal state
  by pushing nodes twice:
    - First for traversal
    - Second for processing after children

-----------------------------------------------------------
Complexity Analysis
-----------------------------------------------------------

Time Complexity:
    O(n) — each node is visited exactly once.

Space Complexity:
    O(h) — where h is the height of the tree.
           Worst case: O(n) for skewed trees
           Best case : O(log n) for balanced trees
===========================================================
"""

from collections import deque
class Node():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    

def build_tree(level):
    if not level or level[0] is None:
        return None

    root = Node(level[0])
    q = deque([root])
    i = 1

    while q and i < len(level):
        node = q.popleft()

        # Left child
        if i < len(level) and level[i] is not None:
            node.left = Node(level[i])
            q.append(node.left)
        i += 1

        # Right child
        if i < len(level) and level[i] is not None:
            node.right = Node(level[i])
            q.append(node.right)
        i += 1

    return root

class Solution():
    def postorder_traversal_rec(self,root):
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
        dfs(root)
        return result

        
    
    def postorder_iterative(self,root):
        result = []
        stack=[(root,False)]
        while stack:
            curr,v = stack.pop()
            if curr:
                if v:
                    result.append(curr.val)
                else:
                    stack.append((curr,True))
                    stack.append((curr.right,False))
                    stack.append((curr.left,False))

        return result


sol = Solution()
root = build_tree([1,None,2,3])
print(sol.postorder_traversal_rec(root))
print(sol.postorder_iterative(root))
root = build_tree([1,2,3,4,5,None,8,None,None,6,7,9])
print(sol.postorder_traversal_rec(root))
print(sol.postorder_iterative(root))
