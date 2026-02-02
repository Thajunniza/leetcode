"""
325. Maximum Size Subarray Sum Equals k

Given an integer array `nums` and an integer `k`,
return the maximum length of a subarray that sums to `k`.

If there is no such subarray, return 0.

Example:
Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3.

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [2, 1] sums to 3? No.
The subarray [-1, 2] sums to 1 with length 2.

Algorithm:
1. Use a prefix sum approach.
2. Maintain a running sum `total`.
3. Use a hashmap `seen` to store the first occurrence index of each prefix sum.
4. For each index:
   - If `total == k`, update answer as `i + 1`.
   - If `(total - k)` exists in `seen`, a subarray summing to `k` exists.
     Update the maximum length.
5. Store prefix sum in hashmap only if it is not already present
   (to ensure maximum length).

Time Complexity: O(n), where n is the length of the array
Space Complexity: O(n), for the hashmap
"""

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        ans = 0
        seen = {}

        for i, num in enumerate(nums):
            total += num

            if total == k:
                ans = max(ans, i + 1)

            remain = total - k
            if remain in seen:
                ans = max(ans, i - seen[remain])

            if total not in seen:
                seen[total] = i

        return ans


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxSubArrayLen([1, -1, 5, -2, 3], 3) == 4
    assert sol.maxSubArrayLen([-2, -1, 2, 1], 1) == 2
    assert sol.maxSubArrayLen([1, 2, 3], 6) == 3
    assert sol.maxSubArrayLen([1, -1, 1, -1], 0) == 4
    assert sol.maxSubArrayLen([], 0) == 0

    print("All test cases passed!")
