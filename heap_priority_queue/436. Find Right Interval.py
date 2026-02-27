"""
436. Find Right Interval

This module solves the problem of finding the "right interval"
for each interval in a given list.

Problem:
    - For each interval i, find an interval j such that:
        start_j >= end_i
    - Among all valid j, choose the one with the smallest start_j.
    - If no such interval exists, return -1 for that index.

Core Idea:
    - Use two min-heaps:
        1. start_heap → stores (start, index)
        2. end_heap   → stores (end, index)
    - Process intervals by increasing end time.
    - For each end, remove all starts that are < end.
    - The top of start_heap (if exists) is the correct answer.

Time Complexity:
    O(n log n)

Space Complexity:
    O(n)
"""

import heapq


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
        res = [-1] * n

        start_heap = []
        end_heap = []

        # Build heaps
        for i, (start, end) in enumerate(intervals):
            heapq.heappush(start_heap, (start, i))
            heapq.heappush(end_heap, (end, i))

        # Process intervals ordered by end time
        while end_heap:
            end_time, end_index = heapq.heappop(end_heap)

            # Remove all intervals whose start < current end
            while start_heap and start_heap[0][0] < end_time:
                heapq.heappop(start_heap)

            # The smallest valid start (if any) is the answer
            if start_heap:
                res[end_index] = start_heap[0][1]

        return res

s = Solution()

tests = [
    [[1,2]],
    [[3,4],[2,3],[1,2]],
    [[1,4],[2,3],[3,4]],
    [[1,2],[2,3],[3,4]],
    [[5,7],[1,3],[3,5]]
]

for t in tests:
    print("Input:", t)
    print("Output:", s.findRightInterval(t))
    print()