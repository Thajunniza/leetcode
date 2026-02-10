"""
===========================================================
560. Subarray Sum Equals K
===========================================================

Problem:
--------
Given an integer array `nums` and an integer `k`, return the
number of continuous subarrays whose sum equals `k`.

Example:
--------
Input: nums = [1,1,1], k = 2
Output: 2

Explanation:
Subarrays [1,1] starting at indices 0 and 1 sum to 2.

Approach:
---------
Prefix Sum + Hash Map (Optimal O(n) solution)

1. Maintain a running cumulative sum `total`.
2. Maintain a hash map `seen` to store frequency of prefix sums.
   - Initialize with {0: 1} to handle subarrays starting at index 0.
3. For each element `nums[i]`:
   - Update total += nums[i]
   - Check if `total - k` exists in `seen`:
       * If yes, add its frequency to the count of valid subarrays.
   - Update `seen[total] += 1` (or initialize to 1 if not present)

This works because:
   If total_sum(i) - total_sum(j) = k → subarray nums[j+1:i] sums to k

Time Complexity:
----------------
O(n) — single pass through the array.

Space Complexity:
-----------------
O(n) — for the hash map storing prefix sum frequencies.

Author:
-------
Thajunniza M A
"""

# -----------------------------
# Solution Class
# -----------------------------
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = {0: 1}  # prefix sum frequency
        total = 0
        count = 0

        for val in nums:
            total += val
            rem = total - k
            if rem in seen:
                count += seen[rem]
            seen[total] = seen.get(total, 0) + 1
        
        return count


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":

    tests = [
        ([1,1,1], 2, 2),
        ([1,2,3], 3, 2),      # [1,2] and [3]
        ([1,-1,0], 0, 3),     # [1,-1], [-1,0], [0]
        ([3,4,7,2,-3,1,4,2], 7, 4),
        ([], 0, 0),
        ([5], 5, 1),
    ]

    sol = Solution()
    for i, (nums, k, expected) in enumerate(tests, 1):
        result = sol.subarraySum(nums, k)
        print(f"Test {i}: nums={nums}, k={k} | expected={expected}, got={result}")
