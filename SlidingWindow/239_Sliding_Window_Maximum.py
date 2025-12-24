""" 
===========================================================
239. Sliding Window Maximum
===========================================================

🧩 Problem:
You are given an integer array `nums` and an integer `k`.

A sliding window of size `k` moves from left to right.
For each window, return the **maximum value** in that window.

🎯 Goal:
Return an array of length `n - k + 1` where each element is the maximum
of the corresponding window.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation (windows):
[1, 3, -1] -> 3
[3, -1,-3] -> 3
[-1,-3, 5] -> 5
[-3, 5, 3] -> 5
[5, 3, 6] -> 6
[3, 6, 7] -> 7

Example 2:
Input:  nums = [1], k = 1
Output: [1]

-----------------------------------------------------------
Algorithm — Monotonic Deque (Decreasing):
-----------------------------------------------------------

Maintain a deque of indices such that their values are in **decreasing order**.
The front of the deque always holds the index of the current window maximum.

For each index `i`:
1. Remove indices from the front if they are **out of the window** (i - k).
2. Remove indices from the back while nums[i] >= nums[deque[-1]]
   (they can never be maximum again).
3. Append i to the deque.
4. Once i >= k - 1, record nums[deque[0]] as the window maximum.

Key idea:
Each index is added and removed at most once → O(n).

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(k)

-----------------------------------------------------------
"""
# ------------------------------------
# 239. Sliding Window Maximum
# Monotonic Deque (Decreasing)
# ------------------------------------

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []
        if k == 1:
            return nums

        q = deque()  # stores indices, nums[q] is decreasing
        res = []

        for i, val in enumerate(nums):
            # 1) remove out-of-window indices
            while q and q[0] <= i - k:
                q.popleft()

            # 2) maintain decreasing order in deque
            while q and nums[q[-1]] <= val:
                q.pop()

            # 3) add current index
            q.append(i)

            # 4) record max once first window is formed
            if i >= k - 1:
                res.append(nums[q[0]])

        return res


# ------------------------------------
# Driver Test
# ------------------------------------

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Expected: [3,3,5,5,6,7]
    print(sol.maxSlidingWindow([1], 1))                  # Expected: [1]
    print(sol.maxSlidingWindow([9, 11], 2))              # Expected: [11]
    print(sol.maxSlidingWindow([4,-2], 2))               # Expected: [4]
