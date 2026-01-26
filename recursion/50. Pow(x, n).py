"""
50 - Pow(x, n)

Description:
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example:
Input: x = 2.0, n = 10
Output: 1024.0

Input: x = 2.0, n = -2
Output: 0.25

Approach:
Binary Exponentiation (Fast Power).
- If n == 0, return 1
- Recursively compute x^(n//2)
- Square the result
- If n is odd, multiply once more by x
- If n is negative, return reciprocal

Time Complexity:
O(log n)

Space Complexity:
O(log n) due to recursion stack
"""

from typing import *


class Solution:
    def myPow(self, x: float, n: int) -> float:

        def getPow(x: float, n: int) -> float:
            if n == 0:
                return 1

            half = getPow(x, n // 2)
            result = half * half

            if n % 2 == 1:
                result *= x

            return result

        res = getPow(x, abs(n))
        return 1 / res if n < 0 else res


# -------------------- Test Cases --------------------

def test_my_pow():
    sol = Solution()

    assert abs(sol.myPow(2.0, 10) - 1024.0) < 1e-9
    assert abs(sol.myPow(2.0, -2) - 0.25) < 1e-9
    assert abs(sol.myPow(2.0, 0) - 1.0) < 1e-9
    assert abs(sol.myPow(1.0, 1000000) - 1.0) < 1e-9
    assert abs(sol.myPow(-2.0, 3) + 8.0) < 1e-9

    print("All test cases passed.")


if __name__ == "__main__":
    test_my_pow()