"""
162 - Find Peak Element

A peak element in an array is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element and return its index.
The array may contain multiple peaks; return the index of any one of them.

Example:
Input:  nums = [1, 2, 3, 1]
Output: 2  # nums[2] = 3 is a peak

Time Complexity: O(log n) -- Binary search halves the search space
Space Complexity: O(1) -- Constant extra space
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        elif n == 1 or nums[0] > nums[1]:
            return 0
        elif nums[n-1] > nums[n-2]:
            return n-1

        l = 1
        r = n - 2
        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1


# -------------------------------
# Example Test Cases
# -------------------------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], [1, 5]),  # multiple peaks, accept either index
        ([1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([1, 3, 2, 1], 1),
        ([1, 2, 3, 4, 5], 4),  # peak at end
        ([5, 4, 3, 2, 1], 0),  # peak at start
    ]

    for arr, expected in test_cases:
        result = sol.findPeakElement(arr)
        print(f"Input: {arr}")
        print(f"Peak index: {result} (Value: {arr[result]})")
        print(f"Expected: {expected}\n")