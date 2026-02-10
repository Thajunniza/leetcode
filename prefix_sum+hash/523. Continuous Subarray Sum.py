"""
===========================================================
523. Continuous Subarray Sum
===========================================================

Problem:
--------
Given an integer array `nums` and an integer `k`, 
return true if the array has a **continuous subarray of size at least 2** 
whose elements sum to a multiple of k.

Formally, check if there exists a subarray nums[i..j] (i < j) 
such that sum(nums[i..j]) is a multiple of k (i.e., divisible by k).

Example:
--------
Input: nums = [23,2,4,6,7], k = 6
Output: True

Explanation:
The subarray [2,4] sums to 6 which is a multiple of 6.

Approach:
---------
Prefix Sum + Modulo + Hash Map

1. Maintain cumulative sum modulo k: total_sum % k
2. Maintain a hashmap `seen` to store the earliest index of each remainder
   - Initialize with {0: -1} to handle subarrays starting at index 0
3. For each index i:
   - Update total += nums[i]
   - If k != 0, compute remainder = total % k
   - If remainder seen before at index j:
       * If subarray length i - j >= 2 → return True
   - Else, store remainder with current index
4. If no valid subarray found → return False

Time Complexity:
----------------
O(n) — single pass through the array

Space Complexity:
-----------------
O(min(n, k)) — hashmap stores at most n remainders

Author:
-------
Thajunniza M A
"""

# -----------------------------
# Solution Class
# -----------------------------
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {0: -1}  # remainder -> earliest index
        total = 0

        for i, num in enumerate(nums):
            total += num
            if k != 0:
                remainder = total % k
            else:
                remainder = total

            if remainder in seen:
                if i - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = i
        
        return False


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":

    tests = [
        ([23,2,4,6,7], 6, True),
        ([23,2,6,4,7], 6, True),
        ([23,2,6,4,7], 13, False),
        ([0,0], 0, True),
        ([1,2,3], 5, True),  # subarray [2,3] sums to 5
        ([1], 2, False),
    ]

    sol = Solution()
    for i, (nums, k, expected) in enumerate(tests, 1):
        result = sol.checkSubarraySum(nums, k)
        print(f"Test {i}: nums={nums}, k={k} | expected={expected}, got={result}")
