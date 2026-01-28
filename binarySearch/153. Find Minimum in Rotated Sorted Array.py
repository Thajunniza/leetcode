""" 
------------------------------------------------------------
153. Find Minimum in Rotated Sorted Array
------------------------------------------------------------
Problem:
Given a rotated sorted array of unique integers, find the
minimum element. The array was originally sorted in ascending
order and then rotated between 1 and n times.

You must write an algorithm that runs in O(log n) time.

------------------------------------------------------------
Example:
Input:  nums = [4,5,6,7,0,1,2]
Output: 0

Input:  nums = [3,4,5,1,2]
Output: 1

Input:  nums = [11,13,15,17]
Output: 11

------------------------------------------------------------
Algorithm (Binary Search):
1. Initialize left = 0, right = len(nums) - 1
2. Maintain a variable minval to track the minimum found
3. While left <= right:
   - Compute mid
   - If left half is sorted:
        - nums[left] is the minimum of that half
        - Update minval
        - Search in the right half
   - Else:
        - nums[mid] could be the minimum
        - Update minval
        - Search in the left half
4. Return minval

Time Complexity: O(log n)
Space Complexity: O(1)
------------------------------------------------------------
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        minval = float("inf")

        while l <= r:
            mid = (l + r) // 2

            # Left half is sorted
            if nums[l] <= nums[mid]:
                minval = min(minval, nums[l])
                l = mid + 1
            else:
                # Rotation point is in left half
                minval = min(minval, nums[mid])
                r = mid - 1

        return minval


# ------------------------------------------------------------
# Test Run
# ------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [4, 5, 6, 7, 0, 1, 2],
        [3, 4, 5, 1, 2],
        [11, 13, 15, 17],
        [2, 3, 4, 5, 6, 7, 1]
    ]

    for nums in test_cases:
        print("Input:", nums)
        print("Minimum:", sol.findMin(nums))
        print("-" * 40)