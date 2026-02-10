"""
===========================================================
974. Subarray Sums Divisible by K
===========================================================

Problem:
--------
Given an integer array nums and an integer k,
return the number of non-empty subarrays whose sum is divisible by k.

A subarray is contiguous.

Approach:
---------
Prefix Sum + Hash Map (Remainder Frequency)

Key Idea:
---------
If two prefix sums have the same remainder when divided by k,
their difference (subarray between them) is divisible by k.

Mathematically:
---------------
If:
    prefix_sum[j] % k == prefix_sum[i] % k
Then:
    subarray(i+1 → j) sum is divisible by k

Algorithm:
----------
1. Maintain running prefix sum.
2. Compute remainder = prefix_sum % k.
3. Store frequency of each remainder in a hashmap.
4. If remainder was seen before:
       count += frequency of that remainder.
5. Update remainder frequency.

Important:
----------
Initialize hashmap with:
    {0: 1}
This handles subarrays starting from index 0.

Time Complexity:
----------------
O(n) — single pass through array.

Space Complexity:
-----------------
O(k) — at most k different remainders.

Author:
-------
Thajunniza M A
"""

# -----------------------------
# Solution Class
# -----------------------------
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Remainder frequency map
        seen = {0: 1}

        total = 0
        count = 0

        for num in nums:
            total += num
            remainder = total % k

            if remainder in seen:
                count += seen[remainder]
                seen[remainder] += 1
            else:
                seen[remainder] = 1

        return count


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([4,5,0,-2,-3,1], 5, 7),
        ([5], 9, 0),
        ([1,2,3,4,5], 5, 4),
        ([2,-2,2,-4], 6, 2),
    ]

    for i, (nums, k, expected) in enumerate(tests, 1):
        result = sol.subarraysDivByK(nums, k)
        print(f"Test {i}: expected={expected}, got={result}")
