"""
===========================================================
83. Remove Duplicates from Sorted List
===========================================================

🧩 Problem:
Given the head of a sorted linked list, delete all duplicates
such that each element appears only once, and return the 
linked list sorted as well.

🎯 Goal:
Remove all duplicate nodes from a sorted linked list 
while preserving the original order.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Example 3:
Input: head = []
Output: []

-----------------------------------------------------------
Algorithm (Single Pointer Skip Technique):
-----------------------------------------------------------

1. Initialize pointer `curr` at head.
2. While `curr` and `curr.next` exist:
      - If curr.val == curr.next.val:
            Skip duplicate → curr.next = curr.next.next
      - Else:
            Move curr = curr.next
3. Return head.

🧠 Key Insight:
Since the list is sorted, duplicates are always consecutive.
This allows skipping them in-place with O(1) space.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n) — each node is visited at most once

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1) — in-place modification

-----------------------------------------------------------
"""

# ------------------------------------
# 83. Remove Duplicates from Sorted List
# Linked List Pattern
# ------------------------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

# ------------------------------------
# Driver Test
# ------------------------------------
def print_list(node):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print("->".join(vals))

# Test Case 1
head = ListNode(1, ListNode(1, ListNode(2)))
sol = Solution()
new_head = sol.deleteDuplicates(head)
print_list(new_head)  # Expected: 1 -> 2

# Test Case 2
head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
new_head2 = sol.deleteDuplicates(head2)
print_list(new_head2)  # Expected: 1 -> 2 -> 3
