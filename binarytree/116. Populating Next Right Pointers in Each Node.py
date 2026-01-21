"""
116: Populating Next Right Pointers in Each Node
--------------------------------------------------------

Given a perfect binary tree, populate each node's `next` pointer to point to
its next right node. If there is no next right node, the `next` pointer should
be set to `None`.

This module provides:
  • Node class
  • O(1) extra space solution (iterative, perfect binary tree)
  • Optional BFS solution for clarity (uses a queue)
  • Simple test harness to validate and visualize connections

Run:
    python lc116_connect_next_pointers.py

"""
from __future__ import annotations
from typing import Optional, List
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: Optional['Node'] = None,
                 right: Optional['Node'] = None, next: Optional['Node'] = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self) -> str:
        nxt = self.next.val if self.next else None
        return f"Node(val={self.val}, next={nxt})"


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        """
        O(1) extra space iterative solution for a perfect binary tree.

        Invariant:
        - We traverse the current level using already established `next` pointers,
          while wiring `next` pointers for the next level.
        - For each node `curr` on a level:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
        """
        if not root:
            return None
        curr = root
        nxt = root.left
        while curr and nxt:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
            if not curr:
                curr = nxt
                nxt = curr.left
        return root

    def connect_bfs(self, root: Optional[Node]) -> Optional[Node]:
        """Level-order traversal version using a queue (O(n) space).
        Works for perfect binary trees as well as a reference implementation.
        """
        if not root:
            return None
        q: deque[Node] = deque([root])
        while q:
            prev = None
            for _ in range(len(q)):
                node = q.popleft()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root


# ---------------------- Test Utilities ----------------------
def levels_via_next(root: Optional[Node]) -> List[List[int]]:
    """Collect level-order values by following next pointers per level."""
    out: List[List[int]] = []
    level = root
    while level:
        curr = level
        row: List[int] = []
        while curr:
            row.append(curr.val)
            curr = curr.next
        out.append(row)
        level = level.left  # perfect tree: next level's leftmost
    return out


def _build_perfect_tree(vals: List[int]) -> Optional[Node]:
    """Build a perfect binary tree from level-order values. Length must be (2^{h+1}-1)."""
    if not vals:
        return None
    nodes = [None] + [Node(v) for v in vals]  # 1-indexed
    n = len(vals)
    for i in range(1, n + 1):
        li, ri = 2 * i, 2 * i + 1
        if li <= n:
            nodes[i].left = nodes[li]
        if ri <= n:
            nodes[i].right = nodes[ri]
    return nodes[1]


def _run_tests():
    # Perfect tree of height 2 (7 nodes)
    root = _build_perfect_tree([1, 2, 3, 4, 5, 6, 7])
    sol = Solution()
    sol.connect(root)
    lv = levels_via_next(root)
    print("Connected levels via next:", lv)
    assert lv == [[1], [2, 3], [4, 5, 6, 7]]

    # Also test BFS variant
    root2 = _build_perfect_tree([10, 20, 30, 40, 50, 60, 70])
    sol.connect_bfs(root2)
    lv2 = levels_via_next(root2)
    print("Connected levels via next (BFS):", lv2)
    assert lv2 == [[10], [20, 30], [40, 50, 60, 70]]

    # Edge cases
    assert levels_via_next(sol.connect(None)) == []
    single = Node(42)
    sol.connect(single)
    assert levels_via_next(single) == [[42]]

    print("All tests passed.")


if __name__ == "__main__":
    _run_tests()
