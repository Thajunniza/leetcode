# 451. Sort Characters By Frequency

# This module returns the string `s` with characters sorted by decreasing frequency.

# Problem:
#     - Given a string s, sort it so that characters appear in descending order of frequency.
#     - If two characters have the same frequency, any order is acceptable unless specified.

# Core Idea:
#     - Count character frequencies.
#     - Use a max-heap (simulated with negative counts) to always pop the highest-frequency char.
#     - Build the result by appending `char * freq` for each popped entry.

# Why a Heap?
#     - Efficiently retrieves the current max-frequency character.
#     - Avoids sorting all characters by frequency when you prefer iterative extraction.

# Tie-Breaking:
#     - Using tuples (-count, char) produces lexicographic ascending order for ties.
#     - If the problem doesn’t constrain ties (like LeetCode 451), this is acceptable.
#     - If you want a specific tie order, adjust the tuple or use a custom sort.

# Constraints:
#     - 1 <= len(s) <= 5 * 10^5 (typical constraints)
#     - s may contain any ASCII/Unicode characters

# Complexity:
#     - Time  : O(n + k log k)
#               * Counting is O(n)
#               * Heap build/extraction is O(k log k), where k is number of distinct chars
#               * Result assembly is O(n)
#     - Space : O(k) for frequency map + heap

import heapq
from typing import Dict

class Solution(object):
    """DSA-style solution using a max-heap (via negative counts)."""

    def frequencySort(self, s):
        """
        Return the string with characters sorted by decreasing frequency.

        :type s: str
        :rtype: str
        """
        if not s:
            return s

        # 1) Count frequencies
        freq: Dict[str, int] = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        # 2) Push (-count, char) to simulate a max-heap
        heap = []
        for c, count in freq.items():
            heapq.heappush(heap, (-count, c))

        # 3) Pop and build result
        res = []
        while heap:
            neg_count, c = heapq.heappop(heap)
            res.append(c * (-neg_count))  # append block of same char

        return "".join(res)

sol = Solution()
assert sorted(sol.frequencySort("tree")) == sorted("eetr")
assert sol.frequencySort("aaa") == "aaa"
out = sol.frequencySort("cccaaa")
assert sorted(out) == sorted("cccaaa")
assert sol.frequencySort("a") == "a"
assert sol.frequencySort("") == ""