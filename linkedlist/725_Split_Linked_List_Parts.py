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
        # Edge Case
        if not head:
            return result
        n = 0
        curr = head
        # Get the count length
        while curr:
            n += 1
            curr = curr.next
        # Calculate the elemnts
        extra = n % k
        count = n // k
        curr = head
        #Split based on calculation
        for i in range(k):
            if not curr:
                continue
            final = count + 1 if i < extra else count
            result[i] = curr
            for _ in range(final-1):
                if not curr.next:
                    break
                curr = curr.next
            if curr:
                temp = curr.next
                curr.next = None
                curr = temp
            else:
                break
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
