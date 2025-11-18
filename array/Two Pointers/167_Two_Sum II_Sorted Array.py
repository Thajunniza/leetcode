""" 
===========================================================
167. Two Sum II — Input Array Is Sorted
===========================================================

🧩 Problem:
Given a **1-indexed**, **sorted** array of integers numbers,  
find two numbers such that they add up to a specific target number.

Return the **indices (1-based)** of the two numbers as a list [i, j].

You must use **only constant extra space**.

🎯 Goal:
Use the sorted property + two pointers to find the pair in O(n) time.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
Explanation:
    2 + 7 = 9 → indices 1 and 2

Example 2:
Input:  numbers = [2, 3, 4], target = 6
Output: [1, 3]

Example 3:
Input:  numbers = [-1, 0], target = -1
Output: [1, 2]

-----------------------------------------------------------
Algorithm — Two Pointers:
-----------------------------------------------------------
1. Initialize two pointers:
       left  = 0
       right = len(numbers) - 1

2. While left < right:
       sum = numbers[left] + numbers[right]

       - If sum == target:
             → return [left + 1, right + 1] (1-indexed)

       - If sum < target:
             → Move left forward (need larger sum)

       - If sum > target:
             → Move right backward (need smaller sum)

3. If no pair is found, return [].

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

# --------------------------------------------
# 167. Two Sum II — Input Array Is Sorted
# Two Pointers Approach
# --------------------------------------------
from typing import List


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """
    Given a 1-indexed sorted array, return indices of the two
    numbers such that they add up to target.

    Args:
        numbers (List[int]): Sorted list of integers.
        target (int): Target sum.

    Returns:
        List[int]: 1-indexed result [i, j].

    Example:
        >>> two_sum_sorted([2, 7, 11, 15], 9)
        [1, 2]
    """
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed

        elif current_sum < target:
            left += 1  # need bigger sum

        else:  # current_sum > target
            right -= 1  # need smaller sum

    return []


# --------------------------------------------
# Driver Test
# --------------------------------------------
if __name__ == "__main__":

    print(two_sum_sorted([2, 7, 11, 15], 9))     # [1, 2]
    print(two_sum_sorted([2, 3, 4], 6))          # [1, 3]
    print(two_sum_sorted([-1, 0], -1))           # [1, 2]
    print(two_sum_sorted([1, 2, 3, 4], 8))       # [] (no pair)
