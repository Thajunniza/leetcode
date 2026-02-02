"""
485.Max Consecutive Ones

Given a binary array `nums`, return the maximum number of consecutive 1s
in the array.

Example:
Input: nums = [1,1,0,1,1,1]
Output: 3

Input: nums = [1,0,1,1,0,1]
Output: 2

Algorithm:
1. Initialize two variables:
   - `count` to track the current streak of consecutive 1s
   - `ans` to track the maximum streak found so far
2. Traverse the array:
   - If the current element is 1:
       - Increment `count`
       - Update `ans`
   - If the current element is 0:
       - Reset `count` to 0
3. Return `ans`

Time Complexity: O(n), where n is the length of the array
Space Complexity: O(1), constant extra space
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        ans = 0

        for n in nums:
            if n == 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 0

        return ans


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    assert sol.findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3
    assert sol.findMaxConsecutiveOnes([1,0,1,1,0,1]) == 2
    assert sol.findMaxConsecutiveOnes([0,0,0]) == 0
    assert sol.findMaxConsecutiveOnes([1,1,1,1]) == 4
    assert sol.findMaxConsecutiveOnes([]) == 0

    print("All test cases passed!")
