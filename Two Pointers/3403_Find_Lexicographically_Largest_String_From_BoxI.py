"""
===========================================================
3403. Find the Lexicographically Largest String From the Box I
===========================================================

🧩 Problem:
You are given a string `word` and an integer `numFriends`.

You want to split `word` into exactly `numFriends` non-empty parts (in order).
Each friend gets one part. You can choose which friend's part to keep.

Your task:
- Return the **lexicographically largest string** that any friend can receive.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    word = "dbca"
    numFriends = 2

Max length one friend can get:
    n = 4
    maxLen = n - numFriends + 1 = 3

Possible best parts (length ≤ 3):
    "dbc" (from index 0, length 3)
    "bca" (from index 1, length 3)
    "ca"  (from index 2, shorter)
    "a"   (from index 3, shorter)

Lexicographically largest:
    "dbc"

Output:
    "dbc"

Example 2:
Input:
    word = "aaaz"
    numFriends = 2

maxLen = 4 - 2 + 1 = 3
Candidates starting at each position (length ≤ 3):
    "aaa", "aaz", "az", "z"

Largest:
    "z"

Output:
    "z"

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Return the lexicographically largest substring that can appear as a single
friend’s part when splitting into `numFriends` parts.

-----------------------------------------------------------
Pattern / Folder:
-----------------------------------------------------------

• Pattern: Greedy Scan (String)
• Folder suggestion:
    /Strings/3403-FindLexicographicallyLargestStringFromBoxI/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

Key observation:
- If the maximum character in `word` is `max_char`,
  then the lexicographically largest answer MUST start with `max_char`.
  Any substring starting with a smaller character cannot beat it.

Length constraint:
- When splitting into `numFriends` non-empty parts, the longest possible
  part any single friend can receive is:
      maxLen = n - numFriends + 1

So we only need to:
- Look at indices where word[i] == max_char
- Take candidate = word[i : i + maxLen] (or shorter at end)
- Pick the maximum among those candidates

-----------------------------------------------------------
🧠 Algorithm (Optimized Scan):
-----------------------------------------------------------

1. If numFriends == 1:
       return word

2. Compute:
       n = len(word)
       maxLen = n - numFriends + 1
       max_char = max(word)

3. Initialize best = ""

4. For each index i in [0..n-1]:
       If word[i] == max_char:
            candidate = word[i : i + maxLen]
            best = max(best, candidate)

5. Return best

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time Complexity:
    • O(n * maxLen) worst-case (string compare/slice)
    • With n ≤ 5000, this is acceptable.
- Space Complexity:
    • O(maxLen) due to slicing

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends == 1:
            return word

        n = len(word)
        maxLen = n - numFriends + 1
        max_char = max(word)

        best = ""
        for i, ch in enumerate(word):
            if ch == max_char:
                cand = word[i:i + maxLen]  # safe if i+maxLen > n
                if cand > best:
                    best = cand

        return best


# ▶️ TEST CASES
if __name__ == "__main__":
    S = Solution()

    print(S.answerString("dbca", 2))   # Expected: "dbc"
    print(S.answerString("aaaz", 2))   # Expected: "z"
    print(S.answerString("zzabc", 3))  # Expected: "zza"
    print(S.answerString("abc", 1))    # Expected: "abc"
