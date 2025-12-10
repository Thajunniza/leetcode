""" 
===========================================================
2570. Merge Two 2D Arrays by Summing Values
===========================================================

🧩 Problem:
You are given two 2D arrays `nums1` and `nums2` where each array contains
pairs of the form **[id, value]** and:

- Each array is **sorted in increasing order of id**
- Each id appears **at most once** in each array

Your task is to **merge** these two arrays by:

- Matching ids between both arrays
- Summing their values if the id exists in both
- Keeping ids unique
- Returning the merged result sorted by id

🎯 Goal:
Return a **sorted 2D array** of `[id, totalValue]`  
where totalValue = value from nums1 + value from nums2 (or whichever exists).

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:
    nums1 = [[1,2],[2,3],[4,5]]
    nums2 = [[1,4],[3,2],[4,1]]
Output:
    [[1,6],[2,3],[3,2],[4,6]]

Explanation:
- id 1 → 2 + 4 = 6  
- id 2 → only in nums1 → 3  
- id 3 → only in nums2 → 2  
- id 4 → 5 + 1 = 6

Example 2:
Input:
    nums1 = [[2,4],[3,6],[5,5]]
    nums2 = [[1,3],[4,3]]
Output:
    [[1,3],[2,4],[3,6],[4,3],[5,5]]

-----------------------------------------------------------
Algorithm — Two Pointers (Merge Like Merge-Sort):
-----------------------------------------------------------

Since both arrays are sorted by id:

1. Initialize two pointers:
       i = 0  (for nums1)
       j = 0  (for nums2)

2. Compare nums1[i][0] and nums2[j][0]:
       - If ids are equal:
               sum values → add [id, sum] to result
               move both i & j forward
       - If nums1's id < nums2's id:
               add nums1[i] to result
               move i forward
       - If nums2's id < nums1's id:
               add nums2[j]
               move j forward

3. When one list finishes, append the remaining pairs from the other list.

4. Return the merged list.

-----------------------------------------------------------
⏱ Time Complexity:
- O(n + m) → linear merge of both arrays

💾 Space Complexity:
- O(n + m) for output array

This is the optimal approach.

-----------------------------------------------------------
"""
from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = j = 0
        n, m = len(nums1), len(nums2)
        result = []

        while i < n and j < m:
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]

            if id1 == id2:
                # Sum values and move both pointers
                result.append([id1, val1 + val2])
                i += 1
                j += 1

            elif id1 < id2:
                # nums1 id is smaller → append nums1
                result.append([id1, val1])
                i += 1

            else:
                # nums2 id is smaller → append nums2
                result.append([id2, val2])
                j += 1

        # Add remaining elements from nums1
        while i < n:
            result.append(nums1[i])
            i += 1

        # Add remaining elements from nums2
        while j < m:
            result.append(nums2[j])
            j += 1

        return result

if __name__ == "__main__":
    sol = Solution()

    print(sol.mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))
    # [[1, 6], [2, 3], [3, 2], [4, 6]]

    print(sol.mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]))
    # [[1,3],[2,4],[3,6],[4,3],[5,5]]
