"""===========================================================
439. Ternary Expression Parser
===========================================================

🧩 Problem:
You are given a **ternary expression** as a string `expression`.

The expression uses:
    • Condition: 'T' (true) or 'F' (false)
    • Ternary operator:  `? :`
    • Values: single characters (digits or letters), e.g. '1', '2', 'a', etc.

Ternary format:
    condition ? expr1 : expr2

Expressions can be **nested**, for example:
    "T?T?1:2:F?3:4"

Evaluation rules:
    • If condition is 'T', choose the **first** expression (before ':').
    • If condition is 'F', choose the **second** expression (after ':').

The entire expression is guaranteed to be valid and will reduce to a **single character**.

🎯 Goal:
Evaluate the ternary expression and return the final result as a **single-character string**.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  expression = "T?2:3"

Process:
    T ? 2 : 3
    Condition = 'T' → choose "2"

Output:
    "2"


Example 2:
Input:  expression = "F?1:T?4:5"

Process:
    F ? 1 : (T ? 4 : 5)
    First step:
        Condition = 'F' → choose right side: "T?4:5"
    Now evaluate "T?4:5":
        Condition = 'T' → choose "4"

Final result = "4"

Output:
    "4"


Example 3:
Input:  expression = "T?T?1:2:3"

Grouping:
    T ? (T ? 1 : 2) : 3

Step-by-step:
    Inner: T ? 1 : 2 → 1
    Outer: T ? 1 : 3 → 1

Output:
    "1"

-----------------------------------------------------------
Algorithm — Stack + Right-to-Left Scan
-----------------------------------------------------------

Key idea:
    Ternary operators are **right-associative**:
        a ? b : c ? d : e
    is grouped from the right.

This makes it natural to:
    1. Scan the string from **right to left**.
    2. Use a **stack** to hold values and separators ('?' and the result values).

Algorithm:
    • Initialize an empty stack.
    • Iterate `i` from len(expression) - 1 down to 0:
        - Let `c = expression[i]`.

        1) If c == ':'
               → Just skip it (it's only a separator).

        2) Else if stack is not empty and stack[-1] == '?':
               → We found the pattern:   condition ? true_expr : false_expr
                 on the stack as:        '?', true_value, false_value

               Steps:
                    - Pop '?'.
                    - Pop true_val (first popped).
                    - Pop false_val (second popped).
                    - If current char `c` is 'T':
                          push true_val
                      Else (c == 'F'):
                          push false_val

        3) Else:
               → Push `c` onto the stack.

    • At the end, the stack will contain exactly one element:
        stack[-1] → final result (single character).

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    • Single pass through the expression, each character pushed/popped at most once.

Space Complexity:  O(n)
    • Stack stores at most all characters in the expression in the worst case.

-----------------------------------------------------------
Python Solution (Stack + Right-to-Left)
-----------------------------------------------------------
"""

class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        i = len(expression) - 1

        while i >= 0:
            c = expression[i]

            if c == ":":
                i -= 1
                continue

            # If top is '?', then together with current c we can resolve one ternary
            if stack and stack[-1] == "?":
                stack.pop()                 # remove '?'
                true_val = stack.pop()      # value if condition is 'T'
                false_val = stack.pop()     # value if condition is 'F'

                if c == "T":
                    stack.append(true_val)
                else:
                    stack.append(false_val)
            else:
                # Regular character (value, 'T', 'F', or '?')
                stack.append(c)

            i -= 1

        # Final result is the only value left on the stack
        return stack[-1]


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.parseTernary("T?2:3"))
    # Expected: "2"

    print(sol.parseTernary("F?1:T?4:5"))
    # Expected: "4"

    print(sol.parseTernary("T?T?1:2:3"))
    # Expected: "1"

    print(sol.parseTernary("F?T?1:2:3"))
    # Grouping: F ? (T ? 1 : 2) : 3 → F ? 1/2 : 3 → "3"
    # Expected: "3"

    print(sol.parseTernary("T?F?1:2:F?3:4"))
    # You can trace nested decisions; the stack will handle it correctly.
