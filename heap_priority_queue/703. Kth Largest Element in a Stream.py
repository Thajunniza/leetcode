"""
703. Kth Largest Element in a Stream

This module implements a data structure that continuously tracks
the kth largest element in a stream of integers.

Problem:
    - Design a class KthLargest.
    - Constructor receives:
        * k (which kth largest to track)
        * nums (initial list of numbers)
    - Method add(val):
        * Adds val into the stream.
        * Returns the kth largest element so far.

Core Idea:
    - Maintain a min-heap of size k.
    - The heap stores the k largest elements seen so far.
    - The root of the heap is always the kth largest element.

Why Min-Heap?
    - If heap size exceeds k, remove the smallest element.
    - This ensures only the k largest elements remain.
    - heap[0] always gives the kth largest.

Constraints:
    - 1 <= k <= number of elements in stream
    - Efficient updates required per insertion

Complexity:
    - Time  :
        * Constructor → O(n log k)
        * add() → O(log k)
    - Space : O(k) (heap storage)
"""

import heapq


class KthLargest(object):
    """DSA-style solution using a size-k min-heap."""

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []

        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val):
        """
        Add a value to the stream and return kth largest element.

        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    print(kth.add(3))   # 4
    print(kth.add(5))   # 5
    print(kth.add(10))  # 5
    print(kth.add(9))   # 8
    print(kth.add(4))   # 8