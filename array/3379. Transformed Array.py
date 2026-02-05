"""
3379. Transformed Array

Description:
Given an integer array nums of length n, create a new array res such that:
- If nums[i] == 0, then res[i] = 0
- Otherwise, res[i] = nums[(i + nums[i]) % n]

The transformation uses circular indexing.

Example:
Input: nums = [1, -1, 2, 0]
Output: [ -1, 1, 1, 0 ]

Approach:
Circular Indexing using Modulo.
- Iterate through the array using index and value.
- If the value is zero, place zero in the result.
- Otherwise, compute the new index using (i + value) % n.
- Store the value at the computed index into the result array.

Time Complexity:
O(n) - Each element is processed once.

Space Complexity:
O(n) - A new array is created to store results.
"""

class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums

        res = [0] * n

        for i, c in enumerate(nums):
            if c == 0:
                res[i] = 0
            else:
                res[i] = nums[(i + c) % n]

        return res


# -------------------- Test Cases --------------------

def test_constructTransformedArray():
    sol = Solution()

    assert sol.constructTransformedArray([1, -1, 2, 0]) == [-1, 1, 1, 0]
    assert sol.constructTransformedArray([0, 0, 0]) == [0, 0, 0]
    assert sol.constructTransformedArray([2, 2, 2]) == [2, 2, 2]
    assert sol.constructTransformedArray([1]) == [1]
    assert sol.constructTransformedArray([-1, -1, -1]) == [-1, -1, -1]

    print("All test cases passed.")

if __name__ == "__main__":
    test_constructTransformedArray()
