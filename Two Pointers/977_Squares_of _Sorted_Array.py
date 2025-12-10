"""
===========================================================
977. Squares of a Sorted Array
===========================================================

🧩 Problem:
Given an integer array nums sorted in **non-decreasing order**, 
return an array of the **squares of each number**, also sorted 
in non-decreasing order.

Note: nums can contain negative numbers.

🎯 Goal:
Because squaring negative numbers can make large positives,
we must handle both left (negative) and right (positive) sides
carefully and still produce a sorted result in O(n).

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
Explanation:
    Squares: [16, 1, 0, 9, 100]
    Sorted:  [0, 1, 9, 16, 100]

Example 2:
Input:  nums = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]

Example 3:
Input:  nums = [0]
Output: [0]

-----------------------------------------------------------
Algorithm — Two Pointers from Ends:
-----------------------------------------------------------
Idea:
- The largest square will come from either:
    - The most negative number (left side), or
    - The largest positive number (right side)

Steps:
1. Initialize:
       left  = 0
       right = len(nums) - 1
       result = [0] * len(nums)   (to fill from end)

2. Start from the END of result:
       idx = len(nums) - 1

3. While left <= right:
       left_sq  = nums[left]  * nums[left]
       right_sq = nums[right] * nums[right]

       - If left_sq > right_sq:
             result[idx] = left_sq
             left += 1
       - Else:
             result[idx] = right_sq
             right -= 1

       idx -= 1   (fill result from back to front)

4. Return result.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(n) for result
-----------------------------------------------------------
"""


# --------------------------------------------
# 977. Squares of a Sorted Array (Two Pointers)
# --------------------------------------------
from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    """
    Return a sorted array of the squares of each number in nums.

    Args:
        nums (List[int]): Sorted list of integers (may include negatives).

    Returns:
        List[int]: Sorted list of squared values.

    Example:
        >>> sorted_squares([-4, -1, 0, 3, 10])
        [0, 1, 9, 16, 100]
    """
    n = len(nums)
    result = [0] * n

    left = 0
    right = n - 1
    idx = n - 1  # Fill result from the back

    while left <= right:
        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]

        if left_sq > right_sq:
            result[idx] = left_sq
            left += 1
        else:
            result[idx] = right_sq
            right -= 1

        idx -= 1

    return result


# --------------------------------------------
# Driver Test
# --------------------------------------------
if __name__ == "__main__":

    print(sorted_squares([-4, -1, 0, 3, 10]))   # [0, 1, 9, 16, 100]
    print(sorted_squares([-7, -3, 2, 3, 11]))   # [4, 9, 9, 49, 121]
    print(sorted_squares([0]))                  # [0]
    print(sorted_squares([-2, -1]))             # [1, 4]
