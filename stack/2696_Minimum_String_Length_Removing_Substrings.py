"""
===========================================================
2696. Minimum String Length After Removing Substrings
===========================================================

🧩 Problem:
You are given a string `s` consisting only of characters: 'A', 'B', 'C', 'D'.

You can perform the following operation **any number of times**:

    • If the substring "AB" appears in the string, you can remove it.
    • If the substring "CD" appears in the string, you can remove it.

After repeatedly applying these operations (in any order, as long as possible),
you will end up with some final string.

🎯 Goal:
Return the **minimum possible length** of the string after removing all possible
"AB" and "CD" substrings.

You do **not** need the final string, only its length.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "ABFCACDB"

Process:
    s = "ABFCACDB"
    "AB" at start → remove "AB" → "FCACDB"
    Now: "FCACDB"
         "CD" inside → remove "CD" → "FCAB"
    Now: "FCAB"
         "AB" at end → remove "AB" → "FC"

Final string = "FC"
Length = 2

Output: 2


Example 2:
Input:  s = "ACBBD"

Process:
    s = "ACBBD"
    No "AB"
    No "CD"
    Cannot remove anything.

Final string = "ACBBD"
Length = 5

Output: 5

-----------------------------------------------------------
Algorithm — Stack for Pattern Removal
-----------------------------------------------------------

This is a classic **stack-based adjacent removal** problem, similar to:

    • 1544. Make The String Great
    • 1047. Remove All Adjacent Duplicates in String

We scan the string from **left to right** and use a stack:

For each character `c` in `s`:
    • If stack is not empty AND:
          - top is 'A' and c is 'B'  → pattern "AB"
          - top is 'C' and c is 'D'  → pattern "CD"
      → Then we found a removable pair:
            stack.pop()  (remove the previous char)
       And we DO NOT push c (because "AB" or "CD" is fully removed)

    • Otherwise:
      → Just push `c` onto the stack.

At the end:
    • The stack contains the remaining characters after all possible removals.
    • The answer = len(stack)

Why this works:
    • Any time we see a 'B' or 'D', we immediately check if it completes "AB" or "CD"
      with the previous character.
    • Stack naturally handles chain reactions, e.g. removing one pair might expose
      another pair formed with earlier characters.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    • Each character is pushed/popped at most once.

Space Complexity:  O(n)
    • In the worst case, no pattern matches and all characters remain on the stack.

-----------------------------------------------------------
Your Solution (✅ Correct & Optimal)
-----------------------------------------------------------
"""

class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for c in s:
            if stack and stack[-1] == "A" and c == "B":
                stack.pop()
            elif stack and stack[-1] == "C" and c == "D":
                stack.pop()
            else:
                stack.append(c)
        return len(stack)


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.minLength("ABFCACDB"))
    # Expected: 2  (→ "FC")

    print(sol.minLength("ACBBD"))
    # Expected: 5  (no removals)

    print(sol.minLength("AB"))
    # Expected: 0

    print(sol.minLength("CD"))
    # Expected: 0

    print(sol.minLength("AABBCCDD"))
    # "AB" → remove → "ABCCDD"?
    # Actually step by step:
    #   A A B B C C D D
    #   A A B B C C D D
    #   - First "AB" from positions (1,2) or (2,3) depending on order
    # After all removals, the stack logic gives the correct minimal length.
    print(sol.minLength("AAAABBBB"))
    # No "AB" next to each other in alternating order → some removals,
    # stack will handle all cases correctly.
