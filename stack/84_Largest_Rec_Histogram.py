"""
===========================================================
84. Largest Rectangle in Histogram
===========================================================

🧩 Problem:
You are given an array of integers `heights` representing the heights of bars in a histogram.
Each bar has width `1`.

🎯 Goal:
Return the **area of the largest rectangle** that can be formed within the histogram.

The rectangle must be formed by **one or more contiguous bars**.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  heights = [2, 1, 5, 6, 2, 3]

Some possible rectangles:
    - Use bar at index 2 only (height 5):   area = 5 * 1 = 5
    - Use bars at indices 2..3 (5, 6):      min height = 5 → area = 5 * 2 = 10
    - Use bars at indices 1..5 (1,5,6,2,3): min height = 1 → area = 1 * 5 = 5
    - Use bars at indices 2..5 (5,6,2,3):   min height = 2 → area = 2 * 4 = 8

The maximum possible rectangle area is 10.

Output: 10


Example 2:
Input:  heights = [2, 4]

Rectangles:
    - index 0: height 2 → area = 2
    - index 1: height 4 → area = 4
    - indices 0..1: min height = 2 → area = 2 * 2 = 4

Max area = 4

Output: 4


Example 3:
Input:  heights = [6, 2, 5, 4, 5, 1, 6]
Output:  12

One optimal rectangle:
    - indices 2..4 (heights 5, 4, 5)
    - min height = 4, width = 3 → area = 4 * 3 = 12

-----------------------------------------------------------
Intuition — Each Bar as the Limiting Height:
-----------------------------------------------------------

Brute-force thinking:
- For every possible pair `L, R`, find the minimum height in `heights[L..R]`,
  compute area = min_height * (R - L + 1), and track the maximum.
- This is **O(n²)** or worse → too slow.

Better idea:
👉 For each bar `i`, imagine `heights[i]` is the **shortest bar** in some largest rectangle.
We want to know:

> “How far can we extend from bar `i` to the left and to the right while all bars are at least `heights[i]` high?”

If we know:
- `left[i]`  = number of consecutive bars to the **left** of `i` (excluding `i`)  
               with height **≥ heights[i]**
- `right[i]` = number of consecutive bars to the **right** of `i` (excluding `i`)  
               with height **≥ heights[i]**

Then the total width where `heights[i]` is the minimum bar is:

    width[i] = left[i] + 1 + right[i]

So area using bar `i` as limiting height:

    area[i] = heights[i] * width[i]

The answer is:

    max_area = max(area[i]) for all i

So the problem reduces to efficiently computing `left[i]` and `right[i]` for each `i`.

-----------------------------------------------------------
Monotonic Stack — Previous and Next Smaller Bars:
-----------------------------------------------------------

We use a **monotonic increasing stack** (by height) to find, for each index `i`:

- the nearest smaller bar **to the left**
- the nearest smaller bar **to the right**

We don't store those indices directly; instead we store how many bars we can extend to left/right.

-----------------------------------------------------------
LEFT array:
-----------------------------------------------------------

Goal:
    left[i] = number of consecutive bars to the **left** of `i` (excluding `i`)
              that have height ≥ `heights[i]`.

Algorithm:
1️⃣ Initialize an empty stack (to store indices).  
2️⃣ Iterate `i` from `0` to `n-1`:
    - While stack not empty AND `heights[stack.top] >= heights[i]`:
          pop the stack
      (We’re removing bars that are taller or equal, because they cannot act as
       the previous smaller bar anymore.)
    - After popping:
        • If stack not empty:
              previous smaller index = stack.top
              left[i] = i - previous_smaller_index - 1
          (bars between previous_smaller_index+1 and i-1 are ≥ heights[i])
        • If stack empty:
              there is no smaller to the left
              left[i] = i   (all bars from 0 to i-1 are ≥ heights[i])
    - Push `i` onto the stack.

-----------------------------------------------------------
RIGHT array:
-----------------------------------------------------------

Goal:
    right[i] = number of consecutive bars to the **right** of `i` (excluding `i`)
               that have height ≥ `heights[i]`.

Algorithm:
1️⃣ Clear the stack.  
2️⃣ Iterate `i` from `n-1` down to `0`:
    - While stack not empty AND `heights[stack.top] >= heights[i]`:
          pop the stack
    - After popping:
        • If stack not empty:
              next smaller index = stack.top
              right[i] = next_smaller_index - i - 1
          (bars between i+1 and next_smaller_index-1 are ≥ heights[i])
        • If stack empty:
              no smaller to the right
              right[i] = n - i - 1   (all bars from i+1 to n-1 are ≥ heights[i])
    - Push `i` onto the stack.

-----------------------------------------------------------
Combining LEFT and RIGHT:
-----------------------------------------------------------

For each bar i:
- total width where it is the minimum = `left[i] + 1 + right[i]`
- area using heights[i] as limiting bar:

      area[i] = heights[i] * (left[i] + right[i] + 1)

Take the maximum over all i.

This works because:
- By construction, to the left and right edges of this width,
  we have bars strictly smaller than heights[i], or the end of array.
- Inside that region, all bars are ≥ heights[i], so the entire rectangle
  can be "filled" up to heights[i].

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time:  `O(n)` — each index is pushed to and popped from the stack at most once.  
- Space: `O(n)` — for `left`, `right`, and the stack.

-----------------------------------------------------------
Python Implementation (Monotonic Stack with Left/Right Spans):
-----------------------------------------------------------
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0] * n   # left[i] = count of >= bars to the left of i
        right = [0] * n  # right[i] = count of >= bars to the right of i

        # 1️⃣ Compute LEFT spans
        stack = []
        for i, h in enumerate(heights):
            # Pop until we find a strictly smaller bar
            while stack and heights[stack[-1]] >= h:
                stack.pop()

            if stack:
                # previous smaller at stack[-1]
                left[i] = i - stack[-1] - 1
            else:
                # no smaller on left → can extend over all previous bars
                left[i] = i

            stack.append(i)

        # 2️⃣ Compute RIGHT spans
        stack = []
        for i in range(n - 1, -1, -1):
            # Pop until we find a strictly smaller bar
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                # next smaller at stack[-1]
                right[i] = stack[-1] - i - 1
            else:
                # no smaller on right → can extend to the end
                right[i] = n - i - 1

            stack.append(i)

        # 3️⃣ Compute maximal area
        result = 0
        for i, h in enumerate(heights):
            width = left[i] + right[i] + 1
            area = h * width
            result = max(result, area)

        return result


"""
-----------------------------------------------------------
Dry Run Example:
Input: heights = [2, 1, 5, 6, 2, 3]
-----------------------------------------------------------

Step 1: LEFT spans
    i=0, h=2: stack=[], left[0]=0
    i=1, h=1: pop 0 (2>=1), stack empty → left[1]=1
    i=2, h=5: stack=[1], heights[1]=1<5 → left[2]=2-1-1=0
    i=3, h=6: stack=[1,2], heights[2]=5<6 → left[3]=3-2-1=0
    i=4, h=2: pop 3 (6>=2), pop 2 (5>=2), stack=[1], left[4]=4-1-1=2
    i=5, h=3: stack=[1,4], heights[4]=2<3 → left[5]=5-4-1=0

    left = [0, 1, 0, 0, 2, 0]

Step 2: RIGHT spans
    i=5, h=3: stack=[], right[5]=0
    i=4, h=2: pop 5 (3>=2), stack=[], right[4]=1
    i=3, h=6: stack=[4], heights[4]=2<6 → right[3]=4-3-1=0
    i=2, h=5: stack=[4,3], heights[3]=6>=5 pop, heights[4]=2<5 → right[2]=4-2-1=1
    i=1, h=1: pop 3, pop 4, pop 2 (all >=1), stack=[], right[1]=4
    i=0, h=2: stack=[1], heights[1]=1<2 → right[0]=1-0-1=0

    right = [0, 4, 1, 0, 1, 0]

Step 3: Areas
    i=0: h=2, width=0+0+1=1 → area=2
    i=1: h=1, width=1+4+1=6 → area=6
    i=2: h=5, width=0+1+1=2 → area=10  ✅
    i=3: h=6, width=0+0+1=1 → area=6
    i=4: h=2, width=2+1+1=4 → area=8
    i=5: h=3, width=0+0+1=1 → area=3

Max area = 10.

-----------------------------------------------------------
"""

