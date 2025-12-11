"""
===========================================================
2130. Maximum Twin Sum of a Linked List
===========================================================

🧩 Problem:
In a singly linked list of even length n, the twin of the node at position i
(0-based) is the node at position (n - 1 - i).

The twin sum of a node is:
    node.val + twin_node.val

You are given the head of the linked list.
Return the maximum twin sum of the linked list.

🎯 Goal:
Pair nodes from the front and the back of the list:
    index i with index (n - 1 - i)
Compute all twin sums and return the maximum one.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  head = [5, 4, 2, 1]
Output: 6

Explanation:
    n = 4
    Index pairs:
        0 ↔ 3 → 5 + 1 = 6
        1 ↔ 2 → 4 + 2 = 6
    Maximum twin sum = 6.

Example 2:
Input:  head = [4, 2, 2, 3]
Output: 7

Explanation:
    n = 4
    Index pairs:
        0 ↔ 3 → 4 + 3 = 7
        1 ↔ 2 → 2 + 2 = 4
    Maximum twin sum = 7.

Example 3:
Input:  head = [1, 100000]
Output: 100001

Explanation:
    n = 2
    Only one pair:
        0 ↔ 1 → 1 + 100000 = 100001

-----------------------------------------------------------
Algorithm — Fast & Slow + Reverse Second Half:
-----------------------------------------------------------

Pattern:
    - Linked List
    - Fast & Slow Pointers to find middle
    - Reverse the second half in-place
    - Walk from both ends simultaneously to compute twin sums

Steps:

1. Use fast & slow pointers to find the middle:
       - slow moves 1 step at a time
       - fast moves 2 steps at a time
       - When fast reaches the end, slow will be at the start of the second half.

2. Reverse the second half of the list starting from slow:
       - Classic in-place reversal:
             prev = None
             curr = slow
             while curr:
                 nxt = curr.next
                 curr.next = prev
                 prev = curr
                 curr = nxt
       - After reversal, 'prev' is the head of the reversed second half.

3. Initialize:
       - l1 = head           (start of first half)
       - l2 = prev           (start of reversed second half)
       - max_twin_sum = 0

4. Traverse both halves together:
       while l2:
           twin_sum = l1.val + l2.val
           update max_twin_sum
           move l1 = l1.next
           move l2 = l2.next

5. Return max_twin_sum.

(We do not need to restore the list for this problem.)

-----------------------------------------------------------
⏱ Time Complexity:
- Finding middle with fast & slow: O(n)
- Reversing second half: O(n/2)
- Walking both halves to compute twin sums: O(n/2)
- Overall: O(n)

💾 Space Complexity:
- O(1) extra space:
    - Only uses a few pointers (slow, fast, prev, curr, l1, l2)
    - No extra arrays or lists

-----------------------------------------------------------
"""

# ------------------------------------
# 2130. Maximum Twin Sum of a Linked List
# ------------------------------------
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def twin_sum(head: Optional[ListNode]) -> int:
    """
    Compute the maximum twin sum of a linked list of even length.

    A twin pair is:
        - node at position i and node at position (n - 1 - i)

    Args:
        head (Optional[ListNode]): Head of the linked list (even length).

    Returns:
        int: Maximum twin sum.

    Example:
        Given [5, 4, 2, 1]:
            Pairs: (5, 1) and (4, 2)
            Twin sums: 6 and 6
            Output: 6
    """
    if head is None:
        return 0

    # ----------------------------------------
    # Step 1: Find middle using fast & slow
    # ----------------------------------------
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # At this point, 'slow' is at the start of the second half

    # ----------------------------------------
    # Step 2: Reverse the second half in-place
    # ----------------------------------------
    def reverse_list(node: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = node
        while curr:
            nxt = curr.next  # don't shadow built-in 'next'
            curr.next = prev
            prev = curr
            curr = nxt
        return prev  # new head of reversed list

    l1 = head
    l2 = reverse_list(slow)

    # ----------------------------------------
    # Step 3: Walk both halves and track max twin sum
    # ----------------------------------------
    max_sum = 0

    while l2:
        twin_sum_val = l1.val + l2.val
        if twin_sum_val > max_sum:
            max_sum = twin_sum_val

        l1 = l1.next
        l2 = l2.next

    return max_sum


# ------------------------------------
# Driver Test (optional)
# ------------------------------------
if __name__ == "__main__":
    # helper to build a linked list from a Python list
    def build_list(values):
        dummy = ListNode(0)
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    head1 = build_list([5, 4, 2, 1])
    print(twin_sum(head1))  # 6

    head2 = build_list([4, 2, 2, 3])
    print(twin_sum(head2))  # 7

    head3 = build_list([1, 100000])
    print(twin_sum(head3))  # 100001
