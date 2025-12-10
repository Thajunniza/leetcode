""" 
===========================================================
455. Assign Cookies
===========================================================

🧩 Problem:
Assume you are an awesome parent and want to give your children some cookies.

- Each child `i` has a **greed factor** `g[i]`, which is the minimum size of a cookie that the child will be satisfied with.
- Each cookie `j` has a **size** `s[j]`.

You can assign **at most one cookie** to each child, and each cookie can be used **at most once**.

Your task:
Maximize the number of **content children**.

Return the **maximum number of children** that can be made content.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    g = [1,2,3]
    s = [1,1]

Process:
    - Children’s greed (sorted): [1,2,3]
    - Cookie sizes (sorted):     [1,1]

    Assign:
        - Child with greed 1 gets cookie size 1 → content
        - Next child has greed 2, remaining cookie is size 1 → not enough

    Total content children = 1

Output:
    1


Example 2:
Input:
    g = [1,2]
    s = [1,2,3]

Process:
    - Children: [1,2]
    - Cookies:  [1,2,3]

    Assign:
        - Child with greed 1 → cookie 1
        - Child with greed 2 → cookie 2
        - Cookie 3 unused

    Total content children = 2

Output:
    2

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Assign cookies to children such that:
- Each child gets at most one cookie
- A child `i` is content if assigned cookie `j` where `s[j] >= g[i]`
- The total number of content children is maximized

Pattern / Folder:
    • Pattern: Greedy + Two Pointers
    • Folder suggestion:
        /Greedy/455-AssignCookies/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

Greedy idea:
- To satisfy as many children as possible, we should:
    - Use the **smallest cookie** that can satisfy each child
    - Match the **least greedy** child first

Steps:
1. Sort `g` (children’s greed) in non-decreasing order.
2. Sort `s` (cookie sizes) in non-decreasing order.
3. Use two pointers:
    - `i` → index for children (greed array)
    - `j` → index for cookies (size array)

Walk through:
- If `s[j] >= g[i]`, we can satisfy this child:
    - Count this child as content
    - Move to the next child (`i += 1`) and next cookie (`j += 1`)
- Else (`s[j] < g[i]`), this cookie is too small:
    - Try the next larger cookie (`j += 1`)

When we run out of cookies or children, we stop.
The number of content children is simply `i`.

-----------------------------------------------------------
🧠 Algorithm (Greedy + Two Pointers):
-----------------------------------------------------------

1. Sort both arrays:
       g.sort()
       s.sort()

2. Initialize:
       i = 0   # pointer for children
       j = 0   # pointer for cookies
       m = len(g)
       n = len(s)

3. While i < m and j < n:
       if s[j] >= g[i]:
           # cookie j can satisfy child i
           i += 1      # move to next child
           j += 1      # move to next cookie
       else:
           # cookie j too small, try bigger cookie
           j += 1

4. When loop ends:
       - i = number of children satisfied

5. Return i.

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time Complexity:
    • Sorting g: O(m log m)
    • Sorting s: O(n log n)
    • Two-pointer scan: O(m + n)
  Overall: O(m log m + n log n)

- Space Complexity:
    • O(1) extra (in-place sorting, ignoring language sort internals)

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution(object):
    def findContentChildren(self, g, s):
        """
        LeetCode 455. Assign Cookies

        Args:
            g (List[int]): greed factors of children
            s (List[int]): sizes of cookies

        Returns:
            int: maximum number of content children
        """
        # Sort greed factors and cookie sizes
        g.sort()
        s.sort()

        i = 0  # pointer for children
        j = 0  # pointer for cookies
        m = len(g)
        n = len(s)

        # Use two pointers to match cookies to children
        while i < m and j < n:
            if s[j] >= g[i]:
                # cookie s[j] satisfies child g[i]
                i += 1  # move to next child
                j += 1  # move to next cookie
            else:
                # cookie too small, try next cookie
                j += 1

        # i = number of children satisfied
        return i


# ▶️ TEST HERE
if __name__ == "__main__":
    S = Solution()

    g1 = [1,2,3]
    s1 = [1,1]
    print(S.findContentChildren(g1, s1))   # Expected: 1

    g2 = [1,2]
    s2 = [1,2,3]
    print(S.findContentChildren(g2, s2))   # Expected: 2

