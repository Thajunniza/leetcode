"""
===========================================================
1614. Maximum Nesting Depth of the Parentheses
===========================================================

🧩 Problem:
You are given a valid parentheses string `s`.

A parentheses string is valid if:
    • Every opening '(' has a corresponding closing ')'
    • Parentheses are properly nested

The **nesting depth** is defined as:
    • The maximum number of '(' that are open at the same time

🎯 Goal:
Return the **maximum nesting depth** of the parentheses.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input: "(1+(2*3)+((8)/4))+1"

Process:
    (   → depth = 1
    (   → depth = 2
    (   → depth = 3  ← maximum
    )   → depth = 2
    )   → depth = 1
    )   → depth = 0

Output: 3


Example 2:
Input: "(1)+((2))+(((3)))"

Process:
    (   → 1
    (   → 2
    (   → 3  ← maximum
    )   → 2
    )   → 1
    )   → 0

Output: 3


Example 3:
Input: "1+(2*3)/(2-1)"

Process:
    Only one '(' open at any time

Output: 1


Example 4:
Input: "1"

Output: 0

-----------------------------------------------------------
Algorithm — Counter-Based Parenthesis Tracking:
-----------------------------------------------------------

Use an integer counter to track the current depth.

Initialize:
    current_depth = 0
    max_depth = 0

For each character `ch` in the string:
    • If ch == '(':
          - Increment current_depth
          - Update max_depth
    • If ch == ')':
          - Decrement current_depth
    • Ignore all other characters

The maximum value reached by current_depth
is the answer.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    • Single pass through the string

Space Complexity: O(1)
    • Only constant extra variables used

-----------------------------------------------------------
"""

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        max_depth = 0

        for ch in s:
            if ch == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif ch == ')':
                depth -= 1

        return max_depth
def test_maxDepth():
    sol = Solution()

    # Basic cases
    assert sol.maxDepth("(1+(2*3)+((8)/4))+1") == 3
    assert sol.maxDepth("(1)+((2))+(((3)))") == 3
    assert sol.maxDepth("1+(2*3)/(2-1)") == 1

    # Edge cases
    assert sol.maxDepth("1") == 0                    # No parentheses
    assert sol.maxDepth("()") == 1                   # Single pair
    assert sol.maxDepth("(())") == 2                 # Nested
    assert sol.maxDepth("()()()") == 1               # Multiple but not nested
    assert sol.maxDepth("") == 0                     # Empty string
    assert sol.maxDepth("(((())))") == 4
    assert sol.maxDepth("((((()))))") == 5
    assert sol.maxDepth("((((((()))))))") == 7

    print("All test cases passed!")

test_maxDepth()
