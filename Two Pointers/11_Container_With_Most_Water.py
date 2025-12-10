"""
===========================================================
11. Container With Most Water
===========================================================

🧩 Problem:
You are given `n` non-negative integers `height[i]` where each represents a vertical line on the x-axis.

Your task:
- Find **two lines** that together with the x-axis form a container.
- The container should hold the **maximum amount of water**.

Return the **maximum area** of water that can be contained.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    height = [1,8,6,2,5,4,8,3,7]

Process:
    - Lines at index 1 and 8:
        min(height[1], height[8]) = min(8,7) = 7
        width = 8 - 1 = 7
        area = 7 * 7 = 49

Output:
    49

Example 2:
Input:
    height = [1,1]

Output:
    1

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Maximize:
    area = min(height[left], height[right]) * (right - left)

Pattern / Folder:
    • Pattern: Two Pointers
    • Folder suggestion:
        /TwoPointers/11-ContainerWithMostWater/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

Brute force:
- Check all pairs → O(n²) → too slow for large n.

Optimal approach:
- Use **two pointers**:
    - Start at both ends (`left = 0`, `right = n-1`)
    - Compute area
    - Move the pointer pointing to the **shorter line** inward:
        - Because moving the taller line inward cannot increase area (width decreases, height stays same or decreases)
        - Moving the shorter line might find a taller line and increase area

Repeat until pointers meet.

-----------------------------------------------------------
🧠 Algorithm (Two Pointers):
-----------------------------------------------------------

1. Initialize:
       left = 0
       right = n - 1
       result = 0

2. While left < right:
       area = min(height[left], height[right]) * (right - left)
       result = max(result, area)

       # Move the pointer pointing to the smaller height
       if height[left] < height[right]:
           left += 1
       else:
           right -= 1

3. Return result.

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
class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        LeetCode 11. Container With Most Water
        Two-pointer optimal solution.

        Args:
            height (List[int]): heights of vertical lines

        Returns:
            int: maximum water area
        """
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            result = max(result, area)

            # Move the pointer pointing to the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result


# ▶️ TEST CASES
if __name__ == "__main__":
    S = Solution()

    h1 = [1,8,6,2,5,4,8,3,7]
    print(S.maxArea(h1))  # Expected: 49

    h2 = [1,1]
    print(S.maxArea(h2))  # Expected: 1
