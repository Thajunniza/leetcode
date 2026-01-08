"""
===========================================================
1106. Parsing A Boolean Expression
===========================================================

🧩 Problem:
Evaluate a boolean expression string containing:
    • 't' (true) or 'f' (false)
    • Operators: 
        - '!' → NOT
        - '&' → AND
        - '|' → OR
    • Parentheses '(' and ')' to denote sub-expressions
    • Commas ',' as separators

The expression is always valid. Operators can be nested arbitrarily.

🎯 Goal:
Return the final boolean value (True/False) using a **stack-based expression parser**.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Input:  "!(f)"
Output: True

Input:  "|(&(t,f,t),!(t))"
Output: False

Input:  "&(t,|(f,t))"
Output: True

-----------------------------------------------------------
Algorithm — Stack-Based Expression Evaluation:
-----------------------------------------------------------

Core Idea:
Use a **stack** to parse characters and evaluate sub-expressions when a ')' is encountered.

Processing rules:
1. Skip commas ','.
2. Push every other character onto the stack.
3. When encountering ')':
   a. Pop characters until '(' to collect the sub-expression.
   b. Pop the operator before '('.
   c. Apply the operator:
        - '&' → AND all sub-expression values
        - '|' → OR all sub-expression values
        - '!' → NOT the single sub-expression value
   d. Push the result ('t' or 'f') back onto the stack.
4. Continue until the expression is fully parsed.
5. Final result is stack[-1] == 't'.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)  # each character pushed/popped at most once
Space Complexity:  O(n)  # stack

-----------------------------------------------------------
Python Implementation:
-----------------------------------------------------------
"""

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        def parseAnd(vals):
            for v in vals:
                if v == "f":
                    return "f"
            return "t"

        def parseOr(vals):
            for v in vals:
                if v == "t":
                    return "t"
            return "f"

        def parseNot(val):
            return "t" if val == "f" else "f"

        stack = []
        expr = []

        for c in expression:
            if c == ",":
                continue
            elif c == ")":
                # Pop all characters until '('
                while stack and stack[-1] != "(":
                    expr.append(stack.pop())
                stack.pop()  # remove '('
                op = stack.pop()  # operator

                if op == "&":
                    stack.append(parseAnd(expr))
                elif op == "|":
                    stack.append(parseOr(expr))
                elif op == "!":
                    stack.append(parseNot(expr[0]))

                expr = []

            else:
                stack.append(c)

        return stack[-1] == "t" if stack else False

# -----------------------------------------------------------
# Driver Tests
# -----------------------------------------------------------
tests = [
    "!(f)",
    "|(&(t,f,t),!(t))",
    "&(t,|(f,t))"
]

for t in tests:
    print(f"{t} => {Solution().parseBoolExpr(t)}")
