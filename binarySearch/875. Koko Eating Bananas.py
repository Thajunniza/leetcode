"""
875: Koko Eating Bananas

Koko loves bananas. There are n piles of bananas, where the i-th pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her eating speed k (bananas per hour).
Each hour, she chooses one pile and eats up to k bananas from that pile.
If the pile has fewer than k bananas, she eats the entire pile.

Return the minimum integer k such that Koko can eat all the bananas within h hours.

Example:
Input:  piles = [3, 6, 7, 11], h = 8
Output: 4

Explanation:
At speed 4:
3 -> 1 hour
6 -> 2 hours
7 -> 2 hours
11 -> 3 hours
Total = 8 hours

Approach:
Binary Search on Answer (Eating Speed)

- Minimum speed = 1
- Maximum speed = max(piles)
- If Koko can finish eating at speed k, she can also finish at any speed > k
  → monotonic property → binary search

Time Complexity: O(n log M)
    where n = number of piles, M = max bananas in a pile

Space Complexity: O(1)
"""

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to calculate total hours needed at speed k
        def hours_needed(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total

        # Binary search bounds
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            mid = (l + r) // 2
            if hours_needed(mid) <= h:
                res = mid          # valid speed, try smaller
                r = mid - 1
            else:
                l = mid + 1        # speed too slow, increase

        return res


# -------------------------------
# Test Cases
# -------------------------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
        ([1, 1, 1, 1], 4, 1),
        ([312884470], 312884469, 2)
    ]

    for piles, h, expected in test_cases:
        result = sol.minEatingSpeed(piles, h)
        print(f"Piles: {piles}, Hours: {h}")
        print(f"Minimum Eating Speed: {result}")
        print(f"Expected: {expected}")
        print("-" * 40)
