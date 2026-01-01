"""
===========================================================
328. Odd Even Linked List
===========================================================
Given the head of a singly linked list, group all odd-indexed nodes together followed by even-indexed nodes.
Indexing starts at 1. You must do this **in-place** without modifying node values.

Approach:
---------
1. **Initialize pointers**:
   - `odd` points to the first node
   - `even` points to the second node
   - `even_head` stores the start of the even nodes for later connection
2. **Traverse and rearrange**:
   - Connect `odd.next` to `even.next` (next odd node)
   - Move `odd` pointer to `odd.next` (skips one node automatically)
   - Connect `even.next` to `odd.next` (next even node)
   - Move `even` pointer to `even.next`
3. **Connect the end of odd list to even_head**.

Time Complexity:  O(n)  → traverse each node once  
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
    def oddEvenList(self, head):
        """
        Rearrange linked list so all odd-indexed nodes come first, then even-indexed nodes.
        """
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even
        
        while even and even.next:
            # Connect current odd to the next odd node
            odd.next = even.next
            odd = odd.next       # odd pointer moves forward, skipping one node naturally
            
            # Connect current even to the next even node
            even.next = odd.next
            even = even.next
        
        # Connect the end of odd list to the head of even nodes
        odd.next = even_head
        return head

# ------------------------------------
# Driver test
# ------------------------------------
head = build_linked_list([1, 2, 3, 4, 5])
sol = Solution()
sol.oddEvenList(head)

# Print reordered list
curr = head
while curr:
    print(curr.val, end="->" if curr.next else "\n")
    curr = curr.next

head_even = build_linked_list([1, 2, 3, 4])
sol.oddEvenList(head_even)

curr = head_even
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next
