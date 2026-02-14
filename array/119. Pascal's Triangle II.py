"""
===========================================================
119. Pascal's Triangle II
===========================================================

Return the rowIndex-th row (0-indexed) of Pascal’s Triangle.

Approach:
Build each row iteratively from the previous row by
distributing values to the next row.

Time Complexity:  O(n^2)
Space Complexity: O(n)
===========================================================
"""


# ------------------------------------
# Solution: Pascal's Triangle II
# ------------------------------------
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]

        for i in range(rowIndex):
            n = len(res) + 1
            curr = [0] * n

            for j in range(len(res)):
                curr[j] += res[j]
                curr[j + 1] += res[j]

            res = curr

        return res


# ------------------------------------
# Driver Tests
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.getRow(0))  # [1]
    print(sol.getRow(1))  # [1, 1]
    print(sol.getRow(3))  # [1, 3, 3, 1]
    print(sol.getRow(4))  # [1, 4, 6, 4, 1]
