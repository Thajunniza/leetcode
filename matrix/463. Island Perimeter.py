# ===========================================================
# 463. Island Perimeter
# ===========================================================

# 🧩 Problem:
# Given a grid of 0s (water) and 1s (land), compute the
# perimeter of the island. Land cells are connected
# horizontally/vertically, no lakes inside.

# -----------------------------------------------------------
# Approach — Scan & Count Shared Edges:
# -----------------------------------------------------------
# 1. Each land cell contributes 4 edges initially
# 2. For every land cell, check top and left neighbors
#    - If neighbor is land, subtract 2 from perimeter
#      (since the edge is shared)
# 3. Continue for all cells

# -----------------------------------------------------------
# ⏱ Time Complexity:   O(m × n)
# 💾 Space Complexity: O(1)
# -----------------------------------------------------------

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        perimeter = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # each land cell starts with 4 edges
                    perimeter += 4
                    # subtract shared edge with top neighbor
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    # subtract shared edge with left neighbor
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2

        return perimeter


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    grid = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ]
    print(sol.islandPerimeter(grid))
    # Expected Output: 16
