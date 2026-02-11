"""
===========================================================
1524. Number of Sub-arrays With Odd Sum
===========================================================

Problem:
--------
Given an integer array arr,
return the number of subarrays whose sum is odd.

Since the answer can be large, return it modulo 10^9 + 7.

-----------------------------------------------------------
Approach 1: Prefix Sum + Parity Counting
-----------------------------------------------------------

Key Idea:
---------
Let prefix sum at index i be:
    total = arr[0] + ... + arr[i]

A subarray sum is:
    total - previous_prefix

For this to be ODD:
    one must be even and the other odd.

So we maintain:
    even_count  -> number of even prefix sums seen so far
    odd_count   -> number of odd prefix sums seen so far

If current prefix is:
    even -> it can pair with previous odd prefixes
    odd  -> it can pair with previous even prefixes

Initialize:
    even_count = 1 (empty prefix = 0, which is even)

Time Complexity: O(n)
Space Complexity: O(1)
"""

class SolutionPrefix(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        even_count = 1   # empty prefix
        odd_count = 0
        total = 0
        count = 0

        for num in arr:
            total += num

            if total % 2 == 0:
                count += odd_count
                even_count += 1
            else:
                count += even_count
                odd_count += 1

        return count % MOD


"""
-----------------------------------------------------------
Approach 2: Optimized Using Parity Only
-----------------------------------------------------------

Observation:
---------
We don't need full prefix sum.
We only need to track whether prefix is even or odd.

Maintain:
    parity ^= num % 2

If parity == 0 (even):
    add odd_count
If parity == 1 (odd):
    add even_count

Time Complexity: O(n)
Space Complexity: O(1)
"""

class SolutionParity(object):
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7

        even_count = 1
        odd_count = 0
        parity = 0
        count = 0

        for num in arr:
            parity ^= (num & 1)

            if parity == 0:
                count += odd_count
                even_count += 1
            else:
                count += even_count
                odd_count += 1

        return count % MOD


# -----------------------------
# Test Case
# -----------------------------
if __name__ == "__main__":
    arr = [1, 3, 5]

    sol_prefix = SolutionPrefix()
    sol_parity = SolutionParity()

    print("Prefix Method:", sol_prefix.numOfSubarrays(arr))   # Expected: 4
    print("Parity Method:", sol_parity.numOfSubarrays(arr))   # Expected: 4
