"""
===========================================================
187. Repeated DNA Sequences
===========================================================

🧩 Problem:
DNA sequences are composed of the characters `'A'`, `'C'`, `'G'`, and `'T'`.

Given a string `s` representing a DNA sequence, find all the
**10-letter-long substrings** that occur **more than once**.

🎯 Goal:
Return all repeated 10-character-long DNA sequences.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]

Example 2:
Input:  s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

-----------------------------------------------------------
Algorithm — Sliding Window + HashSet:
-----------------------------------------------------------

Maintain a sliding window of fixed length 10.

1. Use a set `seen` to store DNA substrings already encountered.
2. Use a set `result` to store substrings that appear more than once.
3. Initialize two pointers:
   - `left = 0`
   - `right = 10`
4. While `right <= len(s)`:
   - Extract substring `s[left:right]`
   - If substring is already in `seen`, add it to `result`
   - Otherwise, add it to `seen`
   - Move both pointers one step forward
5. Return all elements from `result`

Key idea:
A fixed-size sliding window allows checking overlapping substrings efficiently.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)  
(each 10-length substring is processed once)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(n)  
(sets store up to O(n) substrings)

-----------------------------------------------------------
"""
# ------------------------------------
# 187. Repeated DNA Sequences
# Sliding Window + HashSet
# ------------------------------------

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        result = set()

        left = 0
        right = 10

        while right <= len(s):
            seq = s[left:right]
            if seq in seen:
                result.add(seq)
            else:
                seen.add(seq)
            left += 1
            right += 1

        return list(result)


# ------------------------------------
# Driver Test
# ------------------------------------

sol = Solution()
print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
# Expected: ["AAAAACCCCC", "CCCCCAAAAA"]

print(sol.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
# Expected: ["AAAAAAAAAA"]

print(sol.findRepeatedDnaSequences(""))
# Expected: []

