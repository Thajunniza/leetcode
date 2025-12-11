"""
===========================================================
19. Remove nth Node from End of List
===========================================================

🧩 Problem:
Given the head of a singly linked list and an integer n, remove the nth node from the end of the list
and return the head of the modified list.

🎯 Goal:
Return the modifed head.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

-----------------------------------------------------------
Algorithm — Two Pointers:
-----------------------------------------------------------
1. Initialize left and right pointers pointing to the linked list’s head.
2. Move the right pointer n steps forward
3. If the right pointer has reached the end of the list, i.e., NULL, it means the head is the target node for removal.
In this case, return head.next as the new head of the linked list. 
4. Otherwise, move left and right pointers forward one step at a time.
5. Once the right pointer reaches the end of the linked list, update left.next to left.next.next
6. Finally, return the head, pointing to the updated linked list with the nth node removed.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""


# ------------------------------------
# Definition for singly-linked list node
# ------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ------------------------------------
# Helper: Build a linked list (no cycle)
# ------------------------------------
def build_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for n in arr:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next

def print_list(head, limit=30):
    curr = head
    steps = 0
    while curr and steps < limit:
        print(curr.val, end=' -> ')
        curr = curr.next
        steps += 1
    if curr:
        print('... (cycle or long list)')
    else:
        print('None')

# ------------------------------------
# Remove nth Node from End of List
# head = singly linked list 
# n = nth node from the end of the list
# return head of modified list
# ------------------------------------
def remove_nth_last_node(head, n):
    # Point two pointers, right and left, at head.
    right = head
    left = head

    # Move right pointer n elements away from the left pointer.
    for i in range(n):
        right = right.next
    
    # Removal of the head node.
    if not right:
        return head.next
    
    # Move both pointers until right pointer reaches the last node.
    while right.next:
        right = right.next
        left = left.next

        # At this point, left pointer points to (n-1)th element.
        # So link it to next to next element of left.
    left.next = left.next.next

    return head


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    arr = [3, 2, 0, -4]
    pos = 2  # tail connects to node at index 1

    head = build_linked_list(arr)
    head = remove_nth_last_node(head, pos)
    print(print_list(head))

