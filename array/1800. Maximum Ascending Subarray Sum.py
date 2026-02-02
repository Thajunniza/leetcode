"""
1800.Maximum Ascending Subarray Sum

Given an array of positive integers `nums`, return the maximum possible sum of
an ascending subarray.

An ascending subarray is a contiguous subarray where each element is strictly
greater than the previous one.

Example:
Input: nums = [10, 20, 30, 5, 10, 50]
Output: 65
Explanation: The ascending subarray [5, 10, 50] has the maximum sum.

Input: nums = [10, 20, 30, 40, 50]
Output: 150

Input: nums = [12, 17, 15, 13, 10, 11, 12]
Output: 33

Algorithm:
1. Initialize `total` with the first element of the array.
2. Initialize `max_total` with `total`.
3. Traverse the array starting from index 1:
   - If current element is greater than the previous element:
       - Add it to `total`
   - Otherwise:
       - Reset `total` to the current element
   - Update `max_total` with the maximum of `max_total` and `total`
4. Return `max_total`.

Time Complexity: O(n), where n is the length of the array
Space Complexity: O(1), constant extra space
"""

class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        
        total = nums[0]
        max_total = total

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                total += nums[i]
            else:
                total = nums[i]

            max_total = max(max_total, total)
        
        return max_total


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxAscendingSum([10, 20, 30, 5, 10, 50]) == 65
    assert sol.maxAscendingSum([10, 20, 30, 40, 50]) == 150
    assert sol.maxAscendingSum([12, 17, 15, 13, 10, 11, 12]) == 33
    assert sol.maxAscendingSum([100]) == 100
    assert sol.maxAscendingSum([]) == 0

    print("All test cases passed!")
