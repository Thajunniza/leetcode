"""
===========================================================
394. Decode String
===========================================================

🧩 Problem:
You are given an encoded string `s`. The encoding rule is:
    - `k[encoded_string]` means the `encoded_string` inside the square brackets
      is repeated exactly `k` times.
    - `k` is a positive integer.
    - You may assume that the input string is always valid and contains no extra spaces.
    - Nested encoding is allowed.

Examples:
    - "3[a]" → "aaa"
    - "3[a2[c]]" → "accaccacc"

🎯 Goal:
Decode the string and return it.
Time: O(n), Space: O(n).

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input:  s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input:  s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

-----------------------------------------------------------
Algorithm — Stack-Based Approach:
-----------------------------------------------------------

Core idea:
Use a stack to handle nested brackets and repeated sequences.

Steps:
1. Initialize:
       stack = [[]]   # acts as a stack of lists
       num = 0        # to accumulate digits for multiplier

2. Iterate through each character `c` in `s`:
       - If `c` is a digit:
             • Update num = num * 10 + int(c)
       - If `c` == '[':
             • Push num and a new empty list onto stack
             • Reset num = 0
       - If `c` == ']':
             • Pop the last list (chars) and multiplier
             • Repeat chars * multiplier and append to previous list
       - Else (alphabet):
             • Append character to current list

3. Join the first list in stack to form the final decoded string.

Why this works:
- The stack keeps track of nested sequences.
- When we hit ']', we know the scope of repetition and can expand it.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)  
Space Complexity:  O(n)  

-----------------------------------------------------------
"""

class Solution(object):
    def decodeString(self, s):
        stack = [[]]
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append(num)
                stack.append([])
                num = 0
            elif c == "]":
                chars = stack.pop()
                repeat = stack.pop()
                stack[-1].extend(chars * repeat)
            else:
                stack[-1].append(c)

        return "".join(stack[0])

# ------------------------------------
# Driver Test
# ------------------------------------

sol = Solution()
print(sol.decodeString("3[a]2[bc]"))       # aaabcbc
print(sol.decodeString("3[a2[c]]"))        # accaccacc
print(sol.decodeString("2[abc]3[cd]ef"))   # abcabccdcdcdef
print(sol.decodeString("50[Thaj]"))   # abcabccdcdcdef