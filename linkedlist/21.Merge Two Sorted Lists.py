"""
21 - Merge Two Sorted Lists

Description:
You are given the heads of two sorted linked lists, list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Approach:
Iterative Two-Pointer with Dummy Node.
- Create a 'dummy' node to act as the starting point of the new list.
- Use a 'current' pointer to build the new list.
- Compare the values at the heads of list1 and list2; attach the smaller node to 'current.next'.
- Move the pointer of the chosen list and the 'current' pointer forward.
- Once one list is empty, attach the remainder of the other list directly (O(1) operation).

Time Complexity:
O(n + m), where n and m are the lengths of the two lists. We visit each node exactly once.

Space Complexity:
O(1), as we are rearranging existing nodes and not creating new ones (excluding the dummy node).
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # res acts as the dummy head, dummy is our moving pointer
        res = ListNode(0)
        dummy = res
        
        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        # Optimization: Just link the rest of the non-empty list
        # No loop needed because it's already sorted and linked!
        if list1:
            dummy.next = list1
        else:
            dummy.next = list2
            
        return res.next

# -------------------- Discussion --------------------
# For a test run, you would typically build the linked lists from arrays:
# L1: 1 -> 2 -> 4
# L2: 1 -> 3 -> 4
# Result: 1 -> 1 -> 2 -> 3 -> 4 -> 4
