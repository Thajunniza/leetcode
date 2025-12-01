""" 
===========================================================
225. Implement Stack using Queues
===========================================================

🧩 Problem:
Design a stack using only **queue operations**.

You must support:
    - push(x): Push element x onto stack
    - pop(): Removes the element on top and returns it
    - top(): Returns the element on top
    - empty(): Returns True if the stack is empty

Allowed operations on the queue:
    • enqueue (append)
    • dequeue (popleft)
    • size
    • isEmpty

❗ You are NOT allowed to use built-in stack features.

🎯 Goal:
Simulate **LIFO** behavior (stack) using **FIFO** structure (queue).

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Input:
push(1)
push(2)
top() → 2
pop() → 2
empty() → False

-----------------------------------------------------------
Algorithm — Single Queue Rotation (Best Approach):
-----------------------------------------------------------

Core Idea:
To make `pop()` remove the last inserted element,  
we can **rotate** the queue:

Steps:
1. push(x): Add x to queue normally  
2. pop():
       - Move the first (n-1) elements to the back of the queue
       - The last inserted element now becomes front
       - Pop it using popleft()
3. top(): Simply return the last element of the queue
4. empty(): Check if queue is empty

This simulates the LIFO order perfectly.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

push() : O(1)  
pop()  : O(n)  (because of rotation)  
top()  : O(1)  
empty(): O(1)

Space Complexity: O(n)

-----------------------------------------------------------
"""

from collections import deque

class MyStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, x):
        """
        Push element x onto stack.
        """
        self.q.append(x)

    def pop(self):
        """
        Removes the top element (LIFO).
        We rotate the queue so that the last pushed element comes to the front.
        """
        # Move first n-1 elements to the back
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

        # Now the front is the top of the stack
        return self.q.popleft()

    def top(self):
        """
        Get the top element.
        """
        return self.q[-1] if self.q else None

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


# ------------------------------------
# Driver Test
# ------------------------------------
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())   # 2
print(obj.pop())   # 2
print(obj.empty()) # False

