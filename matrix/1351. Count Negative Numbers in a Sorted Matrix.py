# ===========================================================
# 1351. Count Negative Numbers in a Sorted Matrix
# ===========================================================

# 🧩 Problem:
# Given an m x n grid where each row is sorted in non-increasing order,
# count the total number of negative numbers in the grid.

# -----------------------------------------------------------
# Approach — Binary Search on Each Row:
# -----------------------------------------------------------
# 1. For each row, use binary search to find the first negative number.
# 2. Each negative number contributes to the total count.
# 3. Sum across all rows.
# 4. Edge cases:
#    - Row is all non-negative → contribute 0
#    - Row is empty → skip

# -----------------------------------------------------------
# ⏱ Time Complexity:   O(m * log n)
# 💾 Space Complexity: O(1)
# -----------------------------------------------------------

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def count_negatives_in_row(row):
            """Binary search to count negatives in a sorted row."""
            n = len(row)
            if n == 0 or row[-1] >= 0:
                return 0

            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            # left points to the first negative number
            return n - left

        total = 0
        for row in grid:
            total += count_negatives_in_row(row)

        return total


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    grid1 = [
        [4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3]
    ]
    print(sol.countNegatives(grid1))  # Expected Output: 8

    grid2 = [
        [3, 2],
        [1, 0]
    ]
    print(sol.countNegatives(grid2))  # Expected Output: 0
