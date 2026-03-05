"""
===========================================================
137. Single Number II (Bitmask Method)
===========================================================

🧩 Problem:
Given an integer array `nums`, every element appears three times
except for one element that appears exactly once.

Find and return that single element.

You must implement a solution with:
- Linear runtime
- Constant extra space

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Input:  nums = [2,2,3,2]
Output: 3

Input:  nums = [0,1,0,1,0,1,99]
Output: 99

-----------------------------------------------------------
Algorithm — Bitmask Trick with Ones and Twos:
-----------------------------------------------------------
Idea:

- Maintain two integers, `ones` and `twos`:
  - `ones` holds bits that have appeared **1 time modulo 3**
  - `twos` holds bits that have appeared **2 times modulo 3**

- For each number `num` in `nums`:
    1. Update `ones` with bits seen once, ignoring bits in `twos`
       `ones = (ones ^ num) & ~twos`
    2. Update `twos` with bits seen twice, ignoring bits in updated `ones`
       `twos = (twos ^ num) & ~ones`

- After all numbers are processed, `ones` contains the number
  that appeared exactly once.

Key Insight:
- Bits appearing three times are automatically cleared from both `ones` and `twos`.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

# ------------------------------------
# Solution: Bitmask Ones and Twos
# ------------------------------------
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones

# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":

    sol = Solution()

    print(sol.singleNumber([2,2,3,2]))               # Expected Output: 3
    print(sol.singleNumber([0,1,0,1,0,1,99]))       # Expected Output: 99
    print(sol.singleNumber([30000,500,100,30000,100,30000,100]))  # Expected Output: 500