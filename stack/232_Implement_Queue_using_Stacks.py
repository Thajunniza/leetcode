"""
===========================================================
232. Implement Queue using Stacks
===========================================================

🧩 Problem:
Design a queue using only **stack operations**.

You must implement:
    - push(x): Push element to the back of queue
    - pop(): Remove the element from the front of queue
    - peek(): Get the front element
    - empty(): Check if the queue is empty

Valid stack operations you may use:
    • push
    • pop
    • peek (top element)
    • isEmpty

🎯 Goal:
Simulate **FIFO queue** behavior using **LIFO stacks**.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Input:
push(1)
push(2)
peek() → 1
pop() → 1
empty() → False

-----------------------------------------------------------
Algorithm — Two Stack Method (Optimal for Google):
-----------------------------------------------------------

Use two stacks:

    - inStack  → handle push operations
    - outStack → handle pop/peek operations

Logic:
1️⃣ push(x):
        Push to inStack directly.

2️⃣ pop():
        If outStack is empty:
            Move ALL elements from inStack → outStack
        Now pop from outStack (front of queue).

3️⃣ peek():
        Same logic as pop, but return top instead of removing.

4️⃣ empty():
        Queue is empty only if BOTH stacks are empty.

Why this works:
- inStack stores newest elements.
- outStack stores elements in reversed order (front at top).
- We only move elements **when needed**, making amortized cost **O(1)**.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

push():   O(1)  
pop():    Amortized O(1)  
peek():   Amortized O(1)  
empty():  O(1)

Space Complexity: O(n)

-----------------------------------------------------------
"""

class MyQueue(object):

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x):
        """
        Push element x to the back of the queue.
        """
        self.inStack.append(x)

    def pop(self):
        """
        Removes and returns the element at the front of the queue.
        If outStack is empty, refill it from inStack.
        """
        self._move()
        return self.outStack.pop()

    def peek(self):
        """
        Returns the front element without removing it.
        """
        self._move()
        return self.outStack[-1]

    def empty(self):
        """
        Returns True if the queue is empty.
        """
        return not self.inStack and not self.outStack

    def _move(self):
        """
        Move elements from inStack to outStack only when needed.
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())


# ------------------------------------
# Driver Test
# ------------------------------------
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())   # 1
print(obj.pop())    # 1
print(obj.empty())  # False
