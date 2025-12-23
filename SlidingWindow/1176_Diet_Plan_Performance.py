"""
===========================================================
1176. Diet Plan Performance
===========================================================

🧩 Problem:
You are given an array `calories` where `calories[i]` represents calories
consumed on day `i`.

Given:
- an integer `k` (window size),
- integers `lower` and `upper`,

Evaluate each **contiguous subarray of length `k`** and compute a score.

Scoring rules for each window:
- If total calories > upper → +1
- If total calories < lower → −1
- Otherwise → 0

🎯 Goal:
Return the **total score** after evaluating all windows.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:
    calories = [1,2,3,4,5]
    k = 1
    lower = 3
    upper = 3
Output:
    0

Example 2:
Input:
    calories = [3,2]
    k = 2
    lower = 0
    upper = 1
Output:
    1

-----------------------------------------------------------
Algorithm — Fixed Size Sliding Window:
-----------------------------------------------------------

1. Compute the sum of the first window of size `k`
2. Score the window based on `lower` and `upper`
3. Slide the window one step at a time:
   - Add the new element entering the window
   - Subtract the element leaving the window
   - Score each window
4. Accumulate and return the total score

Key idea:
Reuse the previous window sum to update the next window in O(1) time.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1)

-----------------------------------------------------------
"""
# ------------------------------------
# 1176. Diet Plan Performance
# Fixed Size Sliding Window
# ------------------------------------

class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if k <= 0 or k > len(calories):
            return 0

        def score(window_sum):
            if window_sum > upper:
                return 1
            if window_sum < lower:
                return -1
            return 0

        result = 0
        window_sum = sum(calories[:k])
        result += score(window_sum)

        for i in range(k, len(calories)):
            window_sum += calories[i] - calories[i - k]
            result += score(window_sum)

        return result


# ------------------------------------
# Driver Test
# ------------------------------------

sol = Solution()
print(sol.dietPlanPerformance([1,2,3,4,5], 1, 3, 3))  # Expected: 0
print(sol.dietPlanPerformance([3,2], 2, 0, 1))       # Expected: 1
print(sol.dietPlanPerformance([6,5,0,0], 2, 1, 5))   # Expected: 0
