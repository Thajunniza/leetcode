# ===========================================================
# 59. Spiral Matrix II
# ===========================================================

# 🧩 Problem:
# Given an integer n, generate an n x n matrix filled 
# with elements from 1 to n^2 in spiral order.

# -----------------------------------------------------------
# Approach — Layer by Layer Boundaries:
# -----------------------------------------------------------
# 1. Maintain four boundaries: top, bottom, left, right
# 2. Traverse in the order: top row → right column → bottom row → left column
# 3. Fill numbers incrementally
# 4. Shrink boundaries after each traversal
# 5. Repeat until boundaries cross

# -----------------------------------------------------------
# ⏱ Time Complexity:   O(n × n)
# 💾 Space Complexity: O(n × n) for the output matrix
# -----------------------------------------------------------

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # initialize empty n x n matrix
        res = [[0] * n for _ in range(n)]

        left, right = 0, n - 1
        top, bottom = 0, n - 1
        num = 0

        while left <= right and top <= bottom:

            # 1. top row (left → right)
            for col in range(left, right + 1):
                num += 1
                res[top][col] = num
            top += 1

            # 2. right column (top → bottom)
            for row in range(top, bottom + 1):
                num += 1
                res[row][right] = num
            right -= 1

            # 3. bottom row (right → left)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    num += 1
                    res[bottom][col] = num
                bottom -= 1

            # 4. left column (bottom → top)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    num += 1
                    res[row][left] = num
                left += 1

        return res


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    n = 3
    matrix = sol.generateMatrix(n)
    for row in matrix:
        print(row)
    # Expected Output:
    # [1, 2, 3]
    # [8, 9, 4]
    # [7, 6, 5]
