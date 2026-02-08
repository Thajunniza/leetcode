"""
===========================================================
542. 01 Matrix 
===========================================================

Problem:
--------
Given an m x n matrix mat of 0s and 1s,
return a matrix where each cell contains the distance
to the nearest 0.

Distance is measured in number of steps (up, down, left, right).

Key Insight:
------------
• All 0s are starting points (distance = 0)
• Use Multi-Source BFS
• First time we visit a cell = shortest distance

Time Complexity: O(m * n)
Space Complexity: O(m * n)

Author:
-------
Thajunniza M A
"""

from collections import deque

# -----------------------------
# Solution Class
# -----------------------------
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        m = len(mat)
        n = len(mat[0])

        # Result matrix
        res = [[0] * n for _ in range(m)]

        # Visited set to avoid revisiting cells
        visited = set()

        # BFS queue
        q = deque()

        # 4 possible directions
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        # -----------------------------
        # Step 1: Add all zeros to queue
        # -----------------------------
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))   # mark zero as visited

        # -----------------------------
        # Step 2: BFS
        # -----------------------------
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Boundary + visited check
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    res[nr][nc] = res[r][c] + 1
                    visited.add((nr, nc))
                    q.append((nr, nc))

        return res


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":
    sol = Solution()

    mat1 = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    print("Test Case 1:")
    print(sol.updateMatrix(mat1))
    # Expected:
    # [[0,0,0],
    #  [0,1,0],
    #  [0,0,0]]

    mat2 = [
        [0,0,0],
        [0,1,0],
        [1,1,1]
    ]
    print("\nTest Case 2:")
    print(sol.updateMatrix(mat2))
    # Expected:
    # [[0,0,0],
    #  [0,1,0],
    #  [1,2,1]]
