"""
===========================================================
3329. Count Substrings With K-Frequency Characters II
===========================================================

🧩 Problem:
Given a string `s` and an integer `k`, return the total number of 
non-empty **substrings** of `s` where **at least one character** appears 
**at least `k` times**.

In other words, count all substrings where there exists some character 
with frequency ≥ k.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "abacb", k = 2
Output: 4
Explanation:
The valid substrings are:
* "aba"  (character 'a' appears 2 times)
* "abac" (character 'a' appears 2 times)
* "abacb" (character 'a' appears 2 times)
* "bacb" (character 'b' appears 2 times) :contentReference[oaicite:0]{index=0}

Example 2:
Input:  s = "abcde", k = 1
Output: 15
Explanation:
Every substring is valid because each character appears ≥1 time. :contentReference[oaicite:1]{index=1}

-----------------------------------------------------------
🎯 Goal:
For each substring of `s`, check if there exists **any character** whose 
frequency in that substring is >= k, and count all such substrings.

-----------------------------------------------------------
Algorithm — Sliding Window:
-----------------------------------------------------------

We count **valid substrings ending at each right pointer**.  
Use two pointers (`left` and `right`) and a frequency array `count[]`:

1. Initialize `left = 0`, answer `ans = 0`, and a frequency array `count[26] = {0}`.
2. Expand the `right` pointer through the string.
   * Increment frequency of `s[right]`.
3. While the frequency of `s[right]` is **≥ k**:
   * All substrings starting at `left` and ending from `right`..end are valid,
     so add `(n - right)` to `ans`.
   * Decrement frequency of `s[left]` and increment `left`.
4. Continue until `right` reaches the end.
5. Return `ans`.

Key idea:
Once we detect a character’s frequency ≥ k inside the current window 
[`left..right`], any extension of that window to the right still contains 
that frequency, so we can count all such substrings at once. :contentReference[oaicite:2]{index=2}

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n) — the `left` pointer and `right` pointer each traverse the string at most once.

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1) (constant space for frequency array of size 26)

-----------------------------------------------------------
"""
# ------------------------------------
# 3329. Count Substrings With K-Frequency Characters II
# Sliding Window — Two Pointers
# ------------------------------------

class Solution(object):
    def countSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        count = [0] * 26
        ans = 0
        left = 0

        for right in range(n):
            idx = ord(s[right]) - ord('a')
            count[idx] += 1

            # while this character's frequency reaches >= k
            while count[idx] >= k:
                # all substrings from left to end with this right are valid
                ans += (n - right)
                # shrink window
                count[ord(s[left]) - ord('a')] -= 1
                left += 1

        return ans


# ------------------------------------
# Driver Test
# ------------------------------------
sol = Solution()
print(sol.countSubstrings("abacb", 2))  # Expected: 4
print(sol.countSubstrings("abcde", 1))  # Expected: 15
print(sol.countSubstrings("aaabb", 2))  # Expected: ?
