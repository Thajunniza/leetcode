"""
Problem: Nth Root of a Number

Given two integers n and m, find the integer nth root of m.
The nth root of m is an integer x such that:
    x^n = m

If no such integer exists, return -1.

---------------------------------
Examples:
Input:  n = 3, m = 27
Output: 3

Input:  n = 4, m = 16
Output: 2

Input:  n = 2, m = 20
Output: -1
---------------------------------

Approach: Binary Search

We search for x in the range [1, m].
- Compute mid^n
- If mid^n == m → return mid
- If mid^n < m → search right
- Else → search left

Time Complexity: O(log m * n)
Space Complexity: O(1)
"""

class Solution:
    def nthRoot(self, n: int, m: int) -> int:
        if m == 0:
            return 0
        if m == 1:
            return 1

        l, r = 1, m

        while l <= r:
            mid = (l + r) // 2
            val = mid ** n

            if val == m:
                return mid
            elif val < m:
                l = mid + 1
            else:
                r = mid - 1

        return -1


# ---------------------------------
# Test Cases
# ---------------------------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (3, 27, 3),
        (4, 16, 2),
        (2, 20, -1),
        (1, 5, 5),
        (5, 1, 1),
        (3, 64, 4)
    ]

    for n, m, expected in test_cases:
        result = sol.nthRoot(n, m)
        print(f"nthRoot({n}, {m}) = {result}")
        print(f"Expected: {expected}")
        print("-" * 25)