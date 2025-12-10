"""
===========================================================
217. Contains Duplicate
===========================================================

🧩 Problem:
You are given an integer array `nums`.

Your task is to determine whether **any value appears at least twice** in the array.

Return:
    • True  → if the array contains a duplicate  
    • False → if all elements are distinct  

🎯 Goal:
Detect duplicates in the most efficient way.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  nums = [1,2,3,1]
Output: True
Explanation: 1 appears twice.

Example 2:
Input:  nums = [1,2,3,4]
Output: False

Example 3:
Input:  nums = [1,1,1,3,3,4,3,2,4,2]
Output: True

-----------------------------------------------------------
Algorithm — HashSet (Best & Optimal Approach):
-----------------------------------------------------------

Core Idea:
A set only stores **unique** values.

As we scan through `nums`:
    • If the number is already in the set → duplicate found → return True  
    • Otherwise, add it to the set and continue  

If we finish scanning with no duplicates → return False.

This gives O(n) performance.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)  
Space Complexity:  O(n) (set to track seen elements)

-----------------------------------------------------------
Python Implementation:
-----------------------------------------------------------

"""

class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False


print(Solution().containsDuplicate([1,2,3,1]))          # True
print(Solution().containsDuplicate([1,2,3,4]))          # False
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2]))  # True
