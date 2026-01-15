
"""
============================================================
94 . Binary Tree Inorder Traversal 
============================================================

Problem Summary
---------------
Implement:
1) A utility to **build a binary tree** from a level-order (BFS) array representation where
   `None` indicates a missing child.
2) An **inorder traversal (recursive)** that returns a list of node values visited in
   Left → Root → Right order.

Why This Matters (Interview Signal)
-----------------------------------
- Tests understanding of tree representation (arrays ↔ pointers).
- Assesses recursion fundamentals (base case, divide & conquer).
- Exercises traversal correctness and stack/space awareness.
- Common building block for many Google-style tree problems.

Input Format
------------
- Level-order list (array) of node values: e.g., [1, None, 2, 3]
  - The array is interpreted breadth-first, left-to-right.
  - Use `None` for absent children.

Output
------
- `build_tree(level)` → returns the root `Node` of the constructed binary tree.
- `Solution.inorder_traversal_rec(root)` → returns a `List[int]` of the inorder traversal.

Examples
--------
1) Example A
   Input (level): [1, None, 2, 3]
   The tree is:
           1
            \
             2
            /
           3
   Inorder: [1, 3, 2]

2) Example B
   Input (level): [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
   The tree is:
               1
             /   \
            2     3
           / \     \
          4   5     8
             / \   /
            6   7 9
   Inorder: [4, 2, 6, 5, 7, 1, 3, 9, 8]

High-Level Algorithms
---------------------
A) Build Tree from Level Order (BFS):
   - Use a queue to attach children as we iterate the level-order array.
   - For each node taken from the queue:
       * If next array value is not None → create left child.
       * If the following value is not None → create right child.
   - Continue until the array is exhausted.

B) Inorder Traversal (Recursive):
   - Recurse on left subtree → visit node → recurse on right subtree.
   - Base case: if node is None, return.

Complexity Analysis
-------------------
Let n be the number of elements in the input `level` array.

- build_tree(level):
  * Time:  O(n) — each array element is processed once.
  * Space: O(n) — queue can hold up to O(n) nodes in the worst case; the tree itself is O(n).

- inorder_traversal_rec(root):
  * Time:  O(m) — where m is the number of nodes in the tree (each visited exactly once).
  * Space: O(h) recursion stack where h is the tree height (worst-case O(m) for skewed trees,
           O(log m) for balanced trees).
  * Output list also uses O(m) space.

Edge Cases & Assumptions
------------------------
- Empty input: [] or [None] → returns None.
- Inputs may contain trailing `None` entries (safe to ignore).
- Tree may be skewed (all left or all right).
- Non-integer values are acceptable as long as they’re comparable/printable.
- Level-order input must be consistent with binary tree layering semantics.

Testing Checklist
-----------------
- Empty tree: [], [None]
- Single node: [1]
- Only left chain: [1, 2, None, 3]
- Only right chain: [1, None, 2, None, 3]
- Mixed with gaps: [1, 2, 3, None, 5, None, 8]
- Larger complete/near-complete trees.

Notes
-----
- For production usage, consider adding input validation and guards against malformed arrays.
- An iterative inorder traversal (with a stack) yields O(1) recursion risk if desired.

"""



from collections import deque
class Node():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    


class Solution():
    def inorder_traversal_rec(self,root):
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result
    
    def inorder_iterative(self,root):
        result = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result


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


sol = Solution()
root = build_tree([1,None,2,3])
print(sol.inorder_traversal_rec(root))
print(sol.inorder_iterative(root))
root = build_tree([1,2,3,4,5,None,8,None,None,6,7,9])
print(sol.inorder_traversal_rec(root))
print(sol.inorder_iterative(root))
