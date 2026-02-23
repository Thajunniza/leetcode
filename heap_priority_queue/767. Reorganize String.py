"""
767. Reorganize String

This module solves the problem of rearranging characters in a string
so that no two adjacent characters are the same.

Problem:
    - Given a string s.
    - Rearrange the characters so that no two adjacent characters are equal.
    - If it is impossible, return an empty string "".

Core functions:
    - reorganizeString(s) : Uses a max-heap (simulated using negatives)
                            to always pick the character with the
                            highest remaining frequency while enforcing
                            a one-step cooldown to avoid adjacency.

Constraints:
    - 1 <= len(s) <= large constraints.
    - s consists of lowercase English letters.
    - Greedy selection ensures valid construction if feasible.

Key Insight:
    - If the maximum frequency of any character exceeds (n + 1) // 2,
      reorganization is impossible (pigeonhole principle).

Complexity:
    - Time  : O(n log k)
              * Heapify → O(k)
              * n pops/pushes → O(log k) each
              where k = number of unique characters
    - Space : O(k) (heap + frequency map)
"""

import heapq


class Solution(object):
    """DSA-style solution using max-heap with cooldown tracking."""

    def reorganizeString(self, s):
        """
        Rearrange string so no adjacent characters are equal.

        :type s: str
        :rtype: str
        """

        # Step 1: Frequency count
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        # Early impossibility check
        max_freq = max(freq.values())
        if max_freq > (len(s) + 1) // 2:
            return ""

        # Step 2: Build max-heap using negatives
        maxHeap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(maxHeap)

        prev = None  # Stores previous (count, char) temporarily
        result = []

        # Step 3: Greedy construction
        while maxHeap or prev:
            if not maxHeap and prev:
                return ""

            count, char = heapq.heappop(maxHeap)
            result.append(char)
            count += 1  # Since count is negative

            # Push previous back after one gap
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            # Hold current char if still remaining
            if count != 0:
                prev = (count, char)

        return "".join(result)


# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    sol = Solution()
    s = "aab"
    print(f"Reorganized string: {sol.reorganizeString(s)}")