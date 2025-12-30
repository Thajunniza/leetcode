"""
===========================================================
143. Reorder List
===========================================================
Given the head of a singly linked list, reorder it to follow the pattern:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → … 

You must do this **in-place** without modifying node values.

Approach:
---------
1. **Find the middle** using Fast–Slow Pointer Technique:
   - slow moves 1 step, fast moves 2 steps.
   - When fast reaches the end, slow is at the middle.
2. **Reverse the second half** of the list starting after the middle.
3. **Merge two halves**:
   - Alternate nodes from the first and reversed second halves.

Time Complexity:  O(n)  → traverse the list a few times  
Space Complexity: O(1)  → no extra data structures
"""

# ------------------------------------
# Helper function to build linked list
# ------------------------------------
def build_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for n in arr:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next

# ------------------------------------
# Definition for singly-linked list node
# ------------------------------------
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ------------------------------------
# Main Solution
# ------------------------------------
class Solution(object):
    def reorderList(self, head):
        """
        Reorder the list in-place:
        - Find middle
        - Reverse second half
        - Merge two halves alternately
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow.next
        slow.next = None  # split the list
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        second = prev

        # Step 3: Merge two halves
        first = head
        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next

# ------------------------------------
# Driver test
# ------------------------------------
head = build_linked_list([1, 2, 3, 4, 5])
sol = Solution()
sol.reorderList(head)

# Print reordered list
curr = head
while curr:
    print(curr.val, end="->" if curr.next else "\n")
    curr = curr.next

head_even = build_linked_list([1, 2, 3, 4])
sol.reorderList(head_even)

curr = head_even
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next
