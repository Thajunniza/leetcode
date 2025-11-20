"""
===========================================================
Linked List Cycle III — Length of Cycle (Fast & Slow)
===========================================================

🧩 Problem:
You are given the head of a singly linked list.

Somewhere in the list, the tail may connect back to a previous node, forming
a cycle. Your job is to determine the **length of the cycle**.

If there is:
- a cycle → return the number of nodes in the cycle.
- no cycle → return 0.

Note:
The test case input usually gives:
  - an array of node values
  - an index 'pos' where the tail connects (or -1 if no cycle)
This 'pos' is only used to construct the list and is NOT passed to the function.

🎯 Goal:
Return the **length of the cycle** in the linked list.
If there is no cycle, return **0**.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  head = [3, 2, 0, -4], pos = 1
Cycle:  tail connects to node with value 2
Output: 3
Explanation:
   The cycle is: 2 → 0 → -4 → 2 (3 nodes)

Example 2:
Input:  head = [1, 2], pos = 0
Cycle:  tail connects to node with value 1
Output: 2

Example 3:
Input:  head = [1], pos = -1
Cycle:  no cycle
Output: 0

-----------------------------------------------------------
Algorithm — Fast & Slow Pointer (Floyd) + Count Length:
-----------------------------------------------------------
1. Use two pointers:
      slow moves 1 step at a time
      fast moves 2 steps at a time

2. Move both pointers inside a loop:
      while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
          if slow == fast:
              a) A cycle is detected
              b) Break out of the loop

3. If the loop finishes because fast or fast.next became None:
      → There is NO cycle → return 0.

4. If a cycle is detected:
      - Keep one pointer at the meeting node (say 'slow').
      - Move another pointer around the cycle, counting nodes until
        it comes back to 'slow'.

      Steps:
        count = 1
        curr = slow.next
        while curr != slow:
            curr = curr.next
            count += 1

5. Return 'count' as the length of the cycle.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
   (At most one full traversal + one loop around the cycle)

💾 Space Complexity:  O(1)
   (Only a few pointer variables and a counter)
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
# Solution: Count Length of Cycle in Linked List
# ------------------------------------
class Solution:
    def count_cycle_length(self, head: ListNode) -> int:
        """
        Return the length of the cycle in the linked list.
        If there is no cycle, return 0.
        """
        if not head or not head.next:
            return 0

        slow = head
        fast = head

        # Phase 1: Detect cycle using fast & slow pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Cycle detected → measure its length
                return self._measure_cycle_length(slow)

        # No cycle
        return 0

    def _measure_cycle_length(self, meet_node: ListNode) -> int:
        """
        Given a node inside the cycle (meet_node),
        walk the cycle once to count its length.
        """
        count = 1
        curr = meet_node.next

        while curr != meet_node:
            curr = curr.next
            count += 1

        return count


# ------------------------------------
# Helper: Build Linked List with Optional Cycle
# ------------------------------------
def build_cyclic_list(values, pos):
    """
    Build a linked list from `values` and create a cycle at index `pos`.

    Args:
        values (List[int]): node values
        pos (int): index where tail connects; -1 for no cycle

    Returns:
        ListNode: head of the constructed (possibly cyclic) linked list
    """
    if not values:
        return None

    dummy = ListNode()
    curr = dummy
    cycle_node = None

    for index, val in enumerate(values):
        curr.next = ListNode(val)
        curr = curr.next
        if index == pos:
            cycle_node = curr

    # Create cycle if pos is valid
    if pos != -1:
        curr.next = cycle_node

    return dummy.next


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    # Example: head = [3, 2, 0, -4], pos = 1
    head = build_cyclic_list([3, 2, 0, -4], pos=1)
    sol = Solution()
    print(sol.count_cycle_length(head))   # Expected Output: 3
