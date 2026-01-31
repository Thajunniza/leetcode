"""
Problem: Search a 2D Matrix II
LeetCode: 240

Given an m x n matrix where:
- Integers in each row are sorted in ascending from left to right
- Integers in each column are sorted in ascending from top to bottom

Write an efficient algorithm that searches for a value target in the matrix. 
Return True if the target exists, else False.

Example:
Input: matrix = [
  [1, 4, 7, 11],
  [2, 5, 8, 12],
  [3, 6, 9, 16]
], target = 5
Output: True

Input: matrix = [
  [1, 4, 7, 11],
  [2, 5, 8, 12],
  [3, 6, 9, 16]
], target = 10
Output: False

Algorithm:
1. Start at top-right corner: row = 0, col = n-1
2. While row < m and col >= 0:
   - If matrix[row][col] == target: return True
   - If matrix[row][col] < target: move down (row + 1)
   - If matrix[row][col] > target: move left (col - 1)
3. If loop ends, return False

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        row = 0
        col = len(matrix[0]) - 1
        m = len(matrix)
        
        while row < m and col >= 0:
            val = matrix[row][col]
            if target == val:
                return True
            elif target > val:
                row += 1
            else:
                col -= 1
        
        return False


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    matrix1 = [
        [1, 4, 7, 11],
        [2, 5, 8, 12],
        [3, 6, 9, 16]
    ]
    assert sol.searchMatrix(matrix1, 5) == True
    assert sol.searchMatrix(matrix1, 10) == False
    assert sol.searchMatrix(matrix1, 16) == True
    assert sol.searchMatrix(matrix1, 1) == True
    assert sol.searchMatrix(matrix1, 17) == False

    print("All test cases passed!")
