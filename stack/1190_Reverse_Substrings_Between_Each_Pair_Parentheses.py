"""
===========================================================
1190. Reverse Substrings Between Each Pair of Parentheses
===========================================================

🧩 Problem:
You are given a string s that consists of:
    - lowercase English letters
    - '(' and ')'

Your task:
Reverse the characters inside each pair of matching parentheses,  
starting from the **innermost** pair and moving outward.

Return the final string with **all parentheses removed** after processing.

🎯 Goal:
Correctly reverse nested parentheses using a stack.
Time: O(n), Space: O(n).

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "(abcd)"
Output: "dcba"

Example 2:
Input:  s = "(u(love)i)"
Output: "iloveu"

Explanation:
    Innermost: "(love)" → "evol"
    Then: "(u evol i)" → "iloveu"

Example 3:
Input:  s = "(ed(et(oc))el)"
Output: "leetcode"

Example 4:
Input:  s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"

-----------------------------------------------------------
Algorithm — Stack of Lists (Optimal for Google):
-----------------------------------------------------------

Core Idea:
Use a **stack** where each level is a list of characters.

- When '(' appears → start a new level by pushing an empty list.
- When ')' appears:
      • pop the current list,
      • reverse it,
      • append it to the previous list.
- When letters appear → append them to the current list.

This handles nesting naturally (LIFO), and using lists keeps the solution O(n).

Steps:
1️⃣ Initialize: stack = [[]]  
2️⃣ For each character:
       - '(' → push new []
       - ')' → pop, reverse, extend into previous
       - letter → append to current list
3️⃣ Final answer = join characters in stack[0]

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)  
    - Each character is processed a constant number of times.

Space Complexity:  O(n)  
    - Stack levels and result storage.

-----------------------------------------------------------
"""

class Solution(object):
    def reverseParentheses(self, s):
        """
        Reverse substrings between each pair of parentheses.
        Uses a stack of lists for O(n) performance.
        """
        stack = [[]]  # Each level holds characters for that depth

        for ch in s:
            if ch == '(':
                stack.append([])  # Start new level
            elif ch == ')':
                temp = stack.pop()  # Finish this level
                temp = temp[::-1]      # Reverse substring
                stack[-1].extend(temp)  # Append to previous level
            else:
                stack[-1].append(ch)  # Add normal characters

        return "".join(stack[0])

# ------------------------------------
# Driver Test
# ------------------------------------
sol = Solution()
print(sol.reverseParentheses("(abcd)"))                 # dcba
print(sol.reverseParentheses("(u(love)i)"))             # iloveu
print(sol.reverseParentheses("(ed(et(oc))el)"))         # leetcode
print(sol.reverseParentheses("a(bcdefghijkl(mno)p)q"))  # apmnolkjihgfedcbq
