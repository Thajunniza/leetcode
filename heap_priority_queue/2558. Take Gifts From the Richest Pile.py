"""
2558. Take Gifts From the Richest Pile

This module solves the problem of repeatedly taking gifts from
the richest pile.

Problem:
    - You are given an array of integers representing gift piles.
    - In each operation:
        * Choose the largest pile.
        * Replace it with floor(sqrt(pile)).
    - Perform exactly k operations.
    - Return the total number of gifts remaining.

Core functions:
    - pickGifts(gifts, k) : Uses a max-heap (simulated using negatives)
                            to efficiently retrieve the largest pile
                            at each step.

Constraints:
    - gifts contains positive integers.
    - 1 <= k <= large constraints (handled efficiently via heap).
    - Heap ensures greedy selection of largest pile each iteration.

Complexity:
    - Time  : O(n + k log n)
              * Heapify → O(n)
              * k operations → O(log n) each
    - Space : O(n) (heap storage)
"""

import heapq


class Solution(object):
    """DSA-style solution using max-heap (via negatives)."""

    def pickGifts(self, gifts, k):
        """
        Return total gifts remaining after k operations.

        :type gifts: List[int]
        :type k: int
        :rtype: int
        """

        # Convert to max-heap using negatives
        gifts = [-val for val in gifts]
        heapq.heapify(gifts)

        # Perform k operations
        for _ in range(k):
            val = -heapq.heappop(gifts)
            heapq.heappush(gifts, -int(val ** 0.5))

        # Compute remaining total
        total = 0
        for val in gifts:
            total += -val

        return total


# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    sol = Solution()
    gifts = [25, 64, 9, 4, 100]
    k = 4
    print(f"Remaining gifts after {k} operations: {sol.pickGifts(gifts, k)}")