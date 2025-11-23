"""
===========================================================
1768. Merge Strings Alternately
===========================================================

🧩 Problem:
You are given two strings `word1` and `word2`.

You must form a new string by taking characters **alternately** from each string:
- Take word1[0], then word2[0]
- Then word1[1], then word2[1]
- Continue until one string finishes

After one string ends, **append the remaining characters** of the longer string.

Return the merged string.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    word1 = "abc"
    word2 = "pqr"

Process:
    a + p → "ap"
    b + q → "apbq"
    c + r → "apbqcr"

Output:
    "apbqcr"


Example 2:
Input:
    word1 = "ab"
    word2 = "pqrs"

Process:
    a + p → "ap"
    b + q → "apbq"
    leftover from word2 = "rs"

Output:
    "apbqrs"

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Merge two strings by:
- Picking characters alternately from word1 and word2
- Starting at index 0 for both
- Appending remaining characters from the longer string

Pattern / Folder:
    • Pattern: Two Pointers (String)
    • Folder suggestion:
        /TwoPointers/1768-MergeStringsAlternately/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

Use two pointers:
- p → tracks characters of word1
- q → tracks characters of word2

While both have characters:
    append word1[p], append word2[q]
    increment both pointers

When one string ends:
    append the remaining substring of the other string.

This is the easiest version of the two-pointer merge pattern.

-----------------------------------------------------------
🧠 Algorithm (Two Pointer):
-----------------------------------------------------------

1. Initialize:
       p = q = 0
       len1 = len(word1)
       len2 = len(word2)
       result = []

2. While p < len1 and q < len2:
       append word1[p]
       append word2[q]
       p += 1
       q += 1

3. Append leftover characters:
       if p < len1: append word1[p:]
       if q < len2: append word2[q:]

4. Join and return the final string.

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time Complexity:  O(n + m)
- Space Complexity: O(n + m)

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        LeetCode 1768. Merge Strings Alternately

        Args:
            word1 (str)
            word2 (str)

        Returns:
            str: merged string
        """
        p = 0
        q = 0
        len1 = len(word1)
        len2 = len(word2)
        result = []

        # Take characters alternately
        while p < len1 and q < len2:
            result.append(word1[p])
            result.append(word2[q])
            p += 1
            q += 1

        # Append leftover characters
        if p < len1:
            result.append(word1[p:])

        if q < len2:
            result.append(word2[q:])

        return "".join(result)


# ▶️ TEST HERE
if __name__ == "__main__":
    S = Solution()
    print(S.mergeAlternately("abc", "pqr"))      # "apbqcr"
    print(S.mergeAlternately("ab", "pqrs"))      # "apbqrs"
    print(S.mergeAlternately("abcd", "pq"))      # "apbqcd"
