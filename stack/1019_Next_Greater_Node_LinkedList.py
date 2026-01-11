"""
===========================================================
1019. Next Greater Node in Linked List
===========================================================

Approach: Monotonic Decreasing Stack (Right-to-Left)

The problem asks for the **next greater value to the RIGHT**
for each node in a singly linked list.

Since a linked list does not allow backward traversal,
we first convert it into an array to enable indexed access.

-----------------------------------------------------------
Algorithm:
-----------------------------------------------------------
1. Traverse the linked list and store all node values in an array `values`.
2. Initialize:
       • an empty stack (monotonic decreasing)
       • a result array initialized with 0s
3. Traverse the array from RIGHT to LEFT:
       • Pop elements from the stack while they are
         less than or equal to the current value
       • If the stack is not empty, the top element
         is the next greater value
       • Push the current value onto the stack
4. Return the result array.

-----------------------------------------------------------
Monotonic Stack Invariant:
-----------------------------------------------------------
• Stack maintains values in strictly decreasing order
• Top of stack always represents the nearest greater
  element to the right

-----------------------------------------------------------
Why Right-to-Left Works:
-----------------------------------------------------------
• Right side elements are already processed
• Stack contains only valid future candidates
• Each element is pushed and popped once

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(n)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(n)

-----------------------------------------------------------
Key Insight to Remember:
-----------------------------------------------------------
"Next greater to the right → monotonic decreasing stack.
Traverse from right to left and resolve using stack top."

===========================================================
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        # Convert linked list to array
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        n = len(values)
        result = [0] * n
        stack = []  # monotonic decreasing stack (values)

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= values[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(values[i])

        return result

# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------
def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


# ---------------------------------------------------------
# Test Cases
# ---------------------------------------------------------
def test_nextLargerNodes():
    sol = Solution()

    # Given examples
    head = build_linked_list([2, 1, 5])
    assert sol.nextLargerNodes(head) == [5, 5, 0]

    head = build_linked_list([2, 7, 4, 3, 5])
    assert sol.nextLargerNodes(head) == [7, 0, 5, 5, 0]

    # All increasing
    head = build_linked_list([1, 2, 3, 4])
    assert sol.nextLargerNodes(head) == [2, 3, 4, 0]

    # All decreasing
    head = build_linked_list([4, 3, 2, 1])
    assert sol.nextLargerNodes(head) == [0, 0, 0, 0]

    # Single node
    head = build_linked_list([10])
    assert sol.nextLargerNodes(head) == [0]

    # Empty list
    head = build_linked_list([])
    assert sol.nextLargerNodes(head) == []

    print("All test cases passed!")


# ---------------------------------------------------------
# Driver
# ---------------------------------------------------------
if __name__ == "__main__":
    test_nextLargerNodes()
