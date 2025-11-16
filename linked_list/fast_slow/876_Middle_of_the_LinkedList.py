"""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node.
If there are two middle nodes (even length), return the second.

Approach:
---------
Use the Fast–Slow Pointer Technique:
- Slow pointer moves 1 step at a time.
- Fast pointer moves 2 steps at a time.
When fast reaches the end, slow will be at the middle.
This automatically gives the SECOND middle for even-length lists.

Time Complexity:  O(n)  → we traverse each node once
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
# Main Solution using Fast–Slow Pointers
# ------------------------------------
class Solution(object):
    def middleNode(self, head):
        """
        Fast–Slow Pointer Technique:
        - fast moves 2 nodes at a time
        - slow moves 1 node at a time
        - when fast reaches end, slow reaches the middle
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next       # move 1 step
            fast = fast.next.next  # move 2 steps

        return slow   # slow is the middle node


# ------------------------------------
# Driver test
# ------------------------------------
head = build_linked_list([1, 2, 3, 4, 5])
sol = Solution()
middleNode = sol.middleNode(head)
print(middleNode.val)   # Output: 3
