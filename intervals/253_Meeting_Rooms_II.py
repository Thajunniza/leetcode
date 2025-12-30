"""
===========================================================
253. Meeting Rooms II
===========================================================

🧩 Problem:
You are given an array of meeting time intervals where
each interval is represented as:

    [start, end]

Find the minimum number of conference rooms required
to hold all meetings.

🎯 Goal:
Return the minimum number of rooms needed so that
no meetings in the same room overlap.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation:
At time 5, two meetings overlap → 2 rooms needed

Example 2:
Input:  intervals = [[7,10],[2,4]]
Output: 1
Explanation:
Meetings do not overlap → 1 room is sufficient

Example 3:
Input:  intervals = [[1,4],[2,3],[3,6]]
Output: 2
Explanation:
Maximum simultaneous meetings at any time is 2

-----------------------------------------------------------
Algorithm — Intervals Pattern (Timeline / Two Pointers):
-----------------------------------------------------------

1. Separate all start times into array `start`
2. Separate all end times into array `end`
3. Sort both arrays
4. Use two pointers:
    - `s` for start times
    - `e` for end times
5. Traverse through all starts:
    - If start[s] < end[e]:
          A meeting starts before another ends
          → need a new room (count += 1)
    - Else:
          A meeting has ended
          → free a room (count -= 1, e += 1)
6. Track the maximum value of `count`
7. Return the maximum count as the answer

Key Idea:
The maximum number of simultaneous meetings at any
moment equals the minimum number of rooms required.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n log n) — sorting start and end times

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(n) — separate start and end arrays

-----------------------------------------------------------
"""

# ------------------------------------
# 253. Meeting Rooms II
# Intervals Pattern
# ------------------------------------

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        start = []
        end = []

        for s, e in intervals:
            start.append(s)
            end.append(e)

        start.sort()
        end.sort()

        s = 0
        e = 0
        count = 0
        result = 0

        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1

            result = max(result, count)

        return result


# ------------------------------------
# Driver Test
# ------------------------------------
sol = Solution()
print(sol.minMeetingRooms([[0,30],[5,10],[15,20]]))  # Expected: 2
print(sol.minMeetingRooms([[7,10],[2,4]]))          # Expected: 1
print(sol.minMeetingRooms([[1,4],[2,3],[3,6]]))     # Expected: 2
print(sol.minMeetingRooms([]))                      # Expected: 0

