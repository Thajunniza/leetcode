"""
===========================================================
209. Minimum Size Subarray Sum
===========================================================

🧩 Problem:
Given an array of **positive integers** `nums` and a positive integer `target`,
find the **minimal length** of a contiguous subarray
for which the sum is **greater than or equal to target**.

If there is no such subarray, return `0`.

🎯 Goal:
Return the **smallest window size** whose sum ≥ target.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: Subarray [4,3] has the minimal length 2.

Example 2:
Input:  target = 4, nums = [1,4,4]
Output: 1
Explanation: Subarray [4] has length 1.

Example 3:
Input:  target = 11, nums = [1,1,1,1,1]
Output: 0
Explanation: No subarray sum reaches 11.

-----------------------------------------------------------
Algorithm — Sliding Window (Expand + Shrink):
-----------------------------------------------------------

Maintain a window [left .. right] whose sum is tracked.

1. Initialize:
   - left = 0
   - total = 0
   - minLen = infinity
2. Expand `right` from 0..n-1:
   - Add nums[right] to total
3. While total >= target:
   - Update minLen with current window size
   - Shrink window from the left:
       → subtract nums[left]
       → move left forward
4. If minLen was never updated, return 0
   else return minLen

Key idea:
When the sum condition is satisfied, **shrink aggressively**
to find the smallest valid window.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)  
(each pointer moves at most once)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1)  
(no extra data structures)

-----------------------------------------------------------

"""
# ------------------------------------
# 209. Minimum Size Subarray Sum
# Sliding Window (Shrink from Left)
# ------------------------------------

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        total = 0
        minLen = float('inf')

        for right, val in enumerate(nums):
            total += val

            while total >= target:
                minLen = min(minLen, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if minLen == float('inf') else minLen


# ------------------------------------
# Driver Test
# ------------------------------------

sol = Solution()
print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))  # Expected: 2
print(sol.minSubArrayLen(4, [1,4,4]))        # Expected: 1
print(sol.minSubArrayLen(11, [1,1,1,1,1]))   # Expected: 0
