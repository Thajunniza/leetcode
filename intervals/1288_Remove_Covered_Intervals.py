"""
===========================================================
1288 - Remove Covered Intervals
===========================================================

🧩 Problem:
Given an array of intervals where intervals[i] = [li, ri], 
remove all intervals that are covered by another interval.

An interval [a, b) is covered by interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals after removing all covered intervals.

Example 1:
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: [1,4] is covered by [2,8], so we remove it.
Remaining: [3,6], [2,8]

Example 2:
Input: intervals = [[1,4],[2,3]]
Output: 1
Explanation: [2,3] is covered by [1,4]

Example 3:
Input: intervals = [[1,2],[1,4],[3,4]]
Output: 1
Explanation: [1,2] and [3,4] are covered by [1,4]

-----------------------------------------------------------
Approach — Sort + Greedy:
-----------------------------------------------------------
1. Sort intervals:
   - Primary: by start point (ascending)
   - Secondary: by end point (descending) - ensures longer intervals 
     with same start come first

2. Traverse sorted intervals:
   - Track `prev_end` (rightmost end point seen so far)
   - For each interval [start, end]:
       * If end > prev_end: NOT covered, count it, update prev_end
       * Else: covered by previous interval, skip it

3. Return count of non-covered intervals

Key Insight:
After sorting, if current interval's end <= prev_end, it must be 
covered because:
- Its start >= previous starts (due to sorting)
- Its end <= previous interval's end

-----------------------------------------------------------
⏱ Time Complexity:   O(n log n)  # dominated by sorting
💾 Space Complexity:  O(1)        # excluding sort space
-----------------------------------------------------------
"""

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Sort by start ascending, then by end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        prev_end = 0
        
        for start, end in intervals:
            # If current interval extends beyond previous end,
            # it's NOT covered
            if end > prev_end:
                count += 1
                prev_end = end
            # else: current interval is covered, skip it
        
        return count


# -----------------------------------------------------------
# Driver Examples
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    intervals1 = [[1,4],[3,6],[2,8]]
    print(sol.removeCoveredIntervals(intervals1))
    # Expected Output: 2
    # After sort: [[1,4],[2,8],[3,6]]
    # [1,4]: count=1, prev_end=4
    # [2,8]: 8>4, count=2, prev_end=8
    # [3,6]: 6<8, covered!
    
    # Example 2
    intervals2 = [[1,4],[2,3]]
    print(sol.removeCoveredIntervals(intervals2))
    # Expected Output: 1
    
    # Example 3
    intervals3 = [[1,2],[1,4],[3,4]]
    print(sol.removeCoveredIntervals(intervals3))
    # Expected Output: 1
    # After sort: [[1,4],[1,2],[3,4]]
    # [1,4]: count=1, prev_end=4
    # [1,2]: 2<4, covered!
    # [3,4]: 4=4, covered!