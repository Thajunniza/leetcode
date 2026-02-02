"""
136. Single Number

Given a non-empty array of integers `nums`, every element appears twice
except for one. Find that single one.

Example:
Input: nums = [2, 2, 1]
Output: 1

Input: nums = [4, 1, 2, 1, 2]
Output: 4

Algorithm:
1. Initialize a variable `res` to 0.
2. Traverse the array and XOR each element with `res`.
3. XOR properties used:
   - a ^ a = 0
   - a ^ 0 = a
   - XOR is commutative and associative
4. All paired numbers cancel out, leaving the single number.

Time Complexity: O(n), where n is the length of the array
Space Complexity: O(1), constant extra space
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res ^= n
        return res


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    assert sol.singleNumber([2, 2, 1]) == 1
    assert sol.singleNumber([4, 1, 2, 1, 2]) == 4
    assert sol.singleNumber([1]) == 1
    assert sol.singleNumber([0, 0, 99]) == 99

    print("All test cases passed!")
