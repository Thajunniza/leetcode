"""
===========================================================
1. Two Sum
===========================================================

🧩 Problem:
Given an array of integers `nums` and an integer `target`,
return **indices** of the two numbers such that:

        nums[i] + nums[j] == target

Rules:
- Each input has exactly **one** solution.
- You may **not** use the same element twice.
- Return the answer in **any order**.

-----------------------------------------------------------
Example:
-----------------------------------------------------------
Input:
    nums   = [2, 7, 11, 15]
    target = 9

Output: [0, 1]

Explanation:
2 + 7 = 9

===========================================================
🔍 Pattern:
HashMap (Dictionary) Lookup  
→ fastest way  
→ one-pass scanning  
→ store {number: index}

-----------------------------------------------------------
🧠 Best Approach: One-Pass HashMap
-----------------------------------------------------------
1. Create an empty hashmap `seen`.
2. Iterate through array:
       For each number `x` at index `i`:
          complement = target - x
          If complement exists in `seen`, return [seen[complement], i]
3. Otherwise store `seen[x] = i`
4. Guaranteed to find exactly one solution.

-----------------------------------------------------------
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  O(n)  
Space: O(n)

===========================================================
✅ Python Solution (LeetCode style)
===========================================================
from typing import List
"""
class Solution:
    def twoSum(self, nums, target: int):
        seen = {}

        for i, x in enumerate(nums):
            diff = target - x
            if diff in seen:
                return [seen[diff], i]
            seen[x] = i

        return []   # Normally never reached



# Example run
if __name__ == "__main__":
    S = Solution()
    nums   = [2, 7, 11, 15]
    target = 9

    print("Input    :", nums)
    print("Target   :", target)
    print("Two Sum  :", S.twoSum(nums, target))

# Expected:
# Two Sum: [0, 1]

 
