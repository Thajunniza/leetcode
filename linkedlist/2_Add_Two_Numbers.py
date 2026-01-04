"""
===========================================================
2. Add Two Numbers
===========================================================

🧩 Problem:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

-----------------------------------------------------------
Example :
-----------------------------------------------------------
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Explanation: 9999999 + 9999 = 10009998

-----------------------------------------------------------
Brute Force Approach: Convert to Numbers
-----------------------------------------------------------
1. Convert linked list l1 to integer num1
2. Convert linked list l2 to integer num2
3. Calculate sum = num1 + num2
4. Convert sum back to linked list in reverse order

Problems:
- Can cause integer overflow for very large numbers
- Not efficient as it requires multiple passes
-----------------------------------------------------------
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  O(max(m, n))
Space: O(max(m, n))

-----------------------------------------------------------
🧠 Better Approach: Simulate Addition with Carry
-----------------------------------------------------------
Key Insight:
Since digits are already in reverse order, we can add them directly 
from left to right, just like manual addition!

Algorithm:
1. Create a dummy head node to simplify result list construction
2. Initialize carry = 0
3. Use current pointer to build result list
4. While l1 or l2 or carry exists:
   - Get values from l1 and l2 (0 if None)
   - Calculate sum = val1 + val2 + carry
   - Calculate new digit = sum % 10
   - Calculate new carry = sum // 10
   - Create new node with digit value
   - Move pointers forward
5. Return dummy.next

Edge Cases:
- Different length lists
- Final carry (e.g., 99 + 1 = 100)
- One or both lists are [0]

Example Walkthrough:
l1 = [2,4,3] (represents 342)
l2 = [5,6,4] (represents 465)

Step 1: 2 + 5 + 0 = 7, digit = 7, carry = 0
Step 2: 4 + 6 + 0 = 10, digit = 0, carry = 1
Step 3: 3 + 4 + 1 = 8, digit = 8, carry = 0
Result: [7,0,8] (represents 807)

-----------------------------------------------------------
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  O(max(m, n)) where m, n are lengths of l1 and l2
Space: O(max(m, n)) for the result linked list

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create dummy head to simplify result list construction
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Process both lists and carry
        while l1 or l2 or carry:
            # Get values from current nodes (0 if None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10
            
            # Create new node with digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next

# -----------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------
def createLinkedList(values):
    """
    Create a linked list from a list of values.
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    
    return head

def linkedListToList(head):
    """
    Convert linked list to Python list for easy display.
    """
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

def linkedListToNumber(head):
    """
    Convert linked list to actual number (for verification).
    """
    number = 0
    multiplier = 1
    curr = head
    while curr:
        number += curr.val * multiplier
        multiplier *= 10
        curr = curr.next
    return number

# -----------------------------------------------------------
# Driver Examples
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: 342 + 465 = 807
    print("=== Example 1 ===")
    l1 = createLinkedList([2, 4, 3])
    l2 = createLinkedList([5, 6, 4])
    result = sol.addTwoNumbers(l1, l2)
    print(f"Input: l1 = {linkedListToList(l1)}, l2 = {linkedListToList(l2)}")
    print(f"Output: {linkedListToList(result)}")
    print(f"Verification: {linkedListToNumber(l1)} + {linkedListToNumber(l2)} = {linkedListToNumber(result)}")
    print(f"Expected: [7,0,8]")
    
    # Example 2: 0 + 0 = 0
    print("\n=== Example 2 ===")
    l1 = createLinkedList([0])
    l2 = createLinkedList([0])
    result = sol.addTwoNumbers(l1, l2)
    print(f"Input: l1 = {linkedListToList(l1)}, l2 = {linkedListToList(l2)}")
    print(f"Output: {linkedListToList(result)}")
    print(f"Expected: [0]")
    
    # Example 3: 9999999 + 9999 = 10009998
    print("\n=== Example 3 ===")
    l1 = createLinkedList([9, 9, 9, 9, 9, 9, 9])
    l2 = createLinkedList([9, 9, 9, 9])
    result = sol.addTwoNumbers(l1, l2)
    print(f"Input: l1 = {linkedListToList(l1)}, l2 = {linkedListToList(l2)}")
    print(f"Output: {linkedListToList(result)}")
    print(f"Verification: {linkedListToNumber(l1)} + {linkedListToNumber(l2)} = {linkedListToNumber(result)}")
    print(f"Expected: [8,9,9,9,0,0,0,1]")
    
    # Example 4: Different lengths
    print("\n=== Example 4 ===")
    l1 = createLinkedList([9, 9])
    l2 = createLinkedList([1])
    result = sol.addTwoNumbers(l1, l2)
    print(f"Input: l1 = {linkedListToList(l1)}, l2 = {linkedListToList(l2)}")
    print(f"Output: {linkedListToList(result)}")
    print(f"Verification: {linkedListToNumber(l1)} + {linkedListToNumber(l2)} = {linkedListToNumber(result)}")
    print(f"Expected: [0,0,1]")
    
    # Example 5: Final carry
    print("\n=== Example 5 ===")
    l1 = createLinkedList([5])
    l2 = createLinkedList([5])
    result = sol.addTwoNumbers(l1, l2)
    print(f"Input: l1 = {linkedListToList(l1)}, l2 = {linkedListToList(l2)}")
    print(f"Output: {linkedListToList(result)}")
    print(f"Verification: {linkedListToNumber(l1)} + {linkedListToNumber(l2)} = {linkedListToNumber(result)}")
    print(f"Expected: [0,1]")