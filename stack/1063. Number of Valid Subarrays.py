
"""
===========================================================
1063. Number of Valid Subarrays
===========================================================

🧩 Problem:
Given an integer array `nums`, count the number of subarrays such that the **minimum** of the subarray is equal to its **first element**.

Formally, for each starting index `i`, count how many subarrays `nums[i..j]` (with `j ≥ i`) satisfy:
- `nums[i] ≤ nums[k]` for all `k` in `[i..j]`.

🎯 Goal:
Return the **total number** of such subarrays across all start indices.  
Use a **monotonic stack** to achieve **O(n)** time and **O(n)** space.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  `nums = [1,4,2]`  
Valid subarrays:  
- start at 0: `[1]`, `[1,4]` (stop before `2` since `2 < 1` is false, but here `2 < 1` is false—actually we stop because `2 < 1` would be strictly smaller; since `2` is not < `1`, it’s okay; correction: we stop at a strictly **smaller** than the start, so we can include `4`, but not beyond an element `< 1`)  
- start at 1: `[4]`  
- start at 2: `[2]`  
Output: `4`

Example 2:
Input:  `nums = [1,3,3]`  
Valid subarrays:  
- start at 0: `[1]`, `[1,3]`, `[1,3,3]`  
- start at 1: `[3]`, `[3,3]`  
- start at 2: `[3]`  
Output: `6`

Example 3:
Input:  `nums = [2,1]`  
Valid subarrays:  
- start at 0: `[2]` (cannot include `1` since `1 < 2` is strictly smaller)  
- start at 1: `[1]`  
Output: `2`

Example 4:
Input:  `nums = [3,2,1]`  
Valid subarrays: `[3]`, `[2]`, `[1]`  
Output: `3`

-----------------------------------------------------------
Algorithm — Monotonic Increasing Stack:
-----------------------------------------------------------

Core idea:
For each index `i`, the number of valid subarrays **starting at `i`** equals the distance to the **next element strictly smaller** than `nums[i]` on its right. If no such element exists, we can extend to the end.

Why “strictly smaller”?  
- Equal values are allowed (the minimum remains the first element).  
- A strictly smaller value breaks the condition (the first element would no longer be the minimum).

Steps:
1. Traverse the array from **right to left** maintaining a stack of indices whose values are in **strictly increasing** order from bottom to top.
2. For index `i` with value `x = nums[i]`:
   - Pop from the stack while `nums[stack[-1]] >= x` to ensure the next remaining top (if any) is **strictly smaller** than `x`.
   - Let `idx` be `stack[-1]` if the stack is not empty; otherwise `n` (no smaller to the right).
   - The count of valid subarrays starting at `i` is `idx - i`.
   - Push `i` onto the stack.
3. Sum these counts for all `i`.

This works because the first strictly smaller element marks the earliest position where the first element would be beaten by a smaller minimum if we extend further.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

- **Time Complexity:** `O(n)`  
  Each index is pushed and popped at most once.

- **Space Complexity:** `O(n)`  
  The stack can hold up to `n` indices in the worst case (strictly increasing array).

-----------------------------------------------------------
"""

# Python 3 solution in the requested style

from typing import List

class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        LeetCode 1063: Number of Valid Subarrays
        Counts subarrays where the minimum equals the first element.

        Approach:
        - For each start index i, find the index of the next element to the right that is
          STRICTLY smaller than nums[i]. If none, treat as n.
        - The number of valid subarrays starting at i is exactly (next_smaller_index - i).
        - Use a monotonic increasing stack scanning right-to-left to compute those distances
          in O(n) time.

        Why it works:
        - Equal values do not break validity; only a strictly smaller value does.
        - The "next strictly smaller" boundary determines how far we can extend right.
        """
        n = len(nums)
        stack = []  # holds indices; values are strictly increasing from bottom to top
        total = 0

        for i in range(n - 1, -1, -1):
            # Ensure the top is the next STRICTLY smaller value
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            idx = stack[-1] if stack else n  # next index with value < nums[i], or n if none
            total += idx - i
            stack.append(i)

        return total


#------------------------------------
# Driver Test
#------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.validSubarrays([1,4,2]))   # 4
    print(sol.validSubarrays([1,3,3]))   # 6
    print(sol.validSubarrays([2,1]))     # 2
    print(sol.validSubarrays([3,2,1]))   # 3
    print(sol.validSubarrays([1]))       # 1
    print(sol.validSubarrays([1,1]))     # 3
    print(sol.validSubarrays([1,2]))     # 3
