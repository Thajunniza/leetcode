"""
--------------------------------------------------
693: Binary Number with Alternating Bits
--------------------------------------------------

Given a positive integer n, return True if its binary representation
has alternating bits (i.e., no two adjacent bits are the same).
Otherwise, return False.

This problem can be solved by scanning bits from least significant 
to most significant and ensuring adjacent bits differ.

--------------------------------------------------
Examples:
Input:
    n = 5        # binary: 101
Output:
    True

Input:
    n = 7        # binary: 111
Output:
    False

Input:
    n = 10       # binary: 1010
Output:
    True

Input:
    n = 11       # binary: 1011
Output:
    False
--------------------------------------------------
"""


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = n % 2
        n = n // 2
        while n > 0:
            curr = n % 2
            if prev == curr:
                return False
            prev = curr
            n = n // 2

        return True


# --------------------------------------------------
# Algorithm Explanation:
# --------------------------------------------------
# 1. Read the least significant bit (LSB) as `prev`.
# 2. Repeatedly shift the number right by one bit (integer divide by 2).
# 3. At each step, read the current LSB as `curr`:
#       - If `curr == prev`, adjacent bits are equal → return False.
#       - Else, set prev = curr and continue.
# 4. If the loop completes, bits were alternating → return True.
#
# Notes:
# - This scans each bit once → O(log n) time, O(1) space.
# - Uses modulo (n % 2) and integer division (n // 2) to extract and shift bits,
#   exactly as in the original code.
#
# --------------------------------------------------
# Time Complexity: O(log n)  (number of bits in n)
# Space Complexity: O(1)
# --------------------------------------------------


# --------------------------------------------------
# Test Cases
# --------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Basic cases
    print(sol.hasAlternatingBits(5))    # 0b101  -> True
    print(sol.hasAlternatingBits(7))    # 0b111  -> False
    print(sol.hasAlternatingBits(10))   # 0b1010 -> True
    print(sol.hasAlternatingBits(11))   # 0b1011 -> False

    # Edge-ish cases
    print(sol.hasAlternatingBits(1))    # 0b1    -> True
    print(sol.hasAlternatingBits(2))    # 0b10   -> True
    print(sol.hasAlternatingBits(3))    # 0b11   -> False
    # If you want to define behavior for 0 explicitly:
    print(sol.hasAlternatingBits(0))  # 0b0    -> (your choice: True/False)
