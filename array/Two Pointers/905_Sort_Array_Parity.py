""" 
===========================================================
905. Sort Array By Parity
===========================================================

🧩 Problem:
You are given an integer array `nums`.  
Your task:
Rearrange the array so that all **even** integers come before all **odd** integers.

You may return the result **in any order**, but:
- Even numbers must appear first
- Odd numbers must appear after

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    nums = [3,1,2,4]

Possible Output:
    [2,4,3,1]
    (evens first, odds next)

Example 2:
Input:
    nums = [0]

Output:
    [0]

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Rearrange the array such that:
- All even numbers appear first
- All odd numbers appear after
- Can be done **in-place**

Pattern / Folder:
    • Pattern: Two Pointers (Partition)
    • Folder:  /TwoPointers/905-SortArrayByParity/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

Use **two pointers**:
- `p` starts at the beginning (left side)
- `q` starts at the end (right side)

While `p < q`:
- If nums[p] is even → it's already in the correct side → move p forward
- If nums[q] is odd  → it's already in the correct side → move q backward
- Else:
    - nums[p] is odd and nums[q] is even → swap them

This partitions the array in-place into evens first, odds later.

-----------------------------------------------------------
🧠 Algorithm (Two Pointer Partition):
-----------------------------------------------------------

1. Initialize:
       p = 0
       q = len(nums) - 1

2. While p < q:
       if nums[p] is even:
           p += 1
       elif nums[q] is odd:
           q -= 1
       else:
           swap nums[p] and nums[q]
           p += 1
           q -= 1

3. Return nums

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time Complexity:  **O(n)**
- Space Complexity: **O(1)**
  (in-place rearrangement)

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        LeetCode 905. Sort Array By Parity
        Two-pointer in-place partitioning
        """
        p = 0
        q = len(nums) - 1

        while p < q:
            if nums[p] % 2 == 0:
                p += 1
            elif nums[q] % 2 == 1:
                q -= 1
            else:
                nums[p], nums[q] = nums[q], nums[p]
                p += 1
                q -= 1

        return nums


# ▶️ TEST HERE
if __name__ == "__main__":
    S = Solution()
    print(S.sortArrayByParity([3,1,2,4]))   # Example output: [2,4,3,1]
    print(S.sortArrayByParity([0]))         # Output: [0]

