""" 
===========================================================
2109. Adding Spaces to a String
===========================================================

🧩 Problem:
You are given:
- a string `s`
- a 0-indexed integer array `spaces` of **strictly increasing** positions

Each `spaces[k]` represents an index in `s` **before which** you must insert a space `" "`.

Return the **resulting string** after inserting all spaces.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    s = "LeetcodeHelpsMeLearn"
    spaces = [8, 13, 15]

Process:
    Insert space before index 8:  "Leetcode HelpsMeLearn"
    Insert space before index 13: "Leetcode Helps MeLearn"
    Insert space before index 15: "Leetcode Helps Me Learn"

Output:
    "Leetcode Helps Me Learn"


Example 2:
Input:
    s = "icodeinpython"
    spaces = [1, 5, 7, 9]

Process:
    "i code in py thon"

Output:
    "i code in py thon"


Example 3:
Input:
    s = "spacing"
    spaces = [0,1,2,3,4,5,6]

Process:
    " s p a c i n g"

Output:
    " s p a c i n g"

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Insert spaces into the string `s` at the specified indices in `spaces`, such that:
- All spaces are added in **one pass** or linear time
- You do **not** repeatedly shift the string (no repeated `.insert()` on arrays)

Pattern / Folder:
    • Pattern: Two Pointers, String Segmentation
    • Folder suggestion:
        /TwoPointers/2109-AddingSpacesToString/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

Instead of inserting spaces directly into the string (which would cause shifting and O(n²) behavior):

1. Treat `spaces` as **cut positions** that split `s` into segments.
2. Build a list `res` of substrings:
    - From index `0` to `spaces[0]`
    - From `spaces[0]` to `spaces[1]`
    - From `spaces[1]` to `spaces[2]`
    - ...
3. After processing all indices in `spaces`, append the **remaining tail** of `s`.
4. Finally, join these segments with `" ".join(res)` — this is equivalent to adding a space before each `spaces[k]`.

We use:
- `i` → current starting index in `s` for the next segment
- `j` → index into the `spaces` array

Since `spaces` is sorted, we can walk both `s` and `spaces` in one pass.

-----------------------------------------------------------
🧠 Algorithm (Segment & Join):
-----------------------------------------------------------

1. Initialize:
       res = []         # list of substrings
       i = 0            # current start in s
       j = 0            # index in spaces
       sLen = len(s)

2. While i < sLen and j < len(spaces):
       # spaces[j] is the index where we want to insert a space BEFORE it.
       res.append(s[i:spaces[j]])   # substring from i to spaces[j]-1
       i = spaces[j]                # move start to this position
       j += 1                       # move to next space position

3. After the loop, if we still have remaining characters in s:
       if i < sLen:
           res.append(s[i:sLen])    # append the remaining tail

4. Join all parts with spaces:
       return " ".join(res)

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

Let:
    n = len(s)
    k = len(spaces)

- Time Complexity:  **O(n + k)**
  - Each character of `s` is part of exactly one slice.
- Space Complexity: **O(n)**
  - For the result list / final string.

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution(object):
    def addSpaces(self, s, spaces):
        """
        LeetCode 2109. Adding Spaces to a String

        Args:
            s (str): original string
            spaces (List[int]): positions where spaces must be inserted

        Returns:
            str: resulting string with spaces inserted
        """
        res = []
        i = 0
        j = 0
        sLen = len(s)

        # Build segments based on space positions
        while i < sLen and j < len(spaces):
            res.append(s[i:spaces[j]])  # substring before the next space index
            i = spaces[j]               # move start to that index
            j += 1

        # Append any remaining substring after the last space position
        if i < sLen:
            res.append(s[i:sLen])

        # Join all segments with spaces in between
        return " ".join(res)


# ▶️ TEST HERE
if __name__ == "__main__":
    S = Solution()

    print(S.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]))
    # Expected: "Leetcode Helps Me Learn"

    print(S.addSpaces("icodeinpython", [1, 5, 7, 9]))
    # Expected: "i code in py thon"

    print(S.addSpaces("spacing", [0,1,2,3,4,5,6]))
    # Expected: " s p a c i n g"

