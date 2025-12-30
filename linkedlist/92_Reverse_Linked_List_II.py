"""
===========================================================
92. Reverse Linked List II
===========================================================

🧩 Problem:
Given the head of a singly linked list and two integers 
`left` and `right`, reverse the nodes from position left 
to right, and return the modified list.

🎯 Goal:
Return the head of the list after reversing the sublist.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  1 → 2 → 3 → 4 → 5, left = 2, right = 4
Output: 1 → 4 → 3 → 2 → 5

Example 2:
Input:  1 → 2 → 3, left = 1, right = 2
Output: 2 → 1 → 3

-----------------------------------------------------------
Algorithm — Iterative Sublist Reversal:
-----------------------------------------------------------

1. Create a dummy node pointing to head (helps handle head reversal)
2. Move `prev` to the node **before position left**
3. `curr` points to the `left` node
4. Reverse `right - left + 1` nodes:
    - Store next node: `nextNode = curr.next`
    - Reverse pointer: `curr.next = prev_sub`
    - Move `prev_sub = curr`, `curr = nextNode`
5. Connect reversed sublist back:
    - `prev.next.next = curr` (tail of reversed → next part)
    - `prev.next = prev_sub` (previous node → head of reversed)
6. Return `dummy.next`

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(N) — traverse each node once

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1) — constant extra memory

-----------------------------------------------------------
"""

# ------------------------------------
# 92. Reverse Linked List II
# Iterative Sublist Reversal
# ------------------------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # Reverse sublist
        curr = prev.next
        prev_sub = None
        for _ in range(right - left + 1):
            nextNode = curr.next
            curr.next = prev_sub
            prev_sub = curr
            curr = nextNode

        # Connect reversed sublist back
        tail = prev.next
        tail.next = curr
        prev.next = prev_sub

        return dummy.next

# ------------------------------------
# Driver Test
# ------------------------------------
def print_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print("->".join(vals))

# Sample Test
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
new_head = sol.reverseBetween(head, 2, 4)
print_list(new_head)  # Expected: 1 → 4 → 3 → 2 → 5

head2 = ListNode(1, ListNode(2, ListNode(3)))
new_head2 = sol.reverseBetween(head2, 1, 2)
print_list(new_head2)  # Expected: 2 → 1 → 3
