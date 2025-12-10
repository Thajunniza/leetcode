"""
===========================================================
88. Merge Sorted Array
===========================================================

🧩 Problem:
You are given two sorted integer arrays `nums1` and `nums2` where:
- `nums1` has a length of **m + n**
- The **first m** elements of `nums1` are valid
- The **last n** elements are **zeros**, acting as buffer space
- `nums2` has **n** elements

Your task:
Merge `nums2` into `nums1` **in-place** so that `nums1` becomes a **single sorted array**.

You must modify `nums1` directly and **not** return anything.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],      n = 3

Process:
- Compare from the back:
      nums1[2] = 3
      nums2[2] = 6 → place 6 at end
- Continue moving backwards…

Final nums1:
    [1,2,2,3,5,6]

Output:
    nums1 = [1,2,2,3,5,6]


Example 2:
Input:
    nums1 = [1], m = 1
    nums2 = [],  n = 0

Output:
    [1]

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Merge the two sorted arrays **from the end** to avoid overwriting useful data.

Pattern / Folder:
    • Pattern: Two Pointers (Backward Merge)
    • Folder suggestion:
        /TwoPointers/88-MergeSortedArray/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

Instead of merging from the front (which causes overwriting), merge from the **back**:

Have 3 pointers:
- `p1 = m - 1` → last valid element in nums1  
- `p2 = n - 1` → last element in nums2  
- `p = m + n - 1` → last position of nums1 (write position)

While both arrays still have elements:
- Compare nums1[p1] and nums2[p2]
- Place the **bigger one** into nums1[p]
- Move pointers backward

Finally, if nums2 has leftover elements, copy them to the front.

-----------------------------------------------------------
🧠 Algorithm (Two Pointer Backward):
-----------------------------------------------------------

1. Set:
       p1 = m - 1
       p2 = n - 1
       p  = m + n - 1

2. While p1 >= 0 and p2 >= 0:
       if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
       else:
            nums1[p] = nums2[p2]
            p2 -= 1
       p -= 1

3. Copy remaining nums2 elements (if any):
       while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1

4. nums1 now contains the merged sorted array.

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time Complexity:  **O(m + n)**
- Space Complexity: **O(1)**  
  (In-place merge)

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        LeetCode 88. Merge Sorted Array

        Args:
            nums1 (List[int]): first sorted array with buffer space
            m (int): number of valid elements in nums1
            nums2 (List[int]): second sorted array
            n (int): number of elements in nums2

        Returns:
            None: modifies nums1 in-place
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # Merge from the back
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Copy remaining nums2 values (if any)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1


# ▶️ TEST HERE
if __name__ == "__main__":
    S = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    S.merge(nums1, 3, nums2, 3)
    print(nums1)   # Output: [1,2,2,3,5,6]

