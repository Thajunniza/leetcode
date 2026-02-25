"""
295: Find Median from Data Stream

Two-heap (max-heap + min-heap) streaming median that supports O(log n) inserts
and O(1) median queries. This version keeps the user's original structure and
variable names while tightening the balancing logic.

Approach
--------
- Maintain two heaps:
  - `small`: max-heap for the lower half (implemented by pushing negatives)
  - `large`: min-heap for the upper half
- Invariants:
  - All elements in `small` <= all elements in `large`
  - Size difference is at most 1, with `small` allowed to hold the extra element
- Steps to add a number:
  1) Push into `small` (as negative for max-heap behavior).
  2) If the order property is violated (top of small > top of large), move one
     element from `small` to `large`.
  3) Rebalance sizes so `len(small) >= len(large)` and the difference is <= 1.

Complexity
----------
- addNum:     O(log n) due to heap push/pop.
- findMedian: O(1) using heap tops.
- Space:      O(n) for storing the stream in two heaps.

Run this file directly to see a quick sanity test.
"""

import heapq


class MedianFinder(object):

    def __init__(self):
        self.small = []  # max-heap via negatives (lower half)
        self.large = []  # min-heap (upper half)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Always push into small (as negative to simulate max-heap)
        heapq.heappush(self.small, -num)

        # Ensure ordering: max(small) <= min(large)
        if self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Rebalance sizes so that len(small) >= len(large)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        """
        :rtype: float
        """
        m = len(self.small)
        n = len(self.large)
        if m > n:
            return float(-self.small[0])
        else:
            return (self.large[0] + (-self.small[0])) / 2.0


# -------------------------- Quick Sanity Test --------------------------
if __name__ == "__main__":
    mf = MedianFinder()
    stream = [5, 15, 1, 3, 2, 8, 10, 12]
    for x in stream:
        mf.addNum(x)
        print(f"after add({x}) -> median = {mf.findMedian()}")
    # Example output sequence of medians should look reasonable:
    # 5.0, 10.0, 5.0, 4.0, 3.0, 4.0, 6.5, 7.5