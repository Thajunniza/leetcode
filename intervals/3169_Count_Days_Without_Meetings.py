"""
===========================================================
3169 - Count Days Without Meetings
===========================================================

🧩 Problem:
You are given a positive integer `days` representing the total number 
of days an employee is available for work (numbered from 1 to days). 
You are also given a 2D array `meetings` of size n where 
meetings[i] = [start_i, end_i] represents the starting and ending 
days of meeting i (inclusive).

Return the count of days when the employee is available for work but 
has no meetings scheduled.

Note: The meetings may overlap.

Example 1:
Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
Output: 2
Explanation:
Days 4 and 8 have no meetings scheduled.

Example 2:
Input: days = 5, meetings = [[2,4],[1,3]]
Output: 1
Explanation:
Day 5 has no meeting scheduled.

Example 3:
Input: days = 6, meetings = [[1,6]]
Output: 0
Explanation:
All days from 1 to 6 have meetings scheduled.

-----------------------------------------------------------
Approach — Single Pass with Tracking:
-----------------------------------------------------------

Corrected Logic:
1. Sort meetings by start time
2. Track `last_covered` - the last day that's covered by a meeting
3. For each meeting:
   - If it starts after `last_covered`, add the gap
   - Update `last_covered` to the max of current and meeting's end
4. After loop, add remaining days after last meeting

-----------------------------------------------------------
⏱ Time Complexity:   O(n log n)  # sorting meetings
💾 Space Complexity:  O(1)        # no extra space needed
-----------------------------------------------------------
"""

class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        if not meetings:
            return days
        
        meetings.sort(key=lambda x: x[0])
        count = 0
        last_covered = 0  # Last day covered by meetings
        
        for start, end in meetings:
            if start > last_covered + 1:
                # Gap between last covered day and current meeting start
                count += (start - last_covered - 1)
            
            # Update last covered day
            last_covered = max(last_covered, end)
        
        # Add remaining days after last meeting
        if last_covered < days:
            count += (days - last_covered)
        
        return count





# -----------------------------------------------------------
# Driver Examples to Show the Bug
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    
    # Example 1
    days1 = 10
    meetings1 = [[5,7],[1,3],[9,10]]
    print("Example 1:")
    print(f"{sol.countDays(days1, meetings1)}")
 
    # Example showing the bug clearly
    days_bug = 10
    meetings_bug = [[5,7]]
    print(f"{sol.countDays(days_bug, meetings_bug)}")
  
    
    # Example 2
    days2 = 5
    meetings2 = [[2,4],[1,3]]
    print("Example 2:")
    print(f"{sol.countDays(days2, meetings2)}")
   
    


