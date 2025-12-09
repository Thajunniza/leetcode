"""
===========================================================
1944. Number of Visible People in a Queue
===========================================================

🧩 Problem:
There are `n` people standing in a queue, all facing to the **right**.

You are given an array `heights` of length `n` where:
    heights[i] = height of the i-th person (0-indexed).

A person `i` can **see** person `j` (where `j > i`) if:
1️⃣ Every person between `i` and `j` has height **strictly less** than both `heights[i]` and `heights[j]`.  
2️⃣ Person `j` is the first person in that direction who is **taller or equal** than all those in between.

🎯 Goal:
For each person `i`, compute **how many people to the right** they can see.

Return an array `ans` of length `n` where:
    ans[i] = number of people person i can see to their right.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  heights = [10, 6, 8, 5, 11, 9]

Output: [3, 1, 2, 1, 1, 0]

Explanation:
Person 0 (height 10) can see:
    - Person 1 (6): visible
    - Person 2 (8): visible (6 < 8 < 10)
    - Person 4 (11): visible; after seeing a taller/equal person, stop.
Total: 3

Person 1 (6) can see:
    - Person 2 (8): visible (no one between is taller than min(6,8))
    - Person 4 (11) is not visible directly because 8 (at index 2) blocks view.
Total: 1

Person 2 (8) can see:
    - Person 3 (5): visible
    - Person 4 (11): visible (5 < 8 < 11), then stop.
Total: 2

Person 3 (5) can see:
    - Person 4 (11): visible, then stop.
Total: 1

Person 4 (11) can see:
    - Person 5 (9): visible (shorter and no one between)
Total: 1

Person 5 (9) can see:
    - No one (end of queue)
Total: 0

-----------------------------------------------------------
Intuition — Monotonic Decreasing Stack (Right-to-Left):
-----------------------------------------------------------

We want, for each person `i`, to know how many people to the **right** they can see.

Observation:
- Everyone looks **right**.
- From `i`’s point of view:
  - They can see every **shorter** person until they meet the first person who is
    **taller or equal** than them.
  - Once they see a taller/equal person, they **cannot see beyond** that person.

Key idea:
Traverse from **right to left** and maintain a stack of indices representing a
**monotonically decreasing sequence of heights**.

For each index `i`:

1️⃣ Pop shorter people:
   - While stack is not empty and `heights[stack.top] < heights[i]`:
       • Pop the stack.
       • Each popped person is **visible** to `i`.
       • Increase `ans[i]` for each pop.

   Why?
   - Because a shorter person on the right with no taller blocker between them and `i`
     is directly visible.  
   - When we pop them, we also know that `i` is taller, so this shorter person
     cannot block `i`’s view further to the right.

2️⃣ If stack is not empty after popping:
   - The new top is the **first taller or equal** person to the right of `i`.
   - That person is also **visible**, so increment `ans[i]` by 1.

   Why?
   - By definition, visibility continues through strictly shorter people until
     the first taller or equal person, which is also counted.

3️⃣ Push `i` onto the stack:
   - We now consider `i` as a candidate blocker for people further to the left.

-----------------------------------------------------------
Algorithm Steps:
-----------------------------------------------------------

1️⃣ Initialize:
    - `n = len(heights)`
    - `ans = [0] * n`
    - `stack = []`   # will store indices, maintaining decreasing heights

2️⃣ Iterate `i` from `n-1` down to `0`:
    - `ans[i] = 0`
    - While stack not empty and `heights[stack[-1]] < heights[i]`:
          pop stack
          ans[i] += 1      # each popped person is visible

    - If stack not empty:
          ans[i] += 1      # first taller/equal person is also visible

    - Push `i` onto stack.

3️⃣ Return `ans`.

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------

- The stack keeps indices of people in **strictly decreasing height order** from top to bottom.
- For a current person `i`:
  - Popping all shorter people:
    • Each popped index corresponds to a person directly visible to `i`.
    • They are strictly shorter and are not blocked by another taller person between.
  - If after popping, a person remains at the top of the stack:
    • That person is the nearest taller/equal person to the right.
    • They are also visible and **stop** further visibility.

Each person is pushed once and popped at most once → **O(n)** overall.

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time:  `O(n)` — single pass, each index pushed/popped at most once.
- Space: `O(n)` — for the stack and the answer array.

-----------------------------------------------------------
Python Implementation (Monotonic Decreasing Stack):
-----------------------------------------------------------
"""

from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        stack = []  # will store indices, heights are decreasing

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            # Pop all shorter people – each is visible
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
                ans[i] += 1

            # If someone is still on stack, they are the first taller/equal → visible
            if stack:
                ans[i] += 1

            # Current person becomes a potential blocker for those on the left
            stack.append(i)

        return ans


"""
-----------------------------------------------------------
Dry Run Example:
Input: heights = [10, 6, 8, 5, 11, 9]
-----------------------------------------------------------

Start:
    ans   = [0, 0, 0, 0, 0, 0]
    stack = []

i = 5, h = 9:
    stack empty → no pops, no taller/equal
    push 5
    ans = [0, 0, 0, 0, 0, 0]
    stack = [5]

i = 4, h = 11:
    while heights[5] < 11 → 9 < 11 → pop 5, ans[4] += 1 → ans[4] = 1
    stack empty → no taller/equal
    push 4
    ans   = [0, 0, 0, 0, 1, 0]
    stack = [4]

i = 3, h = 5:
    heights[4] < 5? 11 < 5 → no
    stack not empty → ans[3] += 1 → ans[3] = 1 (sees person 4)
    push 3
    ans   = [0, 0, 0, 1, 1, 0]
    stack = [4, 3]

i = 2, h = 8:
    heights[3] < 8 → 5 < 8 → pop 3, ans[2] += 1 → ans[2] = 1
    heights[4] < 8? 11 < 8? no
    stack not empty → ans[2] += 1 → ans[2] = 2 (sees person 4)
    push 2
    ans   = [0, 0, 2, 1, 1, 0]
    stack = [4, 2]

i = 1, h = 6:
    heights[2] < 6? 8 < 6? no
    stack not empty → ans[1] += 1 → ans[1] = 1 (sees person 2)
    push 1
    ans   = [0, 1, 2, 1, 1, 0]
    stack = [4, 2, 1]

i = 0, h = 10:
    heights[1] < 10 → 6 < 10 → pop 1, ans[0] = 1
    heights[2] < 10 → 8 < 10 → pop 2, ans[0] = 2
    heights[4] < 10? 11 < 10? no
    stack not empty → ans[0] += 1 → ans[0] = 3 (sees person 4)
    push 0
    ans   = [3, 1, 2, 1, 1, 0]
    stack = [4, 0]

Final:
    ans = [3, 1, 2, 1, 1, 0] ✅

-----------------------------------------------------------
"""
