# ===========================================================
# 2965 - Find Missing and Repeated Number in 2D Grid
# ===========================================================

# 🧩 Problem:
# Given an n x n grid containing numbers from 1 to n^2, exactly
# one number is missing and exactly one number is repeated.  
# Find the repeated and missing numbers.

# 🎯 Goal:
# Return a list: [repeated, missing]

# -----------------------------------------------------------
# Examples:
# -----------------------------------------------------------

# Input:  grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 8]
# ]
# Output: [8, 9]

# Input:  grid = [
#     [1, 1],
#     [3, 4]
# ]
# Output: [1, 2]

# -----------------------------------------------------------
# Algorithm — Hashmap (Simple Approach):
# -----------------------------------------------------------
# 1. Initialize a dictionary `count_map` to count occurrences.
# 2. Iterate over each number in the grid:
#        count_map[num] += 1
# 3. Iterate from 1 to n^2:
#    a. If number not in map → missing
#    b. If count > 1 → repeated
# 4. Return [repeated, missing]

# ⏱ Time Complexity:   O(n^2)  
# 💾 Space Complexity:  O(n^2)

# -----------------------------------------------------------
# Algorithm — XOR (Optimal O(1) Space):
# -----------------------------------------------------------
# 1. Compute XOR of all numbers in the grid and 1..n^2:
#        xorAll = repeated ^ missing
# 2. Find rightmost set bit in xorAll.
# 3. Partition numbers into two groups by this bit and XOR separately.
# 4. You will get two values → one repeated, one missing.
# 5. Check grid to determine which is repeated.

# ⏱ Time Complexity:   O(n^2)  
# 💾 Space Complexity:  O(1)
# -----------------------------------------------------------


# ------------------------------------
# Solution 1: Hashmap
# ------------------------------------
class SolutionHashmap(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        count_map = {}
        n = len(grid)
        missing = -1
        repeated = -1

        # Count occurrences
        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                count_map[val] = count_map.get(val, 0) + 1

        # Find missing and repeated numbers
        for i in range(1, n*n + 1):
            if i not in count_map:
                missing = i
            elif count_map[i] > 1:
                repeated = i

        return [repeated, missing]


# ------------------------------------
# Solution 2: XOR (O(1) Space)
# ------------------------------------
class SolutionXOR(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        total_numbers = n * n
        xorAll = 0

        # Step 1: XOR all grid numbers
        for i in range(n):
            for j in range(n):
                xorAll ^= grid[i][j]

        # XOR with numbers from 1 to n^2
        for i in range(1, total_numbers + 1):
            xorAll ^= i

        # Step 2: Find rightmost set bit
        set_bit = xorAll & -xorAll

        # Step 3: Divide into two groups and XOR
        x = 0  # candidate 1
        y = 0  # candidate 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] & set_bit:
                    x ^= grid[i][j]
                else:
                    y ^= grid[i][j]

        for i in range(1, total_numbers + 1):
            if i & set_bit:
                x ^= i
            else:
                y ^= i

        # Step 4: Determine repeated and missing
        for i in range(n):
            for j in range(n):
                if grid[i][j] == x:
                    return [x, y]
                if grid[i][j] == y:
                    return [y, x]

        return [-1, -1]  # fallback


# ------------------------------------
# Driver Tests
# ------------------------------------
if __name__ == "__main__":
    grid1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 8]
    ]

    grid2 = [
        [1, 1],
        [3, 4]
    ]

    print("Hashmap Solution:")
    sol1 = SolutionHashmap()
    print(sol1.findMissingAndRepeatedValues(grid1))  # Output: [8, 9]
    print(sol1.findMissingAndRepeatedValues(grid2))  # Output: [1, 2]

    print("\nXOR Solution:")
    sol2 = SolutionXOR()
    print(sol2.findMissingAndRepeatedValues(grid1))  # Output: [8, 9]
    print(sol2.findMissingAndRepeatedValues(grid2))  # Output: [1, 2]
