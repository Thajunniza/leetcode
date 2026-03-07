"""
===========================================================
476. Number Complement
===========================================================

🧩 Problem:
Given a positive integer `num`, return its bitwise complement.

The complement flips every bit in the binary representation
of `num`, but only up to its most significant bit.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Input:  num = 5
Binary: 101
Output: 2
Binary: 010

Input:  num = 1
Binary: 1
Output: 0
Binary: 0

-----------------------------------------------------------
Algorithm — Bit Extraction
-----------------------------------------------------------
Idea:

1. Extract the last bit using:
        num & 1

2. Flip the bit using:
        bit ^ 1

3. Place the flipped bit into the result at the correct position.

4. Shift the number right:
        num >> 1

5. Continue until `num` becomes 0.

Key Insight:
- Process each bit individually.
- Build the complement number using bit shifts.

-----------------------------------------------------------
⏱ Time Complexity:   O(log n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

# ------------------------------------
# Solution: Extract Bit + Flip
# ------------------------------------
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        res = 0
        bit_pos = 0

        while num > 0:

            # get last bit
            bit = num & 1

            # flip it
            bit ^= 1

            # place it in result
            res |= (bit << bit_pos)

            # move to next bit
            num >>= 1
            bit_pos += 1

        return res


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":

    sol = Solution()

    print(sol.findComplement(5))   # Expected Output: 2
    print(sol.findComplement(1))   # Expected Output: 0
    print(sol.findComplement(10))  # Expected Output: 5