"""
===========================================================
424. Longest Repeating Character Replacement
===========================================================

🧩 Problem:
You are given a string `s` (uppercase English letters) and an integer `k`.

You can choose any character and replace it with any other character
at most `k` times.

Find the length of the longest substring that can be made of the same
character after at most `k` replacements.

🎯 Goal:
Return the maximum length of such a substring.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with 'B' (or two 'B's with 'A') → "BBBB"

Example 2:
Input:  s = "AABABBA", k = 1
Output: 4
Explanation: "AABA" or "ABBA" can be made all one character with 1 replacement.

-----------------------------------------------------------
Algorithm — Sliding Window + Frequency Map:
-----------------------------------------------------------

Maintain a window [left .. right] and character counts inside it.

1. Use a dictionary `freq` to store counts of characters in the window.
2. Track `maxCount` = the maximum frequency of a single character in the window.
3. For each `right`:
   - Add s[right] to freq and update maxCount
   - If window_len - maxCount > k, shrink from the left until valid:
       → decrement freq[s[left]]
       → left += 1
4. Update best length after each step.

Key idea:
A window is valid if the number of characters to replace
(window_len - maxCount) is ≤ k.

Note:
We do NOT recompute maxCount when shrinking; this is safe and keeps O(n).

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1)  (bounded by alphabet size, typically 26)

-----------------------------------------------------------
"""
# ------------------------------------
# 424. Longest Repeating Character Replacement
# Sliding Window + Frequency Map
# ------------------------------------

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        freq = {}
        maxCount = 0
        best = 0

        for right, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            maxCount = max(maxCount, freq[ch])

            while (right - left + 1) - maxCount > k:
                freq[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best


# ------------------------------------
# Driver Test
# ------------------------------------

sol = Solution()
print(sol.characterReplacement("ABAB", 2))      # Expected: 4
print(sol.characterReplacement("AABABBA", 1))   # Expected: 4
print(sol.characterReplacement("", 3))          # Expected: 0
print(sol.characterReplacement("AAAA", 0))      # Expected: 4
print(sol.characterReplacement("ABCDE", 1))     # Expected: 2
