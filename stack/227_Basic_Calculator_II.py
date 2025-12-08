"""
===========================================================
227. Basic Calculator II
===========================================================

🧩 Problem:
You are given a string `s` representing a valid arithmetic expression that contains:
    • non-negative integers
    • operators: `+`, `-`, `*`, `/`
    • and spaces

Evaluate the expression and return the **integer result**.

Important details:
    • There are **no parentheses** in the expression.
    • The expression is always valid.
    • Division is **integer division truncated toward zero** (e.g., `-3/2 -> -1`).

🎯 Goal:
Compute the expression’s value following standard operator precedence:
    • `*` and `/` have higher precedence than `+` and `-`.
    • Operators are left-associative within the same precedence level.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "3+2*2"
Compute:
    2*2 = 4
    3 + 4 = 7

Output: 7


Example 2:
Input:  s = " 3/2 "
Compute:
    3/2 = 1 (truncate toward zero)

Output: 1


Example 3:
Input:  s = " 3+5 / 2 "
Compute:
    5/2 = 2 (truncate)
    3 + 2 = 5

Output: 5


Example 4:
Input:  s = "14-3/2"
Compute:
    3/2 = 1 (truncate)
    14 - 1 = 13

Output: 13

-----------------------------------------------------------
Approach A — Stack (One Pass, Simple & Reliable):
-----------------------------------------------------------

Pattern: 📚 Use a stack to handle precedence on the fly.

We scan the string once, building numbers and applying the **previous operator** (`last_op`) when we encounter a new operator or reach the end:

- Maintain:
  1️⃣ `num`: current number being parsed from digits.
  2️⃣ `last_op`: previous operator (start with `'+'`).
  3️⃣ `stack`: list of partial terms respecting precedence:
     • On `+`: push `+num`
     • On `-`: push `-num`
     • On `*`: pop top `t`, push `t * num`
     • On `/`: pop top `t`, push `truncate(t / num)` toward zero

Why it works:
- Multiplication/division are applied immediately to the latest term (stack top), preserving precedence.
- Addition/subtraction are deferred by pushing signed values to be summed later.

Division truncation toward zero:
- In Python, use `int(a / b)` (not `//`) to truncate toward zero.

⏱ Complexity:
- Time: `O(n)` — single pass.
- Space: `O(n)` — worst-case when many `+`/`-` terms.

-----------------------------------------------------------
Python Implementation (Stack):
-----------------------------------------------------------
"""


class SolutionStack:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        last_op = '+'

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            # apply when we see an operator or we are at the end
            if ch in '+-*/' or i == len(s) - 1:
                if last_op == '+':
                    stack.append(num)
                elif last_op == '-':
                    stack.append(-num)
                elif last_op == '*':
                    prev = stack.pop()
                    stack.append(prev * num)
                elif last_op == '/':
                    prev = stack.pop()
                    stack.append(int(prev / num))  # truncate toward zero

                last_op = ch
                num = 0

        return sum(stack)
""" 
-----------------------------------------------------------
Approach B — O(1) Extra Space (No Stack):
-----------------------------------------------------------

Pattern: 🧮 Track `result` and the `last_term` to honor precedence.

We keep:
  • `result`: sum of fully committed terms so far.
  • `last_term`: the most recent term waiting to be committed.
  • `num`: current number being parsed.
  • `last_op`: previous operator.

Processing rule when we hit an operator or end:
- On `+` or `-`:
  • First add `last_term` to `result`.
  • Then set `last_term = ±num` accordingly.
- On `*` or `/`:
  • Update `last_term = last_term * num` or `int(last_term / num)`.
  • Do **not** add to `result` yet (keep precedence).
At the end, return `result + last_term`.

Why it works:
- `last_term` holds the term under current precedence; multiplication/division modify it before committing.
- Addition/subtraction commit the previous `last_term` and start a new one.

⏱ Complexity:
- Time: `O(n)` — single pass.
- Space: `O(1)` — constant extra variables.

-----------------------------------------------------------
Python Implementation (O(1) Space):
-----------------------------------------------------------
"""

class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        last_term = 0
        num = 0
        last_op = '+'

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            # Apply when operator is seen or we're at the end
            if ch in '+-*/' or i == len(s) - 1:
                if last_op == '+':
                    result += last_term
                    last_term = num
                elif last_op == '-':
                    result += last_term
                    last_term = -num
                elif last_op == '*':
                    last_term = last_term * num
                elif last_op == '/':
                    last_term = int(last_term / num)  # truncate toward zero

                last_op = ch
                num = 0

        return result + last_term

def run_tests():
    cases = [
        ("3+2*2", 7),
        (" 3/2 ", 1),
        (" 3+5 / 2 ", 5),
        ("14-3/2", 13),
        ("100-20*3+4/2", 42),
        ("0", 0),
        ("1+2*3-4/2", 5),  # 1 + 6 - 2 = 5
        ("10/3+10/(-3)".replace("(-3)", "-3"), 3 + (-3)),  # 3 + (-3) = 0 (shows trunc toward zero)
    ]
    sO1 = Solution()
    sStack = SolutionStack()
    for expr, expected in cases:
        r1 = sO1.calculate(expr)
        r2 = sStack.calculate(expr)
        print(f"{expr!r}: O(1)={r1}, Stack={r2}, Expected={expected}, OK={r1==expected and r2==expected}")

if __name__ == "__main__":
    run_tests()
