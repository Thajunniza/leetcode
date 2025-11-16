"""
===========================================================
258. Add Digits (Digital Root)
===========================================================

🧩 Problem:
Given an integer num, repeatedly add its digits until only 
one digit remains. Return that single digit.

Example:
Input: 38
Process: 3+8=11 → 1+1=2
Output: 2

-----------------------------------------------------------
Approach — Digital Root:
-----------------------------------------------------------
The repeated digit sum of a number follows the mathematical 
property of the digital root:

- If num == 0 → return 0
- If num % 9 == 0 → return 9
- Otherwise return num % 9

This avoids loops and recursion.

-----------------------------------------------------------
⏱ Time Complexity:   O(1)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        
        remainder = num % 9
        if remainder == 0:
            return 9
        
        return remainder


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.addDigits(38))  # Expected Output: 2
    print(sol.addDigits(383))  # Expected Output: 5
