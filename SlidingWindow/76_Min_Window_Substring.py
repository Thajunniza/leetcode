"""
===========================================================
76. Minimum Window Substring
===========================================================

🧩 Problem:
Given two strings `s` and `t`, return the **minimum window substring**
of `s` such that every character in `t` (including duplicates)
is included in the window.

If no such substring exists, return an empty string "".

🎯 Goal:
Return the **smallest substring** of `s` that contains all characters
of `t` with correct frequencies.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input:  s = "a", t = "a"
Output: "a"

Example 3:
Input:  s = "a", t = "aa"
Output: ""

-----------------------------------------------------------
Algorithm — Sliding Window + Frequency Maps:
-----------------------------------------------------------

Maintain a window [left .. right] that expands and shrinks.

1. Build `need` map with character frequencies from `t`
2. Use `have` map to track current window frequencies
3. Track:
   - `required` = number of distinct characters in `t`
   - `count` = how many characters currently meet required frequency
4. Expand `right`:
   - Add s[right] to `have`
   - If have[ch] == need[ch], increment count
5. While window is valid (count == required):
   - Update minimum window
   - Shrink from the left
   - If a required character falls below need, decrement count
6. Return the best window found

Key idea:
Expand until valid, then shrink to get the smallest valid window.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(|t|)

-----------------------------------------------------------
"""
# ------------------------------------
# 76. Minimum Window Substring
# Sliding Window + Frequency Maps
# ------------------------------------

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        need = {}
        have = {}
        count = 0

        # build frequency map for t
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
                have[c] = 0

        required = len(need)
        left = 0
        minlen = float("inf")
        result = ""

        for right, c in enumerate(s):
            if c in need:
                have[c] += 1
                if have[c] == need[c]:
                    count += 1

            # shrink window while valid
            while count == required:
                currlen = right - left + 1
                if currlen < minlen:
                    minlen = currlen
                    result = s[left:right + 1]

                val = s[left]
                if val in need:
                    have[val] -= 1
                    if have[val] < need[val]:
                        count -= 1

                left += 1

        return result


# ------------------------------------
# Driver Test
# ------------------------------------

if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))  # Expected: "BANC"
    print(sol.minWindow("a", "a"))                # Expected: "a"
    print(sol.minWindow("a", "aa"))               # Expected: ""
    print(sol.minWindow("aa", "aa"))              # Expected: "aa"
