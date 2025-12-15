"""
2444. Count Subarrays With Fixed Bounds
===========================================================

🧩 Problem:
You are given an integer array `nums` and two integers `minK` and `maxK`.

Your task:
- Count the number of **subarrays** such that:
    - The **minimum value** in the subarray is exactly `minK`
    - The **maximum value** in the subarray is exactly `maxK`

Return the **total number of valid subarrays**.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    nums = [1,3,5,2,7,5]
    minK = 1
    maxK = 5

Process:
    Valid subarrays must:
        - Contain at least one `1`
        - Contain at least one `5`
        - Contain NO values < 1 or > 5

Valid subarrays:
    [1,3,5]
    [1,3,5,2]
    [1,3,5,2]
    [1,3,5]
    ...

Output:
    2

Example 2:
Input:
    nums = [1,1,1,1]
    minK = 1
    maxK = 1

Output:
    10

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Count all subarrays where:
    min(subarray) == minK
    max(subarray) == maxK

-----------------------------------------------------------
Pattern / Folder:
-----------------------------------------------------------

• Pattern: Sliding Window / One Pass
• Folder suggestion:
    /SlidingWindow/2444-CountSubarraysWithFixedBounds/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

Brute force:
- Generate all subarrays → O(n²)
- Check min and max for each → O(n)
- Total O(n³) → too slow

Optimal idea:
- Traverse array once
- Track:
    - Last position of `minK`
    - Last position of `maxK`
    - Last position of an **invalid element**

For each index:
- Count how many valid subarrays **end at this index**

-----------------------------------------------------------
🧠 Algorithm (One Pass):
-----------------------------------------------------------

Maintain three pointers:
    minpt     → last index where nums[i] == minK
    maxpt     → last index where nums[i] == maxK
    invalid   → last index where nums[i] < minK or nums[i] > maxK

1. Initialize:
       minpt = -1
       maxpt = -1
       invalid = -1
       count = 0

2. Iterate i from 0 to n-1:

       If nums[i] is invalid:
           invalid = i
           reset minpt and maxpt

       If nums[i] == minK:
           minpt = i

       If nums[i] == maxK:
           maxpt = i

       If both minpt and maxpt are valid:
           valid_subarrays_ending_here =
               min(minpt, maxpt) - invalid
           add to count

3. Return count

-----------------------------------------------------------
🧠 Why min(minpt, maxpt) - invalid works:
-----------------------------------------------------------

For subarrays ending at index `i`:
- Start must be AFTER `invalid`
- Start must be BEFORE or AT the earlier of `minK` or `maxK`

Valid start range:
    (invalid + 1) → min(minpt, maxpt)

Number of valid starts:
    min(minpt, maxpt) - invalid

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time Complexity:
    • O(n) → single pass
- Space Complexity:
    • O(1)

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        minpt = maxpt = invalid = -1
        count = 0

        for i, x in enumerate(nums):
            if x < minK or x > maxK:
                invalid = i
                minpt = maxpt = -1
                continue

            if x == minK:
                minpt = i
            if x == maxK:
                maxpt = i

            if minpt != -1 and maxpt != -1:
                count += min(minpt, maxpt) - invalid

        return count
    
# ▶️ TEST CASES
if __name__ == "__main__":
    S = Solution()

    print(S.countSubarrays([1,3,5,2,7,5], 1, 5))  # Expected: 2
    print(S.countSubarrays([1,5], 1, 5))          # Expected: 1
    print(S.countSubarrays([1,1,1,1], 1, 1))      