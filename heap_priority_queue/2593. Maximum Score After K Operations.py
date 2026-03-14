"""
===========================================================
2593. Maximum Score After K Operations
===========================================================

Problem:
Given a list of integers `nums` and an integer `k`, perform 
the following operation exactly `k` times:

1. Pick the maximum number from `nums`.
2. Add it to the score.
3. Replace it with floor(max / 3).

Return the total score after k operations.

Approach:
- Use a max-heap to efficiently get the maximum element.
- Store negatives to simulate a max-heap with Python's heapq.
- Pop the max, add to score, push floor division result back.
- Repeat k times.

Time Complexity: O(k log n), where n = len(nums)
Space Complexity: O(n)
"""

import heapq

class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Build max-heap using negatives
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        ans = 0
        for _ in range(k):
            max_element = heapq.heappop(max_heap)
            ans -= max_element                  # add positive value
            heapq.heappush(max_heap, max_element // 3)  # push reduced value

        return ans


"""
-----------------------------------------------------------
Test Cases
-----------------------------------------------------------
"""

if __name__ == "__main__":
    s = Solution()

    nums = [1,10,3,3,3]
    k = 3
    print(s.maxKelements(nums, k))  # Expected: 17

    nums = [10, 20, 7]
    k = 4
    print(s.maxKelements(nums, k))  # Expected: 44

    nums = [5, 19, 8]
    k = 3
    print(s.maxKelements(nums, k))  # Expected: 33

    nums = [1,1,1]
    k = 5
    print(s.maxKelements(nums, k))  # Expected: 5