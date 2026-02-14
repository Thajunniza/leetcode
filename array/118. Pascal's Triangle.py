"""
===========================================================
118. Pascal's Triangle
===========================================================

🧩 Problem:
Given an integer `numRows`, return the first `numRows` of
Pascal’s Triangle.

In Pascal’s Triangle:
- The first row is [1]
- Each row starts and ends with 1
- Each inner element is the sum of the two elements above it

Mathematically:
    triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

🎯 Goal:
Return a 2D list containing the first `numRows` rows.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Input:  numRows = 1  
Output: [[1]]

Input:  numRows = 5  
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

-----------------------------------------------------------
Algorithm — Build Using Previous Row:
-----------------------------------------------------------
1. Initialize result list `res`.

2. Iterate from row index 0 to numRows - 1.

3. For each row `i`:
   a. Create a list of size (i + 1) filled with 1s.
   b. For positions 1 to i-1:
          row[j] = res[i-1][j-1] + res[i-1][j]

4. Append the row to result.

5. Return result.

-----------------------------------------------------------
⏱ Time Complexity:   O(n²)
    Total elements = n(n+1)/2

💾 Space Complexity: O(n²)
    We store the full triangle
-----------------------------------------------------------
"""
class Solution:
    def generate(self, numRows: int):
        res = []

        for i in range(numRows):
            # Create row filled with 1s
            row = [1] * (i + 1)

            # Fill inner values
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]

            res.append(row)

        return res
# ------------------------------------
# Driver Tests
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(1))
    print(sol.generate(5))
