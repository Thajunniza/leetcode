"""
===========================================================
1929. Concatenation of Array
===========================================================

🧩 Problem:
You are given an integer array `nums` of length `n`.

Your task is to create a new array `ans` of length **2n**, where:
    ans[i]     = nums[i]       for 0 ≤ i < n  
    ans[i + n] = nums[i]       for 0 ≤ i < n  

In simple terms:
Repeat the array twice.

🎯 Goal:
Return the concatenated array:
    ans = nums + nums

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  nums = [1,2,1]
Output: [1,2,1,1,2,1]

Example 2:
Input:  nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]

-----------------------------------------------------------
Algorithm — Index Mapping (Best Approach):
-----------------------------------------------------------

Core Idea:
We know the final array size = 2 * n.

For each i in range(n):
    ans[i]     = nums[i]
    ans[i + n] = nums[i]

This directly builds the result array in O(n) time.

This is the optimal solution.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)  
Space Complexity:  O(n) (result array of size 2n)

-----------------------------------------------------------
Python Implementation:
-----------------------------------------------------------

"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (2 * n)
        for i in range(n):
            result[i] = nums[i]
            result[i + n] = nums[i]
        return result

# -----------------------------------------------------------
# Driver Test
# -----------------------------------------------------------
print(Solution().getConcatenation([1,2,1]))     # [1,2,1,1,2,1]
print(Solution().getConcatenation([1,3,2,1]))   # [1,3,2,1,1,3,2,1]
