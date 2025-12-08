""" 
===========================================================
962. Maximum Width Ramp
===========================================================

🧩 Problem:
You are given an integer array `nums`.

A **ramp** is a pair of indices `(i, j)` with `i < j` such that:
    • `nums[i] <= nums[j]`

The **width** of the ramp is `j - i`.

🎯 Goal:
Return the **maximum width** among all valid ramps `(i, j)`.
If no ramp exists (e.g., the array is strictly decreasing), return `0`.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  nums = [6, 0, 8, 2, 1, 5]

Some valid ramps:
    (1, 2): nums[1]=0 <= 8 → width = 1
    (1, 5): 0 <= 5 → width = 4  ← maximum
    (3, 5): 2 <= 5 → width = 2

Output: 4


Example 2:
Input:  nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]

A wide ramp:
    (2, 9): nums[2]=1 <= 1 → width = 7

Output: 7


Example 3:
Input:  nums = [5, 4, 3, 2, 1]

Strictly decreasing:
    No pair i<j with nums[i] <= nums[j].

Output: 0

-----------------------------------------------------------
Algorithm — Monotonic Decreasing Stack + Right Scan:
-----------------------------------------------------------

Pattern: 📉 Build candidate starts, then expand from the right.

We want to maximize `j - i` while ensuring `nums[i] <= nums[j]`.

Steps:

1️⃣ **Build a stack of candidate left indices (i) with strictly decreasing values:**
    - Scan left to right.
    - Push index `i` to `stack` only if `nums[i] < nums[stack[-1]]` (or stack is empty).
    - This ensures `nums[stack[0]] > nums[stack[1]] > ...`, keeping only the best (earliest & smallest) left endpoints.

2️⃣ **Scan from right to left (j from n-1 down to 0):**
    - While the top candidate `i = stack[-1]` satisfies `nums[i] <= nums[j]`,
      pop it and compute `width = j - i`, updating the maximum.
    - We pop because a smaller future `j` cannot yield a wider ramp for that `i`.

3️⃣ **Early exit:**
    - If the stack becomes empty, all candidates have been matched; break the loop.

This guarantees each index is pushed and popped at most once → linear time.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Let n = len(nums).

Time Complexity:   O(n)
    - One forward pass to build the stack + one backward pass to compute widths.

Space Complexity:  O(n)
    - The stack may hold up to n indices in the worst case (strictly decreasing array).

-----------------------------------------------------------
Python Implementation:
-----------------------------------------------------------
"""


from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []  # indices with strictly decreasing nums-values

        # 1) Build candidate left endpoints
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        # 2) Scan from the right to get widest ramps first
        result = 0
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                left = stack.pop()
                result = max(result, j - left)
            if not stack:  # all candidates matched
                break

        return result


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxWidthRamp([6,0,8,2,1,5]))            # Expected: 4
    print(sol.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))    # Expected: 7
    print(sol.maxWidthRamp([5,4,3,2,1]))              # Expected: 0
    print(sol.maxWidthRamp([1,2,3,4,5]))              # Expected: 4 (0 to 4)
    print(sol.maxWidthRamp([4,1,2,3,1,5]))            # Expected: 5 (0 to 5)
