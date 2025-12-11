"""
===========================================================
14. Longest Common Prefix
===========================================================

🧩 Problem:
Given an array of strings `strs`, return the **longest common prefix** (LCP) among them.
If there is no common prefix, return `""`.

🎯 Goal:
Find the longest string that is a prefix of **every** string in `strs`.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Input:
strs = ["flower","flow","flight"]
Output: "fl"

Input:
strs = ["dog","racecar","car"]
Output: ""

Input:
strs = ["interview","interval","internal","internet"]
Output: "inte"

-----------------------------------------------------------
Algorithm — Vertical Scanning (Clean & Efficient):
-----------------------------------------------------------

Core Idea:
Use the **first** string as a reference. For each index `i` and character `ch` in the first string, 
check whether all other strings have the **same character** at position `i`.  
Stop at the first mismatch or when any string ends.

Steps:
1. If `strs` is empty → return `""`.
2. Let `first = strs[0]`.
3. For each index `i` and character `ch` in `first`:
   - For every other string `s` in `strs[1:]`:
       - If `i` is out of bounds for `s` **or** `s[i] != ch` → return `first[:i]`.
4. If the loop finishes, the entire `first` is the common prefix → return `first`.

This approach compares characters **column by column** across all strings.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time:  **O(S)** — where `S` is the sum of all characters across the strings (worst-case).  
Space: **O(1)** — constant extra space.

-----------------------------------------------------------
Edge Cases:
-----------------------------------------------------------
- `[]` → `""`  
- `[""]` → `""`  
- `["a"]` → `"a"`  
- `["ab", "a"]` → `"a"`  
- Prefix ends before the shortest string ends: stop at the shortest length.
"""


# -------------------------------
# Python: Vertical Scanning LCP
# -------------------------------
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first = strs[0]
        for i, ch in enumerate(first):
            for s in strs[1:]:
                if i == len(s) or s[i] != ch:
                    return first[:i]

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))  # "fl"
print(sol.longestCommonPrefix(["dog","racecar","car"]))     # ""
print(sol.longestCommonPrefix(["interview","interval","internal","internet"]))  # "inte"
print(sol.longestCommonPrefix(["ab", "a"]))                 # "a"
print(sol.longestCommonPrefix([]))                          # ""
