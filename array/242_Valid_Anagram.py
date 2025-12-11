"""
===========================================================
242. Valid Anagram
===========================================================

🧩 Problem:
Given two strings `s` and `t`, return **True** if `t` is an anagram of `s`, and **False** otherwise.

An **anagram** is formed by rearranging the letters of another string, using all original letters exactly once.

You must support:
    - Works efficiently for lowercase English letters ('a'–'z')

❗ Assumptions (per LeetCode constraints):
    • `s` and `t` consist of lowercase English letters
    • Length up to 50,000

🎯 Goal:
Determine whether two strings have **identical character counts**.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Input:
s = "anagram", t = "nagaram"
Output: True

Input:
s = "rat", t = "car"
Output: False

Input:
s = "a", t = "ab"
Output: False

-----------------------------------------------------------
Algorithm — ASCII Count Array (Best for 'a'–'z'):
-----------------------------------------------------------

Core Idea:
Use a fixed array of size 26 (for letters 'a'–'z') and map each character
to an index via its ASCII value: `idx = ord(ch) - ord('a')`.

Steps:
1. If lengths differ, return False
2. Initialize `counts = [0] * 26`
3. For each position i:
     - counts[ord(s[i]) - ord('a')] += 1
     - counts[ord(t[i]) - ord('a')] -= 1
4. If all counts are zero, strings are anagrams

This guarantees matching frequencies for all letters.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time:  O(n) — single pass through both strings  
Space: O(1) — fixed size array (26), independent of input length

(Note: “Auxiliary space” is O(1); total space including input strings is O(n))

-----------------------------------------------------------
Edge Cases:
-----------------------------------------------------------
- Different lengths → immediately False
- Empty strings "" and "" → True
- Non-lowercase characters? (Not allowed by constraints; use a dictionary/Counter if needed)

===========================================================
"""


# -------------------------------
# Python: ASCII Array Approach
# -------------------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1) Length check prevents index errors
        if len(s) != len(t):
            return False

        # 2) Fixed-size counts for 'a'..'z'
        counts = [0] * 26

        # 3) Single pass: increment for s, decrement for t
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1

        # 4) All must return to zero
        return all(c == 0 for c in counts)


# ------------------------------------
# Driver Tests
# ------------------------------------
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))  # True
print(sol.isAnagram("rat", "car"))          # False
print(sol.isAnagram("", ""))                # True
print(sol.isAnagram("a", "a"))              # True
print(sol.isAnagram("abc", "ab"))           # False
