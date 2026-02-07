# ===========================================================
# 1260. Shift 2D Grid
# ===========================================================

# 🧩 Problem:
# Given an m x n grid and an integer k, shift the grid k times.
# Each shift moves elements to the right, wrapping around rows.

# -----------------------------------------------------------
# Approach — Index Mapping (2D → 1D → 2D):
# -----------------------------------------------------------
# Treat the grid as a 1D array of size (m * n)
# Convert (row, col) → index
# Shift index by k using modulo
# Convert back to (row, col)

# -----------------------------------------------------------
# ⏱ Time Complexity:   O(m × n)
# 💾 Space Complexity: O(m × n)
# -----------------------------------------------------------

class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        total = m * n

        def topos(r, c):
            return r * n + c

        def toidx(pos):
            return pos // n, pos % n

        res = [[0] * n for _ in range(m)]
        k %= total

        for i in range(m):
            for j in range(n):
                pos = (topos(i, j) + k) % total
                r, c = toidx(pos)
                res[r][c] = grid[i][j]

        return res


# -----------------------------------------------------------
# Driver Code
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    k = 1
    print(sol.shiftGrid(grid, k))
    # Expected Output:
    # [
    #   [9, 1, 2],
    #   [3, 4, 5],
    #   [6, 7, 8]
    # ]
