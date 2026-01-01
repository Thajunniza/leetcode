"""
708. Insert into a Sorted Circular Linked List

Given a node from a circular sorted linked list and a value insertVal,
insert insertVal into the list such that it remains sorted.
Return the original head of the list.
"""

# ------------------------------------
# Definition for a Node
# ------------------------------------
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# ------------------------------------
# Main Solution
# ------------------------------------
class Solution(object):
    def insert(self, head, insertVal):
        """
        Insert insertVal into a sorted circular linked list.
        """
        new_node = Node(insertVal)
        
        # Empty list
        if not head:
            new_node.next = new_node
            return new_node
        
        curr = head
        while True:
            # Case 1: insertVal fits between curr and curr.next
            if curr.val <= insertVal <= curr.next.val:
                break
            # Case 2: At boundary (largest -> smallest)
            if curr.val > curr.next.val:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    break
            # Move forward
            curr = curr.next
            # If full circle, break
            if curr == head:
                break
        
        # Insert new_node after curr
        new_node.next = curr.next
        curr.next = new_node
        
        return head

# ------------------------------------
# Driver test
# ------------------------------------
# Circular list: 3 -> 4 -> 1 -> back to 3
n1 = Node(3)
n2 = Node(4)
n3 = Node(1)
n1.next = n2
n2.next = n3
n3.next = n1
head = n1

sol = Solution()
head = sol.insert(head, 2)

# Print list for 6 nodes to show circular insertion
curr = head
for _ in range(6):
    print(curr.val, end="->")
    curr = curr.next
print("...")
