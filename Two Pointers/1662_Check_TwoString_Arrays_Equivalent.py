""" 
===========================================================
1662. Check If Two String Arrays are Equivalent
===========================================================

🧩 Problem:
You are given two string arrays `word1` and `word2`.

A string `s` is formed by concatenating all the strings in `word1` in order.  
A string `t` is formed by concatenating all the strings in `word2` in order.

Your task:
Return `True` if `s` and `t` are **the same string**, otherwise return `False`.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]

Process:
    s = "ab" + "c"   = "abc"
    t = "a" + "bc"   = "abc"

Output:
    True


Example 2:
Input:
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]

Process:
    s = "a" + "cb"   = "acb"
    t = "ab" + "c"   = "abc"

Output:
    False


Example 3:
Input:
    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]

Process:
    s = "abc" + "d" + "defg" = "abcddefg"
    t = "abcddefg"

Output:
    True

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Determine whether the **concatenation** of all strings in `word1`
is **exactly equal** to the concatenation of all strings in `word2`.

You should aim for:
- Time: O(total characters)
- Space: O(1) extra (streaming / pointer solution)

Pattern / Folder:
    • Pattern: Two Pointers, String Streaming
    • Folder suggestion:
        /TwoPointers/1662-CheckIfStringArraysAreEquivalent/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

Naive way:
- Build `s = "".join(word1)`
- Build `t = "".join(word2)`
- Compare `s == t`

This works but:
- Uses extra space proportional to total string length.

Optimized way (your approach 👍):
- Treat `word1` and `word2` like **streams of characters**
- Use pointers to walk them in parallel **without creating the full strings**.

Use:
- `w1` → index of current string in `word1`
- `w2` → index of current string in `word2`
- `i`  → index of current character in `word1[w1]`
- `j`  → index of current character in `word2[w2]`

At each step:
- Compare `word1[w1][i]` and `word2[w2][j]`
- If they differ → return False
- Move `i` and `j` forward
- If we reach end of `word1[w1]`, move to `w1 + 1`, reset `i = 0`
- If we reach end of `word2[w2]`, move to `w2 + 1`, reset `j = 0`

At the end:
- Both streams must be fully consumed at the same time:
    • `w1 == len(word1)` and `w2 == len(word2)`

-----------------------------------------------------------
🧠 Algorithm (Two Pointers – Streaming Comparison):
-----------------------------------------------------------

1. Initialize:
       w1 = 0   # index into word1 array
       w2 = 0   # index into word2 array
       i = 0    # char index in word1[w1]
       j = 0    # char index in word2[w2]

2. While w1 < len(word1) and w2 < len(word2):
       if word1[w1][i] != word2[w2][j]:
           return False

       # move character pointers
       i += 1
       j += 1

       # if we've reached end of current string in word1
       if i == len(word1[w1]):
           w1 += 1
           i = 0

       # if we've reached end of current string in word2
       if j == len(word2[w2]):
           w2 += 1
           j = 0

3. After loop:
       # both must be fully consumed
       if w1 != len(word1) or w2 != len(word2):
           return False

4. Otherwise:
       return True

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

Let:
    N1 = total number of characters in word1
    N2 = total number of characters in word2

- Time Complexity:  **O(N1 + N2)**
  We scan each character at most once.

- Space Complexity: **O(1)**
  We only use a few indices, no extra strings or arrays.

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        LeetCode 1662. Check If Two String Arrays are Equivalent

        Compare the arrays as continuous character streams
        using O(1) extra space.
        """
        w1 = 0  # index for word1 array
        w2 = 0  # index for word2 array
        i = 0   # index inside word1[w1]
        j = 0   # index inside word2[w2]

        # Compare characters while both arrays still have words
        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][i] != word2[w2][j]:
                return False

            i += 1
            j += 1

            # Move to next string in word1 if needed
            if i == len(word1[w1]):
                w1 += 1
                i = 0

            # Move to next string in word2 if needed
            if j == len(word2[w2]):
                w2 += 1
                j = 0

        # Both must be fully consumed for strings to be equal
        if w1 != len(word1) or w2 != len(word2):
            return False

        return True


# ▶️ TEST HERE
if __name__ == "__main__":
    S = Solution()

    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(S.arrayStringsAreEqual(word1, word2))   # Expected: True

    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    print(S.arrayStringsAreEqual(word1, word2))   # Expected: False

    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    print(S.arrayStringsAreEqual(word1, word2))   # Expected: True

