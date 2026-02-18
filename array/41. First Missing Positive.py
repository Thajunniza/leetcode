"""
===========================================================
41. First Missing Positive
===========================================================

🧩 Problem:
Given an unsorted integer array nums,
return the smallest missing positive integer.

You must run in O(n) time and O(1) extra space.

-----------------------------------------------------------
Approach — Index Marking (Sign Encoding)
-----------------------------------------------------------

Key idea:
For array of size n, the answer must be in range [1, n+1].

Steps:

1. Replace negative numbers, zeros, and numbers > n with (n+1).
2. Use index marking:
      For each value x in [1, n]:
          mark nums[x-1] as negative.
3. The first index with positive value → missing number.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Step 1: Clean invalid values
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Step 2: Mark presence
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                nums[val - 1] = -abs(nums[val - 1])

        # Step 3: Find first missing
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


# ==========================
# ✅ Test Cases
# ==========================
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([1, 1], 2),
        ([2, 2], 1),
    ]

    for nums, expected in test_cases:
        result = sol.firstMissingPositive(nums[:])
        print("Input:     ", nums)
        print("Output:    ", result)
        print("Expected:  ", expected)
        print("Pass:      ", result == expected)
        print("-" * 40)
