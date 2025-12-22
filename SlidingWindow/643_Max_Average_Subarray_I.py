"""
===========================================================
643. Maximum Average Subarray I
===========================================================

🧩 Problem:
You are given an integer array `nums` and an integer `k`.

Find the contiguous subarray of length `k` that has the maximum average,
and return that maximum average value.

🎯 Goal:
Return the maximum possible average among all subarrays of size `k`.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  nums = [1,12,-5,-6,50,3], k = 4
Windows of size 4:
  [1,12,-5,-6]   sum = 2   avg = 0.5
  [12,-5,-6,50]  sum = 51  avg = 12.75   ✅ max
  [-5,-6,50,3]   sum = 42  avg = 10.5
Output: 12.75

Example 2:
Input:  nums = [5], k = 1
Output: 5.0

-----------------------------------------------------------
Algorithm — Fixed Sliding Window (size k):
-----------------------------------------------------------

1. Compute the sum of the first window of size k.
2. Set maxTotal = that window sum.
3. Slide the window one step at a time:
     - Add the new entering element: nums[i]
     - Remove the leaving element:  nums[i-k]
     - Update maxTotal = max(maxTotal, total)
4. Return maxTotal / k (use float division to avoid integer truncation).

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)  (each element enters and leaves the window once)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1)  (constant extra space)

-----------------------------------------------------------

"""

# ------------------------------------
# 643. Maximum Average Subarray I — Fixed Sliding Window
# ------------------------------------

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)

        total = 0
        for i in range(k):
            total += nums[i]

        maxTotal = total

        for i in range(k, n):
            total += nums[i] - nums[i - k]
            maxTotal = max(maxTotal, total)

        return float(maxTotal) / k


# ------------------------------------
# Driver Test
# ------------------------------------

s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))
# Expected: 12.75

print(s.findMaxAverage([5], 1))
# Expected: 5.0
