"""
===========================================================
20. Valid Parentheses
===========================================================

🧩 Problem:
Given a string s containing just the characters:
    - '(' , ')'  
    - '{' , '}'  
    - '[' , ']'

Determine whether the input string is **valid**.

A string is valid if:
1. Every opening bracket has a corresponding closing bracket  
2. Brackets are closed in the **correct order**  
3. A closing bracket cannot appear before its matching opening bracket  

🎯 Goal:
Return True if the string represents a **valid sequence of brackets**,  
otherwise return False. Use a **stack-based approach** with O(n) time and O(n) space.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "()"
Output: True

Example 2:
Input:  s = "()[]{}"
Output: True

Example 3:
Input:  s = "(]"
Output: False

Example 4:
Input:  s = "([{}])"
Output: True

Example 5:
Input:  s = "([)]"
Output: False

-----------------------------------------------------------
Algorithm — Stack + Matching Pairs:
-----------------------------------------------------------

Core idea:
Use a **stack** to track opening brackets.

Steps:
1. Create a map for closing → opening brackets:
       pairs = {
           ')': '(',
           '}': '{',
           ']': '['
       }

2. Initialize an empty stack.

3. Iterate through each character c in s:
       - If c is a **closing bracket** (exists in `pairs`):
             • If stack is empty → invalid → return False  
             • Pop the top element from stack  
             • If popped element != pairs[c] → invalid → return False  
       - Else:
             • c is an opening bracket → push it onto the stack

4. After processing all characters:
       - If the stack is empty → all brackets matched → return True  
       - If the stack is not empty → some openings not closed → return False  

Why this works:
- The stack always keeps track of the **most recent unmatched opening bracket**.
- Matching a closing bracket with the top of the stack enforces **correct order**.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

- Time Complexity:   O(n)  
      We scan the string once, and each character is pushed/popped at most once.

- Space Complexity:  O(n)  
      In the worst case (all opening brackets), all characters are stored in the stack.

-----------------------------------------------------------
"""
class Solution(object):
    def isValid(self, s):
        validParen = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        stack = []
        
        for c in s:
            if c in validParen:
                if stack and stack[-1] == validParen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0

#------------------------------------
#Driver Test
#------------------------------------


sol = Solution()
print(sol.isValid("()")) # True
print(sol.isValid("()[]{}")) # True
print(sol.isValid("(]")) # False
print(sol.isValid("([)]")) # False
print(sol.isValid("{[]}")) # True
