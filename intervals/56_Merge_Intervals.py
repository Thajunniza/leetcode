"""
===========================================================
56. Merge Intervals
===========================================================

🧩 Problem:
You are given an array of intervals where
each interval is represented as:

    [start, end]

Merge all overlapping intervals and return an array
of the non-overlapping intervals that cover all ranges.

🎯 Goal:
Combine intervals so that:
- No two intervals overlap
- All original ranges are covered

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Example 2:
Input:  intervals = [[1,4],[4,5]]
Output: [[1,5]]

Example 3:
Input:  intervals = [[1,4],[2,3]]
Output: [[1,4]]

-----------------------------------------------------------
Algorithm — Intervals Pattern:
-----------------------------------------------------------

1. Sort intervals by their start time.
2. Initialize a result list with the first interval.
3. Iterate through remaining intervals:
    - Let the last interval in result be `prev`
    - If current.start <= prev.end:
          Merge by extending:
              prev.end = max(prev.end, current.end)
    - Else:
          No overlap → append current interval
4. Return the merged result list.

Key Idea:
After sorting by start time, an interval can only overlap
with the immediately previous interval.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n log n) — due to sorting

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(n) — output list

-----------------------------------------------------------
"""
# ------------------------------------
# 56. Merge Intervals
# Intervals Pattern
# ------------------------------------

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Step 1: sort by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            # overlap condition
            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        return merged


# ------------------------------------
# Driver Test
# ------------------------------------
sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))  # Expected: [[1,6],[8,10],[15,18]]
print(sol.merge([[1,4],[4,5]]))                # Expected: [[1,5]]
print(sol.merge([[1,4],[2,3]]))                # Expected: [[1,4]]
print(sol.merge([[1,4]]))                      # Expected: [[1,4]]
