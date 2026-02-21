"""
215. Kth Largest Element in an Array

This module solves the problem of finding the kth largest element
in an unsorted array using a min-heap of size k.

Core functions:
    - findKthLargest(nums, k) : Maintains a min-heap of size k
                                and returns the root as the kth largest.

Constraints:
    - Does not sort the entire array.
    - Space optimized to O(k) using heap.
    - Time complexity O(n log k), suitable for FAANG-level interviews.
"""

import heapq

class Solution(object):
    """DSA-style solution for finding kth largest element using a min heap."""

    def findKthLargest(self, nums, k):
        """
        Find the kth largest element in an unsorted array.

        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []

        for num in nums:
            heapq.heappush(heap, num)       # push element into heap
            if len(heap) > k:               # maintain size k
                heapq.heappop(heap)         # remove smallest

        return heap[0]                      # root of min-heap = kth largest


# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(f"{k}th largest element in {nums}: {sol.findKthLargest(nums, k)}")