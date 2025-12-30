"""
===========================================================
24. Swap Nodes in Pairs
===========================================================

🧩 Problem:
Given a singly linked list, swap every two adjacent nodes 
and return its head. You must swap the actual nodes, not 
just their values.

🎯 Goal:
Return the head of the modified list with pairs swapped.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  1 → 2 → 3 → 4
Output: 2 → 1 → 4 → 3

Example 2:
Input:  1 → 2 → 3
Output: 2 → 1 → 3

Example 3:
Input:  1
Output: 1

-----------------------------------------------------------
Algorithm — Iterative with Dummy Node:
-----------------------------------------------------------

1. Create a dummy node pointing to head (helps handle head swaps)
2. Initialize prev = dummy
3. While prev.next and prev.next.next exist:
    - first = prev.next
    - second = prev.next.next
    - Swap links:
        prev.next = second
        first.next = second.next
        second.next = first
    - Move prev forward to first
4. Return dummy.next

Key Idea:
By always swapping prev.next and prev.next.next and moving 
prev forward, we process the list in pairs with O(1) space 
and O(N) time.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(N) — traverse each node once

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1) — constant extra memory (dummy + pointers)

-----------------------------------------------------------
"""

# ------------------------------------
# 24. Swap Nodes in Pairs
# Iterative Approach with Dummy Node
# ------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        # swap
        prev.next = second
        first.next = second.next
        second.next = first

        # move prev forward
        prev = first

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
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
new_head = swap_pairs(head)
print_list(new_head)  # Expected: 2 → 1 → 4 → 3

head2 = ListNode(1, ListNode(2, ListNode(3)))
new_head2 = swap_pairs(head2)
print_list(new_head2)  # Expected: 2 → 1 → 3

head3 = ListNode(1)
new_head3 = swap_pairs(head3)
print_list(new_head3)  # Expected: 1
