"""
===========================================================
1578. Minimum Time to Make Rope Colorful
===========================================================

🧩 Problem:
You are given:

- A string `colors` where each character represents the color of a balloon.
- An array `neededTime` where `neededTime[i]` is the time needed to **remove** the `i`-th balloon.

The rope becomes **colorful** if *no two adjacent balloons have the same color*.

You want to remove balloons so that:
- No two adjacent balloons have the same color.
- The **total time** spent removing balloons is **minimum**.

Return the **minimum total time** required.

---

🎯 Goal:
For every group of **consecutive same-colored balloons**:
- Keep **only ONE** balloon (the one with the maximum removal cost).
- Remove all the others → add their `neededTime` to the result.

---

🧠 Pattern:
- **Greedy**
- **Two Pointers**
- Track the balloon with the **maximum cost** inside each same-color run.

---

📌 Example 1:
```text
Input:  
colors = "abaac"
time   = [1,2,3,4,5]

Output: 3

Explanation:
Group "aa" at positions 2 and 3:
- costs = [3, 4]
- Keep 4 (max), remove 3 → answer = 3

Input:
colors = "abc"
time   = [1,2,3]

Output: 0   (no adjacent duplicates)

colors = "aabaa"
time   = [1,2,3,4,1]

Groups:
- "aa" at start: remove 1 → keep 2
- "aa" at end:   remove 1 → keep 4

Total = 1 + 1 = 2

"""

"""
1578. Minimum Time to Make Rope Colorful

Pattern:
    - Greedy
    - Two Pointers (on same-color groups)

Goal:
    Remove minimum total time so that no two adjacent balloons
    on the rope have the same color.
"""

class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        p = 0
        q = 1
        result = 0

        while q < len(colors):
            if colors[p] == colors[q]:
                # Remove the smaller cost balloon
                if neededTime[p] < neededTime[q]:
                    result += neededTime[p]
                    p = q     # keep balloon with higher time
                else:
                    result += neededTime[q]
            else:
                # New color group begins
                p = q

            q += 1

        return result


# =======================
# 🔍 TESTING THE FUNCTION
# =======================
if __name__ == "__main__":
    sol = Solution()

    tests = [
        # (colors, neededTime), expected
        (("abaac", [1, 2, 3, 4, 5]), 3),
        (("abc",   [1, 2, 3]), 0),
        (("aabaa", [1, 2, 3, 4, 1]), 2),
        (("aaaa",  [1, 2, 3, 4]), 6),      # remove 1+2+3, keep 4
        (("bbaaa", [3, 5, 2, 4, 6]), 9),   # bb: remove 3; aaa: remove 2+4
        (("c",     [10]), 0),              # single balloon, no removal
    ]

    for (colors, neededTime), expected in tests:
        output = sol.minCost(colors, neededTime)
        print(f"colors={colors}, neededTime={neededTime} -> Output: {output} | Expected: {expected}")
