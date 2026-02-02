"""
Second Largest Element in an Array

Given an array of integers, find the second largest **distinct** element.
If the second largest element does not exist, return -1.

Example:
Input: nums = [12, 35, 1, 10, 34, 1]
Output: 34

Input: nums = [10, 10, 10]
Output: -1

Algorithm:
1. Initialize two variables:
   - max1 to store the largest element
   - max2 to store the second largest element
2. Traverse the array:
   - If current element is greater than max1:
       - Assign max1 to max2
       - Update max1 with current element
   - Else if current element is strictly between max1 and max2:
       - Update max2
3. Return max2 if it exists, otherwise return -1.

Time Complexity: O(n), where n is the number of elements
Space Complexity: O(1), constant extra space
"""

class Solution(object):
    def secondLargestElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 2:
            return -1

        max1 = -1
        max2 = -1

        for n in nums:
            if n > max1:
                max2 = max1
                max1 = n
            elif max2 < n < max1:
                max2 = n

        return max2


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    assert sol.secondLargestElement([12, 35, 1, 10, 34, 1]) == 34
    assert sol.secondLargestElement([10, 10, 10]) == -1
    assert sol.secondLargestElement([10, 20]) == 10
    assert sol.secondLargestElement([20, 10]) == 10
    assert sol.secondLargestElement([5]) == -1

    print("All test cases passed!")
