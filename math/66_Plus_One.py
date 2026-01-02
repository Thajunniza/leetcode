"""
===========================================================
66. Plus One
===========================================================

🧩 Problem:
Given a non-empty array of digits representing a non-negative 
integer, increment the integer by one and return the resulting 
array of digits.

Example:
Input: [1,2,3]
Process: 123 + 1 = 124
Output: [1,2,4]

Input: [9,9,9]
Process: 999 + 1 = 1000
Output: [1,0,0,0]

-----------------------------------------------------------
Approach — Carry Propagation:
-----------------------------------------------------------
1. Start from the last digit (least significant digit).  
2. If the digit is less than 9, increment it and return the array.  
3. If the digit is 9, set it to 0 and propagate the carry to the next digit.  
4. If all digits were 9, insert 1 at the beginning of the array.

This avoids converting the array to an integer and back, making 
it efficient for very large numbers.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)   # n = number of digits
💾 Space Complexity:  O(1)   # in-place, except for possible extra digit
-----------------------------------------------------------
"""

class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        i = n - 1
        
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            i -= 1
        
        return [1] + digits


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1,2,3]))  # Expected Output: [1,2,4]
    print(sol.plusOne([9,9,9]))  # Expected Output: [1,0,0,0]
    print(sol.plusOne([4,3,2,1]))  # Expected Output: [4,3,2,2]

