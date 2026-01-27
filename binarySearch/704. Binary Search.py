"""
--------------------------------------------------
704: Binary Search (Iterative & Recursive)
--------------------------------------------------

Given a sorted array of integers `nums` and an integer `target`,
return the index of `target` if it exists in the array.
If it does not exist, return -1.

You must write an algorithm with O(log n) time complexity.

--------------------------------------------------
Example:
--------------------------------------------------
Input:
nums = [-1, 0, 3, 5, 9, 12]
target = 9

Output:
4

Input:
nums = [-1, 0, 3, 5, 9, 12]
target = 2

Output:
-1

--------------------------------------------------
Algorithm (Binary Search):
--------------------------------------------------
1. Initialize two pointers:
   - left = 0
   - right = len(nums) - 1

2. While left <= right:
   - Compute mid = (left + right) // 2
   - If nums[mid] == target → return mid
   - If nums[mid] > target → search left half
   - Else → search right half

3. If target is not found, return -1

--------------------------------------------------
Time Complexity:
--------------------------------------------------
O(log n)

--------------------------------------------------
Space Complexity:
--------------------------------------------------
Iterative: O(1)
Recursive: O(log n) due to recursion stack
--------------------------------------------------
"""


class Solution:
    # -------------------------------
    # Iterative Binary Search
    # -------------------------------
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    # -------------------------------
    # Recursive Binary Search
    # -------------------------------
    def search_rec(self, nums, target):
        def helper(left, right):
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return helper(left, mid - 1)
            else:
                return helper(mid + 1, right)

        return helper(0, len(nums) - 1)


# --------------------------------------------------
# Test Cases
# --------------------------------------------------
if __name__ == "__main__":
    s = Solution()

    nums = [-1, 0, 3, 5, 9, 12]

    print("Iterative Binary Search")
    print(s.search(nums, 9))   # Expected: 4
    print(s.search(nums, 2))   # Expected: -1

    print("\nRecursive Binary Search")
    print(s.search_rec(nums, 9))  # Expected: 4
    print(s.search_rec(nums, 2))  # Expected: -1