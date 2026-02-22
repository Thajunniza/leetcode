"""
1046. Last Stone Weight

This module solves the problem of repeatedly smashing the two heaviest stones
until at most one stone remains.

Core functions:
    - lastStoneWeight(stones) : Uses a max-heap (simulated via negatives)
                                to repeatedly extract two largest stones,
                                smash them, and push the difference if non-zero.

Approach:
    - Convert list into max-heap using negative values.
    - Pop two largest elements.
    - If they are unequal, push their difference back.
    - Continue until ≤ 1 stone remains.

Complexity:
    - Time  : O(n log n)
              * heapify → O(n)
              * up to n heap operations → O(log n) each
    - Space : O(n) auxiliary (due to new heap list)

Interview Notes:
    - Python’s heapq is a min-heap.
    - Max-heap is simulated by storing negative values.
    - Efficient compared to repeated sorting (O(n² log n)).
"""

import heapq


class Solution(object):
    """DSA-style solution using heap (priority queue)."""

    def lastStoneWeight(self, stones):
        """
        Return the weight of the last remaining stone.

        :type stones: List[int]
        :rtype: int
        """

        # Convert to max heap using negatives
        heap = [-val for val in stones]
        heapq.heapify(heap)

        # Smash stones until at most one remains
        while len(heap) > 1:
            first = -heapq.heappop(heap)   # largest
            second = -heapq.heappop(heap)  # second largest

            if first != second:
                heapq.heappush(heap, -(first - second))

        # If heap empty return 0
        return -heap[0] if heap else 0


# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    sol = Solution()
    stones = [2, 7, 4, 1, 8, 1]
    print(f"Last stone weight: {sol.lastStoneWeight(stones)}")