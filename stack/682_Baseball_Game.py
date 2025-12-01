"""
===========================================================
682. Baseball Game
===========================================================

🧩 Problem:
You are given a list of operations representing a scoring system.

Each operation is one of the following:

1. Integer x:
       Add x as a new score.
2. "+":
       Add a new score equal to the sum of the previous two scores.
3. "D":
       Add a new score equal to double the previous score.
4. "C":
       Invalidate (remove) the previous score.

All operations are guaranteed to be valid.

🎯 Goal:
Return the sum of all valid scores after processing all operations.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  ["5","2","C","D","+"]
Stack process:
    5 → [5]
    2 → [5,2]
    C → [5]
    D → [5,10]
    + → [5,10,15]
Output: 30

Example 2:
Input: ["1","C"]
Output: 0

-----------------------------------------------------------
Algorithm — Stack:
-----------------------------------------------------------

Use a stack to store valid scores:
- Integer → int(op), push to stack
- "C" → pop last score
- "D" → push double of last score
- "+" → push sum of last two scores

At the end, sum stack.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)  
Space Complexity:  O(n)

-----------------------------------------------------------
"""

class Solution(object):
    def calPoints(self, operations):
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()

            elif op == "D":
                stack.append(2 * stack[-1])

            elif op == "+":
                stack.append(stack[-1] + stack[-2])

            else:
                stack.append(int(op))

        return sum(stack)


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.calPoints(["5","2","C","D","+"]))  # 30
    print(sol.calPoints(["1","C"]))              # 0
    print(sol.calPoints(["5","-2","4","C","D","9","+","+"])) # 27
