"""
===========================================================
49. Group Anagrams
===========================================================

🧩 Problem:
Given an array of strings `strs`, group the **anagrams** together.  
Return a list of lists, where each inner list contains words that are anagrams of each other.

🎯 Goal:
Words are anagrams if, after sorting their characters, they become identical.  
Use that property to group them efficiently.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Input:
strs = ["eat","tea","tan","ate","nat","bat"]

Output (order may vary):
[
  ["eat","tea","ate"],
  ["tan","nat"],
  ["bat"]
]

Input:
strs = [""]
Output:
[[""]]

Input:
strs = ["a"]
Output:
[["a"]]

-----------------------------------------------------------
Algorithm — Sorted String as Key (Clean & Reliable):
-----------------------------------------------------------

Core Idea:
Two strings are anagrams iff their **sorted characters** are the same.  
Use the sorted string as a **hash map key**:

Steps:
1. Initialize a dictionary `group = {}` mapping `sorted_string -> list_of_words`
2. For each word `s` in `strs`:
   - Compute `key = "".join(sorted(s))`
   - Append `s` to `group[key]`
3. Return `group.values()` as the grouped anagrams

This approach is simple and supports any characters (Unicode-safe).

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Let:
- `n` = number of strings
- `m` = average length of a string

Time:  **O(n · m log m)** (sorting each string)  
Space: **O(n · m)** (storing keys and grouped strings)

===========================================================
"""

# -------------------------------
# Python: Group Anagrams (sorted key)
# -------------------------------
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            key = "".join(sorted(s))  # canonical form of the anagram
            if key in group:
                group[key].append(s)
            else:
                group[key] = [s]
        return list(group.values())


# ------------------------------------
# Driver Tests
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # Expected (order may vary): [["eat","tea","ate"], ["tan","nat"], ["bat"]]

    print(sol.groupAnagrams([""]))
    # [[""]]

    print(sol.groupAnagrams(["a"]))
    # [["a"]]
