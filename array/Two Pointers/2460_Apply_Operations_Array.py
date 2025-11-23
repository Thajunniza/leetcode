""" 
===========================================================
2460. Apply Operations to an Array
===========================================================

🧩 Problem:
You are given a **0-indexed** array of integers `nums`.

You need to perform the following operations **in order**:

1️⃣ For each index `i` from `0` to `len(nums) - 2`:
    - If `nums[i] == nums[i + 1]`, then:
        - Set `nums[i] = 2 * nums[i]`
        - Set `nums[i + 1] = 0`

2️⃣ After completing step 1 for the whole array:
    - **Move all zeros to the end** of the array
    - Keep the **relative order of non-zero elements** the same

Return the resulting array `nums`.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    nums = [1,2,2,1,1,0]

Step 1 (apply operations):
    i = 0: [1,2,2,1,1,0]   → nums[0] != nums[1]
    i = 1: [1,2,2,1,1,0]   → nums[1] == nums[2] → [1,4,0,1,1,0]
    i = 3: [1,4,0,1,1,0]   → nums[3] == nums[4] → [1,4,0,2,0,0]

Step 2 (move zeros to end, stable):
    [1,4,2,0,0,0]

Output:
    [1,4,2,0,0,0]


Example 2:
Input:
    nums = [0,1]

Step 1:
    i = 0: nums[0] != nums[1] → [0,1]

Step 2 (move zeros to end):
    [1,0]

Output:
    [1,0]

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

- Apply the transformation rules:
    • Combine equal adjacent elements into double at the left index  
    • Set the right one to 0  
- Then **shift all zeros to the end** of the array
- While **preserving order** of non-zero elements

Pattern / Folder:
    • Pattern: Two Pointers, In-place Transformation
    • Folder suggestion:
        /TwoPointers/2460-ApplyOperationsToArray/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

We can solve this in **two clear passes**:

1️⃣ **First pass – Apply merge operations:**
   - Loop with index `i` from `0` to `n - 2`
   - If `nums[i] == nums[i+1]`:
        - Double `nums[i]`
        - Set `nums[i+1] = 0`
        - Skip the next index (`i += 2`) because `nums[i+1]` is zero and we shouldn't chain it
   - Else: just move to next index (`i += 1`)

2️⃣ **Second pass – Move zeros to the end (stable):**
   - Use a **two-pointer compaction pattern**:
       - `p` → the position to place the next non-zero
       - Iterate `i` from `0` to `n - 1`:
           • If `nums[i] != 0`:
               - Swap `nums[i]` and `nums[p]`
               - Increment `p`
   - This keeps the relative order of non-zero elements.

This approach is clean, in-place, and O(n).

-----------------------------------------------------------
🧠 Algorithm (Two-Pass + Two Pointers):
-----------------------------------------------------------

1. Let `n = len(nums)`.

2. First pass – apply operations:
       i = 0
       while i < n - 1:
           if nums[i] == nums[i + 1]:
               nums[i] = 2 * nums[i]
               nums[i + 1] = 0
               i += 2      # skip next index
           else:
               i += 1

3. Second pass – move zeros to end:
       p = 0  # next position to place non-zero
       for i in range(n):
           if nums[i] != 0:
               nums[p], nums[i] = nums[i], nums[p]
               p += 1

4. Return nums.

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

Let `n = len(nums)`:

- Time Complexity:  **O(n)**
  - First pass: O(n)
  - Second pass: O(n)

- Space Complexity: **O(1)**
  - In-place updates only

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution(object):
    def applyOperations(self, nums):
        """
        LeetCode 2460. Apply Operations to an Array

        Apply pair merge operations, then move all zeros
        to the end while preserving the order of non-zero elements.
        """
        n = len(nums)

        # Step 1: Apply operations
        i = 0
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                i += 2
            else:
                i += 1

        # Step 2: Move zeros to the end (stable)
        p = 0  # position to put next non-zero element
        for i in range(n):
            if nums[i] != 0:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        return nums


# ▶️ TEST HERE
if __name__ == "__main__":
    S = Solution()

    nums1 = [1,2,2,1,1,0]
    print(S.applyOperations(nums1))   # Expected: [1,4,2,0,0,0]

    nums2 = [0,1]
    print(S.applyOperations(nums2))   # Expected: [1,0]

