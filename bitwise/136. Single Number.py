"""
===========================================================
136. Single Number (XOR Bit Manipulation)
===========================================================

🧩 Problem:
Given a non-empty array of integers `nums`, every element appears
twice except for one element that appears only once.

Find and return that single element.

You must implement a solution with:
- Linear runtime
- Constant extra space

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Input:  nums = [2,2,1]
Output: 1

Input:  nums = [4,1,2,1,2]
Output: 4

Input:  nums = [1]
Output: 1

-----------------------------------------------------------
Algorithm — XOR Cancellation Trick:
-----------------------------------------------------------
Key XOR Properties:

1. a ^ a = 0
2. a ^ 0 = a
3. XOR is commutative and associative

If we XOR all numbers together:
- Pairs cancel out
- Only the unique number remains

Example:
[4,1,2,1,2]

4 ^ 1 ^ 2 ^ 1 ^ 2
= 4 ^ (1^1) ^ (2^2)
= 4 ^ 0 ^ 0
= 4

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""


# ------------------------------------
# Solution: XOR Accumulation
# ------------------------------------
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for num in nums:
            res = res ^ num   # XOR cancellation

        return res


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":

    sol = Solution()

    print(sol.singleNumber([2,2,1]))         # Expected Output: 1
    print(sol.singleNumber([4,1,2,1,2]))     # Expected Output: 4
    print(sol.singleNumber([1]))             # Expected Output: 1