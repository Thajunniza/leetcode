"""
===========================================================
696. Count Binary Substrings
===========================================================

🧩 Problem:
Given a binary string s,
return the number of non-empty substrings that:

1. Have the same number of 0s and 1s.
2. All 0s and all 1s in the substring are grouped consecutively.

-----------------------------------------------------------
Approach — Group Counting (Run Length Encoding Insight)
-----------------------------------------------------------

Key idea:
Valid substrings are formed between two consecutive
groups of different characters.

If we compute the size of each consecutive group,
for every adjacent pair:

    count += min(previous_group_size, current_group_size)

Example:
s = "00110011"

Groups → [2, 2, 2, 2]

Valid substrings =
min(2,2) + min(2,2) + min(2,2)
= 2 + 2 + 2 = 6

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

class Solution(object):
    def countBinarySubstrings(self, s):
        prev = 0      # previous group length
        curr = 1      # current group length
        res = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                res += min(prev, curr)
                prev = curr
                curr = 1

        # Add last pair
        res += min(prev, curr)

        return res


# ==========================
# ✅ Test Cases
# ==========================
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("00110011", 6),
        ("10101", 4),
        ("000111", 3),
        ("01", 1),
        ("0000", 0),
    ]

    for s, expected in test_cases:
        result = sol.countBinarySubstrings(s)
        print("Input:     ", s)
        print("Output:    ", result)
        print("Expected:  ", expected)
        print("Pass:      ", result == expected)
        print("-" * 40)
