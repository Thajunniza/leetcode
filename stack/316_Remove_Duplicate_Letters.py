"""
===========================================================
316. Remove Duplicate Letters
===========================================================

🧩 Problem:
You are given a string `s`.  
Your task is to **remove duplicate letters** so that:

1️⃣ Every letter appears **once and only once**.  
2️⃣ The resulting string is the **smallest in lexicographical order** among all possible results.

🎯 Goal:
Return the **lexicographically smallest** string containing each distinct character **exactly once**.

This is a classic **Greedy + Monotonic Stack** problem.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:   s = "bcabc"
Output:  "abc"
Explanation:
    - We must remove duplicates of 'b' and 'c'.
    - "abc" is the smallest possible result.

Example 2:
Input:   s = "cbacdcbc"
Output:  "acdb"
Explanation:
    Possible results include "cadb", "acdb".
    "acdb" is lexicographically smallest.

Example 3:
Input:   s = "bbcaac"
Output:  "bac"
Explanation:
    Keep one b, one a, one c → best lexicographic ordering is "bac".

-----------------------------------------------------------
Intuition — Greedy Monotonic Stack:
-----------------------------------------------------------

We want the **smallest lexicographical string** while ensuring **each character appears exactly once**.

To achieve this, we build the answer using a **stack** with these rules:

-----------------------------------------------------------
Rule 1️⃣ — Use “last occurrence” index
-----------------------------------------------------------
Before removing a character from the stack, we must check:

➡ “Will this character appear again later?”

We only remove a character from the stack if it will appear later  
(because then we can safely re-add it in a better position).

-----------------------------------------------------------
Rule 2️⃣ — Maintain a monotonically increasing result
-----------------------------------------------------------
WHEN we see a character `c`, we try to remove characters from the top of the stack:

Pop while ALL are true:
- stack not empty
- current char `c` is *smaller* than stack top
- stack top appears again later (so safe to remove)
- stack top is not already removed

This ensures our final string is lexicographically minimal.

-----------------------------------------------------------
Rule 3️⃣ — Ensure each character is added only once
-----------------------------------------------------------
Use a `visited` set to track characters already in the result.

-----------------------------------------------------------
Algorithm Steps:
-----------------------------------------------------------

1️⃣ Compute `last_occurrence[ch]` = last index of each character.  
2️⃣ Initialize:
      stack = []
      visited = set()
3️⃣ For each index `i` and character `ch` in `s`:
      - If `ch` already in visited → skip
      - Otherwise:
          • While stack not empty AND
                top of stack > ch AND
                last occurrence of stack top > i:
                   pop stack top  
                   remove from visited
          • Push ch onto stack  
          • Mark ch as visited
4️⃣ Convert stack to string → answer

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------

This is a perfect example of:

⭐ Greedy choice:
   - Keep result lexicographically smallest *at every step*.

⭐ Safe choice:
   - Only remove a character if it occurs again later.

⭐ Monotonic stack:
   - Maintains increasing lexical order.

This method guarantees the optimal result.

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time:  `O(n)` — each character pushed and popped at most once  
- Space: `O(1)` or `O(26)` — only lowercase letters

-----------------------------------------------------------
Python Implementation (Monotonic Stack):
-----------------------------------------------------------
"""

from typing import List

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {ch: i for i, ch in enumerate(s)}  # last occurrence of each letter
        stack = []
        visited = set()

        for i, ch in enumerate(s):
            if ch in visited:
                continue

            # maintain lexicographically smallest result
            while stack and ch < stack[-1] and last[stack[-1]] > i:
                removed = stack.pop()
                visited.remove(removed)

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)


"""
-----------------------------------------------------------
Dry Run Example:
Input: "cbacdcbc"
-----------------------------------------------------------

last occurrences:
    c:7, b:6, a:2, d:4

Iterate:
i=0 'c': stack=['c']
i=1 'b': 'b' < 'c' and last[c]=7>1 → pop 'c'; stack=['b','c'] afterward? NO.
Correct: stack=['b'], then append 'b'? No — process carefully.

Final stack ends as: ['a','c','d','b']

Output: "acdb"
-----------------------------------------------------------
"""


"""