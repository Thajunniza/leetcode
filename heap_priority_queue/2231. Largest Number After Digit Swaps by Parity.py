# --------------------------------------------------
# 2231: Largest Number After Digit Swaps by Parity
# --------------------------------------------------

# You are given a positive integer `num`. You may swap any two digits of `num`
# that have the same parity (i.e., both odd digits or both even digits).

# Return the largest possible value of `num` after any number of such swaps.

# --------------------------------------------------
# Example:
# Input:
#     num = 65875
# Output:
#     87655

# Explanation:
# Odd digits are {5, 7, 5} and even digits are {6, 8}.
# Sort odds descending → {7, 5, 5}, evens descending → {8, 6}.
# Rebuild by original parity positions to get 87655.
# --------------------------------------------------
from typing import List
import heapq


class Solution:
    def largestInteger(self, num: int) -> int:
        """
        Heap-based greedy:
        - Separate digits into two max-heaps (odd, even) using negatives.
        - Reconstruct the number from most to least significant position,
          always taking the largest available digit of matching parity.
        """
        if num == 0:
            return 0

        digits = []   # original digits, least-significant to most
        odd = []      # max-heap via negatives
        even = []     # max-heap via negatives

        n = num
        while n > 0:
            d = n % 10
            if d % 2:
                heapq.heappush(odd, -d)
            else:
                heapq.heappush(even, -d)
            digits.append(d)
            n //= 10

        res = 0
        # Rebuild from most significant to least significant
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] % 2:
                res = res * 10 + (-heapq.heappop(odd))
            else:
                res = res * 10 + (-heapq.heappop(even))

        return res


# --------------------------------------------------
# Algorithm Explanation:
# --------------------------------------------------
# 1. Extract all digits of `num`. Push odd digits into an "odd" max-heap
#    and even digits into an "even" max-heap (Python's heapq is a min-heap,
#    so we store negatives to simulate max-heap behavior).
# 2. Traverse the original digits from most significant to least significant.
#    For each position, check the original digit's parity and pop the largest
#    available digit from the corresponding heap, appending it to the answer.
# 3. This guarantees the leftmost positions get the largest possible same-parity
#    digits, yielding the maximum number allowed by the parity-swap constraint.
#
# --------------------------------------------------
# Time Complexity: O(d log d), where d is the number of digits (≤ 10 here).
# Space Complexity: O(d) for the heaps and digit storage.
# --------------------------------------------------


# --------------------------------------------------
# Test Cases
# --------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.largestInteger(0))        # Expected: 0
    print(sol.largestInteger(1))        # Expected: 1
    print(sol.largestInteger(12))       # Expected: 21
    print(sol.largestInteger(1234))     # Expected: 3412
    print(sol.largestInteger(65875))    # Expected: 87655
    print(sol.largestInteger(111222))   # Expected: 222111
    print(sol.largestInteger(9070))     # Expected: 9700