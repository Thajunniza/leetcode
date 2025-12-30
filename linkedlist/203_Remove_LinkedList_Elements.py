"""
===========================================================
203. Remove Linked List Elements
===========================================================

🧩 Problem:
Given the head of a linked list and an integer `val`,
remove all the nodes of the linked list that have
Node.val == val, and return the new head.

🎯 Goal:
Delete every node matching given value and return the
remaining linked list.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input:  head = [], val = 1
Output: []

Example 3:
Input:  head = [7,7,7,7], val = 7
Output: []

-----------------------------------------------------------
Algorithm (Two-Pointer Skip Technique):
-----------------------------------------------------------

1. Create dummy node pointing to head (dummy → head)
2. Use pointer `curr` starting at dummy
3. While curr.next exists:
       - If curr.next.val == target val:
             Skip node → curr.next = curr.next.next
       - Else:
             Move curr = curr.next
4. Return dummy.next (ensures head deletions are handled)

🧠 Key Insight:
Keeping pointer on node *before* deletion simplifies logic
and handles head deletion without extra checks.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n) — must inspect each node once

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1) — in-place deletion

-----------------------------------------------------------
"""

# ------------------------------------
# 203. Remove Linked List Elements
# Linked List Pattern
# ------------------------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next


# ------------------------------------
# Driver Test
# ------------------------------------
def print_list(node):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print(" -> ".join(vals))


# Test Case
head = ListNode(1,
        ListNode(2,
        ListNode(6,
        ListNode(3,
        ListNode(4,
        ListNode(5,
        ListNode(6)))))))

val = 6
sol = Solution()
new_head = sol.removeElements(head, val)
print_list(new_head)  # Expected: 1 -> 2 -> 3 -> 4 -> 5
