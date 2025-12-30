"""
===========================================================
1474. Delete N Nodes After M Nodes of Linked List
===========================================================

🧩 Problem:
Given the head of a linked list and two integers `m` and `n`,
delete `n` nodes after keeping `m` nodes repeatedly until the end 
of the list, and return the modified list.

🎯 Goal:
Skip `m` nodes and delete next `n` nodes in a cyclic manner
until the list ends.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input: head = [1,2,3,4,5,6,7,8,9], m = 2, n = 3
Output: [1,2,6,7]

Example 2:
Input: head = [1,2,3,4,5], m = 1, n = 1
Output: [1,3,5]

Example 3:
Input: head = [1,2,3], m = 3, n = 2
Output: [1,2,3]

-----------------------------------------------------------
Algorithm (Skip and Delete Nodes):
-----------------------------------------------------------

1. Start from head pointer `curr`
2. While `curr` exists:
      - Skip `m-1` nodes (stop at m-th node)
      - Delete next `n` nodes by skipping pointers
      - Link current m-th node to the node after deleted nodes
3. Continue the process until reaching the end
4. Return head

🧠 Key Insight:
Use pointer manipulation in-place to delete nodes efficiently.
No extra memory is needed.

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
# 1474. Delete N Nodes After M Nodes
# Linked List Pattern
# ------------------------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: Optional[ListNode]
        :type m: int
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr = head
        
        while curr:
            # Step 1: Skip m-1 nodes (stop at m-th node)
            for _ in range(m - 1):
                if not curr:
                    return head
                curr = curr.next
            
            # If curr is None or no next node, break
            if not curr or not curr.next:
                return head
            
            # Step 2: Delete next n nodes starting from curr.next
            temp = curr.next
            for _ in range(n):
                if not temp:
                    break
                temp = temp.next
            
            # Step 3: Connect m-th node to remaining list
            curr.next = temp
            
            # Move curr pointer forward
            curr = temp
        
        return head

# ------------------------------------
# Driver Test
# ------------------------------------
def print_list(node):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print("->".join(vals))


# Test Case
head = ListNode(1,
        ListNode(2,
        ListNode(3,
        ListNode(4,
        ListNode(5,
        ListNode(6,
        ListNode(7,
        ListNode(8,
        ListNode(9)))))))))

m, n = 2, 3
sol = Solution()
new_head = sol.deleteNodes(head, m, n)
print_list(new_head)  # Expected: 1 -> 2 -> 6 -> 7
