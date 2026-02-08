"""
===========================================================
994. Rotting Oranges
===========================================================

Problem:
--------
Given a grid with:
- 0: empty cell
- 1: fresh orange
- 2: rotten orange

Every minute, rotten oranges rot adjacent fresh oranges.
Return the minimum minutes until no fresh oranges remain.
Return -1 if impossible.

Time Complexity: O(m*n) – each cell visited once
Space Complexity: O(m*n) – for BFS queue and fresh set

Author:
-------
Thajunniza M A
"""

from collections import deque

# -----------------------------
# Solution Class
# -----------------------------
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        def is_valid(r, c):
            if r < 0 or r >= m:
                return False
            if c < 0 or c >= n:
                return False
            if grid[r][c] == 0:
                return False
            return True

        q = deque()
        fresh = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        # Initialize queue with rotten oranges and set of fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh.add((i,j))

        minutes = 0

        # BFS level by level
        while q and fresh:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if is_valid(nr, nc) and (nr, nc) in fresh:
                        fresh.remove((nr, nc))
                        q.append((nr, nc))
            minutes += 1

        return minutes if not fresh else -1


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":
    sol = Solution()

    grid1 = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    print("Test Case 1:", sol.orangesRotting(grid1))  # Expected: 4

    grid2 = [
        [2,1,1],
        [0,1,1],
        [1,0,1]
    ]
    print("Test Case 2:", sol.orangesRotting(grid2))  # Expected: -1

    grid3 = [
        [0,2]
    ]
    print("Test Case 3:", sol.orangesRotting(grid3))  # Expected: 0
