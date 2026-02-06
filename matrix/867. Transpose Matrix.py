# ===========================================================
# 867. Transpose Matrix
# ===========================================================

# 🧩 Problem:
# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal.

# -----------------------------------------------------------
# ⏱ Time Complexity:   O(m × n)
# 💾 Space Complexity: O(m × n)
# -----------------------------------------------------------

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])

        # Create transposed matrix
        res = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]

        return res


# -----------------------------------------------------------
# Driver Code
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(sol.transpose(matrix))
    # Expected Output:
    # [
    #   [1, 4],
    #   [2, 5],
    #   [3, 6]
    # ]
