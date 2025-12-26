"""
===========================================================
2302. Count Subarrays With Score Less Than K
===========================================================

🧩 Problem:
You are given a positive integer array `nums` and an integer `k`.
A **subarray score** is defined as:

    (sum of subarray) * (length of subarray)

Return the number of non-empty contiguous subarrays whose score
is strictly less than `k`.

🎯 Goal:
Count how many continuous windows `[l .. r]` satisfy:
    
    (sum(nums[l..r])) * (r - l + 1)  <  k

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  nums = [2, 1, 4, 3], k = 10
Output: 5
Explanation:
Valid subarrays are:
[2], [2,1], [1], [4], [3]

Example 2:
Input:  nums = [1,1,1], k = 5
Output: 5
Explanation:
Valid subarrays:
[1], [1], [1], [1,1], [1,1]

Example 3:
Input: nums = [3,2,1], k = 7
Output: 3

-----------------------------------------------------------
Algorithm — Sliding Window (Two Pointers):
-----------------------------------------------------------

Because all values in `nums` are POSITIVE, we can use a
sliding window and never need to rewind `right`.

Maintain a running window `[left .. right]`:

1. Expand `right` and add nums[right] to a running sum.
2. Compute:
        score = total_sum * window_length
   While score >= k:
        Shrink window by subtracting nums[left] and increment left.
3. At each `right`, every subarray ending at `right` and starting
   anywhere from `left` to `right` is valid:
        result += (right - left + 1)

Key Idea:
We avoid recomputing sum repeatedly by keeping a running sum
and adjusting with left pointer.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n) — each index visited at most twice.

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1) — uses constant auxiliary space.

-----------------------------------------------------------
"""
# ------------------------------------
# 2302. Count Subarrays With Score < K
# Sliding Window — Two Pointers
# ------------------------------------

class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        total = 0
        result = 0

        for right, val in enumerate(nums):
            total += val

            # shrink window while score ≥ k
            while total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1

            # all subarrays ending at right are valid
            result += (right - left + 1)

        return result


# ------------------------------------
# Driver Test
# ------------------------------------
sol = Solution()
print(sol.countSubarrays([2,1,4,3], 10))   # Expected: 5
print(sol.countSubarrays([1,1,1], 5))      # Expected: 5
print(sol.countSubarrays([3,2,1], 7))      # Expected: 3
print(sol.countSubarrays([1], 1))          # Expected: 0 (1 * 1 = 1 not < 1)
