"""

===========================================================
32. Longest Valid Parentheses
===========================================================

🧩 Problem:
Given a string `s` consisting of only the characters:
  - `'('` and `')'`

Find the **length of the longest** substring of `s` that is a valid parentheses sequence.

A valid parentheses sequence is one where:
1. Every opening bracket `'('` has a corresponding closing bracket `')'`
2. Brackets are closed in the **correct order**
3. No closing bracket appears before its matching opening bracket

🎯 Goal:
Return the **maximum length** of any valid (well-formed) parentheses substring.  
Use an **O(n)** time approach with either **O(1)** or **O(n)** extra space.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  `s = "(()"`
Output: `2`  
Explanation: The longest valid substring is `"()"`.

Example 2:
Input:  `s = ")()())"`
Output: `4`  
Explanation: The longest valid substring is `()()`.

Example 3:
Input:  `s = ""`
Output: `0`

Example 4:
Input:  `s = "()(())"`
Output: `6`  
Explanation: The entire string is valid.

Example 5:
Input:  `s = ")()())()()("`
Output: `4`

-----------------------------------------------------------
Algorithm — Two-Pass Counter (O(1) Space):
-----------------------------------------------------------

Core idea:
Scan the string **left-to-right** and **right-to-left**, counting how many `'('` and `')'` we’ve seen.  
Whenever counts are equal, we have a balanced substring and can update the maximum length.  
We reset if any side outnumbers the other in a direction where it cannot be balanced further.

Steps:
1. **Left-to-right pass:**
   - Maintain `left` (count of `'('`) and `right` (count of `')'`).
   - If `left == right`, update `max_len = max(max_len, 2 * right)`.
   - If `right > left`, reset both to zero (too many closings).

2. **Right-to-left pass:**
   - Reset `left = right = 0`.
   - Iterate from the end to the start.
   - If `left == right`, update `max_len = max(max_len, 2 * left)`.
   - If `left > right`, reset both to zero (too many openings).

Why this works:
- The first pass handles cases with extra `')'` on the left (which cannot be matched).
- The second pass handles cases with extra `'('` on the right.
- Together, they ensure all longest balanced segments are considered.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

- **Time Complexity:** `O(n)`  
  We scan the string twice; each character is processed in constant time.

- **Space Complexity:** `O(1)`  
  Only counters and a maximum tracker are used.

-----------------------------------------------------------

"""


def longestValidParentheses(s):
    # Left-to-right pass
    left = right = 0
    max_len = 0
    for c in s:
        if c == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_len = max(max_len, 2 * right)
        elif right > left:
            left = right = 0

    # Right-to-left pass
    left = right = 0
    for c in reversed(s):
        if c == ')':
            right += 1
        else:
            left += 1
        if left == right:
            max_len = max(max_len, 2 * left)
        elif left > right:
            left = right = 0

    return max_len


def longestValidParentheses_stack(s):
    max_len = 0
    stack = []
    last_invalid = -1  # boundary before the start of a potential valid substring

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:  # c == ')'
            if stack:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    max_len = max(max_len, i - last_invalid)
            else:
                last_invalid = i

    return max_len

print(longestValidParentheses("(()"))          # 2
print(longestValidParentheses(")()())"))       # 4
print(longestValidParentheses(""))             # 0
print(longestValidParentheses("()"))           # 2
print(longestValidParentheses("()(())"))       # 6
print(longestValidParentheses(")()())()()("))  # 4

print(longestValidParentheses_stack("(()"))          # 2
print(longestValidParentheses_stack(")()())"))       # 4
print(longestValidParentheses_stack(""))             # 0
print(longestValidParentheses_stack("()"))           # 2
print(longestValidParentheses_stack("()(())"))       # 6
print(longestValidParentheses_stack(")()())()()("))  # 4
