"""
===========================================================
3174. Clear Digits
===========================================================

🧩 Problem:
You are given a string `s` containing **lowercase letters** and **digits**.

There is one rule:

    When you see a digit:
        → Remove (delete) the **closest letter to its left**.
        → Then remove the digit itself.

Important constraints:
    • Digits can only delete **letters**, never other digits.
    • If no letter exists to the left when a digit appears, nothing is deleted.
    • Continue processing left → right until the end.

🎯 Goal:
Return the final string after applying all deletions.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  "abc3d"
Process:
    a → stack = [a]
    b → [a, b]
    c → [a, b, c]
    3 → digit → remove 'c'
         stack = [a, b]
    d → [a, b, d]

Output: "abd"


Example 2:
Input: "a1b2c3"
Process:
    a → [a]
    1 → remove a → []
    b → [b]
    2 → remove b → []
    c → [c]
    3 → remove c → []

Output: ""


Example 3:
Input: "l0eet1c2o3de"
Process:
    l → [l]
    0 → remove l → []
    e → [e]
    e → [e, e]
    t → [e, e, t]
    1 → remove t → [e, e]
    c → [e, e, c]
    2 → remove c → [e, e]
    o → [e, e, o]
    3 → remove o → [e, e]
    d → [e, e, d]
    e → [e, e, d, e]

Output: "eede"

-----------------------------------------------------------
Algorithm — Stack for Processing Deletions
-----------------------------------------------------------

Scan characters from left to right.

Maintain a stack of characters:

FOR each character `c`:
    • If `c` is a DIGIT:
            → If stack top is a **letter**, pop it.
            → DO NOT push `c` itself.
    • Else (c is a letter):
            → Push it onto the stack.

Why stack?
    • The digit always deletes the **closest previous letter** → exactly stack top.
    • Stack automatically handles multiple deletions and overlapping rules.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    • Each character is processed once.

Space Complexity:  O(n)
    • Stack may hold up to all letters.

-----------------------------------------------------------
Your Solution (Reviewed) — Correct & Optimal
-----------------------------------------------------------

Your logic is perfect ✔  
Just one subtle improvement:  
You do NOT want to pop when the top is a digit (but per rules, digits never get pushed, so your code already works correctly).

Below is the clean final version:

"""

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for c in s:
            if c.isdigit():
                if stack:
                    stack.pop()   # delete closest letter to left
            else:
                stack.append(c)  # push letters only

        return "".join(stack)


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.clearDigits("abc3d"))
    # Expected: "abd"

    print(sol.clearDigits("a1b2c3"))
    # Expected: ""

    print(sol.clearDigits("l0eet1c2o3de"))
    # Expected: "eede"

    print(sol.clearDigits("leetcode"))
    # Expected: "leetcode"

    print(sol.clearDigits("9"))
    # Expected: ""  (no letters to delete)

