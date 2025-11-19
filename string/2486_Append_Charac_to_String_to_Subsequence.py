"""
===========================================================
2486. Append Characters to String to Make Subsequence
===========================================================

🧩 Problem:
You are given two strings `s` (source) and `t` (target).

In one operation, you may append **any character from `t`** to the end of `s`.

Return the **minimum number of characters** that must be appended to `s`
so that `t` becomes a **subsequence** of `s`.

A subsequence keeps the relative order of letters but may skip characters.

🎯 Goal:
Match as many characters of `t` as possible inside `s` from left to right.
Whatever part of `t` cannot be matched must be appended.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:
    s = "coaching"
    t = "coding"
Output: 4
Explanation:
    Matched inside s → "c", "o"
    Unmatched part → "ding" → append 4 characters

Example 2:
Input:
    s = "abcde"
    t = "a"
Output: 0
Explanation:
    "a" is already a subsequence.

Example 3:
Input:
    s = "z"
    t = "abc"
Output: 3
Explanation:
    No characters matched. Need to append all "abc".

Example 4:
Input:
    s = "abc"
    t = "abc"
Output: 0
Explanation:
    Entire target already matched.

-----------------------------------------------------------
Algorithm — Two Pointers (Greedy Match):
-----------------------------------------------------------
1. Use pointer `p` on `s` and loop pointer `q` on `t`.

2. For each character t[q]:
       Scan forward in s starting from p:
            - While p < len(s) and s[p] != t[q]:
                  p += 1

       - If p reaches end → cannot match t[q] → 
         Remaining characters of t must be appended:
             return len(t) - q

       - Else: we matched t[q] → p += 1

3. If the whole t is matched:
       return 0

-----------------------------------------------------------
⏱ Time Complexity:   O(len(s) + len(t))
💾 Space Complexity:  O(1)
-----------------------------------------------------------

"""

# -------------------------------------------------
# 2486. Append Characters to String to Make Subsequence
# Two Pointers — Greedy Match
# -------------------------------------------------
def appendCharacters(s: str, t: str) -> int:
    """
    Return the minimum number of characters to append to `s`
    so that `t` becomes a subsequence of `s`.

    Args:
        s (str): Source string.
        t (str): Target string.

    Returns:
        int: Number of characters to append.

    Example:
        >>> appendCharacters("coaching", "coding")
        4
    """
    p = 0
    n = len(s)

    for q in range(len(t)):
        # Scan s until we match t[q]
        while p < n and s[p] != t[q]:
            p += 1

        # If no more characters in s, everything from t[q:] must be appended
        if p == n:
            return len(t) - q

        # If matched, move p forward in s
        p += 1

    # All characters matched
    return 0


# -------------------------------------------------
# Driver Test
# -------------------------------------------------
if __name__ == "__main__":
    print(appendCharacters("coaching", "coding"))  # 4
    print(appendCharacters("abcde", "a"))          # 0
    print(appendCharacters("z", "abc"))            # 3
    print(appendCharacters("abc", "abc"))          # 0
    print(appendCharacters("ab", "baba"))          # 2
