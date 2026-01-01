"""
===========================================================
25. Reverse Nodes in k-Group
===========================================================

🧩 Problem:
Given the head of a singly linked list and an integer k, reverse the nodes of the list k at a time and return its modified list. 
Nodes that are not a multiple of k at the end should remain as-is.

🎯 Goal:
Reverse nodes in groups of size k in-place using pointer manipulation.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

-----------------------------------------------------------
Algorithm (Reverse in K-Groups):
-----------------------------------------------------------

1. Use a dummy node pointing to head to simplify edge connections.
2. While there are at least k nodes remaining:
      - Reverse the next k nodes using standard pointer reversal.
      - Connect the previous group's tail to the new head.
      - Move the previous group pointer to the tail of reversed group.
3. Stop when fewer than k nodes remain.
4. Return dummy.next as the new head.

🧠 Key Insight:
Reversal is done **in-place** without extra memory. Pointer manipulation is used to efficiently reverse sublists.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n) — each node visited at most once

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1) — in-place modification

-----------------------------------------------------------
"""

# ------------------------------------
# Definition for singly-linked list
# ------------------------------------
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ------------------------------------
# Main Solution
# ------------------------------------
class Solution(object):
    def getKth(self, curr, k):
        """
        Return the k-th node starting from curr (exclusive)
        """
        i = 0
        while curr and i < k:
            curr = curr.next
            i += 1
        return curr

    def reverseKGroup(self, head, k):
        """
        Reverse nodes of linked list in groups of size k.
        """
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        prev_group = dummy

        while True:
            kth = self.getKth(prev_group, k)
            if not kth:
                break
            next_group = kth.next

            # Reverse k nodes
            prev = next_group
            curr = prev_group.next
            while curr != next_group:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            # Reconnect reversed group
            tail = prev_group.next
            prev_group.next = prev
            prev_group = tail

        return dummy.next

# ------------------------------------
# Driver test
# ------------------------------------
def print_list(node):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print("->".join(vals))


# Input list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
curr = head
for i in range(2, 6):
    curr.next = ListNode(i)
    curr = curr.next

sol = Solution()
k = 2
head = sol.reverseKGroup(head, k)

print_list(head)  # Expected Output: 2->1->4->3->5
