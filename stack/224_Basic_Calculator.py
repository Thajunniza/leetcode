"""
===========================================================
224. Basic Calculator
===========================================================

🧩 Problem:
Evaluate a mathematical expression string containing:
    • integers
    • '+', '-'
    • parentheses '(' and ')'
    • spaces

The expression is always valid and must be computed with:
    • correct operator precedence
    • correct handling of nested parentheses
    • support for multi-digit numbers

Important:
No multiplication or division is present in this version.

🎯 Goal:
Return the final evaluated integer using a **stack-based expression parser**.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Input:  "1 + 1"
Output: 2

Input:  " 2-1 + 2 "
Output: 3

Input:  "(1+(4+5+2)-3)+(6+8)"
Output: 23

-----------------------------------------------------------
Algorithm — Stack-Based Expression Evaluation:
-----------------------------------------------------------

Core Idea:
Use:
    • `total` → running sum at current parenthesis level
    • `sign`  → +1 or -1 for the next number
    • `num`   → currently building multi-digit number
    • `stack` → stores previous (total, sign) before '('

Processing rules:
1. Digit:
       Build multi-digit number: num = num * 10 + digit
2. '+' or '-':
       Flush previous number into total using sign
       Reset num and update sign
3. '(':
       Push current (total, sign) onto stack
       Reset total = 0 and sign = +1 for new sub-expression
4. ')':
       Flush last num into total
       Pop sign and previous total from stack
       Combine them: total = prev_total + (prev_sign * total)
5. End of string:
       Add last pending num into total

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)  
Space Complexity:  O(n) due to stack for nested parentheses

-----------------------------------------------------------
Python Implementation:
-----------------------------------------------------------

"""
class Solution:
    def calculate(self, s: str) -> int:
        total = 0
        num = 0
        sign = 1
        stack = []

        for c in s:
            if c == " ":
                continue

            if c.isdigit():
                num = num * 10 + int(c)

            elif c == "+":
                total += num * sign
                num = 0
                sign = 1

            elif c == "-":
                total += num * sign
                num = 0
                sign = -1

            elif c == "(":
                stack.append(total)
                stack.append(sign)
                total = 0
                sign = 1

            elif c == ")":
                total += num * sign
                num = 0
                total *= stack.pop()   # previous sign
                total += stack.pop()   # previous total

        return total + num * sign

# -----------------------------------------------------------
# Driver Test
# -----------------------------------------------------------
s = "(1+(4+5+2)-3)+(6+8)"
print(Solution().calculate(s))   # 23

