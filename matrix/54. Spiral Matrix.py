# ===========================================================
# 54. Spiral Matrix
# ===========================================================

# 🧩 Problem:
# Given an m x n matrix, return all elements of the matrix 
# in spiral order.

# -----------------------------------------------------------
# Approach — Layer by Layer Boundaries:
# -----------------------------------------------------------
# 1. Maintain four boundaries: top, bottom, left, right
# 2. Traverse in the order: 
#    top row → right column → bottom row → left column
# 3. Shrink boundaries after each traversal
# 4. Continue until boundaries cross

# -----------------------------------------------------------
# ⏱ Time Complexity:   O(m × n)
# 💾 Space Complexity: O(1) extra (output excluded)
# -----------------------------------------------------------

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        res = []

        while left <= right and top <= bottom:
            # 1. Traverse top row
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # 2. Traverse right column
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # 3. Traverse bottom row (if still valid)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # 4. Traverse left column (if still valid)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(sol.spiralOrder(matrix))
    # Expected Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
