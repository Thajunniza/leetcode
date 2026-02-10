"""
===========================================================
1480. Running Sum of 1D Array
===========================================================

Problem:
--------
Given an array `nums`, return the running sum of the array.

The running sum at index i is defined as:
    runningSum[i] = nums[0] + nums[1] + ... + nums[i]

Example:
--------
Input:  nums = [1,2,3,4]
Output: [1,3,6,10]

Approach:
---------
Prefix Sum (Cumulative Sum)

1. Maintain a variable `total` initialized to 0.
2. Iterate through the array.
3. Add the current number to `total`.
4. Store `total` as the running sum at that index.

This is the most basic form of the prefix sum pattern.

Time Complexity:
----------------
O(n) — single pass through the array.

Space Complexity:
-----------------
O(n) — if using a separate result array.
O(1) — if modifying input in-place.

Author:
-------
Thajunniza M A
"""

# -----------------------------
# Solution Class (Using Extra Array)
# -----------------------------
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums
        
        result = [0] * n
        total = 0

        for i in range(n):
            total += nums[i]
            result[i] = total 
        
        return result


# -----------------------------
# Optimized In-Place Version
# -----------------------------
class SolutionInPlace(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":

    tests = [
        ([1,2,3,4], [1,3,6,10]),
        ([1,1,1,1,1], [1,2,3,4,5]),
        ([3,1,2,10,1], [3,4,6,16,17]),
        ([], []),
        ([5], [5])
    ]

    print("=== Extra Array Version ===")
    sol = Solution()
    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.runningSum(nums[:])
        print(f"Test {i}: expected={expected}, got={result}")

    print("\n=== In-Place Version ===")
    sol2 = SolutionInPlace()
    for i, (nums, expected) in enumerate(tests, 1):
        result = sol2.runningSum(nums[:])
        print(f"Test {i}: expected={expected}, got={result}")
