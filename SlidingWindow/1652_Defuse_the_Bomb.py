"""
===========================================================
1652. Defuse the Bomb
===========================================================

🧩 Problem:
You are given a circular array `code` and an integer `k`.  
Replace every position with:

- If k > 0 → sum of next k elements
- If k < 0 → sum of previous |k| elements
- If k == 0 → replace all values with 0

Return the resulting transformed array.

🎯 Goal:
Efficiently compute transformed values using a sliding window
instead of recomputing each sum from scratch.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation:
Index 0 → 7+1+4 = 12
Index 1 → 1+4+5 = 10
Index 2 → 4+5+7 = 16
Index 3 → 5+7+1 = 13

Example 2:
Input:  code = [1,2,3,4], k = 0
Output: [0,0,0,0]

Example 3:
Input:  code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation:
Index 0 → previous 2 elements = 9 + 3 = 12
(think circular)

-----------------------------------------------------------
Algorithm — Circular Sliding Window (O(n)):
-----------------------------------------------------------

1️⃣ If k == 0 → return array of zeros  
2️⃣ Determine sliding window start and end:
   - For k > 0 → start at index 1, end = k
   - For k < 0 → start = n+k, end = n-1
3️⃣ Compute initial window sum
4️⃣ Slide window for each index:
      res[i] = total
      total -= code[left]
      total += code[right_next]
      move both left, right forward circularly

Key idea:
Use modulo arithmetic to wrap around the array.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)  — each index processed once

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1)  — only sliding window sum kept (output excluded)

-----------------------------------------------------------
"""

# ------------------------------------
# 1652. Defuse the Bomb — Sliding Window
# ------------------------------------

class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        res = [0] * n

        if k == 0:
            return res

        total = 0
        # Determine initial sliding window
        left = 1 if k > 0 else n + k
        right = k if k > 0 else n - 1

        # Build initial window
        for i in range(left, right + 1):
            total += code[i % n]

        # Slide across array
        for i in range(n):
            res[i] = total
            total -= code[left % n]
            left += 1
            right += 1
            total += code[right % n]

        return res


# ------------------------------------
# Driver Test
# ------------------------------------

sol = Solution()
print(sol.decrypt([5,7,1,4], 3))   # Expected: [12,10,16,13]
print(sol.decrypt([1,2,3,4], 0))   # Expected: [0,0,0,0]
print(sol.decrypt([2,4,9,3], -2))  # Expected: [12,5,6,13]
