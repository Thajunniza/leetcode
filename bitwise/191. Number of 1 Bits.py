"""
===========================================================
191. Number of 1 Bits (Hamming Weight)
===========================================================

🧩 Problem:
Given an unsigned integer `n`, return the number of '1' bits it has
(i.e., the Hamming weight).

Example:
Input:  n = 11 (binary 1011)
Output: 3
Explanation: There are three 1 bits.

-----------------------------------------------------------
Solution 1 — Brian Kernighan’s Trick:
-----------------------------------------------------------
- n & (n-1) removes the lowest set bit
- Count how many times we can do this until n becomes 0
- Efficient when few bits are set
-----------------------------------------------------------
Solution 2 — Right Shift Method:
-----------------------------------------------------------
- Iterate over all bits (32 iterations)
- Check LSB: n & 1 → increment count
- Right shift n by 1
- Works for any number of set bits
===========================================================
"""


# ------------------------------------
# Solution 1: Brian Kernighan's Trick
# ------------------------------------
class SolutionKernighan(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = n & (n - 1)  # remove the rightmost 1 bit
            count += 1
        return count


# ------------------------------------
# Solution 2: Right Shift Method
# ------------------------------------
class SolutionShift(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for _ in range(32):          # iterate over all 32 bits
            count += n & 1            # add 1 if LSB is set
            n = n >> 1                # shift right
        return count


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":

    test_cases = [11, 128, 4294967293]  # 11=1011, 128=10000000, 4294967293=111...1101

    print("Brian Kernighan's Trick:")
    sol1 = SolutionKernighan()
    for num in test_cases:
        print("n =", num, "-> Hamming Weight =", sol1.hammingWeight(num))

    print("\nRight Shift Method:")
    sol2 = SolutionShift()
    for num in test_cases:
        print("n =", num, "-> Hamming Weight =", sol2.hammingWeight(num))