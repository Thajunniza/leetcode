""" 
===========================================================
961. N-Repeated Element in Size 2N Array
===========================================================

🧩 Problem:
You are given an integer array nums of size 2N.
Exactly one element is repeated N times, and all other
elements appear exactly once.

Return the element that is repeated N times.

Example:
Input: [1,2,3,3]
Output: 3

Input: [2,1,2,5,3,2]
Output: 2

-----------------------------------------------------------
Approach — Hash Set / Frequency Check:
-----------------------------------------------------------
1. Iterate through the array.
2. Maintain a hash set (or dictionary) to track seen elements.
3. If an element is already present in the set, return it
   immediately.
4. Since exactly one element is repeated N times, the first
   duplicate encountered is the answer.

This approach leverages constant-time lookups provided by
hash-based data structures.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(n)
-----------------------------------------------------------
"""

class Solution(object):
    def repeatedNTimes(self, nums):
        seen = {}
        for val in nums:
            if val in seen:
                return val
            seen[val] = 1


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.repeatedNTimes([1,2,3,3]))       # Expected Output: 3
    print(sol.repeatedNTimes([2,1,2,5,3,2]))   # Expected Output: 2
