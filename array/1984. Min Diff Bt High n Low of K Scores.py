"""
1984: Minimum Difference Between Highest and Lowest of K Scores
------------------------------------------------------------
Problem Statement:
------------------------------------------------------------
Given an integer array `nums` and an integer `k`,
select exactly `k` elements such that the difference between
the maximum and minimum elements is minimized.

Return this minimum possible difference.

------------------------------------------------------------
Example:
------------------------------------------------------------
Input:
    nums = [9, 4, 1, 7]
    k = 2

Sorted nums:
    [1, 4, 7, 9]

Possible groups of size k:
    [1, 4] -> difference = 3
    [4, 7] -> difference = 3
    [7, 9] -> difference = 2

Output:
    2

------------------------------------------------------------
Key Insight:
------------------------------------------------------------
After sorting, the minimum difference for any k elements
must occur between k consecutive elements.

So we only need to check all contiguous windows of size k.
"""

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        Algorithm:
        1. If k == 1, return 0 (single element has no difference).
        2. Sort the array.
        3. Slide a window of size k across the array.
        4. For each window, compute:
              nums[i + k - 1] - nums[i]
        5. Return the minimum difference found.
        """

        # Edge case
        if k == 1:
            return 0

        # Step 1: Sort the array
        nums.sort()

        # Step 2: Initialize minimum difference
        min_diff = float("inf")

        # Step 3: Sliding window
        for i in range(len(nums) - k + 1):
            current_diff = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, current_diff)

        return min_diff


# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------
def run_tests():
    solution = Solution()

    # Test case 1
    nums = [9, 4, 1, 7]
    k = 2
    print("Test 1:", solution.minimumDifference(nums, k))  # Expected: 2

    # Test case 2
    nums = [90]
    k = 1
    print("Test 2:", solution.minimumDifference(nums, k))  # Expected: 0

    # Test case 3
    nums = [1, 5, 6, 14, 15]
    k = 3
    print("Test 3:", solution.minimumDifference(nums, k))  # Expected: 5

    # Test case 4
    nums = [10, 100, 300, 200, 1000, 20, 30]
    k = 3
    print("Test 4:", solution.minimumDifference(nums, k))  # Expected: 20

    # Test case 5
    nums = [3, 3, 3, 3]
    k = 2
    print("Test 5:", solution.minimumDifference(nums, k))  # Expected: 0


if __name__ == "__main__":
    run_tests()


"""
------------------------------------------------------------
Time Complexity:
------------------------------------------------------------
Sorting:      O(n log n)
Sliding window: O(n)

Total: O(n log n)

------------------------------------------------------------
Space Complexity:
------------------------------------------------------------
O(1) extra space (sorting done in place)

------------------------------------------------------------
Why This Is Optimal:
------------------------------------------------------------
- Checking all combinations is exponential.
- Sorting reduces the problem to checking consecutive groups.
- Sliding window ensures minimal operations.
"""