"""
--------------------------------------------------
34: Find First and Last Position of Element
--------------------------------------------------

Given a sorted array of integers nums and a target value,
return the starting and ending position of the target.

If the target is not found in the array, return [-1, -1].

The algorithm must run in O(log n) time.

--------------------------------------------------
Example:
Input:
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
Output:
    [3, 4]

Input:
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
Output:
    [-1, -1]
--------------------------------------------------
"""


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # --------------------------------------------------
        # Lower Bound: First index where nums[i] == target
        # --------------------------------------------------
        def lower_bound():
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    if nums[mid] == target:
                        res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return res

        # --------------------------------------------------
        # Upper Bound: Last index where nums[i] == target
        # --------------------------------------------------
        def upper_bound():
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        res = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return res

        first = lower_bound()
        if first == -1:
            return [-1, -1]

        return [first, upper_bound()]


# --------------------------------------------------
# Algorithm Explanation:
# --------------------------------------------------
# 1. Use binary search to find the first occurrence
#    (lower bound) of the target.
# 2. Use binary search to find the last occurrence
#    (upper bound) of the target.
# 3. Each search runs in O(log n).
#
# --------------------------------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)
# --------------------------------------------------


# --------------------------------------------------
# Test Cases
# --------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))   # Expected: [3, 4]
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))   # Expected: [-1, -1]
    print(sol.searchRange([], 0))                   # Expected: [-1, -1]
    print(sol.searchRange([1], 1))                  # Expected: [0, 0]
    print(sol.searchRange([2, 2, 2, 2], 2))          # Expected: [0, 3]