# ------------------------------------------------------------
# 410: Split Array Largest Sum
# ------------------------------------------------------------
# Problem:
# Given an array nums of n non-negative integers and an integer k,
# split the array into k or fewer non-empty contiguous subarrays
# such that the largest sum among these subarrays is minimized.
#
# Example:
# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
#
# Explanation:
# Split the array into [7,2,5] and [10,8], sums = 14 and 18.
# Maximum sum = 18, which is minimized.
#
# ------------------------------------------------------------
# Algorithm:
# 1. Set low = max(nums), high = sum(nums)
# 2. Binary search on possible largest subarray sum (mid):
#    - Use a greedy split:
#        * Add numbers to current subarray until total > mid
#        * Start a new subarray with current number
#        * If total subarrays used <= k → feasible
# 3. Adjust binary search:
#    - Feasible → try smaller mid (r = mid - 1)
#    - Not feasible → try larger mid (l = mid + 1)
# 4. Return minimum feasible largest sum
#
# ------------------------------------------------------------
# Time Complexity: O(n log(sum(nums)))
# Space Complexity: O(1)
# ------------------------------------------------------------
# Test Case:
# nums = [7,2,5,10,8], k = 2
# Expected Output: 18
# ------------------------------------------------------------

from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(maxNum: int) -> bool:
            count = 1  # start with first subarray
            total = 0
            for n in nums:
                if total + n <= maxNum:
                    total += n
                else:
                    count += 1
                    total = n
            return count <= k
        
        if not nums or len(nums) < k:
            return -1
        
        l = max(nums)
        r = sum(nums)
        ans = r
        
        while l <= r:
            mid = (l + r) // 2
            if can_split(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans

# ------------------- Test Run -------------------
if __name__ == "__main__":
    test_cases = [
        ([7,2,5,10,8], 2),
        ([1,2,3,4,5], 2),
        ([1,4,4], 3)
    ]
    
    sol = Solution()
    for nums, k in test_cases:
        result = sol.splitArray(nums, k)
        print("Input: nums =", nums, ", k =", k)
        print("Output:", result)
