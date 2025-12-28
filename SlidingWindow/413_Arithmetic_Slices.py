""" 
===========================================================
413. Arithmetic Slices
===========================================================

🧩 Problem:
Given an integer array `nums`, return the number of
arithmetic slices (subarrays of length ≥ 3 with constant differences).

🎯 Goal:
Count all contiguous subarrays where the difference between
consecutive elements is the same.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  nums = [1,2,3,4]
Output: 3
Explanation: Arithmetic slices are [1,2,3], [2,3,4], [1,2,3,4]

Example 2:
Input:  nums = [1]
Output: 0
Explanation: Array too short to form any arithmetic slice

Example 3:
Input:  nums = [1,3,5,7,9]
Output: 6
Explanation: Slices: [1,3,5], [3,5,7], [5,7,9], [1,3,5,7], [3,5,7,9], [1,3,5,7,9]

-----------------------------------------------------------
Algorithm — Sliding Window + Count of Slices:
-----------------------------------------------------------

Maintain a window with a constant difference.

1. Initialize `count = 0` (slices ending at current index), `result = 0`
2. Iterate from i = 2 to n-1:
   - Compute `curr_diff = nums[i] - nums[i-1]`
   - If `curr_diff == prev_diff`:
       → count += 1
       → result += count
   - Else:
       → Reset count = 0
       → Update prev_diff = curr_diff
3. Return result

Key idea:
Each time the difference is the same, extend all slices ending at previous index.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)  (single pass over array)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1)  (only counters and prev_diff)

-----------------------------------------------------------
"""
# ------------------------------------
# 413. Arithmetic Slices
# Sliding Window + Count
# ------------------------------------

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0

        result = 0
        count = 0
        prev_diff = nums[1] - nums[0]

        for i in range(2, n):
            curr_diff = nums[i] - nums[i-1]
            if curr_diff == prev_diff:
                count += 1
                result += count
            else:
                count = 0
                prev_diff = curr_diff

        return result

# ------------------------------------
# Driver Test
# ------------------------------------

sol = Solution()
print(sol.numberOfArithmeticSlices([1,2,3,4]))       # Expected: 3
print(sol.numberOfArithmeticSlices([1]))             # Expected: 0
print(sol.numberOfArithmeticSlices([1,3,5,7,9]))     # Expected: 6
print(sol.numberOfArithmeticSlices([7,7,7,7]))       # Expected: 3

