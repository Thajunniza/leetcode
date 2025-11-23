""" 
===========================================================
26. Remove Duplicates from Sorted Array
===========================================================

🧩 Problem:
You are given an integer array `nums` sorted in **non-decreasing order**.

Your task:
Remove the **duplicates in-place** such that each unique element appears **only once**.
The **relative order** of the elements should be kept the same.

After removing duplicates, the first `k` elements of `nums` should hold the final result.
It does **not** matter what you leave beyond index `k - 1`.

Return `k` — the number of unique elements.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    nums = [1,1,2]

Process:
    Unique elements: [1,2]
    Place them at the beginning of nums:
        nums = [1,2,_]

Output:
    k = 2
    nums = [1,2, _]


Example 2:
Input:
    nums = [0,0,1,1,1,2,2,3,3,4]

Process:
    Unique sequence: [0,1,2,3,4]
    Place them at the beginning:
        nums = [0,1,2,3,4,_,_,_,_,_]

Output:
    k = 5
    nums = [0,1,2,3,4,_,_,_,_,_]

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

- Keep **only one copy** of each value in the sorted array.
- Modify `nums` **in-place** so that:
    • First `k` positions contain the unique elements  
    • Return `k`

Pattern / Folder:
    • Pattern: Two Pointers (Slow/Fast)
    • Folder suggestion:
        /TwoPointers/26-RemoveDuplicatesFromSortedArray/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

Because the array is **sorted**, duplicates are always **next to each other**.

Use a **two-pointer** approach:
- `p` → slow pointer, points to the position of the **last unique element**
- `i` → fast pointer, scans through the array

For each index `i`:
- If `nums[i] != nums[p]`, we found a **new unique element**:
    - Move `p` forward
    - Write `nums[i]` into `nums[p]`

At the end:
- All unique values are stored from `nums[0]` to `nums[p]`
- The answer `k` is `p + 1`

-----------------------------------------------------------
🧠 Algorithm (Two Pointers – Unique Compaction):
-----------------------------------------------------------

1. Edge case:
       If nums is empty, return 0

2. Initialize:
       p = 0   # index of last unique element

3. Loop i from 1 to n - 1:
       if nums[i] != nums[p]:
           p += 1
           nums[p] = nums[i]

4. Number of unique elements = p + 1  
   Return p + 1.

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time Complexity:  **O(n)**
- Space Complexity: **O(1)**  
  (In-place, no extra data structure)

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        LeetCode 26. Remove Duplicates from Sorted Array

        Args:
            nums (List[int]): sorted input array

        Returns:
            int: number of unique elements (k)
        """
        n = len(nums)
        if n == 0:
            return 0

        p = 0  # last unique element index

        for i in range(1, n):
            if nums[i] != nums[p]:
                p += 1
                nums[p] = nums[i]

        return p + 1


# ▶️ TEST HERE
if __name__ == "__main__":
    S = Solution()

    nums1 = [1,1,2]
    k1 = S.removeDuplicates(nums1)
    print(k1, nums1[:k1])   # Expected: 2 [1, 2]

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = S.removeDuplicates(nums2)
    print(k2, nums2[:k2])   # Expected: 5 [0, 1, 2, 3, 4]

