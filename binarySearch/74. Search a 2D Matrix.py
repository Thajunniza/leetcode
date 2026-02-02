"""
74: Search a 2D Matrix

Given an m x n matrix where:
- Each row is sorted in ascending order
- The first integer of each row is greater than the last integer of the previous row

Write an efficient algorithm that searches for a value `target` in the matrix. 
Return True if the target exists, else False.

Example:
Input: matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], target = 3
Output: True

Input: matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], target = 13
Output: False

Algorithm:
1. First, use binary search on the rows to identify which row may contain the target.
   - Compare target with the first and last element of the middle row.
2. Once the candidate row is found, use binary search within that row.
3. Return True if found, else False.

Time Complexity: O(log(m) + log(n)) => O(log(mn))
Space Complexity: O(1) (no extra space used)

"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # Helper: Binary search in 1D array
        def is_available(nums):
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False
        
        # Binary search on rows
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            nums = matrix[mid]

            if target > nums[-1]:
                top = mid + 1
            elif target < nums[0]:
                bottom = mid - 1
            else:
                # Target is within this row
                return is_available(nums)
        
        return False


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    assert sol.searchMatrix(matrix1, 3) == True
    assert sol.searchMatrix(matrix1, 13) == False
    assert sol.searchMatrix(matrix1, 50) == True
    assert sol.searchMatrix(matrix1, 0) == False

    print("All test cases passed!")
