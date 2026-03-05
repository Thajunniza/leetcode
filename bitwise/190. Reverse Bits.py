"""
===========================================================
190. Reverse Bits
===========================================================

🧩 Problem:
Reverse the bits of a given 32-bit unsigned integer `n`
and return the resulting integer.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Input:  n = 43261596
Output: 964176192

Input:  n = 4294967293
Output: 3221225471

Input:  n = 1
Output: 2147483648

-----------------------------------------------------------
Algorithm — Bitwise Reversal:
-----------------------------------------------------------
Idea:

- Initialize `res = 0`
- Process **all 32 bits** of `n`:
    1. Extract the least significant bit: `bit = n & 1`
    2. Shift `res` left by 1: `res = res << 1`
    3. OR `bit` into `res`: `res = res | bit`
    4. Shift `n` right by 1 to process the next bit: `n = n >> 1`
- Return `res` after 32 iterations

Key Insight:
- By shifting `res` left before adding the bit, we place each bit in the correct reversed position.
- Using a **fixed 32-iteration loop** ensures that leading zeros are handled correctly.

-----------------------------------------------------------
⏱ Time Complexity:   O(32) → O(1)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

# ------------------------------------
# Solution: Bitwise Reversal
# ------------------------------------
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for _ in range(32): 
            bit = n & 1
            n = n >> 1
            res = (res << 1) | bit
        return res

# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":

    sol = Solution()

    print(sol.reverseBits(43261596))    # Expected Output: 964176192
    print(sol.reverseBits(4294967293))  # Expected Output: 3221225471
    print(sol.reverseBits(0))           # Expected Output: 0
    print(sol.reverseBits(1))           # Expected Output: 2147483648