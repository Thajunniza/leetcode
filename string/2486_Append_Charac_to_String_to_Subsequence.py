"""
===========================================================
2486. Append Characters to String
===========================================================

🧩 Problem:
You are given two strings **s** and **t**.
Your task is to determine the **minimum number of characters** you must append 
to the end of **s** so that **t becomes a subsequence of s**.

A subsequence means:
Characters of t must appear in s **in the same order**, but not necessarily contiguously.

-----------------------------------------------------------
Example:
-----------------------------------------------------------

Example 1:
Input:
    s = "coaching"
    t = "coding"
Output:
    4
Explanation:
    Current subsequence matched: "co" → "co"
    Remaining characters: "ding" → need to append 4 chars.

Example 2:
Input:
    s = "abc"
    t = "abc"
Output:
    0
Explanation:
    Already a subsequence.

Example 3:
Input:
    s = "abc"
    t = "abcd"
Output:
    1
Explanation:
    Missing only 'd'.

-----------------------------------------------------------
🎯 Goal:
Find how many characters from **t** are NOT present as a subsequence in **s**, 
and append them.

===========================================================
✅ Two-Pointer Approach (Optimal)
===========================================================

We use two pointers:
- **p** → walks through `s`
- **q** → walks through `t`

Whenever `s[p] == t[q]`, we move q (meaning we matched one character of t).
Always move p to continue scanning s.

At the end:
- `q` = number of matched characters
- answer = `len(t) - q`

-----------------------------------------------------------
⏱️ Time Complexity:  O(n1 + n2)
📦 Space Complexity: O(1)
-----------------------------------------------------------

===========================================================
💡 Python Solution
===========================================================

```python
"""

def appendCharacters(s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        p = 0  # pointer for s
        q = 0  # pointer for t
        n1 = len(s)
        n2 = len(t)

        # Match as many chars of t inside s as possible
        while p < n1 and q < n2:
            if s[p] == t[q]:
                q += 1
            p += 1

        # Remaining unmatched chars in t
        return n2 - q



# -------------------------------------------------
# Driver Test
# -------------------------------------------------
if __name__ == "__main__":
    print(appendCharacters("coaching", "coding"))  # 4
    print(appendCharacters("abcde", "a"))          # 0
    print(appendCharacters("z", "abc"))            # 3
    print(appendCharacters("abc", "abc"))          # 0
    print(appendCharacters("ab", "baba"))          # 2
