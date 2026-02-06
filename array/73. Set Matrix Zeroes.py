# ===========================================================
# 73. Set Matrix Zeroes (O(1) Space)
# ===========================================================

# 🧩 Problem:
# Given an m x n integer matrix, if an element is 0,
# set its entire row and column to 0s.
#
# You must do it in-place using constant extra space.

# -----------------------------------------------------------
# Approach — First Row & First Column as Markers:
# -----------------------------------------------------------
# Key idea:
# - Use the first row to mark zero-columns
# - Use the first column to mark zero-rows
#
# Steps:
# 1. Check if first row has any zero → rowZero flag
# 2. Check if first column has any zero → colZero flag
# 3. Traverse the rest of the matrix (excluding first row/col):
#    - If matrix[i][j] == 0:
#      - Mark matrix[i][0] = 0 (row marker)
#      - Mark matrix[0][j] = 0 (column marker)
# 4. Zero out cells based on markers
# 5. Finally, zero first row / first column if needed

# -----------------------------------------------------------
# ⏱ Time Complexity:   O(m × n)
# 💾 Space Complexity: O(1)
# -----------------------------------------------------------

class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        rowZero = False
        colZero = False

        # Step 1: Check first row
        for j in range(n):
            if matrix[0][j] == 0:
                rowZero = True
                break

        # Step 2: Check first column
        for i in range(m):
            if matrix[i][0] == 0:
                colZero = True
                break

        # Step 3: Use first row & column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 4: Zero based on row markers
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Step 5: Zero based on column markers
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Step 6: Zero first row if needed
        if rowZero:
            for j in range(n):
                matrix[0][j] = 0

        # Step 7: Zero first column if needed
        if colZero:
            for i in range(m):
                matrix[i][0] = 0
# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    mat = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    sol.setZeroes(mat)
    print(mat)
    # Expected Output:
    # [
    #   [1, 0, 1],
    #   [0, 0, 0],
    #   [1, 0, 1]
    # ]