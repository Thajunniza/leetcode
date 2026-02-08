"""
===========================================================
2061. Number of Spaces Cleaning Robot Cleaned – Test Suite
===========================================================

Problem:
--------
A robot starts at position (0,0) facing right in a room.
The room is represented as a 2D grid:
- 0 → empty space
- 1 → obstacle

Robot rules:
- If the cell in front is empty, move forward
- Otherwise, turn right 90 degrees
- The robot stops when it revisits the same (row, col, direction)

Return the number of unique cells cleaned.

Time Complexity:
---------------
O(m * n * 4) – each cell visited in 4 directions max

Space Complexity:
----------------
O(m * n * 4) – visited state tracking

Algorithm:
----------
1. Track direction order: Right → Down → Left → Up
2. Maintain a visited set for (row, col, direction)
3. Maintain a cleaned set for unique cells
4. Simulate movement until a state repeats
5. Return size of cleaned set

Author:
-------
Thajunniza M A
"""

# -----------------------------
# Solution Class
# -----------------------------
class Solution(object):
    def numberOfCleanRooms(self, room):
        """
        :type room: List[List[int]]
        :rtype: int
        """

        # Directions: Right → Down → Left → Up
        direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        row = 0
        col = 0
        dir_idx = 0

        visited = set()   # (row, col, direction)
        cleaned = set()   # (row, col)

        m = len(room)
        n = len(room[0])

        def is_valid(r, c):
            if r < 0 or r >= m:
                return False
            if c < 0 or c >= n:
                return False
            if room[r][c] == 1:
                return False
            return True

        while True:
            state = (row, col, dir_idx)

            # Stop if state repeats
            if state in visited:
                break

            visited.add(state)
            cleaned.add((row, col))

            # Move or rotate
            dr, dc = direc[dir_idx]
            nxt_row = row + dr
            nxt_col = col + dc

            if is_valid(nxt_row, nxt_col):
                row = nxt_row
                col = nxt_col
            else:
                dir_idx = (dir_idx + 1) % 4

        return len(cleaned)


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    room1 = [
        [0,0,0],
        [1,1,0],
        [0,0,0]
    ]
    print("Test Case 1")
    print("Cleaned Spaces:", sol.numberOfCleanRooms(room1))  # Expected: 7
    print()

    # Test Case 2
    room2 = [
        [0,1,0],
        [0,1,0],
        [0,0,0]
    ]
    print("Test Case 2")
    print("Cleaned Spaces:", sol.numberOfCleanRooms(room2))
    print()

    # Test Case 3: Single cell
    room3 = [[0]]
    print("Test Case 3")
    print("Cleaned Spaces:", sol.numberOfCleanRooms(room3))  # Expected: 1
    print()

    # Test Case 4: Fully blocked
    room4 = [
        [0,1],
        [1,1]
    ]
    print("Test Case 4")
    print("Cleaned Spaces:", sol.numberOfCleanRooms(room4))  # Expected: 1
