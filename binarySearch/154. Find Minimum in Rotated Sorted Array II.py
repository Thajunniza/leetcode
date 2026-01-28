# ------------------------------------------------------------
# 154: Find Minimum in Rotated Sorted Array II
# ------------------------------------------------------------
# Problem:
# Given a rotated sorted array that may contain duplicates,
# find the minimum element. The array was originally sorted
# in ascending order and then rotated.
#
# You must handle duplicates, which may prevent a clear
# binary search choice at some steps.
#
# ------------------------------------------------------------
# Example:
# Input:  nums = [2,2,2,0,1]
# Output: 0
#
# Input:  nums = [1,3,5]
# Output: 1
#
# Input:  nums = [3,3,1,3]
# Output: 1
#
# ------------------------------------------------------------
# Algorithm (Binary Search with duplicates):
# 1. Initialize left = 0, right = len(nums) - 1
# 2. Maintain a variable min_val to track the minimum
# 3. While left <= right:
#    - Compute mid
#    - If left half is strictly sorted (nums[left] < nums[mid]):
#         - Minimum of left half is nums[left]
#         - Update min_val
#         - Search right half (left = mid + 1)
#    - Else if left half is unsorted (nums[left] > nums[mid]):
#         - Minimum could be nums[mid]
#         - Update min_val
#         - Search left half (right = mid - 1)
#    - Else (nums[left] == nums[mid]):
#         - Cannot determine which half has minimum
#         - Update min_val with nums[left]
#         - Move left pointer by one (left += 1)
# 4. Return min_val
# ------------------------------------------------------------

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        min_val = float("inf")

        while l <= r:
            mid = (l + r) // 2

            if nums[l] < nums[mid]:
                # Left half is strictly sorted
                min_val = min(min_val, nums[l])
                l = mid + 1
            elif nums[l] > nums[mid]:
                # Minimum is in left half
                min_val = min(min_val, nums[mid])
                r = mid - 1
            else:
                # nums[l] == nums[mid], cannot determine
                min_val = min(min_val, nums[l])
                l += 1

        return min_val

# ------------------------------------------------------------
# Test Run
# ------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [2,2,2,0,1],
        [1,3,5],
        [3,3,1,3],
        [10,1,10,10,10],
        [1,1,1,1,1]
    ]

    for nums in test_cases:
        print("Input:", nums)
        print("Minimum:", sol.findMin(nums))
        print("-" * 40)