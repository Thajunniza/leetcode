"""
===========================================================
394. Decode String
===========================================================

🧩 Problem:
You are given an encoded string `s`. The encoding rule is:
    - `k[encoded_string]` means the `encoded_string` inside the square brackets
      is repeated exactly `k` times.
    - `k` is a positive integer.
    - The input string is always valid.
    - Nested encoding is allowed.

Examples:
    - "3[a]" → "aaa"
    - "3[a2[c]]" → "accaccacc"

🎯 Goal:
Decode the string and return it.

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
Algorithm — Stack-Based Approach (Your Logic):
-----------------------------------------------------------

Core Idea:
Use a single stack to store:
    - numbers (repeat counts)
    - opening brackets '['
    - characters / decoded substrings

A temporary list `substr` is used to collect characters when decoding
a bracketed expression.

Steps:
1. Initialize:
       stack = []      # holds numbers, '[', and strings
       substr = []     # collects substring during decoding
       num = 0         # builds multi-digit repeat counts

2. Iterate through each character `c` in `s`:
       - If `c` is a digit:
             • Build the full number using:
               num = num * 10 + int(c)

       - If `c` == '[':
             • Push the current number to stack
             • Push '[' to mark the start of substring
             • Reset num = 0

       - If `c` == ']':
             • Pop elements from stack until '[' is found
             • Store popped characters in `substr`
             • Pop '['
             • Pop repeat count `k`
             • Reverse `substr`, join it, and repeat `k` times
             • Push decoded string back to stack
             • Reset `substr` and `num`

       - Else (alphabet character):
             • Push character onto stack

3. After traversal:
       - Join all elements in stack to form the final decoded string

Why this works:
- The stack preserves order and nesting.
- Each ']' defines a complete decoding scope.
- Reversing `substr` restores correct character order.
- Supports nested and multi-digit encodings.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n + output_size)
Space Complexity:  O(n + output_size)

-----------------------------------------------------------
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        substr = []
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
                continue
            if c == "[":
                stack.append(num)
                stack.append(c)
                num = 0
            elif c == "]":
                while stack and stack[-1] != "[":
                    substr.append(stack.pop())
                stack.pop()
                k = int(stack.pop())
                decoded = "".join(substr[::-1]) * k
                stack.append(decoded)
                substr = []
                num = 0
            else:
                stack.append(c)
        
        return "".join(stack)
    
    
sol = Solution()
print(sol.decodeString("3[a]2[bc]"))        # aaabcbc
print(sol.decodeString("3[a2[c]]"))         # accaccacc
print(sol.decodeString("2[abc]3[cd]ef"))    # abcabccdcdcdef
print(sol.decodeString("50[Thaj]"))          # Thaj repeated 50 times
