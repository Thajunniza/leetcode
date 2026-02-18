"""
===========================================================
645. Set Mismatch (Index Marking Technique)
===========================================================

🧩 Problem:
You are given an integer array nums of size n containing numbers 
from 1 to n.

One number appears twice (duplicate) and one number is missing.
Return them as [duplicate, missing].

You must solve it in O(n) time and O(1) extra space.

-----------------------------------------------------------
Approach — Index Marking (Sign Flip Technique):
-----------------------------------------------------------
Since numbers are in range [1, n], each number maps to an index:

number x → index (x - 1)

Algorithm:

1. Traverse the array.
2. For each number x:
      - Go to index abs(x) - 1
      - If value there is already negative → duplicate found
      - Otherwise, mark it negative (visited)
3. Traverse again:
      - The index whose value is still positive
        corresponds to the missing number.

Why this works:
- Negative value = number has been seen
- Positive value after traversal = number never seen

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

class Solution(object):
    def findErrorNums(self, nums):
        duplicate = -1
        missing = -1

        # Step 1: Find duplicate
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicate = abs(num)
            else:
                nums[index] *= -1

        # Step 2: Find missing
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break

        return [duplicate, missing]


# ==========================
# ✅ Test Cases
# ==========================
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 2, 2, 4], [2, 3]),
        ([1, 1], [1, 2]),
        ([2, 2], [2, 1]),
        ([3, 2, 3, 4, 6, 5], [3, 1]),
        ([4, 3, 2, 7, 8, 2, 3, 1], [2, 5]),
    ]

    for nums, expected in test_cases:
        result = sol.findErrorNums(nums[:])  # copy to avoid mutation
        print("Input:     ", nums)
        print("Output:    ", result)
        print("Expected:  ", expected)
        print("Pass:      ", result == expected)
        print("-" * 40)
