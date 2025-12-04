"""
===========================================================
946. Validate Stack Sequences
===========================================================

🧩 Problem:
You are given two integer arrays:

    pushed = sequence of values pushed onto a stack (in order)
    popped = sequence of values popped from the stack (in order)

We start with an empty stack and perform **push** and **pop** operations.

🎯 Goal:
Return True if `popped` **could be** the result of popping from the stack after
pushing elements in the order of `pushed`.
Otherwise, return False.

In other words:
Is there some valid sequence of stack operations (push & pop) that:
    • pushes elements in exactly the order of `pushed`
    • pops elements in exactly the order of `popped`?

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]

Simulation:
    push 1 → [1]
    push 2 → [1, 2]
    push 3 → [1, 2, 3]
    push 4 → [1, 2, 3, 4]
    pop 4  → [1, 2, 3]
    push 5 → [1, 2, 3, 5]
    pop 5  → [1, 2, 3]
    pop 3  → [1, 2]
    pop 2  → [1]
    pop 1  → []

All pops match popped in order → True.

Output: True


Example 2:
Input:
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]

No valid sequence of pushes/pops can produce this `popped`.
For example, once 1 is popped, 2 cannot still be in the stack **below** it.

Output: False

-----------------------------------------------------------
Algorithm — Stack Simulation:
-----------------------------------------------------------

We simulate the process:

    • Use a stack.
    • Use a pointer j for popped (initially 0).

For each value x in pushed:
    1) push x onto stack
    2) while stack is not empty AND top of stack == popped[j]:
           pop from stack
           j += 1

Why this works:
    • Every time the top of the stack matches the next required popped value,
      we pop it immediately.
    • We only push in the order of `pushed`.
    • If after processing all pushes we managed to pop every element in `popped`
      (i.e., j == len(popped)), the sequence is valid.

If some elements in `popped` are not matched, it's invalid.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    • Each element is pushed and popped at most once.

Space Complexity:  O(n)
    • Stack may hold up to n elements.


"""

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0  # pointer for popped

        for x in pushed:
            stack.append(x)
            # Try to pop as long as the top matches the next popped element
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        # If we matched all elements in popped, it's a valid sequence
        return j == len(popped)


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    # Expected: True

    print(sol.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
    # Expected: False

    print(sol.validateStackSequences([], []))
    # Expected: True

    print(sol.validateStackSequences([1], [1]))
    # Expected: True
