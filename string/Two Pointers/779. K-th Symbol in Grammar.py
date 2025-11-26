"""
===========================================================
779. K-th Symbol in Grammar
===========================================================

🧩 Problem:
We build a special grammar sequence row by row:

- Row 1: `0`
- To get the next row:
  - Replace every `0` with `01`
  - Replace every `1` with `10`

So the rows look like:

- Row 1:                    0
- Row 2:                  0 1
- Row 3:               0 1 1 0
- Row 4:            0 1 1 0 1 0 0 1
- ...

Given two integers `n` and `k`, return the **k-th symbol** in the **n-th row** (1-indexed).

---

🎯 Goal:
Compute `grammar[n][k]` **without** actually building the full string (because length grows as `2^(n-1)`).

---

🧠 Intuition (Tree / Interval View):

Think of it like a binary tree:

- Level 1: `0`
- Each `0` expands to `0 (left child), 1 (right child)`
- Each `1` expands to `1 (left child), 0 (right child)`

So, moving from top to bottom:

- If you go to **left child**, symbol stays the **same**
- If you go to **right child**, symbol gets **flipped** (0 → 1, 1 → 0)

Now think of row `n` as positions `1` to `2^(n-1)`.

We can binary-search on this interval:

- Start with:
  - `l = 1`, `r = 2^(n-1)`
  - `curr = 0` (root symbol)
- For each level (n - 1 steps):
  - Compute `mid = (l + r) // 2`
  - If `k` is in **left half** → `[l, mid]`  
    - Move `r = mid`, symbol unchanged.
  - If `k` is in **right half** → `[mid+1, r]`  
    - Move `l = mid + 1`, and **flip** `curr`.

At the end, `curr` is the answer.

---

📌 Example:

Say `n = 4`, `k = 5`:

Row 4 is: `0 1 1 0 1 0 0 1` → 5th symbol = `1`

Using interval method:

- Row length = `2^(4-1) = 8`
- Start: `l=1, r=8, curr=0`

1️⃣ Level 1:  
mid = 4  
k = 5 > 4 → go right  
→ flip `curr` from 0 → 1  
→ `l = 5, r = 8`

2️⃣ Level 2:  
mid = (5+8)//2 = 6  
k = 5 ≤ 6 → go left  
→ `r = 6`, curr stays 1

3️⃣ Level 3:  
mid = (5+6)//2 = 5  
k = 5 ≤ 5 → go left  
→ `r = 5`, curr stays 1

Done → answer = `1`

---

🧾 Algorithm (Iterative Binary-Search Style):

1. Let `l = 1`, `r = 2^(n-1)`, `curr = 0`.
2. Repeat `n-1` times:
   - `mid = (l + r) // 2`
   - If `k <= mid`:
     - `r = mid`  (go to left half, same symbol)
   - Else:
     - `l = mid + 1` (go to right half)
     - Flip `curr` (0 → 1 or 1 → 0)
3. Return `curr`.

---

⏱️ Time & Space Complexity:

- Each step reduces range one level down → **n-1 steps**
- **Time:** `O(n)`
- **Space:** `O(1)`

---

💻 Python Solution (Your Iterative Version, Slightly Cleaned):

```python
"""
class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        l = 1
        r = 2 ** (n - 1)
        curr = 0  # symbol at current level

        for _ in range(n - 1):
            mid = (l + r) // 2
            if k <= mid:
                # Go to left half, symbol unchanged
                r = mid
            else:
                # Go to right half, symbol flips
                l = mid + 1
                curr ^= 1  # flip 0 <-> 1

        return curr

if __name__ == "__main__":
    sol = Solution()

    tests = [
        (1, 1, 0),   # Row 1: 0
        (2, 1, 0),   # Row 2: 0 1
        (2, 2, 1),
        (3, 1, 0),   # Row 3: 0 1 1 0
        (3, 2, 1),
        (3, 3, 1),
        (3, 4, 0),
        (4, 5, 1),   # Row 4: 0 1 1 0 1 0 0 1
        (4, 8, 1),
        (5, 16, 0),
    ]

    for n, k, expected in tests:
        output = sol.kthGrammar(n, k)
        print(f"n={n}, k={k} -> Output: {output} | Expected: {expected}")

