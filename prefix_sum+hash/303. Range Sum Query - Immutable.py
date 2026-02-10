"""
===========================================================
303. Range Sum Query - Immutable
===========================================================

Problem:
--------
Given an integer array `nums`, handle multiple queries of the form:

    sumRange(left, right)

which returns the sum of elements between indices
left and right (inclusive).

The array does NOT change after initialization.

Approach:
---------
Prefix Sum (Precomputation for O(1) Queries)

1. During initialization:
   - Build a prefix sum array where:
       prefix[i] = sum of nums[0] to nums[i]

2. To answer a query:
   - If left == 0:
         return prefix[right]
   - Otherwise:
         return prefix[right] - prefix[left - 1]

Why this works:
---------------
prefix[right]        = sum(0 → right)
prefix[left - 1]     = sum(0 → left-1)

Subtracting gives:
sum(left → right)

Time Complexity:
----------------
Initialization: O(n)
Each query:     O(1)

Space Complexity:
-----------------
O(n) for storing prefix array.

Author:
-------
Thajunniza M A
"""

# -----------------------------
# Solution Class (Prefix Sum)
# -----------------------------
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.prefix = [0] * n

        total = 0
        for i in range(n):
            total += nums[i]
            self.prefix[i] = total

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]


# -----------------------------
# Alternative Implementation (n+1 Prefix Version)
# Cleaner Query Logic
# -----------------------------
class NumArrayAlt(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.prefix = [0] * (n + 1)

        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right + 1] - self.prefix[left]


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":

    nums = [-2, 0, 3, -5, 2, -1]

    print("=== Prefix (size n) Version ===")
    obj = NumArray(nums)
    print(obj.sumRange(0, 2))  # 1
    print(obj.sumRange(2, 5))  # -1
    print(obj.sumRange(0, 5))  # -3

    print("\n=== Prefix (size n+1) Version ===")
    obj2 = NumArrayAlt(nums)
    print(obj2.sumRange(0, 2))  # 1
    print(obj2.sumRange(2, 5))  # -1
    print(obj2.sumRange(0, 5))  # -3
