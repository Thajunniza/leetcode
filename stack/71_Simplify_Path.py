"""
===========================================================
71. Simplify Path
===========================================================

🧩 Problem:
Given a string `path` representing an absolute Unix-style file path, simplify it.
Rules:
    - `.` means current directory → ignore.
    - `..` means go up one directory → pop from stack if possible.
    - Multiple slashes `//` should be treated as a single slash.
    - The result must start with `/` and have no trailing slash (except root).

Examples:
    - "/home/" → "/home"
    - "/../" → "/"
    - "/home//foo/" → "/home/foo"

🎯 Goal:
Return the simplified canonical path.
Time: O(n), Space: O(n).

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  path = "/home/"
Output: "/home"

Example 2:
Input:  path = "/../"
Output: "/"

Example 3:
Input:  path = "/home//foo/"
Output: "/home/foo"

Example 4:
Input:  path = "/a/./b/../../c/"
Output: "/c"

-----------------------------------------------------------
Algorithm — Stack-Based Approach:
-----------------------------------------------------------

Core idea:
Split the path by `/` and process each segment:
    - Ignore empty segments and "."
    - If segment is "..", pop from stack if not empty
    - Else, push segment onto stack

Steps:
1. Initialize an empty list `result` as a stack.
2. Split `path` by "/" into segments.
3. For each segment:
       - If segment == "..": pop from stack if possible
       - Else if segment != "" and segment != ".": push onto stack
4. Join stack with "/" and prepend root "/".
5. If stack is empty, return "/".

Why this works:
- Stack naturally handles directory traversal.
- Skips redundant slashes and current directory markers.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)  
Space Complexity:  O(n)  

-----------------------------------------------------------
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = []
        for c in path.split("/"):
            if c == "..":
                if result:
                    result.pop()
            elif c and c != ".":
                result.append(c)
        return "/" + "/".join(result) if result else "/"

# ------------------------------------
# Driver Test
# ------------------------------------

sol = Solution()
print(sol.simplifyPath("/home/"))           # /home
print(sol.simplifyPath("/../"))             # /
print(sol.simplifyPath("/home//foo/"))      # /home/foo
print(sol.simplifyPath("/a/./b/../../c/"))  # /c
print(sol.simplifyPath("/..."))             # /...