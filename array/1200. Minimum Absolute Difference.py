# =====================================================================
# 1200: Minimum Absolute Difference
# Given an array of distinct integers, arr, find all pairs of elements 
# with the minimum absolute difference of any two elements. 
# Return the pairs in ascending order.
# =====================================================================

from typing import List

class Solution:
    """
    Algorithm:
    1. Sort the array. After sorting, the minimum absolute difference
       must occur between adjacent elements.
    2. Iterate through the sorted array:
        - Calculate the difference between arr[i] and arr[i-1]
        - If difference < min_diff, reset result list and update min_diff
        - If difference == min_diff, append the pair to result
    3. Return the result list.

    Time Complexity: O(n log n) -> Sorting dominates
    Space Complexity: O(n) -> Result list storing pairs
    """

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()  # Step 1: Sort array
        min_diff = float("inf")
        result = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]  # No abs() needed after sorting

            if diff < min_diff:
                min_diff = diff
                result = [[arr[i - 1], arr[i]]]
            elif diff == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result


# ===========================
# Test Case
# ===========================
if __name__ == "__main__":
    sol = Solution()

    arr = [3, 8, -10, 23, 19, -4, -14, 27]
    # Sorted: [-14, -10, -4, 3, 8, 19, 23, 27]
    # Minimum absolute difference = 4
    # Expected output: [[-14, -10], [19, 23], [23, 27]]

    output = sol.minimumAbsDifference(arr)
    print("Input:", arr)
    print("Output:", output)
    # Output should be: [[-14, -10], [19, 23], [23, 27]]