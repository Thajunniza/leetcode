"""
LeetCode 23: Merge k Sorted Lists

Robust min-heap solution that avoids comparing ListNode objects directly
by adding a deterministic tie-breaker to each heap item.

Approach
--------
- Maintain a min-heap with at most one node from each list.
- Heap item: (node.val, unique_counter, node)
  The unique counter prevents Python from comparing ListNode objects when
  node values tie.
- Repeatedly pop the smallest node and push its successor.

Complexity
----------
- Time:  O(N log k), where N is the total number of nodes and k is the
         number of input lists.
- Space: O(k) for the heap.

Run this file directly to see a quick sanity test.
"""

import heapq
from itertools import count
from typing import List, Optional


class ListNode(object):
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode(val={self.val})"


class Solution(object):
    def mergeKLists(self, lists: 'List[Optional[ListNode]]') -> 'Optional[ListNode]':
        """
        Merge k sorted linked lists and return it as one sorted list.
        Uses a min-heap with a stable counter as a tie-breaker.
        """
        min_heap = []
        ctr = count()  # unique, increasing tie-breaker to avoid comparing nodes

        for node in lists:
            if node is not None:
                heapq.heappush(min_heap, (node.val, next(ctr), node))

        dummy = ListNode(0)
        curr = dummy

        while min_heap:
            _, _, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            if node.next is not None:
                heapq.heappush(min_heap, (node.next.val, next(ctr), node.next))

        return dummy.next


# -------------------------- Helpers & Demo --------------------------

def build_list(*vals) -> Optional[ListNode]:
    """Build a linked list from values and return its head."""
    dummy = ListNode(0)
    p = dummy
    for v in vals:
        p.next = ListNode(v)
        p = p.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> list:
    """Convert a linked list to a Python list of values."""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    # Quick sanity tests
    lists = [
        build_list(1, 4, 5),
        build_list(1, 3, 4),
        build_list(2, 6)
    ]

    merged = Solution().mergeKLists(lists)
    print(to_list(merged))  # Expected: [1, 1, 2, 3, 4, 4, 5, 6]