"""
===========================================================
150. Evaluate Reverse Polish Notation
===========================================================

🧩 Problem:
You are given an array of strings `tokens` that represents an arithmetic expression
in Reverse Polish Notation (RPN).

Valid operators are: "+", "-", "*", "/".
Each operand may be an integer or another expression.

Rules:
    • RPN means operator comes **after** its operands:
          ["2", "1", "+", "3", "*"]  → (2 + 1) * 3
    • Division between two integers should **truncate toward zero**.
    • There will be no division by zero.
    • The input is always a valid RPN expression.

🎯 Goal:
Evaluate the expression and return the result as an integer.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  tokens = ["2","1","+","3","*"]
Process:
    2  → [2]
    1  → [2, 1]
    +  → pop 1, 2 → 2 + 1 = 3  → [3]
    3  → [3, 3]
    *  → pop 3, 3 → 3 * 3 = 9  → [9]

Output: 9


Example 2:
Input:  tokens = ["4","13","5","/","+"]
Process:
    4   → [4]
    13  → [4, 13]
    5   → [4, 13, 5]
    /   → pop 5, 13 → 13 / 5 = 2 (truncate) → [4, 2]
    +   → pop 2, 4 → 4 + 2 = 6 → [6]

Output: 6


Example 3:
Input:  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
You just mechanically follow stack operations; final result is 22.

Output: 22

-----------------------------------------------------------
Algorithm — Stack Evaluation:
-----------------------------------------------------------

RPN is naturally evaluated using a stack.

For each token t in tokens:
    • If t is a number:
          → Convert to int and push onto stack.
    • If t is an operator (+, -, *, /):
          → Pop the top two numbers:  b = stack.pop(), a = stack.pop()
          → Compute a (op) b
          → Push result back onto stack.

At the end:
    The stack will contain exactly one value → the final result.

⚠ Important detail for division:
    LeetCode expects "truncate toward zero" behavior:
        -3 / 2 → -1
    Using a // b does floor division:
        -3 // 2 → -2  (WRONG)
    So we must do:
        int(a / b)  # this truncates toward zero

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    • Each token is processed exactly once.

Space Complexity:  O(n)
    • Stack may store up to n/2 numbers in worst-case.

-----------------------------------------------------------
"""

from typing import List


class Solution:
    def operation(self, a: int, b: int, op: str) -> int:
        """
        Applies the arithmetic operation `op` on operands `a` and `b`.

        Args:
            a (int): First operand (left).
            b (int): Second operand (right).
            op (str): Operator, one of "+", "-", "*", "/".

        Returns:
            int: Result of a (op) b.
        """
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            # Truncate toward zero as per problem statement
            return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates the value of an arithmetic expression in Reverse Polish Notation.

        Args:
            tokens (List[str]): List of tokens (operands and operators).

        Returns:
            int: Evaluated result of the expression.
        """
        stack: List[int] = []

        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                # Pop in correct order: a is left operand, b is right operand
                b = stack.pop()
                a = stack.pop()
                result = self.operation(a, b, t)
                stack.append(result)
            else:
                # Token is a number
                stack.append(int(t))

        return stack[-1]


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.evalRPN(["2", "1", "+", "3", "*"]))
    # Expected: 9

    print(sol.evalRPN(["4", "13", "5", "/", "+"]))
    # Expected: 6

    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    # Expected: 22

    print(sol.evalRPN(["3", "-4", "/"]))
    # 3 / -4 = 0.75 → truncate toward zero → 0
    # Expected: 0
