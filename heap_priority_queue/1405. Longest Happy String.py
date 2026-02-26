# --------------------------------------------------
# 1405: Longest Happy String
# --------------------------------------------------

# A happy string is a string where no three consecutive characters
# are the same.

# You are given three integers:
#     a → number of 'a'
#     b → number of 'b'
#     c → number of 'c'

# Return the *longest possible happy string* that can be formed using
# at most a 'a's, b 'b's, and c 'c's.

# --------------------------------------------------
# Example:
# Input:
#     a = 1, b = 1, c = 7
# Output:
#     "ccaccbcc"

# Explanation:
# We always pick the most frequent remaining character unless it would
# create three in a row, in which case we pick the next best option.
# --------------------------------------------------


import heapq
from typing import List


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Greedy max‑heap approach:
        - Always pick the character with the highest remaining count.
        - If using it would cause three identical chars in a row,
          pick the next-best character instead.
        - Use a max‑heap with negative counts.
        """

        have = []
        if a > 0:
            heapq.heappush(have, (-a, "a"))
        if b > 0:
            heapq.heappush(have, (-b, "b"))
        if c > 0:
            heapq.heappush(have, (-c, "c"))

        res = []

        while have:
            count, char = heapq.heappop(have)

            # If adding this char causes 'xxx'
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                # If no alternative, we are done
                if not have:
                    break

                # Use the next-best character
                count2, char2 = heapq.heappop(have)
                res.append(char2)
                count2 += 1     # reduce negative count

                if -count2 > 0:
                    heapq.heappush(have, (count2, char2))

                # Push back the originally skipped char
                heapq.heappush(have, (count, char))

            else:
                # Safe to use this character
                res.append(char)
                count += 1      # reduce negative count
                if -count > 0:
                    heapq.heappush(have, (count, char))

        return "".join(res)


# --------------------------------------------------
# Algorithm Explanation:
# --------------------------------------------------
# 1. Build a max‑heap containing (-count, char) for 'a', 'b', 'c'.
# 2. Pop the most frequent character.
# 3. If adding it produces three consecutive same characters,
#       - Pop the next most frequent character instead.
#       - Add it to the result, decrement its count, push back the first one.
# 4. Otherwise, use the popped character normally.
# 5. Continue until no characters can be used.
#
# --------------------------------------------------
# Time Complexity: O(a + b + c) * log 3  ≈ O(a + b + c)
# Space Complexity: O(1) heap of size ≤ 3
# --------------------------------------------------


# --------------------------------------------------
# Test Cases
# --------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.longestDiverseString(1, 1, 7))  # Example, expected length <= 9
    print(sol.longestDiverseString(2, 2, 1))  # e.g., "aabbc"
    print(sol.longestDiverseString(7, 1, 0))  # e.g., "aabaa"
    print(sol.longestDiverseString(0, 0, 0))  # Expected: ""