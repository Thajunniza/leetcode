"""
===========================================================
1721. Swapping Nodes in a Linked List
===========================================================
Given the head of a singly linked list and an integer k, swap the values
of the kth node from the beginning and the kth node from the end.
Return the head of the linked list.

Approach:
---------
1. Find the kth node from the start.
2. Use two pointers to find the kth node from the end:
   - Move `fast` to the end while moving `slow` from head.
3. Swap the values of the two nodes.

Time Complexity:  O(n)  → traverse the list once  
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
    def swapNodes(self, head, k):
        """
        Swap values of kth node from start and kth node from end.
        """
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        # Step 1: Find kth node from start
        first_k = head
        for _ in range(k-1):
            first_k = first_k.next
        
        # Step 2: Find kth node from end
        slow = head
        fast = first_k
        while fast.next:
            slow = slow.next
            fast = fast.next
        second_k = slow
        
        # Step 3: Swap values
        first_k.val, second_k.val = second_k.val, first_k.val
        
        return head

# ------------------------------------
# Driver test
# ------------------------------------
head = build_linked_list([1, 2, 3, 4, 5])
sol = Solution()
sol.swapNodes(head, 2)

# Print list after swap
curr = head
while curr:
    print(curr.val, end="->" if curr.next else "\n")
    curr = curr.next

head_even = build_linked_list([1, 2, 3, 4])
sol.swapNodes(head_even, 1)

curr = head_even
while curr:
    print(curr.val, end="->" if curr.next else "\n")
    curr = curr.next
