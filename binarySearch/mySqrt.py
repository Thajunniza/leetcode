"""
Problem: Integer Square Root

Given a non-negative integer n, return the integer square root of n.
The integer square root is the greatest integer x such that:
    x * x <= n

Do NOT use any built-in square root functions.

---------------------------------
Examples:
Input:  n = 25
Output: 5

Input:  n = 30
Output: 5
---------------------------------

Approach 1: Brute Force
- Try all integers starting from 1
- Keep updating result while i*i <= n

Time Complexity: O(√n)
Space Complexity: O(1)
"""

class Solution:
    def getsqrt(self, n: int) -> int:
        # Edge cases
        if n == 0 or n == 1:
            return n

        i = 1
        res = 1

        while i * i <= n:
            res = i
            i += 1

        return res


"""
---------------------------------
Approach 2: Binary Search (Optimized)

We perform binary search on the answer space [1, n].
Store the last valid mid where mid*mid <= n.

Time Complexity: O(log n)
Space Complexity: O(1)
---------------------------------
"""

class SolutionBinarySearch:
    def getsqrt(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        l, r = 1, n
        ans = 0

        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= n:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans


# ---------------------------------
# Test Cases
# ---------------------------------
if __name__ == "__main__":
    sol = Solution()
    sol_bs = SolutionBinarySearch()

    test_cases = [
        (4, 2),
        (25, 5),
        (30, 5),
        (100, 10),
        (1, 1),
        (0, 0),
        (8, 2)
    ]

    print("Brute Force Results:")
    for n, expected in test_cases:
        print(f"Input: {n}, Output: {sol.getsqrt(n)}, Expected: {expected}")

    print("\nBinary Search Results:")
    for n, expected in test_cases:
        print(f"Input: {n}, Output: {sol_bs.getsqrt(n)}, Expected: {expected}")