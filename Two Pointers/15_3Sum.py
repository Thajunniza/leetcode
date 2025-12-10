"""
===========================================================
15. 3Sum
===========================================================

🧩 Problem:
Given an integer array nums, return all the UNIQUE triplets 
[nums[i], nums[j], nums[k]] such that:

    i != j, i != k, j != k
    nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.

🎯 Goal:
Find all unique combinations of 3 numbers in the array that sum to 0.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 0], [-1, 0, 1]]
Explanation:
    Triplets that sum to 0:
    - [-1, -1, 2]  → 0
    - [-1, 0, 1]   → 0
    Unique triplets (sorted inside and as a set):
    [[-1, -1, 2], [-1, 0, 1]]

Example 2:
Input:  nums = [0, 1, 1]
Output: []
Explanation:
    No three numbers sum to 0.

Example 3:
Input:  nums = [0, 0, 0]
Output: [[0, 0, 0]]
Explanation:
    Only one valid triplet.

-----------------------------------------------------------
Algorithm — Sorting + Two Pointers:
-----------------------------------------------------------
1. Sort the array nums.

2. Loop over each index i from 0 to len(nums)-3:
       - Let current number be nums[i].
       - If i > 0 and nums[i] == nums[i-1]:
             → skip to avoid duplicate triplets starting with same value.

3. For each i, use TWO POINTERS:
       left  = i + 1
       right = len(nums) - 1

   While left < right:
       total = nums[i] + nums[left] + nums[right]

       - If total == 0:
             → We found a triplet [nums[i], nums[left], nums[right]]
             → Add it to the result list.
             → Move left and right to the next NEW values (skip duplicates).

       - If total < 0:
             → Need a larger sum → move left forward (left += 1)

       - If total > 0:
             → Need a smaller sum → move right backward (right -= 1)

4. Continue until all i are processed.

5. Return the result list of unique triplets.

-----------------------------------------------------------
⏱ Time Complexity:
- Sorting: O(n log n)
- Outer loop over i: O(n)
- Inner two-pointer scan per i: O(n)
- Total: O(n^2)

💾 Space Complexity:
- Sorting is in-place (if allowed): O(1) extra
- Result list holds the triplets: O(k) where k is number of triplets
-----------------------------------------------------------
"""


# ------------------------------------
# 3Sum — Sorting + Two Pointers
# ------------------------------------
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Return all unique triplets [a, b, c] in nums such that a + b + c == 0.

    Args:
        nums (List[int]): Input array of integers.

    Returns:
        List[List[int]]: List of unique triplets whose sum is 0.

    Example:
        >>> three_sum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
    """
    nums.sort()  # Step 1: Sort the array
    n = len(nums)
    result: List[List[int]] = []

    for i in range(n - 2):
        # Skip duplicate values for the first element of the triplet
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Move left pointer and skip duplicates
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Move right pointer and skip duplicates
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                # Need a larger sum -> move left forward
                left += 1
            else:
                # total > 0: Need a smaller sum -> move right backward
                right -= 1

    return result


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":

    print(three_sum([-1, 0, 1, 2, -1, -4]))   # [[-1, -1, 2], [-1, 0, 1]]
    print(three_sum([0, 1, 1]))               # []
    print(three_sum([0, 0, 0]))               # [[0, 0, 0]]
    print(three_sum([-2, 0, 1, 1, 2]))        # [[-2, 0, 2], [-2, 1, 1]]
