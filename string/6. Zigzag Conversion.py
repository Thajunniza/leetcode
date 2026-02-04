"""
6 - ZigZag Conversion

Description:
Convert a string s into a zigzag pattern across numRows and read row by row to form a new string.

Example:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Approach:
- Use a list of strings, one per row.
- Traverse s, appending characters to the current row.
- Change direction when reaching the top or bottom.
- Join all rows at the end to get the result.

Time Complexity:
O(n) - Each character is processed once.

Space Complexity:
O(n) - Storing characters in rows.
"""

class Solution(object):
    def convert(self, s, numRows):
        if numRows <= 1 or len(s) <= numRows:
            return s

        rows = [""] * numRows
        i, direction = 0, 1

        for c in s:
            rows[i] += c
            if i == 0: direction = 1
            if i == numRows - 1: direction = -1
            i += direction

        return "".join(rows)

# -------------------- Test Cases --------------------

def test_convert():
    sol = Solution()
    assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert sol.convert("PAYPALISHIRING", 1) == "PAYPALISHIRING"
    assert sol.convert("ABC", 5) == "ABC"
    assert sol.convert("", 3) == ""
    assert sol.convert("ABCD", 2) == "ACBD"
    print("All test cases passed.")

if __name__ == "__main__":
    test_convert()
