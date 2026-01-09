
"""
===========================================================
Score of Parentheses
===========================================================

🧩 Problem:
Given a **balanced parentheses string** `s` consisting only of `'('` and `')'`, compute its **score** based on the rules:

- `"()"` has score **1**.
- `AB` has score **A + B**, where `A` and `B` are balanced parentheses strings.
- `(A)` has score **2 × A**, where `A` is a balanced parentheses string.

🎯 Goal:
Return the **integer score** of `s`.
Use an **O(n) time, O(1) space** approach (depth-based), or alternatively a **stack-based** approach with O(n) time and O(n) space.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "()"
Output: 1
Reason: "()" = 1.

Example 2:
Input:  s = "()()"
Output: 2
Reason: "()" + "()" = 1 + 1 = 2.

Example 3:
Input:  s = "(())"
Output: 2
Reason: "(())" = 2 × 1 = 2.

Example 4:
Input:  s = "(()(()))"
Output: 6
Reason: Inside outer parentheses: "()(())" = 1 + 2 = 3, so outer ⇒ 2 × 3 = 6.

Example 5:
Input:  s = "(((())))"
Output: 8
Reason: 2 × (2 × (2 × 1)) = 8.

-----------------------------------------------------------
Algorithm — Depth-Based (O(1) space):
-----------------------------------------------------------

Core idea:
Every primitive pair "()" contributes 2^depth **after** we close it, where depth is the current nesting level *after* processing ')'.
We detect a primitive pair when the current character is ')' and the previous character is '('.

Steps:
1. Initialize depth = 0, total = 0.
2. Iterate characters with index i:
   - If s[i] == '(': increment depth.
   - Else (a closing bracket):
       - Decrement depth.
       - If s[i-1] == '(' (we just closed "()"), add 2^depth to total.
3. Return total.

Why this works:
- For "()" at depth d (before reading ')'), its contribution is 2^(d-1).
  After decrementing depth on ')', depth == d-1, so we add 2^depth.
- Summing these contributions respects both concatenation (A + B) and nesting (2 × A).

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

- Time Complexity:   O(n)
  We scan the string once; each character results in O(1) work.

- Space Complexity:  O(1) (depth-based)
  Only a few integers are maintained.

(Alternative stack approach uses O(n) space but is also linear time.)
"""

class Solution(object):
    def scoreOfParentheses(self, s):
        """
        Depth-based implementation: O(n) time, O(1) space.

        :type s: str
        :rtype: int
        """
        depth = 0
        total = 0
        for i, c in enumerate(s):
            if c == '(':
                depth += 1
            else:
                depth -= 1
                # If we just closed a primitive "()", add 2^depth
                if s[i - 1] == '(':
                    total += 1 << depth  # faster than 2 ** depth
        return total


# ------------------------------------
# Alternative — Stack-Based Implementation (Optional)
# ------------------------------------
class SolutionStack(object):
    def scoreOfParentheses(self, s):
        """
        Stack-based implementation: O(n) time, O(n) space.

        :type s: str
        :rtype: int
        """
        stack = [0]  # base frame score
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                v = stack.pop()
                # "()" contributes 1; "(A)" contributes 2*A
                stack[-1] += max(2 * v, 1)
        return stack[0]


# ------------------------------------
# Driver Tests
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.scoreOfParentheses("()"))         # 1
    print(sol.scoreOfParentheses("()()"))       # 2
    print(sol.scoreOfParentheses("(())"))       # 2
    print(sol.scoreOfParentheses("(()(()))"))   # 6
    print(sol.scoreOfParentheses("(((())))"))   # 8
    print(sol.scoreOfParentheses("()(())"))     # 3

    # Optional: Compare with stack-based solution
    sol_stack = SolutionStack()
    print(sol_stack.scoreOfParentheses("()"))         # 1
    print(sol_stack.scoreOfParentheses("()()"))       # 2
    print(sol_stack.scoreOfParentheses("(())"))       # 2
    print(sol_stack.scoreOfParentheses("(()(()))"))   # 6
    print(sol_stack.scoreOfParentheses("(((())))"))   # 8
    print(sol_stack.scoreOfParentheses("()(())"))     # 3
