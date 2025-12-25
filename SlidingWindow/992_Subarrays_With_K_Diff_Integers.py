"""
===========================================================
992. Subarrays With K Different Integers
===========================================================

🧩 Problem:
Given an integer array `nums` and an integer `k`,
return the number of subarrays that contain **exactly**
`k` distinct integers.

🎯 Goal:
Count how many contiguous subarrays include:
- exactly k unique values
(not more, not less)

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  nums = [1,2,1,2,3], k = 2
Output: 7
Explanation:
Subarrays with exactly 2 unique nums:
[1,2], [2,1], [1,2], [2,3],
[1,2,1], [2,1,2], [1,2,1,2]

Example 2:
Input:  nums = [1,2,1,3,4], k = 3
Output: 3
Explanation:
Exactly 3 unique:
[1,2,1,3], [2,1,3], [1,3,4]

-----------------------------------------------------------
Algorithm — Sliding Window (At Most K) Formula
-----------------------------------------------------------

Instead of counting "exactly K" directly,
compute using:

    EXACT(k) = AT_MOST(k) – AT_MOST(k - 1)

Where:
- AT_MOST(k) counts subarrays with ≤ k distinct numbers

Sliding Window Key Idea:
1️⃣ Expand `right` pointer
2️⃣ Track frequency of elements inside the window
3️⃣ If unique_count > k → shrink from left
4️⃣ Add (right - left + 1) to result each step
   (every window ending at right creates this many valid subarrays)

-----------------------------------------------------------
Time Complexity:
O(N) — every element enters and leaves window once

-----------------------------------------------------------
Python Solution (.py)
-----------------------------------------------------------
"""
class Solution(object):

    def subarraysWithKDistinct(self, nums, k):
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums, k):
        freq = {}
        left = 0
        result = 0

        for right, val in enumerate(nums):
            freq[val] = freq.get(val, 0) + 1

            # shrink while too many distinct
            while len(freq) > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            # all subarrays ending at right contribute
            result += (right - left + 1)

        return result

# -----------------------------
# DRIVER TEST
# -----------------------------
if __name__ == "__main__":

    tests = [
        ([1, 2, 1, 2, 3], 2, 7),
        ([1, 2, 1, 3, 4], 3, 3),
        ([1, 1, 1, 1], 1, 10),
        ([1, 2, 3], 1, 3),
        ([1, 2, 3], 2, 2),
        ([1, 2, 3], 3, 1),
    ]
    sol = Solution()
    for nums, k, expected in tests:
        result = sol.subarraysWithKDistinct(nums, k)
        print(f"nums={nums}, k={k} -> result={result}, expected={expected}, PASS={result==expected}")