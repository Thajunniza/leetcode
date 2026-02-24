"""
846. Hand of Straights

This module solves the problem of determining whether a deck of cards
can be rearranged into groups of consecutive cards of fixed size.

Problem:
    - Given an integer array hand where hand[i] is the value of a card.
    - Given an integer groupSize.
    - Rearrange the cards into groups of size groupSize.
    - Each group must contain consecutive integers.
    - Return True if possible, otherwise False.

Core functions:
    - isNStraightHand(hand, groupSize) : Uses a min-heap combined with
      a frequency map to always start forming groups from the smallest
      available card, preserving greedy correctness.

Constraints:
    - 1 <= len(hand) <= large constraints.
    - 0 <= hand[i] <= large values.
    - 1 <= groupSize <= len(hand)
    - Total number of cards must be divisible by groupSize.

Key Insight:
    - If total cards are not divisible by groupSize → impossible.
    - Always start building sequences from the smallest available card.
    - If the smallest card cannot form a full consecutive group,
      no valid rearrangement exists (greedy invariant).

Complexity:
    - Time  : O(N log U)
              * Heapify → O(U)
              * Each card processed once
              * Heap operations → O(log U)
              where U = number of unique cards
    - Space : O(U) (frequency map + heap)
"""

import heapq


class Solution(object):
    """DSA-style greedy solution using min-heap."""

    def isNStraightHand(self, hand, groupSize):
        """
        Determine if cards can be rearranged into
        consecutive groups of size groupSize.

        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """

        n = len(hand)

        # Step 1: Necessary divisibility check
        if n % groupSize != 0:
            return False

        # Step 2: Frequency map
        freq = {}
        for card in hand:
            freq[card] = freq.get(card, 0) + 1

        # Step 3: Min-heap of unique card values
        minHeap = list(freq.keys())
        heapq.heapify(minHeap)

        # Step 4: Greedy group formation
        while minHeap:
            start = minHeap[0]

            # Attempt to build one full group
            for value in range(start, start + groupSize):

                # If missing or exhausted → impossible
                if freq.get(value, 0) == 0:
                    return False

                freq[value] -= 1

                # If count becomes zero, it must be the smallest
                if freq[value] == 0:
                    if value != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
                    del freq[value]

        return True


# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    sol = Solution()
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3
    print(f"Can rearrange: {sol.isNStraightHand(hand, groupSize)}")