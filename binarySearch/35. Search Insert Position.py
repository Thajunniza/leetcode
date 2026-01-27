"""
--------------------------------------------------
35: Search Insert Position (Lower Bound)
--------------------------------------------------

Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index
where it would be inserted in order.

This problem is a classic application of Binary Search to find
the LOWER BOUND (first index where nums[i] >= target).

--------------------------------------------------
Example:
Input:
    nums = [1, 3, 5, 6]
    target = 5
Output:
    2

Input:
    nums = [1, 3, 5, 6]
    target = 2
Output:
    1

Input:
    nums = [1, 3, 5, 6]
    target = 7
Output:
    4
--------------------------------------------------
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        # Default insertion position (if target is greater than all elements)
        result = len(nums)

        while left <= right:
            mid = (left + right) // 2

            # If current element is >= target,
            # this index could be a valid insertion point
            if nums[mid] >= target:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result


# --------------------------------------------------
# Algorithm Explanation:
# --------------------------------------------------
# 1. Use binary search on the sorted array.
# 2. If nums[mid] >= target:
#       - mid is a possible insertion index
#       - store it in result
#       - continue searching in the left half
# 3. If nums[mid] < target:
#       - target must be in the right half
# 4. After the loop, result contains the lower bound index.
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

    print(sol.searchInsert([1, 3, 5, 6], 5))  # Expected: 2
    print(sol.searchInsert([1, 3, 5, 6], 2))  # Expected: 1
    print(sol.searchInsert([1, 3, 5, 6], 7))  # Expected: 4
    print(sol.searchInsert([1, 3, 5, 6], 0))  # Expected: 0