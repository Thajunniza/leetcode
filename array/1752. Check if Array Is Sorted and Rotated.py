"""
1752 - Check if Array Can Be Rotated to Sorted

Given an array of integers `nums`, check if it is possible to rotate the array
(circularly) so that it becomes sorted in non-decreasing order.

Example:
Input: nums = [3, 4, 5, 1, 2]
Output: True
Explanation: Rotating the array by 3 positions gives [1, 2, 3, 4, 5], which is sorted.

Input: nums = [2, 1, 3, 4]
Output: False
Explanation: No rotation can make it fully non-decreasing.

Algorithm:
1. Count the number of "drops" in the array, where nums[i] > nums[i+1] (circularly).
2. If the number of drops is more than 1, return False.
3. Otherwise, return True.

Time Complexity: O(n), where n is the number of elements in nums
Space Complexity: O(1), constant extra space
"""

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n <= 1:
            return True  # empty or single-element array

        count = 0  # count of "drops"
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count += 1
                if count > 1:
                    return False
        return True


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # True cases
    assert sol.check([3, 4, 5, 1, 2]) == True
    assert sol.check([1, 2, 3]) == True
    assert sol.check([1]) == True
    assert sol.check([]) == True
    assert sol.check([2, 2, 2]) == True

    # False cases
    assert sol.check([2, 1, 3, 4]) == False
    assert sol.check([3, 1, 2, 4]) == False
    assert sol.check([3, 5, 1, 4, 2]) == False

    print("All test cases passed!")
