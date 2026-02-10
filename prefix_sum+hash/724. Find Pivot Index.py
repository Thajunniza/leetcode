"""
===========================================================
724. Find Pivot Index
===========================================================

Problem:
--------
Given an array of integers `nums`, return the pivot index.

The pivot index is the index where:
    sum of elements strictly to the left
    ==
    sum of elements strictly to the right

If multiple pivot indices exist, return the leftmost one.
If no pivot index exists, return -1.

Example:
--------
Input:  [1,7,3,6,5,6]
Output: 3

Explanation:
Left of index 3 → 1+7+3 = 11
Right of index 3 → 5+6 = 11

Approach:
---------
Optimized Prefix Sum (No Extra Arrays)

1. Compute total_sum of the array.
2. Maintain a running left_sum.
3. For each index i:
      right_sum = total_sum - left_sum - nums[i]
      if left_sum == right_sum:
           return i
      update left_sum += nums[i]

This avoids building separate left and right arrays.

Time Complexity:
----------------
O(n)

Space Complexity:
-----------------
O(1)

Author:
-------
Thajunniza M A
"""

# -----------------------------
# Optimal Solution (O(1) Space)
# -----------------------------
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":

    tests = [
        ([1,7,3,6,5,6], 3),
        ([1,2,3], -1),
        ([2,1,-1], 0),
        ([0,0,0,0], 0),
        ([], -1),
        ([1], 0),
    ]

    sol = Solution()
    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.pivotIndex(nums)
        print(f"Test {i}: nums={nums} | expected={expected}, got={result}")
