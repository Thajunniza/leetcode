"""
===========================================================
1598. Crawler Log Folder
===========================================================

🧩 Problem:
You are given a list of folder navigation logs from a file system crawler.

Each log entry represents one operation:

    "../"  → Move to the parent folder (if already at root, stay at root)
    "./"   → Stay in the current folder (no change)
    "x/"   → Move into a child folder named x

You start at the **root folder**.

🎯 Goal:
Return the **minimum number of operations** needed to return to the root folder
after processing all logs.

This is equal to:  
    The *depth* of the folder you end up in  
    (because each depth level requires one "../" to go back to root)

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input: ["d1/","d2/","../","d21/","./"]

Process:
    d1/   → go into d1     → depth 1
    d2/   → go into d2     → depth 2
    ../   → back to d1     → depth 1
    d21/  → go into d21    → depth 2
    ./    → stay           → depth 2

Final depth = 2 → need 2 operations to return to root.

Output: 2


Example 2:
Input: ["d1/","d2/","./","d3/","../","d31/","../"]

Process:
    d1   → depth 1
    d2   → depth 2
    ./   → depth 2
    d3   → depth 3
    ../  → depth 2
    d31  → depth 3
    ../  → depth 2

Output: 2


Example 3:
Input: ["../","../","../"]

Process:
    Already at root, "../" does nothing.
    Still at depth 0.

Output: 0

-----------------------------------------------------------
Algorithm — Stack for Directory Depth:
-----------------------------------------------------------

Use a stack to represent the current path:

For each log entry:
    "../"   → pop stack if not empty (go up)
    "./"    → do nothing (stay)
    "x/"    → push folder name onto stack (go down)

Reason:
The number of folders in the stack equals the current depth.

The final answer is simply:
    len(stack)

This equals the number of "../" operations needed to get back to root.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    • One pass over logs, stack push/pop is O(1)

Space Complexity:  O(n)
    • Worst case: all logs push new directories

-----------------------------------------------------------
"""

# =========================================================
# Your Solution (Reviewed & Perfect)
# =========================================================

class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []
        for n in logs:
            if n == "../":
                if stack:
                    stack.pop()
            elif n == "./":
                continue
            else:
                stack.append(n)  # directory name with trailing '/'
        
        return len(stack)


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.minOperations(["d1/","d2/","../","d21/","./"]))
    # Expected: 2

    print(sol.minOperations(["d1/","d2/","./","d3/","../","d31/","../"]))
    # Expected: 2

    print(sol.minOperations(["../","../","../"]))
    # Expected: 0

    print(sol.minOperations(["a/","b/","c/","../","../"]))
    # Expected: 1

    print(sol.minOperations(["./","./","x/"]))
    # Expected: 1
