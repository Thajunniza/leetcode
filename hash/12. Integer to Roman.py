# ===========================================================
# 12. Integer to Roman
# ===========================================================

# 🧩 Problem:
# Given an integer num, convert it to a Roman numeral.
# Roman numerals are represented by seven different symbols:
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# Special subtractive cases:
# IV (4), IX (9), XL (40), XC (90), CD (400), CM (900)

# Example:
# Input: 3
# Output: "III"
#
# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3
#
# Input: 1994
# Output: "MCMXCIV"

# -----------------------------------------------------------
# Approach — Greedy Decomposition:
# -----------------------------------------------------------
# 1. Maintain a list of (value, symbol) pairs in descending order.
# 2. For each value:
#    - Determine how many times it fits into num.
#    - Append the corresponding symbol that many times.
#    - Reduce num using modulo.
# 3. Continue until num becomes 0.
#
# Greedy works because Roman numerals are constructed using
# the largest possible symbols first.

# -----------------------------------------------------------
# ⏱ Time Complexity:   O(1)
# 💾 Space Complexity: O(1)
# -----------------------------------------------------------

class Solution(object):
    def intToRoman(self, num):
        vals = [
            (1000, "M"),
            (900,  "CM"),
            (500,  "D"),
            (400,  "CD"),
            (100,  "C"),
            (90,   "XC"),
            (50,   "L"),
            (40,   "XL"),
            (10,   "X"),
            (9,    "IX"),
            (5,    "V"),
            (4,    "IV"),
            (1,    "I")
        ]

        ans = ""

        for value, symbol in vals:
            count = num // value
            if count:
                ans += symbol * count
                num %= value

        return ans


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(3))     # Expected Output: "III"
    print(sol.intToRoman(58))    # Expected Output: "LVIII"
    print(sol.intToRoman(1994))  # Expected Output: "MCMXCIV"
