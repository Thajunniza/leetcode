"""
===========================================================
252. Meeting Rooms
===========================================================

🧩 Problem:
You are given an array of meeting time intervals where
each interval is represented as:

    [start, end]

Determine if a person can attend all meetings
without any overlaps.

🎯 Goal:
Return:
- True  → if no meetings overlap
- False → if at least one overlap exists

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  intervals = [[0,30],[5,10],[15,20]]
Output: False
Explanation:
Meeting [5,10] overlaps with [0,30]

Example 2:
Input:  intervals = [[7,10],[2,4]]
Output: True
Explanation:
Meetings do not overlap

Example 3:
Input:  intervals = [[1,2],[2,3],[3,4]]
Output: True
Explanation:
Touching endpoints are allowed

-----------------------------------------------------------
Algorithm — Intervals Pattern:
-----------------------------------------------------------

1. If there are no intervals → return True
2. Sort intervals by start time
3. Track the end time of the previous meeting
4. Iterate through intervals:
    - If current.start < previous.end:
          Overlap detected → return False
    - Else:
          Update previous.end = current.end
5. If no overlaps found → return True

Key Idea:
After sorting by start time, a meeting can only overlap
with the immediately previous meeting.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n log n) — due to sorting

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1) — no extra space (in-place comparison)

-----------------------------------------------------------
"""

# ------------------------------------
# 252. Meeting Rooms
# Intervals Pattern
# ------------------------------------

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True

        # Step 1: sort by start time
        intervals.sort(key=lambda x: x[0])

        prev_end = intervals[0][1]

        # Step 2: check overlaps
        for start, end in intervals[1:]:
            if start < prev_end:
                return False
            prev_end = end

        return True


# ------------------------------------
# Driver Test
# ------------------------------------
sol = Solution()
print(sol.canAttendMeetings([[0,30],[5,10],[15,20]]))  # Expected: False
print(sol.canAttendMeetings([[7,10],[2,4]]))          # Expected: True
print(sol.canAttendMeetings([[1,2],[2,3],[3,4]]))     # Expected: True
print(sol.canAttendMeetings([]))                      # Expected: True

