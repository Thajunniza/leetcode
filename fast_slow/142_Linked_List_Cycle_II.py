"""
===========================================================
142. Linked List Cycle II (Find Start of Cycle)
===========================================================

🧩 Problem:
Given the head of a linked list, return the node where the cycle begins.
If no cycle exists, return None.

You are *not* given the `pos` parameter in the function; it's only used
internally for testing. Your job is to detect the cycle **and** return the 
starting node of the cycle.

🎯 Goal:
Return the node where the cycle starts, or None if the list has no cycle.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Input:  head = [3,2,0,-4], pos = 1
Output: Node with value 2
Explanation: Tail connects to node index 1 (value = 2)

-----------------------------------------------------------
Algorithm — Floyd's Tortoise & Hare:
-----------------------------------------------------------
1️⃣ Phase 1 — Detect if a cycle exists  
    - Slow moves 1 step  
    - Fast moves 2 steps  
    - If slow == fast → cycle detected

2️⃣ Phase 2 — Find start node  
    - Move slow to head  
    - Move slow and fast one step at a time  
    - The point where they meet is the cycle start

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


# ------------------------------------
# Helper: Create cycle at position 'pos'
# pos = index where tail should connect
# pos = -1 → no cycle
# ------------------------------------
def create_cycle(head, pos):
    if pos == -1:
        return head

    curr = head
    cycle_node = None
    index = 0

    while curr.next:
        if index == pos:
            cycle_node = curr
        curr = curr.next
        index += 1

    curr.next = cycle_node  # create cycle
    return head


# ------------------------------------
# Solution: Return start of cycle
# ------------------------------------
class Solution:
    def detectCycle(self, head):
        slow = fast = head

        # Phase 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            # loop exited without break → no cycle
            return None

        # Phase 2: Find start of cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow   # start node of cycle

# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    arr = [3, 2, 0, -4]
    pos = 1  # tail connects to node at index 1

    head = build_linked_list(arr)
    head = create_cycle(head, pos)

    sol = Solution()
    start_node = sol.detectCycle(head)

    if start_node:
        print("Cycle starts at node with value:", start_node.val)
    else:
        print("No cycle detected")
