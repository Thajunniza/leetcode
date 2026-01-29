"""
1283: Find the Smallest Divisor Given a Threshold 
Given an array of integers nums and an integer threshold,
choose a positive integer divisor such that the sum of
ceil(nums[i] / divisor) for all i is less than or equal to threshold.

Return the smallest such divisor.

Example:
Input:  nums = [1, 2, 5, 9], threshold = 6
Output: 5

Explanation:
Divisor = 5
ceil(1/5) + ceil(2/5) + ceil(5/5) + ceil(9/5)
= 1 + 1 + 1 + 2 = 5 ≤ 6

Approach:
Binary Search on Answer

- Minimum divisor = 1
- Maximum divisor = max(nums)
- As divisor increases, the sum of divisions decreases
  → monotonic property → binary search

Time Complexity: O(n log M)
    where n = len(nums), M = max(nums)

Space Complexity: O(1)
"""

from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # Helper function to calculate sum of divisions for a given divisor
        def get_divisor_sum(d):
            total = 0
            for n in nums:
                # Integer ceiling division (Python 2 & 3 safe)
                total += (n + d - 1) // d
            return total

        l = 1
        r = max(nums)
        ans = r

        while l <= r:
            mid = (l + r) // 2
            if get_divisor_sum(mid) <= threshold:
                ans = mid          # valid divisor, try smaller
                r = mid - 1
            else:
                l = mid + 1        # divisor too small, increase

        return ans


# -------------------------------
# Test Cases
# -------------------------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 2, 5, 9], 6, 5),
        ([2, 3, 5, 7, 11], 11, 3),
        ([19], 5, 4),
        ([1, 1, 1, 1], 4, 1),
        ([1000000], 1, 1000000)
    ]

    for nums, threshold, expected in test_cases:
        result = sol.smallestDivisor(nums, threshold)
        print(f"Nums: {nums}, Threshold: {threshold}")
        print(f"Smallest Divisor: {result}")
        print(f"Expected: {expected}")
        print("-" * 40)
