""" 
===========================================================
1249. Minimum Remove to Make Valid Parentheses
===========================================================

🧩 Problem:
Given a string s consisting of:
    - lowercase English letters
    - '(' and ')'

Your task is to **remove the minimum number of parentheses** so that the resulting string is a **valid parentheses string**.

You can remove characters from **any position** in the string.
Return **any valid result**.

A valid parentheses string:
    - "" (empty string) is valid
    - "abc", "a(b)c", "(abc)" are valid
    - Every '(' must have a matching ')' **after** it
    - No ')' can appear without a matching '(' before it

🎯 Goal:
Remove the **minimum** number of '(' or ')' to make the string valid,  
using O(n) time and O(n) space.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"

Explanation:
    Remove the last ')' to make it valid.

Example 2:
Input:  s = "a)b(c)d"
Output: "ab(c)d"

Explanation:
    Remove the extra ')' after 'a'.

Example 3:
Input:  s = "))(("
Output: ""

Explanation:
    We must remove all characters.

Example 4:
Input:  s = "(a(b(c)d)"
Output: "a(b(c)d)" or "(a(bc)d)"   (any valid result is fine)

-----------------------------------------------------------
Algorithm — Stack of Indices + Rebuild:
-----------------------------------------------------------

Core idea:
We only care about **mismatched parentheses**:
    - ')' that has no matching '(' before it
    - '(' that is never closed by a ')'

Steps:
1. Convert s to a list of characters `chars` (easier to modify).
2. Create an empty stack to store indices of `'('`.
3. Iterate over i, ch in enumerate(chars):
       - If ch == '(':
            • push index i to stack
       - Else if ch == ')':
            • If stack not empty:
                  - pop one '(' index from stack (we matched this ')')
              Else:
                  - this ')' is **unmatched** → mark it for removal
                  - easiest: set chars[i] = ''  (empty string)
       - Else: letter → ignore, keep as is

4. After the loop:
       - Any indices left in stack are `'('` that were never matched.
       - For each index i in stack:
             • set chars[i] = ''  (remove these '(')

5. Join and return `"".join(chars)`.

Why this works:
- We only remove:
      • ')' that don’t have an opening '(' before
      • '(' that are left unmatched
- That’s the **minimum** number of removals to make the string valid.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)  
    - Single pass to identify invalid parentheses.
    - One more pass (implicit in join).

Space Complexity:  O(n)  
    - Stack for indices of '('.
    - List of characters.

-----------------------------------------------------------
"""

class Solution(object):
    def minRemoveToMakeValid(self, s):
        chars = list(s)
        stack = []  # stores indices of '('

        # First pass: handle invalid ')'
        for i, ch in enumerate(chars):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()   # match with a previous '('
                else:
                    # Unmatched ')' → remove it
                    chars[i] = ''

        # Second pass: remove any unmatched '(' left in stack
        while stack:
            idx = stack.pop()
            chars[idx] = ''

        # Build final string
        return "".join(chars)
    

# ------------------------------------
# Driver Test
# ------------------------------------
sol = Solution()
print(sol.minRemoveToMakeValid("lee(t(c)o)de)")) # lee(t(c)o)de
print(sol.minRemoveToMakeValid("a)b(c)d")) # ab(c)d
print(sol.minRemoveToMakeValid("))((")) # ''
print(sol.minRemoveToMakeValid("(a(b(c)d)")) # a(b(c)d) or similar