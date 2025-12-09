"""
===========================================================
907. Sum of Subarray Minimums
===========================================================

🧩 Problem:
You are given an integer array `arr`.

For every **non-empty contiguous subarray** of `arr`, find the **minimum** value in that subarray.  
Return the **sum of all those minimums**.

Since the answer can be large, return it **modulo 10^9 + 7**.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:   arr = [3, 1, 2, 4]

All subarrays and their minimums:
    [3]        -> 3
    [3,1]      -> 1
    [3,1,2]    -> 1
    [3,1,2,4]  -> 1
    [1]        -> 1
    [1,2]      -> 1
    [1,2,4]    -> 1
    [2]        -> 2
    [2,4]      -> 2
    [4]        -> 4

Sum = 3 + 1 + 1 + 1 + 1 + 1 + 2 + 2 + 4 = 16

Output: 16


Example 2:
Input:   arr = [11, 81, 94, 43, 3]
Output:  444

(There are many subarrays; the sum of all their minimums is 444.)

-----------------------------------------------------------
Intuition — Contribution of Each Element:
-----------------------------------------------------------

Brute force:  
- Enumerate all subarrays, find the minimum of each → **O(n²)** or worse.  
Too slow for large `n`.

Instead, flip the perspective:

➡ For each index `i`, ask:
    “In how many subarrays is `arr[i]` the **minimum** value?”

If we know that count for each `i`, then:

    answer = Σ ( arr[i]  *  number_of_subarrays_where_arr[i]_is_min )

So the problem becomes:

1️⃣ For every `i`, count how many subarrays have `arr[i]` as their minimum.  
2️⃣ Multiply that count by `arr[i]`.  
3️⃣ Sum for all `i`.

How to count such subarrays?

Consider all subarrays that include index `i`:
They are defined by a start index `L` and end index `R` such that `L <= i <= R`.

`arr[i]` is the minimum in `[L..R]` **iff**:
- All elements between `L` and `R` are **≥ arr[i]**, and
- There is **no smaller value than `arr[i]`** in that range.

So for each index `i`, we find:

- `left[i]`  = how many positions we can extend to the **left** (including `i`)
             before seeing a **strictly smaller** element.
- `right[i]` = how many positions we can extend to the **right** (including `i`)
             before seeing a **smaller or equal** element.

Then:

    number_of_subarrays_where_arr[i]_is_min = left[i] * right[i]

Because:
- We have `left[i]` choices for the start `L`,
- And `right[i]` choices for the end `R`.

So the total contribution of `arr[i]` is:

    contribution[i] = arr[i] * left[i] * right[i]

Sum over all `i` and take modulo.

The only question left: how to compute `left[]` and `right[]` efficiently?

-----------------------------------------------------------
Monotonic Stack Trick — Previous Less & Next Less-or-Equal:
-----------------------------------------------------------

We use two passes with **monotonic stacks**:

1️⃣ First pass (left to right):
    - Maintain a stack of indices with **increasing values**.
    - For each position `i`, pop from stack while `arr[stack.top] > arr[i]`.
    - After popping:
        - If stack is non-empty, `stack.top` is the index of the **previous element ≤ arr[i]**.
          So the previous **strictly smaller** is either that or earlier.
          Distance: `left[i] = i - stack.top`.
        - If stack is empty, there is no smaller element to the left → `left[i] = i + 1`.
    - Push `i`.

Effectively:
- `left[i]` = distance to the previous **strictly smaller** element.

2️⃣ Second pass (right to left):
    - Maintain a stack (again increasing by value).
    - Iterate `i` from `n-1` down to `0`.
    - Pop while `arr[stack.top] >= arr[i]`.
      (Note the `>=` here — this gives us “next smaller or equal”.)
    - After popping:
        - If stack is non-empty, `stack.top` is the index of the next **smaller or equal** element.  
          Distance: `right[i] = stack.top - i`.
        - If stack is empty, no smaller/equal on the right → `right[i] = n - i`.
    - Push `i`.

Now we have:
- `left[i]`  → how far we can extend left.
- `right[i]` → how far we can extend right.

And contribution:

    arr[i] * left[i] * right[i]

-----------------------------------------------------------
Why `<` on the left but `<=` on the right?
-----------------------------------------------------------

This is to handle **duplicates** and avoid double-counting:

- On the **left**, we stop at **strictly smaller** (`<`):
  we allow equal elements to be grouped with the current one from the left side.
- On the **right**, we stop at **smaller or equal** (`<=` via the `>=` pop):
  we force equal elements to belong to the **left-most** index only.

This tie-breaking ensures that each subarray with equal minimums is counted exactly **once**, not multiple times.

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time:  `O(n)` — each element is pushed and popped from the stack at most once.
- Space: `O(n)` — arrays `left`, `right`, and the stacks.

-----------------------------------------------------------
Python Implementation (Monotonic Stack — Your Solution):
-----------------------------------------------------------
"""

from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        
        # left[i]: distance to previous strictly smaller element
        left = [0] * n
        stack = []
        for i, val in enumerate(arr):
            # Pop indices with values > current val (to maintain increasing stack)
            while stack and arr[stack[-1]] > val:
                stack.pop()
            
            if stack:
                # Previous index with value <= val, so strictly smaller is before this
                left[i] = i - stack[-1]
            else:
                # No smaller element on the left
                left[i] = i + 1
            
            stack.append(i)
        
        # right[i]: distance to next smaller-or-equal element
        right = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            # Pop indices with values >= current value to get "next smaller or equal"
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                # Next index with value < current or equal (due to popping >=)
                right[i] = stack[-1] - i
            else:
                # No smaller-or-equal element on the right
                right[i] = n - i
            
            stack.append(i)
        
        MOD = 10**9 + 7
        result = 0
        for i, val in enumerate(arr):
            result = (result + val * left[i] * right[i]) % MOD
        
        return result

"""
-----------------------------------------------------------
(Optional) Alternative — DP + Monotonic Stack (End-at-i Approach):
-----------------------------------------------------------

Pattern:  
- Let `dp[i]` = sum of minimums of all subarrays that **end at index `i`**.
- Final answer = Σ dp[i].

Idea:
- Maintain a monotonic increasing stack of indices `prev` such that `arr[prev] <= arr[i]`.
- Let `prev` be the nearest index to the left with `arr[prev] <= arr[i]`, or `-1` if none.
- Then:

      dp[i] = (prev == -1 ? 0 : dp[prev]) + (i - prev) * arr[i]

Why?

- `(i - prev)` = number of new subarrays ending at `i` where `arr[i]` becomes the minimum.
- `dp[prev]` carries forward contributions of subarrays ending at `prev` that can be extended.

Complexity:
- Time:  `O(n)`
- Space: `O(n)`

Python Implementation (Alternative):
"""

class SolutionAlt:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * n            # dp[i] = sum of mins of subarrays ending at i
        stack = []              # monotonic increasing stack of indices
        MOD = 10**9 + 7
        
        for i, val in enumerate(arr):
            # Maintain monotonic increasing stack
            while stack and arr[stack[-1]] > val:
                stack.pop()
            
            prev = stack[-1] if stack else -1
            
            # If prev == -1, dp contribution from before is 0
            prev_dp = dp[prev] if prev != -1 else 0
            dp[i] = (prev_dp + (i - prev) * val) % MOD
            
            stack.append(i)
        
        return sum(dp) % MOD


def run_tests():
    tests = [
        ([3, 1, 2, 4], 16),
        ([11, 81, 94, 43, 3], 444),
        ([1], 1),
        ([1, 1, 1], 6),       # subarrays: [1],[1],[1],[1,1],[1,1],[1,1,1] → 1+1+1+1+1+1 = 6
        ([2, 9, 7, 8, 3, 4, 6, 1], 88),  # known test
    ]
    
    s = Solution()
    s_alt = SolutionAlt()
    for arr, expected in tests:
        r1 = s.sumSubarrayMins(arr)
        r2 = s_alt.sumSubarrayMins(arr)
        print(f"{arr}: StackLR={r1}, DP+Stack={r2}, Expected={expected}, OK={r1==expected and r2==expected}")

if __name__ == "__main__":
    run_tests()
