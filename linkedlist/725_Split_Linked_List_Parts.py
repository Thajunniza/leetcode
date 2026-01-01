"""
725. Split Linked List in Parts

Given the head of a singly linked list and an integer k,
split the linked list into k consecutive parts.

Each part should have a length as equal as possible:
- No two parts should differ in size by more than 1
- Earlier parts should be larger if sizes differ

Return an array of the k parts.
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
    def splitListToParts(self, head, k):
        """
        Split the linked list into k parts.
        """
        result = [None] * k

        # Step 1: Find length of the list
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next

        # Step 2: Determine base size and extra nodes
        base = n // k          # minimum size of each part
        extra = n % k          # first 'extra' parts get one more node

        curr = head

        # Step 3: Split the list
        for i in range(k):
            if not curr:
                result[i] = None
                continue

            result[i] = curr
            part_size = base + (1 if i < extra else 0)

            # Move to the last node of this part
            for _ in range(part_size - 1):
                curr = curr.next

            # Cut the list
            next_part = curr.next
            curr.next = None
            curr = next_part

        return result

# ------------------------------------
# Driver test
# ------------------------------------
# Input list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
head = ListNode(1)
curr = head
for i in range(2, 8):
    curr.next = ListNode(i)
    curr = curr.next

sol = Solution()
parts = sol.splitListToParts(head, 3)

# Print parts
for part in parts:
    curr = part
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print("None")
