"""
===========================================================
155. Min Stack
===========================================================

🧩 Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Operations:
    - push(x): Push element x onto stack.
    - pop(): Removes the element on top of the stack.
    - top(): Get the top element.
    - getMin(): Retrieve the minimum element in the stack.

🎯 Goal:
All operations should be O(1).

-----------------------------------------------------------
Algorithm — Two-Stack Approach:
-----------------------------------------------------------
Use two stacks:
    - Main stack to store all elements.
    - Min stack to store the minimum value at each level.

Steps:
1. On push:
       - Push value to main stack.
       - If min stack empty or val <= min_stack[-1], push val to min stack.
2. On pop:
       - Pop from main stack.
       - If popped value equals min_stack[-1], pop from min stack.
3. top(): Return last element of main stack.
4. getMin(): Return last element of min stack.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------
Time Complexity:   O(1) for all operations
Space Complexity:  O(n)

-----------------------------------------------------------
"""

class MinStack(object):
    def __init__(self):
        self.items = []  # Main stack
        self.min = []    # Stack to keep track of minimum values

    def push(self, val):
        """
        Push an element onto the stack.
        :type val: int
        :rtype: None
        """
        self.items.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)

    def pop(self):
        """
        Remove the top element from the stack.
        :rtype: None
        """
        if self.items:
            val = self.items.pop()
            if self.min and val == self.min[-1]:
                self.min.pop()

    def top(self):
        """
        Get the top element of the stack.
        :rtype: int or None
        """
        return self.items[-1] if self.items else None

    def getMin(self):
        """
        Retrieve the minimum element in the stack.
        :rtype: int or None
        """
        return self.min[-1] if self.min else None


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    obj = MinStack()
    obj.push(3)
    obj.push(5)
    obj.push(2)
    print(obj.getMin())  # Expected: 2
    obj.pop()
    print(obj.getMin())  # Expected: 3
    print(obj.top())     # Expected: 5
