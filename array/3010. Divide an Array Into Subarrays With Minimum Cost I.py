"""
3010. Divide an Array Into Subarrays With Minimum Cost I

Problem:
You are given an integer array nums of length n.
You must divide nums into 3 disjoint contiguous subarrays.

The cost of a subarray is defined as its first element.
Return the minimum possible sum of the costs of the 3 subarrays.

Examples:
Input: nums = [1,2,3,12]
Output: 6
Explanation:
Possible split: [1], [2], [3,12]
Cost = 1 + 2 + 3 = 6

Input: nums = [5,4,3]
Output: 12

Input: nums = [10,3,1,1]
Output: 12
"""

from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)

        # If exactly 3 elements, each must be its own subarray
        if n == 3:
            return sum(nums)

        # First subarray always starts at index 0
        # Choose two minimum values from the remaining elements
        remaining = nums[1:]
        remaining.sort()

        return nums[0] + remaining[0] + remaining[1]


# -----------------------------
# Algorithm:
# 1. The first subarray always starts at index 0, so its cost is nums[0].
# 2. To minimize total cost, choose the two smallest values from nums[1:]
#    as the starting elements of the remaining two subarrays.
# 3. Return nums[0] + smallest + second smallest.
#
# -----------------------------
# Time Complexity:
# O(n log n) due to sorting the remaining elements.
#
# Space Complexity:
# O(n) for the temporary array.
#
# -----------------------------
# Driver Code (Test Run)
# -----------------------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [1, 2, 3, 12],
        [5, 4, 3],
        [10, 3, 1, 1]
    ]

    for nums in test_cases:
        result = sol.minimumCost(nums)
        print(f"Input: {nums}")
        print(f"Minimum Cost: {result}")
        print("-" * 30)
