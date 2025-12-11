"""
===========================================================
680. Valid Palindrome II
===========================================================

🧩 Problem:
Given a string `s`, return `True` if it can become a palindrome after 
**deleting at most one character**.

A palindrome reads the same forward and backward.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "aba"
Output: True
Explanation: Already a palindrome.

Example 2:
Input:  s = "abca"
Output: True
Explanation:
    Delete 'b' → "aca"
    or delete 'c' → "aba"

Example 3:
Input:  s = "abc"
Output: False
Explanation:
    Removing one character cannot fix the mismatch.

-----------------------------------------------------------
🎯 Core Logic:
-----------------------------------------------------------

Use the **Two-Pointer** technique:

1️⃣ Start with pointers:
    - `l = 0` (left)
    - `r = len(s) - 1` (right)

2️⃣ While characters match (`s[l] == s[r]`):
    - Move inward → `l += 1`, `r -= 1`

3️⃣ When you hit the **first mismatch**, you have two choices:
    - Skip left character → check substring `s[l+1 : r+1]`
    - Skip right character → check substring `s[l : r]`

4️⃣ If **either** substring is a palindrome → return True  
5️⃣ If neither works → return False

💡 At most **one deletion** is allowed, and we check both possibilities.

-----------------------------------------------------------
🧠 Approach:
-----------------------------------------------------------

- Use two pointers to scan the string.
- Only at the first mismatch, try both deletion paths.
- Use slicing + reverse (`[::-1]`) to check quickly if the substring is a palindrome.

-----------------------------------------------------------
💡 Code (Simple & Readable Version):
-----------------------------------------------------------

```python
"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                skipL = s[l+1:r+1]   # delete left character
                skipR = s[l:r]       # delete right character
                return skipL == skipL[::-1] or skipR == skipR[::-1]
        
        return True
    

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("aba", True),
        ("abca", True),
        ("abc", False),
        ("deeee", True),
        ("cbbcc", True),
        ("abcdba", True),   # delete 'c' → "abdba"
        ("abcd", False),
    ]

    for s, expected in tests:
        result = sol.validPalindrome(s)
        print("Input: {!r}, Output: {}, Expected: {}".format(s, result, expected))    
