"""
---------------------------------------------------------------------
510- Inorder Successor in BST II
---------------------------------------------------------------------
Given a node in a Binary Search Tree (BST) with parent pointers, 
find the inorder successor of that node. Each node has the following attributes:
- val : node value
- left : left child
- right : right child
- parent : parent node (None if root)

The inorder successor of a node is the node with the smallest key 
greater than the given node’s value. If no successor exists, return None.

---------------------------------------------------------------------
ALGORITHMS
---------------------------------------------------------------------
1. Root-search + BST traversal
   - Walk up to the root using parent pointers.
   - Starting from the root, use BST ordering to find the successor:
       • If node.val < curr.val → candidate successor, move left
       • Else → move right
   - Time: O(h), Space: O(1)

2. Parent-pointer-only (optimal)
   - Case 1: node has right subtree → return leftmost node in right subtree
   - Case 2: node has no right subtree → walk up until node is left child of parent
   - Time: O(h), Space: O(1)

---------------------------------------------------------------------
EXAMPLE
---------------------------------------------------------------------
Tree:

        20
       /  \
     10    30
       \
        15
          \
           17

Node: 15
Inorder traversal: 10 → 15 → 17 → 20 → 30
Output: 17
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.parent: Optional['Node'] = None


class Solution:
    def inorderSuccessor_root_search(self, node: 'Node') -> 'Optional[Node]':
        """Find successor by walking to root and using BST search"""
        # Step 1: Find root
        curr = node
        while curr.parent:
            curr = curr.parent
        root = curr

        # Step 2: BST search for successor
        successor = None
        curr = root
        while curr:
            if node.val < curr.val:
                successor = curr
                curr = curr.left
            else:
                curr = curr.right
        return successor

    def inorderSuccessor_parent_only(self, node: 'Node') -> 'Optional[Node]':
        """Optimal: use parent pointers only"""
        # Case 1: node has right subtree
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr

        # Case 2: no right subtree
        curr = node
        parent = node.parent
        while parent and curr == parent.right:
            curr = parent
            parent = parent.parent
        return parent


# -------------------------------------------------------------------
# TEST RUN
# -------------------------------------------------------------------
if __name__ == "__main__":
    """
    Construct the following BST with parent pointers:

            20
           /  \
         10    30
           \
            15
              \
               17
    """
    root = Node(20)
    root.left = Node(10)
    root.left.parent = root
    root.right = Node(30)
    root.right.parent = root

    root.left.right = Node(15)
    root.left.right.parent = root.left
    root.left.right.right = Node(17)
    root.left.right.right.parent = root.left.right

    test_nodes = [root.left, root.left.right, root.left.right.right, root, root.right]

    solution = Solution()
    for n in test_nodes:
        succ1 = solution.inorderSuccessor_root_search(n)
        succ2 = solution.inorderSuccessor_parent_only(n)
        print(f"Node {n.val}:")
        print(f"  Root-search successor: {succ1.val if succ1 else 'None'}")
        print(f"  Parent-only successor: {succ2.val if succ2 else 'None'}\n")