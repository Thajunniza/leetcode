"""
===========================================================
2390. Removing Stars From a String
===========================================================

🧩 Problem:
You are given a string `s` consisting of lowercase English letters and stars `'*'`.

When you see a star `'*'`, it performs exactly **one operation**:

        Remove the closest letter to its left.
        The star itself is also removed.

Example:
    "ab*cd" → remove 'b' + '*' → "acd"

You must apply this rule **from left to right**, as the string is read.

🎯 Goal:
Return the final string after all stars have removed the appropriate characters.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "leet**cod*e"

Process:
    l → [l]
    e → [l, e]
    e → [l, e, e]
    t → [l, e, e, t]
    * → remove t → [l, e, e]
    * → remove e → [l, e]
    c → [l, e, c]
    o → [l, e, c, o]
    d → [l, e, c, o, d]
    * → remove d → [l, e, c, o]
    e → [l, e, c, o, e]

Output: "lecoe"


Example 2:
Input:  s = "a*b*c*"
Process:
    a → [a]
    * → remove a → []
    b → [b]
    * → remove b → []
    c → [c]
    * → remove c → []

Output: ""


Example 3:
Input:  s = "erase*****"
Process:
    erase*****
    The five stars delete all five letters.

Output: ""

-----------------------------------------------------------
Algorithm — Stack Simulation:
-----------------------------------------------------------

This is identical in pattern to:

    • 3174 Clear Digits
    • 2696 Minimum String Length After Removing Substrings
    • 1544 Make The String Great
    • 1047 Remove All Adjacent Duplicates

We use a stack:

FOR each character c in s:
    • If c == '*':
          → Pop the top of the stack (remove closest previous letter)
    • Else:
          → Push c onto the stack

At the end, the stack holds the final characters.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    • Single pass over the string.

Space Complexity:  O(n)
    • Stack may hold all letters in worst case.


"""

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.removeStars("leet**cod*e"))
    # Expected: "lecoe"

    print(sol.removeStars("a*b*c*"))
    # Expected: ""

    print(sol.removeStars("erase*****"))
    # Expected: ""

    print(sol.removeStars("abc"))
    # Expected: "abc"

    print(sol.removeStars("*abc"))
    # Expected: "abc"   ('*' does nothing when stack is empty)
