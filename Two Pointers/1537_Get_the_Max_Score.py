"""
===========================================================
1537. Get the Maximum Score
===========================================================

🧩 Problem:
You are given two **sorted strictly increasing** integer arrays `nums1` and `nums2`.

You start from the **beginning** of either array and move **right** one step at a time.
At any point, if the **current value is present in both arrays**, you may **switch** from one array to the other (at that same value).

Your **score** is the sum of all the values you visit.  
Return the **maximum possible score** you can obtain, **modulo 10^9 + 7**.

You may **end** your path in **either array**.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    nums1 = [2,4,5,8,10]
    nums2 = [4,6,8,9]

One optimal path:
    Start in nums1: 2 → 4 → 5 → 8 → 10
    Start in nums2: 4 → 6 → 8 → 9

We compare segment sums between common points:
    Before 4:   nums1: [2]             sum1 = 2
                nums2: []              sum2 = 0   → take max = 2

    Between 4 & 8:
        nums1: [5]                     sum1 = 5
        nums2: [6]                     sum2 = 6   → take max = 6

    After 8 (no more common points):
        nums1: [10]                    sum1 = 10
        nums2: [9]                     sum2 = 9   → take max = 10

Total = 2 (before 4) + 4 (common) + 6 (between) + 8 (common) + 10 (after) = 30

Output:
    30

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Maximize the sum of visited elements by:
- Walking from **left to right** in the arrays
- **Optionally switching** at common elements
- Returning the **maximum score modulo 10^9 + 7**

Pattern / Folder:
    • Pattern: Two Pointers, Merge-like traversal
    • Folder suggestion:
        /TwoPointers/1537-GetMaximumScore/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

Think of it as walking on **two parallel roads**:
- You can walk on road A (`nums1`) or road B (`nums2`)
- At **intersection points** (common values), you are allowed to **switch roads**
- Between intersections, you must pick **one road’s segment sum** (whichever is larger)

So:
1. Move with two pointers `i` and `j` over both arrays.
2. Maintain **running sums** for both paths:
   - `sum1` = sum of nums1 segment since last common point
   - `sum2` = sum of nums2 segment since last common point
3. When you hit a **common element**:
   - Add `max(sum1, sum2)` + that common value to `answer`
   - Reset `sum1` and `sum2` to 0 (start new segment after this common point)
4. At the end, add `max(sum1, sum2)` (for the tail segment) to `answer`.

-----------------------------------------------------------
🧠 Algorithm (Two Pointer + Segment Max):
-----------------------------------------------------------

1. Initialize:
   - `i = j = 0`
   - `sum1 = sum2 = 0`
   - `ans = 0`
   - `MOD = 10**9 + 7`

2. Traverse while `i < len(nums1)` and `j < len(nums2)`:
   - If `nums1[i] < nums2[j]`:
        - `sum1 += nums1[i]`
        - `i += 1`
   - Else if `nums2[j] < nums1[i]`:
        - `sum2 += nums2[j]`
        - `j += 1`
   - Else (nums1[i] == nums2[j], a common element):
        - `ans += max(sum1, sum2) + nums1[i]`
        - `ans %= MOD`
        - Reset `sum1 = 0`, `sum2 = 0`
        - `i += 1`, `j += 1`

3. After the main loop, consume the remaining elements:
   - While `i < len(nums1)`: `sum1 += nums1[i]`, `i += 1`
   - While `j < len(nums2)`: `sum2 += nums2[j]`, `j += 1`

4. Add the final max segment:
   - `ans += max(sum1, sum2)`
   - Return `ans % MOD`

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time Complexity: **O(n + m)**  
  We traverse each array at most once with two pointers.

- Space Complexity: **O(1)**  
  Only a few variables are used; no extra data structures.

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------

```python
"""
class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        LeetCode 1537. Get the Maximum Score

        Args:
            nums1 (List[int]): strictly increasing sorted array
            nums2 (List[int]): strictly increasing sorted array

        Returns:
            int: maximum possible score modulo 10^9 + 7
        """
        MOD = 10**9 + 7
        i = j = 0
        sum1 = sum2 = 0
        ans = 0

        n1, n2 = len(nums1), len(nums2)

        # Walk through both arrays using two pointers
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                # nums1[i] == nums2[j] -> intersection point
                # Add the better path so far + this common value
                best_segment = max(sum1, sum2) + nums1[i]
                ans = (ans + best_segment) % MOD

                # Reset segment sums and move both pointers
                sum1 = 0
                sum2 = 0
                i += 1
                j += 1

        # Add remaining elements in nums1
        while i < n1:
            sum1 += nums1[i]
            i += 1

        # Add remaining elements in nums2
        while j < n2:
            sum2 += nums2[j]
            j += 1

        # Add the best of the final tail segment
        ans = (ans + max(sum1, sum2)) % MOD
        return ans

# ▶️ TEST HERE
if __name__ == "__main__":
    S = Solution()
    nums1 = [2,4,5,8,10]
    nums2 = [4,6,8,9]
    print(S.maxSum(nums1, nums2))  