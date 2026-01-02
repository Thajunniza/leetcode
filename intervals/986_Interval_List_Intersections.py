"""
===========================================================
986 - Interval List Intersections
===========================================================

🧩 Problem:
Given two lists of closed intervals `firstList` and `secondList` 
where each list is pairwise disjoint and sorted by start time, 
find the intersection of these two interval lists.

Example:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], 
       secondList = [[1,5],[8,12],[15,24],[25,26]]
Intersected intervals:
- [0,2] ∩ [1,5] = [1,2]
- [5,10] ∩ [1,5] = [5,5] (ignore zero length if needed)
- [5,10] ∩ [8,12] = [8,10]
- [13,23] ∩ [15,24] = [15,23]
- [24,25] ∩ [15,24] = [24,24]
- [24,25] ∩ [25,26] = [25,25]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

-----------------------------------------------------------
Approach — Two Pointer Merge:
-----------------------------------------------------------
1. Initialize:
   - `result` list to store intersections
   - pointers `i = 0`, `j = 0` for firstList and secondList

2. Traverse both lists until one pointer reaches the end:
   - first = firstList[i], second = secondList[j]
   - Compute overlap interval:
       start = max(first[0], second[0])
       end   = min(first[1], second[1])
   - If start <= end, append [start, end] to result

3. Move the pointer of the interval which **ends earlier**:
   - if first[1] < second[1]: i += 1
   - else: j += 1

4. Return result

-----------------------------------------------------------
⏱ Time Complexity:   O(m + n)   # m = len(firstList), n = len(secondList)
💾 Space Complexity:  O(m + n)   # worst-case all intervals overlap
-----------------------------------------------------------
"""

class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        if not firstList or not secondList:
            return result

        i, j = 0, 0
        l1, l2 = len(firstList), len(secondList)

        while i < l1 and j < l2:
            first, second = firstList[i], secondList[j]
            start = max(first[0], second[0])
            end = min(first[1], second[1])

            if start <= end:
                result.append([start, end])

            # Move pointer of the interval which ends first
            if first[1] < second[1]:
                i += 1
            else:
                j += 1

        return result


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    print(sol.intervalIntersection(firstList, secondList))
    # Expected Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
