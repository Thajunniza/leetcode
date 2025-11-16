"""
===========================================================
141. Linked List Cycle (Floyd’s Tortoise & Hare Algorithm)
===========================================================

🧩 Problem:
Given the head of a linked list, determine if the list contains a cycle.
A cycle occurs if any node can be reached again by continuously following
the next pointer.

The internal variable `pos` (not provided in input) indicates where the 
tail connects, but our function must detect the cycle without using `pos`.

🎯 Goal:
Return True if a cycle exists, otherwise return False.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Input:  head = [3,2,0,-4], pos = 1
Output: True
Explanation: Tail connects to node index 1 (value = 2)

Input:  head = [1,2], pos = 0
Output: True
Explanation: Tail connects to index 0

Input:  head = [1], pos = -1
Output: False

-----------------------------------------------------------
Algorithm — Floyd's Fast & Slow Pointers:
-----------------------------------------------------------
1. Slow moves 1 step at a time.
2. Fast moves 2 steps at a time.
3. If fast and slow ever meet → cycle exists.
4. If fast reaches null → no cycle.

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

    curr.next = cycle_node
    return head


# ------------------------------------
# Solution: Detect Cycle
# ------------------------------------
class Solution:
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # Pointers met → cycle exists
                return True

        return False


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    arr = [3, 2, 0, -4]
    pos = 1  # tail connects to node at index 1

    head = build_linked_list(arr)
    head = create_cycle(head, pos)

    sol = Solution()
    print(sol.hasCycle(head))   # Expected Output: True
