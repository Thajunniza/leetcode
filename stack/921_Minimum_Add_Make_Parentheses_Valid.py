""" 
===========================================================
921. Minimum Add to Make Parentheses Valid
===========================================================

🧩 Problem:
You are given a string `s` containing only the characters `'('` and `')'`.

Your task is to determine the **minimum number of parentheses** you must add so that the resulting string is a **valid parentheses string**.

A valid parentheses string is defined by:
    • `""` (empty) is valid
    • If `A` is valid, then `("(" + A + ")")` is valid
    • If `A` and `B` are valid, then `A + B` is valid

If the string is already valid, the answer is `0`.

🎯 Goal:
Return the **minimum number of parentheses** needed to add to make `s` valid.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "())"
Walkthrough:
    "(" → need one ')': balance = 1
    ")" → matches previous '(': balance = 0
    ")" → stray ')' → need one '(': additions = 1
Result: additions + balance = 1 + 0 = 1

Output: 1


Example 2:
Input:  s = "((("
Walkthrough:
    Three '(' → each needs a ')' later: balance = 3
Result: additions + balance = 0 + 3 = 3

Output: 3


Example 3:
Input:  s = "()"
Already valid → no additions needed.

Output: 0


Example 4:
Input:  s = "()))(("
Walkthrough:
    '('     → balance = 1
    ')'     → balance = 0
    ')'     → additions = 1 (need '(')
    ')'     → additions = 2 (need '(')
    '('     → balance = 1
    '('     → balance = 2
Result: additions + balance = 2 + 2 = 4

Output: 4

-----------------------------------------------------------
Algorithm — Balance Counter (O(1) space):
-----------------------------------------------------------

Pattern: ⚖️ Track unmatched '(' and stray ')'

We process the string left to right using two counters:

1️⃣ `balance`: counts **unmatched '('** seen so far.
    • When we see `'('`, increment `balance`.
    • When we see `')'`, if `balance > 0`, decrement `balance` (it matches a `'('`).

2️⃣ `additions`: counts how many `'('` we need to add for **stray `')'`**.
    • If we see `')'` and `balance == 0`, this `')'` is unmatched → increment `additions`.

At the end:
    • Any remaining `balance` unmatched `'('` each need a `')'`.

Final answer:
    additions + balance

This avoids a full stack and keeps everything in O(1) space.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Let n = length of s.

Time Complexity:   O(n)
    - Single pass through the string.

Space Complexity:  O(1)
    - Uses only two integer counters.

-----------------------------------------------------------
Python Implementation:
-----------------------------------------------------------
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0    # unmatched '('
        additions = 0  # needed '(' for stray ')'
        
        for ch in s:
            if ch == '(':
                balance += 1
            else:  # ch == ')'
                if balance > 0:
                    balance -= 1
                else:
                    additions += 1  # need to add '(' to match this ')'
        
        # remaining unmatched '(' need closing ')'
        return additions + balance


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.minAddToMakeValid("())"))      # Expected: 1
    print(sol.minAddToMakeValid("((("))      # Expected: 3
    print(sol.minAddToMakeValid("()"))       # Expected: 0
    print(sol.minAddToMakeValid("()))(("))   # Expected: 4
    print(sol.minAddToMakeValid(""))         # Expected: 0
    print(sol.minAddToMakeValid(")("))       # Expected: 2

""" -----------------------------------------------------------
Alternative — Stack-Based (for clarity):
-----------------------------------------------------------

Maintain a stack of '(' and count stray ')'. At the end, the stack length equals
the number of unmatched '(' (needing ')').

This is equally O(n) time but uses O(n) space in the worst case.

"""

class SolutionStack:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        additions = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:  # ')'
                if stack:
                    stack.pop()
                else:
                    additions += 1  # need '(' for this stray ')'
        return additions + len(stack)
