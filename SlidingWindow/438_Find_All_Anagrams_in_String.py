""" 
===========================================================
438. Find All Anagrams in a String
===========================================================

🧩 Problem:
Given a string `s` and a pattern `p`, find all start indices 
of `p`'s anagrams in `s`. An anagram uses all letters of `p` exactly once.

🎯 Goal:
Return a list of starting indices where a substring of `s` is an anagram of `p`.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation: Substrings "cba" (index 0) and "bac" (index 6) are anagrams of "abc"

Example 2:
Input:  s = "abab", p = "ab"
Output: [0, 1, 2]
Explanation: Substrings "ab" (0), "ba" (1), "ab" (2) are anagrams

Example 3:
Input:  s = "a", p = "ab"
Output: []
Explanation: Pattern longer than string → no anagrams

-----------------------------------------------------------
Algorithm — Sliding Window + HashMap:
-----------------------------------------------------------

Maintain a sliding window of characters in `s` and track their counts.

1. Build a frequency map `have` for `p`.
2. Initialize `seen` for the current window, `left = 0`, and `count = 0`.
3. Iterate `right` from 0 to len(s)-1:
   - If `s[right]` not in `have`:
       → reset `seen`, `count = 0`, `left = right + 1`
   - Else:
       → Increment `seen[s[right]]`
       → If `seen[s[right]] == have[s[right]]`: increment `count`
       → While `seen[s[right]] > have[s[right]]`: shrink window from left, decrement `count` if needed
   - If `count == number of unique chars in p`, append `left` to result
4. Return result

Key idea:
- Only track counts of characters in `p`
- Use `count` to know when all required letters are fully matched
- Adjust `left` to maintain valid window

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)  (each index visited at most twice)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1) or O(k)  (hashmaps storing letters of `p` and window)

-----------------------------------------------------------
"""
# ------------------------------------
# 438. Find All Anagrams in a String
# Sliding Window + HashMap
# ------------------------------------

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        if len(s) < len(p):
            return result

        # Frequency map for pattern
        have = {}
        for c in p:
            have[c] = have.get(c, 0) + 1

        n = len(have)
        seen = {}
        left = 0
        count = 0

        for right, c in enumerate(s):
            # Reset window if character not in pattern
            if c not in have:
                seen.clear()
                count = 0
                left = right + 1
                continue

            # Expand window
            seen[c] = seen.get(c, 0) + 1
            if seen[c] == have[c]:
                count += 1

            # Shrink window if character exceeds required count
            while seen[c] > have[c]:
                leftval = s[left]
                if seen[leftval] == have[leftval]:
                    count -= 1
                seen[leftval] -= 1
                left += 1

            # Check if current window is valid anagram
            if count == n:
                result.append(left)

        return result

# ------------------------------------
# Driver Test
# ------------------------------------

sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))  # Expected: [0, 6]
print(sol.findAnagrams("abab", "ab"))         # Expected: [0, 1, 2]
print(sol.findAnagrams("a", "ab"))            # Expected: []

