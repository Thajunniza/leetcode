"""
===========================================================
844. Backspace String Compare
===========================================================

🧩 Problem:
Given two strings `s` and `t`, each string represents a text editor input where:
- `'#'` means a **backspace**
- Any lowercase letter is appended to the text

Simulate typing both strings and determine if they are **equal** after all backspaces are applied.

Return `True` if they are equal, otherwise `False`.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    s = "ab#c"
    t = "ad#c"

Process:
    s: "ab#c" → "ac"
    t: "ad#c" → "ac"

Output:
    True


Example 2:
Input:
    s = "ab##"
    t = "c#d#"

Process:
    s: "ab##"  → ""  
    t: "c#d#"  → ""  

Output:
    True


Example 3:
Input:
    s = "a#c"
    t = "b"

Process:
    s: "a#c" → "c"
    t: "b"   → "b"

Output:
    False

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Simulate backspace behavior in both strings and check:
- Do `s` and `t` result in the **same final string**?

Constraints:
- You should aim for **O(n + m) time** and **O(1) extra space**.

Pattern / Folder:
    • Pattern: Two Pointers, String, Backspace Simulation
    • Folder suggestion:
        /TwoPointers/844-BackspaceStringCompare/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

Instead of building the final strings explicitly with stacks:

1. Use **two pointers** starting from the **end** of each string:
    - `i` for `s`
    - `j` for `t`

2. For each pointer, we need to find the **next valid character** after accounting for `'#'`:
    - Maintain a `back` counter.
    - Move left:
        • If current char is `'#'` → increment `back`
        • Else if `back > 0` → skip this character (one backspace applied) and decrement `back`
        • Else → this character is valid; stop here.

3. After getting the next valid index in both strings:
    - If both are valid (i >= 0 and j >= 0), compare:
        • If chars differ → return False
    - If only one is valid → return False

4. Continue until both pointers are exhausted:
    - If we finish without mismatches → return True.

This simulates the backspace behavior **on the fly**, with **no extra arrays or stacks**.

-----------------------------------------------------------
🧠 Algorithm (Two Pointers + Helper getNextIndex):
-----------------------------------------------------------

1. Define `getNextIndex(st, i)`:
       - Input: string `st`, index `i`
       - Output: index of the next valid character after applying backspaces, or -1 if none.
       Steps:
           back = 0
           while i >= 0:
               if st[i] == '#':
                   back += 1
               elif back > 0:
                   back -= 1
               else:
                   break
               i -= 1
           return i

2. Initialize:
       i = len(s) - 1
       j = len(t) - 1

3. While i >= 0 or j >= 0:
       i = getNextIndex(s, i)
       j = getNextIndex(t, j)

       if i < 0 and j < 0:
           return True      # both strings exhausted at same time

       if i < 0 or j < 0:
           return False     # one has chars left, other doesn't

       if s[i] != t[j]:
           return False

       i -= 1
       j -= 1

4. If loop completes:
       return True

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

Let:
    n = len(s)
    m = len(t)

- Time Complexity:  **O(n + m)**
  Each character is processed at most once.

- Space Complexity: **O(1)**
  Only a few pointers and counters used.

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        LeetCode 844. Backspace String Compare

        Compare two strings after simulating backspace operations,
        using two pointers from the end with O(1) extra space.
        """

        def getNextIndex(st, i):
            """
            Return the index of the next valid character in st
            when scanning from right to left, applying backspaces.
            """
            back = 0
            while i >= 0:
                if st[i] == '#':
                    back += 1
                elif back > 0:
                    back -= 1
                else:
                    break
                i -= 1
            return i

        i = len(s) - 1
        j = len(t) - 1

        # Process from the end of both strings
        while i >= 0 or j >= 0:
            i = getNextIndex(s, i)
            j = getNextIndex(t, j)

            # Both strings exhausted
            if i < 0 and j < 0:
                return True

            # One string exhausted but not the other
            if i < 0 or j < 0:
                return False

            # Compare current valid characters
            if s[i] != t[j]:
                return False

            i -= 1
            j -= 1

        return True


# ▶️ TEST HERE
if __name__ == "__main__":
    S = Solution()
    print(S.backspaceCompare("ab#c", "ad#c"))     # True
    print(S.backspaceCompare("ab##", "c#d#"))     # True
    print(S.backspaceCompare("a#c", "b"))         # False

