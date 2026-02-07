# ===========================================================
# 566. Reshape the Matrix
# ===========================================================

# 🧩 Problem:
# Given a 1D array 'original' and integers m and n, 
# reshape it into an m x n 2D matrix in row-wise order.
# If it cannot be reshaped, return an empty matrix.

# -----------------------------------------------------------
# Approach — Index Math:
# -----------------------------------------------------------
# 1. Check if reshaping is possible (len(original) == m*n)
# 2. Initialize an empty m x n matrix
# 3. Fill matrix row by row using:
#    row_index = i // n
#    col_index = i % n
# 4. Return the reshaped matrix

# -----------------------------------------------------------
# ⏱ Time Complexity:   O(m × n)
# 💾 Space Complexity: O(m × n)
# -----------------------------------------------------------

class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        # check if reshape is possible
        if len(original) != m * n:
            return []

        # initialize empty m x n matrix
        res = [[0] * n for _ in range(m)]

        # fill matrix using index math
        for i, val in enumerate(original):
            row = i // n
            col = i % n
            res[row][col] = val

        return res


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    original = [1, 2, 3, 4, 5, 6]
    m, n = 2, 3
    matrix = sol.construct2DArray(original, m, n)
    print(matrix)
    # Expected Output:
    # [[1, 2, 3],
    #  [4, 5, 6]]
