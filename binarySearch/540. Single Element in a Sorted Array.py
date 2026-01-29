"""
540: Single Element in a Sorted Array

Given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once. Find this single element using binary search.

Example:
Input:  [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
Output: 4

Time Complexity: O(log n) -- Binary search halves the search space each time
Space Complexity: O(1) -- No extra space used
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = l + (r - l) // 2

            # Check if mid is the single element
            if (mid == 0 or nums[mid] != nums[mid - 1]) and (mid == n - 1 or nums[mid] != nums[mid + 1]):
                return nums[mid]

            # Decide which side to search based on pair alignment
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or \
               (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                l = mid + 1
            else:
                r = mid - 1

        # Not reachable if input is valid
        return -1


# -------------------------------
# Example Test Cases
# -------------------------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6], 4),
        ([1, 1, 2, 3, 3], 2),
        ([1, 2, 2, 3, 3], 1),
        ([1, 1, 2, 2, 3], 3),
        ([10], 10),
        ([0,0,1,1,2,2,3,3,4], 4)
    ]

    for arr, expected in test_cases:
        result = sol.singleNonDuplicate(arr)
        print(f"Input: {arr}")
        print(f"Single element: {result} (Expected: {expected})\n")