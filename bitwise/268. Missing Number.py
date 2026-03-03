"""
===========================================================
268. Missing Number (XOR / Mathematical Trick)
===========================================================

🧩 Problem:
Given an array `nums` containing `n` distinct numbers taken from
the range [0, n], return the only number in the range that is
missing from the array.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Input:  nums = [3,0,1]
Output: 2

Input:  nums = [0,1]
Output: 2

Input:  nums = [9,6,4,2,3,5,7,0,1]
Output: 8

-----------------------------------------------------------
Algorithm 1 — XOR Trick (Optimal & Elegant)
-----------------------------------------------------------
Key Idea:
If we XOR all indices and all numbers together:

0 ^ 1 ^ 2 ^ ... ^ n
^ nums[0] ^ nums[1] ^ ...

All matching numbers cancel out.

Only the missing number remains.

Because:
a ^ a = 0
a ^ 0 = a

-----------------------------------------------------------
Algorithm 2 — Mathematical Formula
-----------------------------------------------------------
Expected sum = n * (n + 1) // 2
Actual sum   = sum(nums)

Missing = Expected - Actual

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""


# ------------------------------------
# Solution 1: XOR Method (Recommended)
# ------------------------------------
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = n   # start with n because indices go from 0 to n

        for i in range(n):
            res ^= i
            res ^= nums[i]

        return res


# ------------------------------------
# Solution 2: Mathematical Formula
# ------------------------------------
class SolutionMath(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":

    sol = Solution()

    print(sol.missingNumber([3,0,1]))                  # Expected: 2
    print(sol.missingNumber([0,1]))                    # Expected: 2
    print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))      # Expected: 8