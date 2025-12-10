""" 
===========================================================
2161. Partition Array According to Given Pivot
===========================================================

🧩 Problem:
You are given an integer array `nums` and an integer `pivot`.

Rearrange `nums` so that:
1. All elements **less than** `pivot` come **before** elements equal to `pivot`.
2. All elements **equal to** `pivot` come **before** elements **greater than** `pivot`.
3. The **relative order** of elements in each group (**< pivot**, **= pivot**, **> pivot**) is **preserved**.

Return the **rearranged array** (you can use extra space).

-----------------------------------------------------------
Example:
-----------------------------------------------------------
Input:
    nums  = [9,12,5,10,14,3,10]
    pivot = 10

Output:
    [9,5,3,10,10,12,14]

Explanation:
    - Elements < 10 → [9,5,3]
    - Elements = 10 → [10,10]
    - Elements > 10 → [12,14]
    Keep order inside each group and then concatenate.

-----------------------------------------------------------
🔍 Pattern:
Array Partition / 3-Bucket (variation of Two Pointers idea)

- We need **three groups**:
  - `less`   → all nums[i] < pivot
  - `equal`  → all nums[i] == pivot
  - `greater`→ all nums[i] > pivot
- Important: **stable** order inside each group ➝ easier to use **extra arrays** and then join.

-----------------------------------------------------------
🧠 Algorithm:
-----------------------------------------------------------
1. Create three empty lists: `less`, `equal`, `greater`.
2. Loop through each number `x` in `nums`:
      - If `x < pivot`  → append to `less`
      - If `x == pivot` → append to `equal`
      - If `x > pivot`  → append to `greater`
3. Return `less + equal + greater`.

Time:  O(n) — single pass through array  
Space: O(n) — extra arrays for 3 buckets

-----------------------------------------------------------
✅ Python Solution (LeetCode style)
-----------------------------------------------------------
from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []

        for x in nums:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)

        return less + equal + greater

-----------------------------------------------------------
▶️ Runnable Code with Output
-----------------------------------------------------------
"""
def pivotArray(nums, pivot):
    less = []
    equal = []
    greater = []

    for x in nums:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    return less + equal + greater


# Example run
nums  = [9, 12, 5, 10, 14, 3, 10]
pivot = 10

result = pivotArray(nums, pivot)
print("Input nums :", nums)
print("Pivot      :", pivot)
print("Result     :", result)

# Expected:
# Input nums : [9, 12, 5, 10, 14, 3, 10]
# Pivot      : 10
# Result     : [9, 5, 3, 10, 10, 12, 14]



