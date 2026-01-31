"""
1901: Find a Peak Element II (2D Peak)

Given a 2D matrix, return the position [row, col] of any peak element:
- mat[row][col] > neighbors (up, down, left, right)

Algorithm (Binary Search on Columns):
1. Perform binary search on columns:
   - For the middle column, find the row with maximum value.
   - Compare this value with left and right neighbors.
   - Move in the direction of the larger neighbor.
2. Stop when a peak is found.

Time Complexity: O(m * log n)
Space Complexity: O(1)
"""

class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """

        def get_max_index(col):
            """Return row index of maximum element in column `col`"""
            max_val = float("-inf")
            idx = 0
            for i in range(len(mat)):
                if mat[i][col] > max_val:
                    max_val = mat[i][col]
                    idx = i
            return idx

        num_rows = len(mat)
        num_cols = len(mat[0])
        left, right = 0, num_cols - 1

        while left <= right:
            mid = (left + right) // 2
            row_idx = get_max_index(mid)
            val = mat[row_idx][mid]
            left_val = mat[row_idx][mid - 1] if mid - 1 >= 0 else float("-inf")
            right_val = mat[row_idx][mid + 1] if mid + 1 < num_cols else float("-inf")

            # Peak found
            if val >= left_val and val >= right_val:
                return [row_idx, mid]
            # Move left
            elif val < left_val:
                right = mid - 1
            # Move right
            else:
                left = mid + 1

        return [-1, -1]  # fallback, should not happen


# ----------------- Test Cases -----------------
if __name__ == "__main__":
    sol = Solution()
    
    mat1 = [
        [1, 4, 3],
        [6, 7, 5],
        [2, 8, 9]
    ]
    peak1 = sol.findPeakGrid(mat1)
    print(f"Peak at: {peak1}, value = {mat1[peak1[0]][peak1[1]]}")

    mat2 = [
        [10, 20, 15],
        [21, 30, 14],
        [7, 16, 32]
    ]
    peak2 = sol.findPeakGrid(mat2)
    print(f"Peak at: {peak2}, value = {mat2[peak2[0]][peak2[1]]}")
