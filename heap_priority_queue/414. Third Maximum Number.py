"""
===========================================================
414. Third Maximum Number
===========================================================

Problem:
Given an integer array nums, return the third distinct
maximum number in this array.

If the third maximum does not exist, return the maximum
number.

-----------------------------------------------------------
Example
-----------------------------------------------------------
Input:  nums = [3,2,1]
Output: 1

Input:  nums = [1,2]
Output: 2

Input:  nums = [2,2,3,1]
Output: 1
"""

import heapq

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        have = set()
        minH = []

        # Step 1: iterate through numbers
        for val in nums:
            if val not in have:
                heapq.heappush(minH, val)
                have.add(val)

            # Keep only top 3 maximums
            if len(minH) > 3:
                heapq.heappop(minH)

        # Step 2: If less than 3 distinct numbers, return max
        if len(minH) < 3:
            return max(have)

        # Step 3: Otherwise, the root of the heap is the 3rd maximum
        return minH[0]


"""
-----------------------------------------------------------
Algorithm
-----------------------------------------------------------

1. Use a set to track distinct numbers.
2. Use a min heap to maintain the top 3 maximum numbers.
3. Iterate through the array:
      push number into heap if not seen
      if heap size > 3, pop smallest
4. If less than 3 distinct numbers, return maximum.
5. Otherwise, return heap root (3rd maximum).

-----------------------------------------------------------
Time Complexity
-----------------------------------------------------------

O(n) -- each number is pushed/popped at most once; heap size ≤ 3

-----------------------------------------------------------
Space Complexity
-----------------------------------------------------------

O(n) for the set of distinct numbers
"""

nums_list = [
    [3,2,1],
    [1,2],
    [2,2,3,1],
    [1,2,2,5,3,5]
]

for nums in nums_list:
    print(f"Input: {nums}, Third Maximum: {Solution().thirdMax(nums)}")