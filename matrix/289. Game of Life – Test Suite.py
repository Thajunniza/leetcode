"""
===========================================================
289. Game of Life – Test Suite
===========================================================

Problem:
--------
Update the board according to the Game of Life rules in-place.

Rules:
1. Any live cell with fewer than 2 live neighbors dies
2. Any live cell with 2 or 3 live neighbors lives
3. Any live cell with more than 3 live neighbors dies
4. Any dead cell with exactly 3 live neighbors becomes alive

Time Complexity: O(m * n)
Space Complexity: O(1) – in-place using state encoding

Author:
-------
Thajunniza M A
"""

# -----------------------------
# Solution Class
# -----------------------------
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        # -----------------------------
        # Helper Functions
        # -----------------------------
        def is_valid(r,c):
            if r < 0 or r >= m:
                return False
            if c < 0 or c >= n:
                return False
            # Count cells that are currently alive (1 or -1)
            if board[r][c] == 1 or board[r][c] == -1:
                return True
            return False

        def get_live_count(r,c):
            directions = [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,-1),(-1,1),(1,1)]
            count = 0
            for row,col in directions:
                nxt_row = r + row
                nxt_col = c + col
                if is_valid(nxt_row,nxt_col):
                    count += 1
            return count

        # -----------------------------
        # First Pass: Mark changes
        # -----------------------------
        for i in range(m):
            for j in range(n):
                live_count = get_live_count(i,j)
                val = board[i][j]
                if val == 0 and live_count == 3:
                    board[i][j] = 2
                if val == 1 and (live_count < 2 or live_count > 3):
                    board[i][j] = -1
        
        # -----------------------------
        # Second Pass: Finalize board
        # -----------------------------
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1

        return board

# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":
    sol = Solution()

    board1 = [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ]

    print("Original Board:")
    for row in board1:
        print(row)

    sol.gameOfLife(board1)

    print("\nBoard After One Step:")
    for row in board1:
        print(row)
