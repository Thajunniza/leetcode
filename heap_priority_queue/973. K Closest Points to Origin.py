"""
973. K Closest Points to Origin

This module finds the k closest points to the origin (0, 0).

Problem:
    - Given an array of points where points[i] = [xi, yi],
      return the k closest points to the origin.
    - Distance is measured using Euclidean distance.
    - You may return the answer in any order.

Core Idea:
    - Use a max-heap of size k.
    - Compute squared distance: x^2 + y^2 (no need for sqrt).
    - Push (-distance, index) into heap.
    - If heap size exceeds k, pop the farthest point.
    - Remaining elements in heap are the k closest.

Why Max-Heap (via negatives)?
    - We want to remove the farthest point when size > k.
    - By storing negative distances, Python’s min-heap
      behaves like a max-heap.

Constraints:
    - 1 <= points.length <= large constraints
    - 1 <= k <= points.length

Complexity:
    - Time  : O(n log k)
              * n insertions into heap of size k
    - Space : O(k) (heap storage)
"""

import heapq


class Solution(object):
    """DSA-style solution using size-k max-heap."""

    def kClosest(self, points, k):
        """
        Return k closest points to origin.

        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        heap = []

        for i in range(len(points)):
            a, b = points[i]
            val = a ** 2 + b ** 2

            heapq.heappush(heap, (-val, i))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for _, i in heap:
            res.append(points[i])

        return res


# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    sol = Solution()
    points = [[1, 3], [-2, 2], [2, -2]]
    k = 2
    print(f"{k} closest points: {sol.kClosest(points, k)}")