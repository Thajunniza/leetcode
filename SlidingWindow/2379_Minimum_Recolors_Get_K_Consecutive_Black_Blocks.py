""" 
===========================================================
2379. Minimum Recolors to Get K Consecutive Black Blocks
===========================================================

🧩 Problem:
You are given a string `blocks` consisting of 'B' (black) and 'W' (white) blocks.  
Return the minimum number of recolors needed to obtain **k consecutive black blocks**.

🎯 Goal:
Find the minimum number of white blocks in **any window of size k**.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation: The window "WBBWWBB" has 3 whites → recolor them.

Example 2:
Input:  blocks = "WBWBBBW", k = 2
Output: 0
Explanation: The window "BB" already has 2 blacks → no recolor needed.

-----------------------------------------------------------
Algorithm — Sliding Window:
-----------------------------------------------------------

1. Initialize:
   - `left = 0`
   - `w = 0` (count of whites in current window)
   - `result = inf`

2. Iterate `right` over the string:
   - If `blocks[right] == 'W'` → `w += 1`
   - When window size = k:
       → Update `result = min(result, w)`
   - If window exceeds size k:
       → Remove left element if it is 'W' (`w -= 1`)
       → Increment `left`
       → Update `result = min(result, w)`

3. Return `result`

Key idea:
- Only track whites in a sliding window of size k.  
- The **minimum white count** is the minimum recolors needed.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n) — each character visited once

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1) — only a few counters are used

"""
# ------------------------------------
# 2379. Minimum Recolors to Get K Consecutive Black Blocks
# Sliding Window
# ------------------------------------

class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        left = 0
        w = 0
        result = float("inf")

        for right, val in enumerate(blocks):
            if val == "W":
                w += 1

            # First full window
            if right == k - 1:
                result = min(result, w)

            # Slide window
            if right >= k:
                if blocks[left] == "W":
                    w -= 1
                left += 1
                result = min(result, w)

        return result

# ------------------------------------
# Driver Test
# ------------------------------------

sol = Solution()
print(sol.minimumRecolors("WBBWWBBWBW", 7))  # Expected: 3
print(sol.minimumRecolors("WBWBBBW", 2))     # Expected: 0
print(sol.minimumRecolors("BBBBB", 3))       # Expected: 0
print(sol.minimumRecolors("WWWW", 2))        # Expected: 2
