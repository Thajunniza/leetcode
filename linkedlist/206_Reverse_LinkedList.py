"""
===========================================================
206. Reverse Linked List
===========================================================

🧩 Problem:
Given the head of a singly linked list, reverse the list 
and return its head.

🎯 Goal:
Return the new head of the reversed linked list.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  1 → 2 → 3 → 4 → 5
Output: 5 → 4 → 3 → 2 → 1

Example 2:
Input:  1 → 2
Output: 2 → 1

Example 3:
Input:  None
Output: None

-----------------------------------------------------------
Algorithm — Iterative Two Pointers:
-----------------------------------------------------------

1. Initialize two pointers:
    - prev = None
    - curr = head
2. While curr is not None:
    - Store next node: nextNode = curr.next
    - Reverse pointer: curr.next = prev
    - Move prev forward: prev = curr
    - Move curr forward: curr = nextNode
3. At the end, prev points to the new head
4. Return prev

Key Idea:
Reverse links one by one, updating pointers in-place. 
Time O(N), space O(1).

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
# 206. Reverse Linked List
# Iterative Two Pointers
# ------------------------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

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
new_head = sol.reverseList(head)
print_list(new_head)  # Expected: 5 → 4 → 3 → 2 → 1

head2 = ListNode(1, ListNode(2))
new_head2 = sol.reverseList(head2)
print_list(new_head2)  # Expected: 2 → 1

head3 = None
new_head3 = sol.reverseList(head3)
print_list(new_head3)  # Expected: (prints nothing)

