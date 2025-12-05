"""
===========================================================
484. Find Permutation
===========================================================

🧩 Problem:
You are given a string `s` of length `n - 1` consisting only of:
    • 'I' → means perm[i] < perm[i+1]
    • 'D' → means perm[i] > perm[i+1]

You must return the **lexicographically smallest permutation** of numbers  
from `1` to `n` (where `n = len(s) + 1`) that satisfies the pattern in `s`.

A *permutation* means:
    • uses all numbers from 1 to n exactly once  
    • no repeats  
    • must follow the pattern relationships from `s`  

🎯 Goal:
Construct the smallest possible permutation of `[1..n]` that follows  
all 'I' (increase) and 'D' (decrease) constraints.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:
    s = "I"

n = 2 → numbers {1,2}
Constraint:
    perm[0] < perm[1]

Smallest valid:
    [1,2]

Output:
    [1,2]


Example 2:
Input:
    s = "D"

Constraint:
    perm[0] > perm[1]

Smallest valid:
    [2,1]

Output:
    [2,1]


Example 3:
Input:
    s = "IDID"

We want:
    perm[0] < perm[1]
    perm[1] > perm[2]
    perm[2] < perm[3]
    perm[3] > perm[4]

Smallest permutation that satisfies this:
    [1, 3, 2, 5, 4]

Output:
    [1, 3, 2, 5, 4]

-----------------------------------------------------------
Why the Stack Solution Works:
-----------------------------------------------------------

We use the numbers from 1 to n **in order**, but build the permutation by using
a stack to enforce the reverse order on 'D' segments.

Key Trick:
    • Push numbers sequentially into a stack.
    • Whenever an 'I' is encountered (or end of string), we pop the entire stack.

Effect:
    • For "I": stack flush creates increasing order.
    • For "D": numbers accumulate (e.g., 2,3,4), and flushing pops them as 4,3,2
      → automatically creates the required decreasing segment.

This gives the **lexicographically smallest** valid permutation because we always
push numbers in increasing order and only reverse when absolutely required.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    • Push each number once, pop each number once.

Space Complexity:  O(n)
    • Stack and result list each hold up to n items.

-----------------------------------------------------------
Optimal Python Solution (Stack Method)
-----------------------------------------------------------
"""

from typing import List

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s)
        stack = []
        result = []

        for i in range(n + 1):
            # push next number (1..n+1)
            stack.append(i + 1)

            # flush when:
            # 1. we reach an 'I', OR
            # 2. at the very end (i == n)
            if i == n or s[i] == 'I':
                while stack:
                    result.append(stack.pop())

        return result


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.findPermutation("I"))
    # Expected: [1,2]

    print(sol.findPermutation("D"))
    # Expected: [2,1]

    print(sol.findPermutation("IDID"))
    # Expected: [1,3,2,5,4]

    print(sol.findPermutation("DDI"))
    # Expected: [3,2,1,4]

    print(sol.findPermutation("III"))
    # Expected: [1,2,3,4]

    print(sol.findPermutation("DDD"))
    # Expected: [4,3,2,1]
