"""
===========================================================
302. Smallest Rectangle Enclosing Black Pixels
===========================================================

Problem:
--------
You are given a binary image where '1' represents black pixels
and '0' represents white pixels. You are also given the location
(x, y) of one black pixel.

Find the area of the smallest axis-aligned rectangle that encloses
all black pixels.

Constraints:
------------
- All black pixels are connected
- Image is non-empty
- image[i][j] is a string: "0" or "1"

Time Complexity:
----------------
O(m log n + n log m)

Space Complexity:
-----------------
O(1) extra space

Algorithm (Binary Search):
--------------------------
1. Binary search top boundary (first row containing black)
2. Binary search bottom boundary (last row containing black)
3. Binary search left boundary (first column containing black)
4. Binary search right boundary (last column containing black)
5. Area = (bottom - top + 1) * (right - left + 1)

Author:
-------
Thajunniza M A
"""

# -----------------------------
# Solution Class
# -----------------------------
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m = len(image)
        n = len(image[0])

        # -----------------------------
        # Helper Functions
        # -----------------------------
        def is_black_row(row):
            for col in range(n):
                if image[row][col] == "1":
                    return True
            return False

        def is_black_col(col):
            for row in range(m):
                if image[row][col] == "1":
                    return True
            return False

        # -----------------------------
        # Binary Searches
        # -----------------------------
        def find_top():
            t, b = 0, x
            while t < b:
                mid = (t + b) // 2
                if is_black_row(mid):
                    b = mid
                else:
                    t = mid + 1
            return t

        def find_bottom():
            t, b = x, m - 1
            while t < b:
                mid = (t + b + 1) // 2
                if is_black_row(mid):
                    t = mid
                else:
                    b = mid - 1
            return t

        def find_left():
            l, r = 0, y
            while l < r:
                mid = (l + r) // 2
                if is_black_col(mid):
                    r = mid
                else:
                    l = mid + 1
            return l

        def find_right():
            l, r = y, n - 1
            while l < r:
                mid = (l + r + 1) // 2
                if is_black_col(mid):
                    l = mid
                else:
                    r = mid - 1
            return l

        # -----------------------------
        # Compute Area
        # -----------------------------
        top = find_top()
        bottom = find_bottom()
        left = find_left()
        right = find_right()

        return (bottom - top + 1) * (right - left + 1)


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":
    sol = Solution()

    image = [
        ["0","0","1","0"],
        ["0","1","1","0"],
        ["0","1","0","0"]
    ]

    x, y = 0, 2

    print("Minimum Area:", sol.minArea(image, x, y))
    # Expected Output: 6
