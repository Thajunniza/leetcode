"""
===========================================================
200. Number of Islands
===========================================================

Problem:
--------
Given an m x n 2D binary grid `grid` representing a map of
'1's (land) and '0's (water), return the number of islands.

An island is formed by connecting adjacent lands horizontally
or vertically (no diagonals). All four edges of the grid are
assumed to be surrounded by water.

Approach:
---------
BFS (Queue-based Flood Fill)

1. Iterate through every cell in the grid.
2. When a '1' (unvisited land) is found, it starts a new island:
   - Increment the island count.
   - Run BFS from that cell to visit all connected land:
     * Use a queue to explore 4-directional neighbors.
     * Mark each visited land as '0' (sink it) to avoid recounting.
3. Continue scanning; each new '1' found starts another BFS.

This counts each connected component of '1's exactly once.

Time Complexity:
----------------
O(m * n) — each cell is processed at most once.

Space Complexity:
-----------------
O(min(m, n)) to O(m * n) — queue size in the worst case when
a single large island fills most of the grid.

Author:
-------
Thajunniza M A
"""

from collections import deque

# -----------------------------
# Solution Class (BFS) - Modular & Easy to Understand
# -----------------------------
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Guard for empty inputs
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # -------------------------
        # Helper: bounds + land check
        # -------------------------
        def is_valid(r, c):
            """Return True if (r, c) is inside the grid and is land '1'."""
            if r < 0 or r >= m:
                return False
            if c < 0 or c >= n:
                return False
            return grid[r][c] == "1"

        # -------------------------
        # Helper: BFS to sink one island
        # -------------------------
        def bfs(sr, sc):
            """Flood-fill from (sr, sc) and sink the entire island."""
            q = deque()
            q.append((sr, sc))
            grid[sr][sc] = "0"  # mark start as visited (sink)

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_valid(nr, nc):
                        grid[nr][nc] = "0"  # mark when enqueuing to avoid duplicates
                        q.append((nr, nc))

            return 1  # counting exactly one island per BFS

        # -------------------------
        # Main scan
        # -------------------------
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += bfs(i, j)

        return count


# -----------------------------
# Optional: DFS (Iterative with Stack) in the same modular style
# -----------------------------
class SolutionDFS(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_valid(r, c):
            if r < 0 or r >= m:
                return False
            if c < 0 or c >= n:
                return False
            return grid[r][c] == "1"

        def dfs(sr, sc):
            stack = [(sr, sc)]
            grid[sr][sc] = "0"  # mark start as visited (sink)
            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_valid(nr, nc):
                        grid[nr][nc] = "0"
                        stack.append((nr, nc))
            return 1

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += dfs(i, j)

        return count


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":
    import copy

    tests = [
        (
            [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ],
            1
        ),
        (
            [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ],
            3
        ),
        ([], 0),
        ([["0","0"],["0","0"]], 0),
        ([["1"]], 1),
    ]

    print("=== BFS Solution ===")
    sol_bfs = Solution()
    for i, (grid, expected) in enumerate(tests, 1):
        got = sol_bfs.numIslands(copy.deepcopy(grid))
        print(f"Test {i}: expected={expected}, got={got}")

    print("\n=== DFS (Iterative) Solution ===")
    sol_dfs = SolutionDFS()
    for i, (grid, expected) in enumerate(tests, 1):
        got = sol_dfs.numIslands(copy.deepcopy(grid))
        print(f"Test {i}: expected={expected}, got={got}")