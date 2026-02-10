"""
===========================================================
2574. Left and Right Sum Differences
===========================================================

Problem:
--------
Given an integer array `nums`, return a new array `answer` such that:
    answer[i] = |sum(nums[0:i-1]) - sum(nums[i+1:n-1])|

That is, the absolute difference between the sum of elements 
to the left and the sum of elements to the right of index `i`.

Example:
--------
Input:  nums = [10,4,8,3]
Output: [15,1,11,22]

Explanation:
Left sum and right sum for each index:
Index 0: left=0, right=4+8+3=15 → abs(0-15)=15
Index 1: left=10, right=8+3=11 → abs(10-11)=1
Index 2: left=10+4=14, right=3 → abs(14-3)=11
Index 3: left=10+4+8=22, right=0 → abs(22-0)=22

Approach:
---------
Prefix Sum with Total Sum

1. Compute total_sum of the array.
2. Initialize left_sum = 0.
3. Iterate through the array:
      right_sum = total_sum - left_sum - nums[i]
      res[i] = abs(left_sum - right_sum)
      left_sum += nums[i]

Time Complexity:
----------------
O(n) — single pass to compute total + single pass for result.

Space Complexity:
-----------------
O(n) — for the result array.

Author:
-------
Thajunniza M A
"""

# -----------------------------
# Solution Class
# -----------------------------
class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        total = sum(nums)
        res = [0] * n
        left = 0

        for i in range(n):
            right = total - left - nums[i]
            res[i] = abs(left - right)
            left += nums[i]
        
        return res


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":

    tests = [
        ([10,4,8,3], [15,1,11,22]),
        ([1,2,3,4,5], [14,9,5,3,10]),
        ([0,0,0], [0,0,0]),
        ([5], [0]),
        ([], [])
    ]

    sol = Solution()
    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.leftRightDifference(nums)
        print(f"Test {i}: nums={nums} | expected={expected}, got={result}")
