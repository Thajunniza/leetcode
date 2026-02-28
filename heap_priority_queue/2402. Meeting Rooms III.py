"""
===========================================================
2402. Meeting Rooms III
===========================================================

🧩 Problem:
You are given an integer n representing n meeting rooms numbered 
from 0 to n - 1.

You are given a 2D integer array meetings where 
meetings[i] = [start_i, end_i] represents a meeting 
that will be held during the half-closed time interval 
[start_i, end_i).

Rules:
1. Each meeting must be assigned to the available room 
   with the smallest index.
2. If no rooms are available at the meeting start time,
   delay the meeting until the earliest room becomes free.
3. Delayed meetings keep their original duration.
4. Return the room number that hosted the most meetings.
5. If multiple rooms have the same count, return the smallest index.

-----------------------------------------------------------
Example :
-----------------------------------------------------------

Example 1:
Input: n = 2
       meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0

Explanation:
- Meeting [0,10] → Room 0
- Meeting [1,5]  → Room 1
- Meeting [2,7]  → Delayed until Room 1 frees at 5
- Meeting [3,4]  → Delayed until Room 1 frees at 7

Room 0 → 1 meeting  
Room 1 → 3 meetings  
Answer = 1

Example 2:
Input: n = 3
       meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1

-----------------------------------------------------------
Brute Force Approach: Simulate Time
-----------------------------------------------------------

1. Iterate time from 0 to max end time.
2. Track which rooms are busy.
3. Assign meetings manually as time progresses.

Problems:
- Time simulation is inefficient.
- Large time ranges cause TLE.
- Not scalable.

-----------------------------------------------------------
⏱️ Time & Space Complexity (Brute)
-----------------------------------------------------------
Time:  O(T * n)  (T = max time)
Space: O(n)

-----------------------------------------------------------
🧠 Optimal Approach: Two Min-Heaps (Greedy Scheduling)
-----------------------------------------------------------

Key Insight:
This is a scheduling problem requiring:
- Smallest indexed available room
- Earliest finishing busy room

We use two min-heaps:

1. available_rooms → stores free room indices
2. busy_rooms → stores (end_time, room_index)

Algorithm:

1. Sort meetings by start time.
2. Initialize:
   - Min-heap of available rooms [0..n-1]
   - Empty min-heap for busy rooms
   - Count array to track usage
3. For each meeting:
   a. Free all rooms where end_time <= meeting start.
   b. If room available:
        assign immediately.
   c. Else:
        pop earliest finishing room,
        delay meeting,
        push updated end time.
   d. Increment count.
4. Return room with maximum count 
   (smallest index if tie).

-----------------------------------------------------------
Example Walkthrough
-----------------------------------------------------------

n = 2  
meetings = [[0,10],[1,5],[2,7],[3,4]]

Initial:
available = [0,1]
busy = []

Meeting [0,10]
→ Assign Room 0
busy = [(10,0)]

Meeting [1,5]
→ Assign Room 1
busy = [(5,1),(10,0)]

Meeting [2,7]
→ No room free
→ Earliest free = (5,1)
→ Delay meeting to [5,10]
busy = [(10,0),(10,1)]

Meeting [3,4]
→ No room free
→ Earliest free = (10,0)
→ Delay meeting to [10,11]

Final count:
Room 0 = X
Room 1 = Y
Return max count room.

-----------------------------------------------------------
⏱️ Time & Space Complexity (Optimal)
-----------------------------------------------------------

Sorting: O(m log m)
Each meeting: O(log n)

Total Time:  O(m log n)
Space: O(n)

"""
import heapq

class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort(key=lambda x: x[0])
        
        roomH = [i for i in range(n)]
        heapq.heapify(roomH)
        
        endH = []
        count = [0] * n
        
        for start, end in meetings:
            
            # Free rooms
            while endH and endH[0][0] <= start:
                _, room = heapq.heappop(endH)
                heapq.heappush(roomH, room)
            
            if roomH:
                room = heapq.heappop(roomH)
                heapq.heappush(endH, (end, room))
                count[room] += 1
            else:
                end_time, room = heapq.heappop(endH)
                duration = end - start
                heapq.heappush(endH, (end_time + duration, room))
                count[room] += 1
        
        max_count = max(count)
        for i in range(n):
            if count[i] == max_count:
                return i

# -----------------------------------------------------------
# Test Cases for Most Booked Meeting Room
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print("=== Example 1 ===")
    n = 2
    meetings = [[0,10],[1,5],[2,7],[3,4]]
    print(f"Input: n = {n}, meetings = {meetings}")
    print(f"Output: {sol.mostBooked(n, meetings)}")
    print(f"Expected: 0\n")
    
    # Example 2
    print("=== Example 2 ===")
    n = 3
    meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
    print(f"Input: n = {n}, meetings = {meetings}")
    print(f"Output: {sol.mostBooked(n, meetings)}")
    print(f"Expected: 1\n")
    
    # Example 3: All meetings fit without delay
    print("=== Example 3 ===")
    n = 3
    meetings = [[0,2],[3,5],[6,8]]
    print(f"Input: n = {n}, meetings = {meetings}")
    print(f"Output: {sol.mostBooked(n, meetings)}")
    print(f"Expected: 0\n")
    
    # Example 4: All meetings collide, require delays
    print("=== Example 4 ===")
    n = 2
    meetings = [[0,5],[0,5],[0,5],[0,5]]
    print(f"Input: n = {n}, meetings = {meetings}")
    print(f"Output: {sol.mostBooked(n, meetings)}")
    print(f"Expected: 0\n")
    
    # Example 5: Tie case, two rooms equally used
    print("=== Example 5 ===")
    n = 2
    meetings = [[0,2],[0,2],[2,4],[2,4]]
    print(f"Input: n = {n}, meetings = {meetings}")
    print(f"Output: {sol.mostBooked(n, meetings)}")
    print(f"Expected: 0\n")