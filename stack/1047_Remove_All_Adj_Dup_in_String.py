""" 
===========================================================
1047. Remove All Adjacent Duplicates in String
===========================================================

🧩 Problem:
You are given a string s consisting of lowercase English letters.

Your task:
Repeatedly remove **adjacent duplicate characters** from the string.

Two characters are considered adjacent duplicates if:
    - They are next to each other
    - They are the same character

Keep removing duplicates **until no more adjacent duplicates exist**.

Return the final string.

🎯 Goal:
Use a **stack-based** approach to efficiently remove duplicates in O(n) time.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "abbaca"
Output: "ca"

Explanation:
    - "abbaca"
    - remove "bb" → "aaca"
    - remove "aa" → "ca"

Example 2:
Input:  s = "azxxzy"
Output: "ay"

Example 3:
Input:  s = "aaaa"
Output: "a"

Example 4:
Input:  s = "abc"
Output: "abc"   (no duplicates)

-----------------------------------------------------------
Algorithm — Using Stack:
-----------------------------------------------------------

Core idea:
Use a **stack** to build the final string.

Steps:
1. Initialize an empty list `stack`
2. For each character c in s:
       - If stack is not empty AND top of stack equals c:
             • pop the top element (duplicate detected)
       - Else:
             • push c onto the stack
3. After processing all characters, join the stack into the final string

Why this works:
- Stack maintains characters that remain after removing duplicates
- When the same character appears twice consecutively, we remove (pop) it
- This automatically handles chain reactions

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)  
Space Complexity:  O(n)  

-----------------------------------------------------------
"""
class Solution(object):
    def removeDuplicates(self, s):
        stack = []

        for c in s:
            if stack and stack[-1] == c:
                stack.pop()       # Duplicate found → remove
            else:
                stack.append(c)   # Push non-duplicate

        return "".join(stack)
    
#------------------------------------
#Driver Test
#------------------------------------

sol = Solution()
print(sol.removeDuplicates("abbaca")) # ca
print(sol.removeDuplicates("azxxzy")) # ay
print(sol.removeDuplicates("aaaa")) # a
print(sol.removeDuplicates("abc")) # abc