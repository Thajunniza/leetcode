"""
===========================================================
238. Product of Array Except Self
===========================================================

🧩 Problem:
Given an integer array nums, return an array answer such that:

answer[i] is equal to the product of all the elements of nums 
except nums[i].

The solution must:
- Run in O(n) time
- Not use division
- Use constant extra space (excluding output array)

-----------------------------------------------------------
Example :
-----------------------------------------------------------
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

-----------------------------------------------------------
Brute Force Approach:
-----------------------------------------------------------
For each index i:
    - Multiply all elements except nums[i]

Problems:
- O(n²) time
- Too slow for large input sizes

-----------------------------------------------------------
⏱️ Time & Space Complexity (Brute Force)
-----------------------------------------------------------
Time:  O(n²)
Space: O(1)

-----------------------------------------------------------
🧠 Optimal Approach: Prefix & Suffix Products
-----------------------------------------------------------

Key Insight:
For each index i:

answer[i] = (product of elements before i) *
            (product of elements after i)

We compute:
1. Prefix products in first pass.
2. Multiply with suffix products in second pass.

No division needed.
Handles zeros naturally.

-----------------------------------------------------------
Algorithm:
-----------------------------------------------------------
1. Initialize result array with 1s.
2. Traverse left to right:
      - Store prefix product.
3. Traverse right to left:
      - Multiply with suffix product.
4. Return result.

-----------------------------------------------------------
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  O(n)
Space: O(1) extra space (excluding output array)
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n

        # -----------------------------
        # Prefix Pass (Left Products)
        # -----------------------------
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # -----------------------------
        # Suffix Pass (Right Products)
        # -----------------------------
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


# -----------------------------------------------------------
# Driver Code
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print("=== Example 1 ===")
    nums = [1, 2, 3, 4]
    result = sol.productExceptSelf(nums)
    print(f"Input:  {nums}")
    print(f"Output: {result}")
    print("Expected: [24, 12, 8, 6]")

    print("\n=== Example 2 ===")
    nums = [-1, 1, 0, -3, 3]
    result = sol.productExceptSelf(nums)
    print(f"Input:  {nums}")
    print(f"Output: {result}")
    print("Expected: [0, 0, 9, 0, 0]")

    print("\n=== Example 3 (Single Zero) ===")
    nums = [1, 2, 0, 4]
    result = sol.productExceptSelf(nums)
    print(f"Input:  {nums}")
    print(f"Output: {result}")
    print("Expected: [0, 0, 8, 0]")

    print("\n=== Example 4 (Multiple Zeros) ===")
    nums = [0, 2, 0, 4]
    result = sol.productExceptSelf(nums)
    print(f"Input:  {nums}")
    print(f"Output: {result}")
    print("Expected: [0, 0, 0, 0]")