"""
===========================================================
2074. Reverse Even Length Groups
===========================================================

Given the head of a singly linked list, reverse the nodes in each group of increasing size (1, 2, 3, ...) 
only if the group length is even. Otherwise, leave the group as-is.
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
    def reverseEvenLengthGroups(self, head):
        """
        Reverse nodes in even length groups in-place.
        Groups sizes: 1, 2, 3, 4, ...
        """
        if not head or not head.next:
            return head

        n = 1  # initial group size
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            # Step 1: Count actual group size
            i = 0
            temp = curr
            while temp and i < n:
                temp = temp.next
                i += 1

            # Step 2: Odd length group → skip
            if i % 2 == 1:
                for _ in range(i):
                    prev = curr
                    curr = curr.next
            # Step 3: Even length group → reverse
            else:
                prevNode = temp
                node = curr
                for _ in range(i):
                    nextNode = node.next
                    node.next = prevNode
                    prevNode = node
                    node = nextNode

                # Reconnect reversed group
                prev.next = prevNode
                prev = curr
                curr = temp

            n += 1

        return dummy.next

# ------------------------------------
# Driver test
# ------------------------------------
# Input list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
head = ListNode(1)
curr = head
for i in range(2, 10):
    curr.next = ListNode(i)
    curr = curr.next

sol = Solution()
head = sol.reverseEvenLengthGroups(head)

# Print result
curr = head
while curr:
    print(curr.val, end="->" if curr.next else "\n")
    curr = curr.next
