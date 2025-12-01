""" 
===========================================================
1021. Remove Outermost Parentheses
===========================================================

🧩 Problem:
A valid parentheses string is a string that:
    - Is empty ""
    - Or can be written as AB (A and B are valid)
    - Or can be written as (A), where A is valid

A **primitive** parentheses string is a non-empty valid string that cannot be split
into two non-empty valid strings.

Example primitives:
    - "()" 
    - "()()"  ❌ (not primitive, can split into "()" + "()" )
    - "(())"  ✅ primitive

You are given a valid parentheses string s.

Your task:
- Split s into one or more **primitive** valid parentheses strings.
- For **each primitive**, remove its **outermost pair** of parentheses.
- Concatenate the result and return it.

🎯 Goal:
Return the string after removing the **outermost parentheses** of every primitive.
Time: O(n), Space: O(n).

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "(()())(())"
Output: "[]()()"  (just to visualize)
Actual: "()()()"

Explanation:
    Primitive splits:
        "(()())"  +  "(())"
    Remove outermost:
        "(()())" → "()()"
        "(())"   → "()"
    Final: "()()()" 

Example 2:
Input:  s = "(()())(())(()(()))"
Output: "[]()()[]()()()" (visual)
Actual: "()()()()(())"

Explanation:
    Primitive splits:
        "(()())" + "(())" + "(()(()))"
    Remove outermost:
        "(()())"   → "()()"
        "(())"     → "()"
        "(()(()))" → "()(())"
    Final: "()()()()(())"

Example 3:
Input:  s = "()()"
Output: "" (empty primitives inside)
Explanation:
    Primitives: "()" + "()"
    Removing outermost from each → "" + "" → "".

-----------------------------------------------------------
Algorithm — Track Depth (Counter Instead of Full Stack):
-----------------------------------------------------------

Core idea:
We don’t actually need to store the parentheses, only track **nesting level**.

Steps:
1. Initialize:
       result = []
       depth = 0

2. Iterate through each character c in s:
       - If c == '(':
             • If depth > 0:
                    - This '(' is **not** outermost → append to result
             • Increment depth by 1

       - If c == ')':
             • Decrement depth by 1 **first**
             • If depth > 0:
                    - This ')' is **not** outermost → append to result

3. Join result to build final string.

Why this works:
- Outermost '(' is the one that makes depth go from 0 → 1
- Outermost ')' is the one that makes depth go from 1 → 0
- We **skip** these outermost ones and keep the inner ones.

(You can think of depth as a “stack size” without actually storing values.)

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)  
Space Complexity:  O(n)  

-----------------------------------------------------------
"""

class Solution(object):
    def removeOuterParentheses(self, s):
        result = []
        depth = 0

        for c in s:
            if c == '(':
                # If depth > 0, this '(' is not outermost → keep it
                if depth > 0:
                    result.append(c)
                depth += 1
            else:  # c == ')'
                depth -= 1
                # After decreasing, if depth > 0, this ')' is not outermost
                if depth > 0:
                    result.append(c)

        return "".join(result)

# ------------------------------------
# Driver Test
# ------------------------------------


sol = Solution()
print(sol.removeOuterParentheses("(()())(())")) # ()()()
print(sol.removeOuterParentheses("(()())(())(()(()))")) # ()()()()(())
print(sol.removeOuterParentheses("()()")) # ''