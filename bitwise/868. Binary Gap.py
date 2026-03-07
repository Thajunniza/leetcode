"""
===========================================================
868. Binary Gap
===========================================================

🧩 Problem:
Given a positive integer `n`, return the longest distance
between two consecutive 1's in the binary representation of `n`.

If there are fewer than two 1's, return 0.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Input:  n = 22
Binary: 10110
Output: 2

Input:  n = 5
Binary: 101
Output: 2

Input:  n = 8
Binary: 1000
Output: 0

-----------------------------------------------------------
Algorithm — Bit Traversal
-----------------------------------------------------------
Idea:

1. Traverse the bits of `n` from right to left.
2. Track the position of bits using an index `idx`.
3. Whenever we see a `1`:
      - If a previous `1` was seen, compute the distance.
      - Update the maximum distance.
4. Update the last seen index of `1`.

Key Operations:
- `n & 1`  → extract last bit
- `n >> 1` → move to next bit

-----------------------------------------------------------
⏱ Time Complexity:   O(log n)
💾 Space Complexity: O(1)
-----------------------------------------------------------
"""

# ------------------------------------
# Solution
# ------------------------------------
class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 0
        last_idx = -1
        idx = 0

        while n > 0:

            bit = n & 1

            if bit == 1:
                if last_idx != -1:
                    res = max(res, idx - last_idx)

                last_idx = idx

            idx += 1
            n >>= 1

        return res


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":

    sol = Solution()

    print(sol.binaryGap(22))  # Expected: 2
    print(sol.binaryGap(5))   # Expected: 2
    print(sol.binaryGap(8))   # Expected: 0