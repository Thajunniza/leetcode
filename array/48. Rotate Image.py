# ===========================================================
# 48. Rotate Image (O(1) Space)
# ===========================================================

# 🧩 Problem:
# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees clockwise in-place.
#
# You must modify the input matrix directly.

# -----------------------------------------------------------
# Approach — Transpose + Reverse Rows:
# -----------------------------------------------------------
# Key idea:
# - Transpose the matrix (rows → columns)
# - Reverse each row
#
# Steps:
# 1. Transpose the matrix:
#    - Swap matrix[i][j] with matrix[j][i] for j > i
# 2. Reverse each row to get 90° clockwise rotation

# -----------------------------------------------------------
# ⏱ Time Complexity:   O(n²)
# 💾 Space Complexity: O(1)
# -----------------------------------------------------------

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            l, r = 0, n - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1

        return matrix


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(sol.rotate(mat))
    # Expected Output:
    # [
    #   [7, 4, 1],
    #   [8, 5, 2],
    #   [9, 6, 3]
    # ]
