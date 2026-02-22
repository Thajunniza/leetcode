"""
1167. Minimum Cost to Connect Sticks

This module solves the problem of connecting sticks with minimum cost.

Problem:
    - You have an array of sticks with positive lengths.
    - You can connect any two sticks at a cost equal to their sum.
    - Repeat until one stick remains.
    - Return the minimum total cost.

Core functions:
    - connectSticks(sticks) : Uses a min-heap to always combine the
                              two smallest sticks for optimal cost.

Constraints:
    - Stick lengths are positive integers.
    - Heap ensures greedy selection of smallest two sticks each time.

Complexity:
    - Time  : O(n log n)
              * Heapify → O(n)
              * n-1 merges → O(log n) each
    - Space : O(n) (heap storage)
"""

import heapq


class Solution(object):
    """DSA-style solution using min-heap (priority queue)."""

    def connectSticks(self, sticks):
        """
        Return minimum cost to connect all sticks.

        :type sticks: List[int]
        :rtype: int
        """

        heapq.heapify(sticks)  # build min-heap
        total_cost = 0

        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)

            cost = first + second
            total_cost += cost

            heapq.heappush(sticks, cost)

        return total_cost


# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    sol = Solution()
    sticks = [2, 4, 3]
    print(f"Minimum cost to connect sticks {sticks}: {sol.connectSticks(sticks)}")