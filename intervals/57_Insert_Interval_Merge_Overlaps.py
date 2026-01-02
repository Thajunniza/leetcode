"""
===========================================================
57. Insert Interval and Merge Overlaps
===========================================================

🧩 Problem:
Given a list of non-overlapping intervals `existing_intervals` sorted by start time, 
and a new interval `new_interval`, insert the new interval into the list 
and merge any overlapping intervals. Return the updated list of intervals.

Example:
Input: existing_intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], new_interval = [4,8]
Overlapping intervals: [3,5], [6,7], [8,10]
Merged interval: [3,10]
Output: [[1,2],[3,10],[12,16]]

-----------------------------------------------------------
Approach — Interval Insertion & Merging:
-----------------------------------------------------------
1. Initialize:
   - `result` list to store final intervals
   - `start, end` as bounds of `new_interval`
   - `i = 0` to iterate through `existing_intervals`
   - `n = len(existing_intervals)`

2. Add all intervals **before** the new interval (no overlap):
   - While i < n and existing_intervals[i][1] < start:
       - Append existing_intervals[i] to result
       - i += 1

3. Merge all intervals that **overlap** with new_interval:
   - While i < n and existing_intervals[i][0] <= end:
       - start = min(start, existing_intervals[i][0])
       - end = max(end, existing_intervals[i][1])
       - i += 1
   - Append [start, end] to result

4. Add all **remaining intervals** after new_interval:
   - While i < n:
       - Append existing_intervals[i] to result
       - i += 1

5. Return result

-----------------------------------------------------------
⏱ Time Complexity:   O(n)   # n = number of intervals
💾 Space Complexity:  O(n)
-----------------------------------------------------------
"""

def insert_interval(existing_intervals, new_interval):
    result = []
    start, end = new_interval
    n = len(existing_intervals)
    i = 0

    # 1. Intervals before new_interval
    while i < n and existing_intervals[i][1] < start:
        result.append(existing_intervals[i])
        i += 1

    # 2. Merge overlapping intervals
    while i < n and existing_intervals[i][0] <= end:
        start = min(start, existing_intervals[i][0])
        end = max(end, existing_intervals[i][1])
        i += 1
    result.append([start, end])

    # 3. Remaining intervals
    while i < n:
        result.append(existing_intervals[i])
        i += 1

    return result


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,8]
    print(insert_interval(intervals, new_interval))  # Expected Output: [[1,2],[3,10],[12,16]]
