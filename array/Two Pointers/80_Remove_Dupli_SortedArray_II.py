"""
===========================================================
80. Remove Duplicates From Sorted Array II
===========================================================

🧩 Problem:
You are given a **sorted array** `nums`.  
Your task is to **remove duplicates in-place** so that each unique element appears **at most twice**.

You must:
- Modify the array **in-place**
- Keep the **relative order** of elements
- Return the **new length** `k`  
  (the first `k` values of nums must contain the final result)

-----------------------------------------------------------
Example:
-----------------------------------------------------------
Input:  nums = [1,1,1,2,2,3]  
Output: 5  
Modified nums = [1,1,2,2,3,_,_]

Explanation:
- `1` appears 3 times → keep only 2  
- `2` appears 2 times → allowed  
- `3` appears 1 time → allowed  

-----------------------------------------------------------
🔍 Pattern:
Two Pointers  
→ slow pointer = position to write  
→ fast pointer = iterate through array  
→ allow each number max 2 times

-----------------------------------------------------------
🧠 Algorithm (Two Pointers):
-----------------------------------------------------------
1. If array length ≤ 2 → return length  
2. Create pointer `slow = 2`  
3. Iterate `fast` from index 2 to end  
4. For every number:
      If nums[fast] != nums[slow-2],  
      then write nums[fast] at nums[slow] and move slow++
5. Return slow (new length)

-----------------------------------------------------------
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  O(n)  
Space: O(1)

===========================================================
-----------------------------------------------------------
✅ Python Solution
-----------------------------------------------------------
"""
def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    slow = 2

    for fast in range(2, len(nums)):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1

    return slow


# -----------------------------
# Run & Print Output
# -----------------------------
nums = [1, 1, 1, 2, 2, 3]
k = removeDuplicates(nums)

print("New Length:", k)
print("Modified Array:", nums[:k])