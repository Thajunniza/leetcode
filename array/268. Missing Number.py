"""
268.Missing Number

Given an array `nums` containing `n` distinct numbers taken from the range
[0, n], return the one number that is missing from the array.

Example:
Input: nums = [3, 0, 1]
Output: 2

Input: nums = [0, 1]
Output: 2

Algorithm:
1. The numbers are expected to be from 0 to n.
2. Calculate the expected sum of numbers from 0 to n using the formula:
      n * (n + 1) / 2
3. Calculate the actual sum of elements in the array.
4. The missing number is:
      expected_sum - actual_sum

Time Complexity: O(n), where n is the length of the array
Space Complexity: O(1), constant extra space
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    assert sol.missingNumber([3, 0, 1]) == 2
    assert sol.missingNumber([0, 1]) == 2
    assert sol.missingNumber([1]) == 0
    assert sol.missingNumber([0]) == 1
    assert sol.missingNumber([0, 1, 2, 3]) == 4

    print("All test cases passed!")
