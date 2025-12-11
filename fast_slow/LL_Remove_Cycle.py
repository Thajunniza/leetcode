"""
===========================================================
Linked List Cycle IV — Remove Cycle (Fast & Slow)
===========================================================

🧩 Problem:
You are given the head of a singly linked list. The list may contain a cycle
(i.e., a node's next pointer points back to some previous node).

Your task:
    ➤ Detect whether a cycle exists
    ➤ If a cycle exists, REMOVE the cycle
    ➤ Return the head of the fixed (acyclic) linked list

The test case will provide:
    • an array of values (to build the list)
    • an index 'pos' where the tail connects to form a cycle
      (or -1 if no cycle)
These are used ONLY to construct the input — NOT used in your function.


🎯 Goal:
Modify the linked list so that any cycle is completely removed,
leaving a properly terminating list (ending at None).


-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  head = [3, 2, 0, -4], pos = 1
Cycle:  -4 → 2
Output: head becomes:
        3 → 2 → 0 → -4 → None

Example 2:
Input:  head = [1, 2], pos = 0
Cycle:  2 → 1
Output:
        1 → 2 → None

Example 3:
Input:  head = [1], pos = -1
Cycle:  none
Output:
        1 → None


-----------------------------------------------------------
Algorithm — Fast & Slow Pointer + Find Tail of Cycle:
-----------------------------------------------------------

To remove the cycle, we perform **three phases**:

-----------------------------------------------------------
Phase 1 — Detect Cycle Using Floyd’s Algorithm
-----------------------------------------------------------
1. Initialize:
       slow = head
       fast = head

2. Move pointers:
       slow = slow.next
       fast = fast.next.next

3. If slow == fast:
       → cycle detected
   If fast or fast.next becomes None:
       → no cycle → return head as-is


-----------------------------------------------------------
Phase 2 — Find the Start of the Cycle
-----------------------------------------------------------
1. Reset slow to head.
2. Move slow & fast one step at a time:
       slow = slow.next
       fast = fast.next
3. When slow == fast:
       → both are pointing to the first node of the cycle
       call this node 'start'


-----------------------------------------------------------
Phase 3 — Break the Cycle
-----------------------------------------------------------
1. To remove the cycle, we must find the **last node** in the cycle,
   i.e., the node whose:
       tail.next == start

2. From 'start', move one pointer until:
       while node.next != start:
            node = node.next

3. This 'node' is the cycle tail.
4. Set:
       node.next = None
   → This breaks the cycle.


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
# Solution: Remove Cycle from Linked List
# ------------------------------------
class Solution:
    def remove_cycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow = head
        fast = head

        # --------------------------
        # Phase 1: Detect cycle
        # --------------------------
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # No cycle
        if not fast or not fast.next:
            return
