"""
===========================================================
234. Palindrome Linked List (Fast & Slow + List Reversal)
===========================================================

🧩 Problem:
Given the head of a singly linked list, determine whether the list 
is a palindrome.

A palindrome reads the same forward and backward.

🎯 Goal:
Return **True** if the linked list is a palindrome, otherwise **False**.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Input:  head = [1,2,2,1]
Output: True

Input:  head = [1,2]
Output: False

Input:  head = [1]
Output: True

-----------------------------------------------------------
Algorithm — Fast & Slow Pointer + Reverse Second Half:
-----------------------------------------------------------
1. Use two pointers:
      slow moves 1 step
      fast moves 2 steps
2. When fast reaches the end:
      slow is at the middle.
3. If fast is NOT null → the list has odd length:
      skip the middle node.
4. Reverse the second half of the list starting from slow.
5. Compare the first half and reversed second half node by node.
6. If all values match → palindrome.
7. Otherwise → not palindrome.

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
# Helper: Reverse a Linked List
# ------------------------------------
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nextNode = curr.next 
        curr.next = prev 
        prev = curr 
        curr = nextNode
    return prev




# ------------------------------------
# Solution: Check Palindrome Linked List
# ------------------------------------
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        # Edge Case: 0 or 1 node
        if not head or not head.next:
            return True

        # Step 1: Find middle (slow at middle)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Odd length → skip middle
        if fast:  
            slow = slow.next

        # Step 3: Reverse second half
        second_half = reverse_list(slow)

        # Step 4: Compare halves
        p1 = head
        p2 = second_half
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True
            
# ------------------------------------
# Driver Test
# ------------------------------------
def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    head = build_list([1, 2, 2, 1])
    sol = Solution()
    print(sol.isPalindrome(head))   # Expected Output: True
