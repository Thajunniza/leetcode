"""
===========================================================
2674.Split a Circular Linked List
===========================================================

🧩 Problem:
You are given the head of a **circular singly linked list**.
Your task is to **split the list into two circular linked lists**.

Rules:
1. If the number of nodes is **even**, both halves have equal length.
2. If the number of nodes is **odd**, the **first list gets 1 extra node**.
3. Both resulting lists must remain **circular**.
4. Return the heads of both new circular lists.

🎯 Goal:
Split an existing circular linked list into:
    • First circular half  (head1)
    • Second circular half (head2)

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example:
Input:  1 → 2 → 3 → 4 → 5 → (back to 1)
Output:
    First List:  1 → 2 → 3 → (back to 1)
    Second List: 4 → 5 → (back to 4)

Explanation:
    n = 5 (odd)
    First list gets 3 nodes
    Second list gets 2 nodes

Example:
Input:  1 → 2 → 3 → 4 → (back to 1)
Output:
    First List:  1 → 2 → (back to 1)
    Second List: 3 → 4 → (back to 3)

-----------------------------------------------------------
Algorithm — Fast & Slow Pointer (Circular Version)
-----------------------------------------------------------

We use the classic "Tortoise & Hare" approach customized for
**circular** lists.

Steps:

-----------------------------------------------------------
Phase 1 — Find Middle (using circular stopping condition)
-----------------------------------------------------------
1. Initialize:
       slow = head
       fast = head

2. Move:
       slow = slow.next
       fast = fast.next.next

3. Stop when fast reaches either:
       • fast.next == head               (even length)
       • fast.next.next == head          (odd length)

At this point:
    • slow is at the **end of first half**
    • slow.next is the **start of second half**

-----------------------------------------------------------
Phase 2 — Create Two Circular Lists
-----------------------------------------------------------
1. First list:
       head1 = head
       slow.next = head1        → closes first circular list

2. Second list:
       head2 = slow.next
       Move fast appropriately to get to the last node, then:
       fast.next = head2        → closes second circular list

-----------------------------------------------------------
⏱ Time Complexity:  O(n)
💾 Space Complexity: O(1)
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
# Split a Circular Linked List
# ------------------------------------
def split_circular_linked_list(head):
    """
    Split a circular linked list into two circular halves.

    Returns:
        (head1, head2): heads of the two new circular lists.
    """
    if head is None or head.next == head:
        # 0 or 1 node: only one list is meaningful
        return head, None

    slow = head
    fast = head

    # --------------------------
    # Phase 1: Find the mid-point
    # --------------------------
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next

    # First half:
    head1 = head

    # Second half starts after slow
    head2 = slow.next

    # --------------------------
    # Phase 2: Close the second circular list
    # --------------------------
    if fast.next == head:
        # even number of nodes
        fast.next = head2
    else:
        # odd number of nodes
        fast = fast.next
        fast.next = head2

    # --------------------------
    # Phase 3: Close the first circular list
    # --------------------------
    slow.next = head1

    return head1, head2


# ------------------------------------
# Driver Code (Optional)
# ------------------------------------
if __name__ == "__main__":
    # Helper to build circular linked list
    def build_circular(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        curr = head
        for x in arr[1:]:
            curr.next = ListNode(x)
            curr = curr.next
        curr.next = head  # Make it circular
        return head

    head = build_circular([1, 2, 3, 4, 5])
    a, b = split_circular_linked_list(head)

    # Print first list
    print("List 1:", end=" ")
    p = a
    for _ in range(5):
        print(p.val, end="->")
        p = p.next
        if p == a:
            break
    print("...")

    # Print second list
    print("List 2:", end=" ")
    p = b
    for _ in range(5):
        print(p.val, end="->")
        p = p.next
        if p == b:
            break
    print("...")
