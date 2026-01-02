"""
===========================================================
3754 - Concatenate Non-Zero Digits and Multiply by Sum I
===========================================================

🧩 Problem:
Given an integer n, do the following:
1. Extract all non-zero digits in their original order.
2. Concatenate them to form a new number.
3. Compute the sum of all non-zero digits.
4. Return the product of the concatenated number and the digit sum.

Example:
Input: n = 10503
Non-zero digits: 1, 5, 3
Concatenated number: 153
Digit sum: 1 + 5 + 3 = 9
Output: 153 * 9 = 1377

-----------------------------------------------------------
Approach — Digit Manipulation:
-----------------------------------------------------------
1. Initialize:
   - `total` for the sum of digits
   - `x` for concatenated number
   - `multiplier = 1` for place value computation

2. Process digits from **right to left** using modulo/division:
   - rem = n % 10
   - if rem > 0:
       - total += rem
       - x += rem * multiplier
       - multiplier *= 10
   - n //= 10

3. Return x * total

This approach avoids string conversion and preserves digit order using place value arithmetic.

-----------------------------------------------------------
⏱ Time Complexity:   O(d)   # d = number of digits in n
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

class Solution(object):
    def sumAndMultiply(self, n):
        total = 0          # Sum of non-zero digits
        x = 0              # Concatenated number
        multiplier = 1     # Place value for concatenation

        while n > 0:
            rem = n % 10
            if rem > 0:
                total += rem
                x += rem * multiplier
                multiplier *= 10
            n = n // 10

        return x * total


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.sumAndMultiply(10503))  # Expected Output: 1377
    print(sol.sumAndMultiply(9876543210))  # Expected Output: 987654321 * 45 = 444444137
