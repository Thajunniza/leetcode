"""
===========================================================
503. Next Greater Element II
===========================================================

🧩 Problem:
You are given a **circular** integer array `nums` of length `n`.

For each element `nums[i]`, you need to find the **next greater element**:
    • Look to the right: i+1, i+2, …  
    • Because the array is circular, if you reach the end, continue from index 0.  
    • The **first** element strictly greater than `nums[i]` is its “next greater”.

If no such element exists, the result for that index is **-1**.

🎯 Goal:
Return an array `result` of length `n` where:

    result[i] = next greater element of nums[i]
             or -1 if there is none.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:
    nums = [1, 2, 1]

Circular neighbors:

    i = 0, value = 1
        Next elements: 2, 1  → first greater is 2   → result[0] = 2

    i = 1, value = 2
        Next elements: 1, 1  → no greater exists    → result[1] = -1

    i = 2, value = 1
        Next elements (wrap): 1, 2  → first greater is 2 → result[2] = 2

Output:
    [2, -1, 2]


Example 2:
Input:
    nums = [3, 8, 4, 1, 2]

For each index:

    i = 0, 3 → next greater is 8              → 8
    i = 1, 8 → no greater element             → -1
    i = 2, 4 → next greater (circular) is 8   → 8
    i = 3, 1 → next greater is 2              → 2
    i = 4, 2 → next greater (circular) is 3   → 3

Output:
    [8, -1, 8, 2, 3]

-----------------------------------------------------------
Why This Is a Monotonic Stack Problem (Circular Version):
-----------------------------------------------------------

We want the **next greater element to the right** for each index,  
but the array is **circular**, so we may wrap around.

Classic pattern:
    • Use a **monotonic decreasing stack** of indices.
    • For each new element, we pop all smaller elements from the stack and
      set their “next greater” to the current element.

To handle circular behavior:
    • We conceptually iterate the array **twice**:
          indices 0..n-1, then 0..n-2
    • We use:
          idx = i % n
      so that when i ≥ n, we’re “wrapping” over the array again.

Algorithm (your version):
    1. Initialize:
            n = len(nums)
            result = [-1] * n
            stack = []   # holds indices whose next greater is not found yet

    2. Loop i from 0 to (2*n - 2):
            idx = i % n

            While stack not empty AND nums[stack[-1]] < nums[idx]:
                → we found a next greater for stack[-1]
                → result[stack.pop()] = nums[idx]

            If i < n:
                → push idx onto stack (only first pass)

    3. When loop finishes:
            result already has:
                • next greater values filled, OR
                • -1 where none exists.

Why is this enough?
    • Any index i can see at most n-1 future elements in the circular scan.
    • Looping up to i = 2n-2 ensures we’ve exposed enough future indices for all.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    • Each index is pushed at most once and popped at most once.

Space Complexity:  O(n)
    • result and stack both use O(n) extra space.

-----------------------------------------------------------
Monotonic Stack Solution (Your Style)
-----------------------------------------------------------
"""

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack: List[int] = []
        i = 0

        # We iterate up to (2*n - 1) - 1 = 2n - 2
        # This is enough to cover all circular "look ahead" possibilities.
        while i < (2 * n) - 1:
            idx = i % n

            # Resolve next greater for indices whose value is smaller than nums[idx]
            while stack and nums[stack[-1]] < nums[idx]:
                result[stack.pop()] = nums[idx]

            # Only push indices in the first pass
            if i < n:
                stack.append(idx)

            i += 1

        return result


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.nextGreaterElements([1, 2, 1]))
    # Expected: [2, -1, 2]

    print(sol.nextGreaterElements([3, 8, 4, 1, 2]))
    # Expected: [8, -1, 8, 2, 3]

    print(sol.nextGreaterElements([5, 4, 3, 2, 1]))
    # Next greater (circular):
    # 5 → none → -1
    # 4 → 5
    # 3 → 5
    # 2 → 5
    # 1 → 5
    # Expected: [-1, 5, 5, 5, 5]

    print(sol.nextGreaterElements([1, 1, 1, 1]))
    # All equal; no strictly greater element exists
    # Expected: [-1, -1, -1, -1]
