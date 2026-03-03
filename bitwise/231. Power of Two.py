"""
===========================================================
231. Power of Two
===========================================================

A number is a power of two if:
- It is positive
- It has exactly ONE set bit in binary

Key Bitwise Identity:
n & (n - 1) removes the lowest set bit.

If result becomes 0 → only one bit existed.
===========================================================
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # Power of two must be positive
        if n <= 0:
            return False

        # Remove lowest set bit
        return (n & (n - 1)) == 0


# -----------------------------------------------------------
# Driver Code (for testing)
# -----------------------------------------------------------
if __name__ == "__main__":

    sol = Solution()

    test_cases = [16, 8, 4, 3, 0, -2, 1]

    for num in test_cases:
        print("n =", num, "->", sol.isPowerOfTwo(num))