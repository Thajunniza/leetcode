"""
===========================================================
1544. Make The String Great
===========================================================

🧩 Problem:
You are given a string `s` containing only English letters (uppercase & lowercase).

A string is considered **"bad"** if it contains **two adjacent characters** such that:
    • They are the same letter ignoring case  → e.g., 'a' and 'A'
    • But they have **different cases**

These pairs must be **removed**.

Examples of "bad pairs":
    "aA", "Bb", "cC"

You must repeatedly remove such adjacent pairs until the string becomes **good**.

🎯 Goal:
Return the resulting "good" string after removing all bad adjacent pairs.
If the string becomes empty, return `""`.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  "leEeetcode"

Process:
    l   → [l]
    e   → [l, e]
    E   → eE is a bad pair → remove e
           → [l]
    e   → [l, e]
    e,t,c,o,d,e  (no more bad pairs)
Final: "leetcode"

Output: "leetcode"


Example 2:
Input: "abBA"

Process:
    a   → [a]
    b   → [a, b]
    B   → bB is a bad pair → remove b → [a]
    A   → aA is a bad pair → remove a → []
Final: ""

Output: ""


Example 3:
Input: "s"
Output: "s"

-----------------------------------------------------------
Algorithm — Stack-Based Adjacent Removal:
-----------------------------------------------------------

Use a stack to simulate the removal of bad pairs.

For each character `ch`:
    • If stack is not empty AND
      stack[-1] and ch are:
          - the same letter ignoring case
          - but different cases
      → then pop the stack (remove the previous char)
    • Else:
      → push the current character into the stack

To detect a bad pair:
    stack[-1].lower() == ch.lower()
    AND
    stack[-1] != ch

Finally:
    Join the stack characters to form the result string.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    - Each character is pushed/popped at most once.

Space Complexity:  O(n)
    - Stack may hold the entire string in worst case.

-----------------------------------------------------------
"""

class Solution(object):
    def makeGood(self, s):
        """
        Removes ‘bad’ adjacent character pairs until the string becomes good.

        Args:
            s (str): Input string.

        Returns:
            str: Good string after removing bad adjacent pairs.
        """
        stack = []

        for ch in s:
            # Check if a bad pair exists with the top of the stack
            if stack and stack[-1].lower() == ch.lower() and stack[-1] != ch:
                stack.pop()  # Remove the previous conflicting character
            else:
                stack.append(ch)

        return "".join(stack)


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.makeGood("leEeetcode"))  
    # Expected: "leetcode"

    print(sol.makeGood("abBA"))        
    # Expected: ""

    print(sol.makeGood("s"))           
    # Expected: "s"

    print(sol.makeGood("mCcaA"))       
    # Process:
    #   mC  → ok
    #   Cc  → remove C, c
    #   aA  → remove a, A
    # Final → "m"
    # Expected: "m"

    print(sol.makeGood("PpAa"))        
    # All cancel → Expected: ""
