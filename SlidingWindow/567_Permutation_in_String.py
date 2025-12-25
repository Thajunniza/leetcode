"""
===========================================================
567. Permutation in String
===========================================================

🧩 Problem:
Given two strings `s1` and `s2`, return `True` if `s2`
contains a permutation of `s1` as a substring.
Otherwise, return `False`.

In other words, check whether any substring of `s2`
is a rearrangement of `s1`.

🎯 Goal:
Determine if a substring of `s2` exists with:
- Same length as `s1`
- Same character frequencies as `s1`

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s1 = "ab", s2 = "eidbaooo"
Output: True
Explanation: Substring "ba" is a permutation of "ab"

Example 2:
Input:  s1 = "ab", s2 = "eidboaoo"
Output: False
Explanation: No permutation of "ab" exists in s2

Example 3:
Input:  s1 = "adc", s2 = "dcda"
Output: True
Explanation: Substring "dcd" rearranged gives "adc"

-----------------------------------------------------------
Algorithm — Sliding Window + Frequency Map:
-----------------------------------------------------------

Maintain a sliding window [left .. right] over `s2`
that tries to match the character frequencies of `s1`.

1. Build a frequency map `have` for characters in `s1`.
2. Use a dictionary `seen` to track current window counts.
3. Expand `right` across `s2`:
   - If `s2[right]` is NOT in `have`:
       → Reset window (clear `seen`, move `left`)
   - Else:
       → Add char to `seen`
       → While frequency exceeds required:
           Shrink window from the left
4. If window length equals `len(s1)`:
   → A permutation is found → return True
5. If traversal completes, return False

Key idea:
Only shrink when a character exceeds its allowed frequency.
Reset completely when encountering invalid characters.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)  (each character processed at most twice)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(k)  (k = number of unique characters in s1)

-----------------------------------------------------------
"""
# ------------------------------------
# 567. Permutation in String
# Sliding Window + Frequency Map
# ------------------------------------

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False

        # Frequency map for s1
        have = {}
        for c in s1:
            have[c] = have.get(c, 0) + 1

        seen = {}
        left = 0

        for right, ch in enumerate(s2):

            # Valid character
            if ch in have:
                seen[ch] = seen.get(ch, 0) + 1

                # Shrink window if frequency exceeds
                while seen[ch] > have[ch]:
                    leftch = s2[left]
                    seen[leftch] -= 1
                    if seen[leftch] == 0:
                        del seen[leftch]
                    left += 1

                # Check exact window size
                if right - left + 1 == l1:
                    return True

            # Invalid character → reset window
            else:
                seen.clear()
                left = right + 1

        return False


# ------------------------------------
# Driver Test
# ------------------------------------

sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo"))  # Expected: True
print(sol.checkInclusion("ab", "eidboaoo"))  # Expected: False
print(sol.checkInclusion("adc", "dcda"))     # Expected: True
print(sol.checkInclusion("a", "a"))          # Expected: True
