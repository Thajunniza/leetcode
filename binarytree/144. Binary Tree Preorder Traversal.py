

"""
============================================================
LeetCode 144 — Binary Tree Preorder Traversal
============================================================

Problem
-------
Given the root of a binary tree, return the preorder traversal of its nodes' values.
Preorder traverses nodes in the order: Root → Left → Right.

Why Interviewers Care
---------------------
- Tests understanding of the recursion mental model (visit node before children).
- Evaluates ability to convert recursive traversal to iterative (stack-based) safely.
- Optional: Morris traversal shows deep knowledge and space optimization thinking.

Definitions
-----------
- Preorder (DFS): Visit current node, then left subtree, then right subtree.
- Output: A list of node values in preorder order.

Examples
--------
1) Input:
       1
        \
         2
        /
       3
   Preorder: [1, 2, 3]
   (Array level-order form for building: [1, None, 2, 3])

2) Input:
             1
           /   \
          2     3
         / \     \
        4   5     8
           / \   /
          6   7 9
   Preorder: [1, 2, 4, 5, 6, 7, 3, 8, 9]
   (Array level-order: [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])

Approaches
----------
A) Recursive DFS (Preorder):
   - Visit node → recurse left → recurse right.
   - Easiest to write and explain. Watch recursion depth on skewed trees.

B) Iterative (Explicit Stack):
   - Push root; pop, visit, then push right then left (so left pops first).
   - Robust against deep recursion; preferred for production if depth is large.

C) Morris Preorder (O(1) Extra Space):
   - Thread tree temporarily via predecessor.right pointers.
   - Visit on first encounter; remove threads on second encounter.
   - No stack/recursion; modifies pointers temporarily (must restore).

Complexity
---------
Let n be the number of nodes.

- Recursive:
  * Time:  O(n), each node visited once.
  * Space: O(h) recursion stack, h = tree height (O(n) worst-case skewed, O(log n) balanced).
- Iterative (Stack):
  * Time:  O(n)
  * Space: O(h) for the stack in the worst case.
- Morris:
  * Time:  O(n)
  * Space: O(1) extra space (no recursion/stack), but temporarily threads the tree.

Edge Cases
----------
- root is None → return []
- Single node → [root.val]
- Completely skewed tree (all left or all right)
- Trees with duplicate values are allowed (just visit order matters)

Testing Checklist
-----------------
- Empty: []
- Single: [1]
- Right-leaning: [1, None, 2, None, 3]
- Left-leaning: [1, 2, None, 3]
- Mixed with gaps: [1, 2, 3, None, 5, None, 8]
- Larger near-complete tree (verify against hand-computed preorder)


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
    def preorder_traversal_rec(self,root):
        result = []
        def dfs(node):
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result
    
    def preorder_iterative(self,root):
        result = []
        if not root:
            return result
        stack = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return result

        




sol = Solution()
root = build_tree([1,None,2,3])
print(sol.preorder_traversal_rec(root))
print(sol.preorder_iterative(root))
root = build_tree([1,2,3,4,5,None,8,None,None,6,7,9])
print(sol.preorder_traversal_rec(root))
print(sol.preorder_iterative(root))
