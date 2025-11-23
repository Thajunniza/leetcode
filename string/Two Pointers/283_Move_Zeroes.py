""" 
===========================================================
283. Move Zeroes
===========================================================

🧩 Problem:
Given an integer array `nums`, move all **0**'s to the **end** of the array while keeping the **relative order** of the non-zero elements.

You must perform the operation **in-place**, without making a copy of the array.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    nums = [0,1,0,3,12]

Process:
    Move all non-zero elements forward in order:
        → [1,3,12,_,_]
    Fill the remaining positions with zero:
        → [1,3,12,0,0]

Output:
    [1,3,12,0,0]


Example 2:
Input:
    nums = [0]

Output:
    [0]

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Shift all non-zero elements to the **front**, in their original order,  
and move all zeroes to the **end**, with no extra space used.

Pattern / Folder:
    • Pattern: Two Pointers (Compaction)
    • Folder suggestion:
        /TwoPointers/283-MoveZeroes/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

Use **two pointers**:
- `i` → scans every element
- `p` → position where the next non-zero element should be written

Algorithm idea:
1. When you see a **non-zero**, write it at position `p`
2. If it came from a different index (`i != p`), set `nums[i] = 0`
3. Increment `p`
4. Continue scanning until the end

This effectively:
- Compacts non-zero elements at the front
- Pushes all zeros to the back
- Preserves relative order

-----------------------------------------------------------
🧠 Algorithm (Two Pointers – In-place Rewrite):
-----------------------------------------------------------

1. Initialize:
       p = 0       # next index to fill with non-zero
       i = 0       # scan pointer

2. While i < n:
       if nums[i] != 0:
           nums[p] = nums[i]
           if i != p:
               nums[i] = 0
           p += 1
       i += 1

3. Array is now modified such that:
       - all non-zeros are in front
       - all zeros are at the end
       - order is preserved

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time Complexity:  **O(n)**
- Space Complexity: **O(1)**  
  (Everything is done in-place)

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        LeetCode 283. Move Zeroes

        Args:
            nums (List[int]): input array
            
        Returns:
            None: modifies nums in-place
        """
        p = 0
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] != 0:
                nums[p] = nums[i]
                if i != p:
                    nums[i] = 0
                p += 1
            i += 1


# ▶️ TEST HERE
if __name__ == "__main__":
    S = Solution()
    nums = [0,1,0,3,12]
    S.moveZeroes(nums)
    print(nums)   # Expected: [1,3,12,0,0]
