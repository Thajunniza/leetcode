""" 
===========================================================
456. 132 Pattern
===========================================================

🧩 Problem:
You are given an array of integers `nums`.

A **132 pattern** is a subsequence of three integers `(nums[i], nums[j], nums[k])`
with indices `i < j < k` such that:

    nums[i] < nums[k] < nums[j]

🎯 Goal:
Return `True` if there is a **132 pattern** in `nums`, otherwise return `False`.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  nums = [1, 2, 3, 4]
Explanation:
    No triple (i < j < k) with nums[i] < nums[k] < nums[j].
Output: False

Example 2:
Input:  nums = [3, 1, 4, 2]
Explanation:
    The triple (1, 4, 2) with indices (i=1, j=2, k=3) gives 1 < 2 < 4.
Output: True

Example 3:
Input:  nums = [-1, 3, 2, 0]
Explanation:
    Possible triples like (-1, 3, 2) satisfy -1 < 2 < 3.
Output: True

-----------------------------------------------------------
Algorithm — Recommended (Right-to-Left Monotonic Stack):
-----------------------------------------------------------

Pattern: 📉 Scan from right; track candidates for “3” and “2”.

Intuition:
- We want `nums[i] < nums[k] < nums[j]` with `i < j < k`.
- Traverse **from right to left**:
  - Maintain a **monotonic decreasing stack** of candidates for `nums[j]` (the “3”).
  - Keep a variable `third` that stores the **best candidate for `nums[k]`** (the “2”), which is the last popped value smaller than the current “3”.
- If we encounter a value `x = nums[i]` that is **less than `third`**, then `x < third < top_of_stack` → found 132.

Steps:
1️⃣ Initialize `stack = []` and `third = -∞`.
2️⃣ For each `x` from right to left:
    • If `x < third` → return `True`.
    • While stack and `x > stack[-1]`, set `third = stack.pop()` (popped becomes new “2”).
    • Push `x` onto `stack` (candidate “3”).
3️⃣ If loop finishes, return `False`.

Why it works:
- The stack holds decreasing “peaks” as possible `nums[j]`.
- Each popped value becomes a new `nums[k]` candidate (`third`) that is **less than** a valid `nums[j]` seen to its right.
- Finding any `nums[i]` smaller than `third` completes the inequality.

⏱ Complexity:
- Time: `O(n)` — each element is pushed/popped at most once.
- Space: `O(n)` — stack in worst case.

-----------------------------------------------------------
Python Implementation (Recommended):
-----------------------------------------------------------

"""

from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        stack = []              # candidates for j (the "3"), kept decreasing
        third = float('-inf')   # best candidate for k (the "2")

        for x in reversed(nums):
            # x plays "1": if it's less than our "2", we found 1 < 2 < 3
            if x < third:
                return True

            # Maintain decreasing stack; popped values are new candidates for "2"
            while stack and x > stack[-1]:
                third = stack.pop()

            # Push current as a candidate "3"
            stack.append(x)

        return False
""" 
-----------------------------------------------------------
Alternative — Left-to-Right Stack with Prefix-Min per j:
-----------------------------------------------------------

Pattern: 🧭 Track `min_before_j` and candidate “3”s; test current as “2”.

Intuition:
- As you scan left-to-right, keep:
  • `min_before`: the minimum value seen so far (candidate “1”).
  • A stack of pairs `[j_value, min_before_j]` for each index `j` (candidate “3”, with the best “1” before it).
- For current number `n` (candidate “2” at k):
  • Pop while `n >= j_value` to ensure `n < j_value`.
  • If stack exists and `n > min_before_j`, then `min_before_j < n < j_value` → 132 found.

⏱ Complexity:
- Time: `O(n)`
- Space: `O(n)`

-----------------------------------------------------------
Python Implementation (Alternative):
-----------------------------------------------------------
"""

from typing import List

class SolutionAlt:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        stack = []              # each entry: [j_value, min_before_j]
        min_before = nums[0]    # prefix minimum (candidate "1")

        for n in nums:
            # Maintain stack with j_value strictly greater than current n
            while stack and n >= stack[-1][0]:
                stack.pop()

            # If current n ("2") is greater than min_before_j ("1"),
            # and stack top j_value > n, we have 1 < 2 < 3 with i < j < k.
            if stack and n > stack[-1][1]:
                return True

            # Record current as a future candidate "3", with its prefix min
            stack.append([n, min_before])
            min_before = min(min_before, n)

        return False


def run_tests():
    tests = [
        ([1, 2, 3, 4], False),
        ([3, 1, 4, 2], True),
        ([-1, 3, 2, 0], True),
        ([1, 0, 1, -4, -3], False),
        ([3, 5, 0, 3, 4], True),     # 3, 5, 4
        ([6, 12, 3, 4, 6, 11, 20], True),  # 3, 6, 4 or 3, 11, 6
        ([1, 4, 0, -1, -2, -3, -1, -2], True),  # 1, 4, -1
        ([5, 4, 3, 2, 1], False),
    ]
    s = Solution()
    s_alt = SolutionAlt()
    for arr, expected in tests:
        r1 = s.find132pattern(arr)
        r2 = s_alt.find132pattern(arr)
        print(f"{arr}: Rec={r1}, Alt={r2}, Expected={expected}, OK={r1==expected and r2==expected}")

if __name__ == "__main__":
    run_tests()
