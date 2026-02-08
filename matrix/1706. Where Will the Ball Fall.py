# ===========================================================
# 1706. Where Will the Ball Fall
# ===========================================================

# 🧩 Problem:
# Given an m x n grid where:
# - 1  -> board slopes to the right (\)
# - -1 -> board slopes to the left (/)
# Drop a ball from each column at the top and find
# the column where it falls at the bottom.
# Return -1 if the ball gets stuck.

# -----------------------------------------------------------
# Approach — Simulation Row by Row:
# -----------------------------------------------------------
# 1. For each starting column, simulate the ball's path downwards.
# 2. Ball moves according to slope:
#    - 1  -> move down & right
#    - -1 -> move down & left
# 3. Ball gets stuck if:
#    - Hits the wall (next_col < 0 or next_col >= n)
#    - Forms a V-shape with neighbor: grid[row][col] != grid[row][next_col]
# 4. Append final column index or -1 to the result array.

# -----------------------------------------------------------
# ⏱ Time Complexity:   O(m * n)
# 💾 Space Complexity: O(n)
# -----------------------------------------------------------

class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        result = []

        # simulate each ball dropped from top column
        for col_start in range(n):
            col = col_start
            for row in range(m):
                next_col = col + grid[row][col]  # move left/right based on slope

                # ball stuck conditions
                if next_col < 0 or next_col >= n or grid[row][col] != grid[row][next_col]:
                    col = -1
                    break

                # move ball to next column
                col = next_col

            result.append(col)

        return result


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    grid1 = [
        [1, 1, 1, -1, -1],
        [1, 1, 1, -1, -1],
        [-1, -1, -1, 1, 1],
        [1, 1, 1, 1, -1],
        [-1, -1, -1, -1, -1]
    ]
    print(sol.findBall(grid1))
    # Expected Output: [1, -1, -1, -1, -1]

    grid2 = [
        [1, 1, -1],
        [1, 1, -1],
        [-1, -1, 1]
    ]
    print(sol.findBall(grid2))
    # Expected Output: [-1, -1, -1]
