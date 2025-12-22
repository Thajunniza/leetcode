"""
===========================================================
3. Longest Substring Without Repeating Characters
===========================================================

🧩 Problem:
Given a string `s`, find the length of the longest substring
without repeating characters.

🎯 Goal:
Return the maximum length of a substring with all unique characters.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "abcabcbb"
Output: 3
Explanation: Longest substring is "abc" (length 3)

Example 2:
Input:  s = "bbbbb"
Output: 1
Explanation: Longest substring is "b" (length 1)

Example 3:
Input:  s = "pwwkew"
Output: 3
Explanation: Longest substring is "wke" (length 3)
Note: "pwke" is not a substring (not contiguous)

-----------------------------------------------------------
Algorithm — Sliding Window + HashMap (last seen index):
-----------------------------------------------------------

Maintain a window [left .. right] with unique characters.

1. Use a dictionary `last` to store the last index where each character appeared.
2. Expand `right` from 0..n-1:
   - If s[right] was seen AND last[s[right]] >= left:
       → Move left to last[s[right]] + 1 (skip the duplicate)
   - Update last[s[right]] = right
   - Update answer = max(answer, right - left + 1)
3. Return answer

Key idea:
When a duplicate appears, jump `left` forward (never move left backward).

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)  (each index visited at most once)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(min(n, alphabet))  (map of last seen positions)

-----------------------------------------------------------

"""

# ------------------------------------
# 3. Longest Substring Without Repeating Characters
# Sliding Window + Last Seen Index
# ------------------------------------

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = {}
        left = 0
        best = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            best = max(best, right - left + 1)

        return best


# ------------------------------------
# Driver Test
# ------------------------------------

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Expected: 3
print(sol.lengthOfLongestSubstring("bbbbb"))     # Expected: 1
print(sol.lengthOfLongestSubstring("pwwkew"))    # Expected: 3
print(sol.lengthOfLongestSubstring(""))          # Expected: 0
