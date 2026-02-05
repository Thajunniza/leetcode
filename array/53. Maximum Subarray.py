"""
53 - Maximum Subarray

Description:
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.

Approach:
Kadane’s Algorithm (Dynamic Programming).
- Maintain a running sum (total).
- If total becomes negative, reset it to 0 since it cannot contribute to a maximum sum.
- Add the current number to total.
- Track the maximum sum encountered so far.

Time Complexity:
O(n) - Each element is visited once.

Space Complexity:
O(1) - Uses constant extra space.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0
            total += n
            ans = max(ans, total)

        return ans


# -------------------- Test Cases --------------------

def test_maxSubArray():
    sol = Solution()

    assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([5,4,-1,7,8]) == 23
    assert sol.maxSubArray([-1,-2,-3]) == -1
    assert sol.maxSubArray([-2, -1]) == -1

    print("All test cases passed.")

if __name__ == "__main__":
    test_maxSubArray()
