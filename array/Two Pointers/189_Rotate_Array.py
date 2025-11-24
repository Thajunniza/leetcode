""" 
# ------------------------------------
# 189. Rotate Array — Reverse Trick
# ------------------------------------

"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array nums to the right by k steps in-place.

        Args:
            nums (List[int]): Input array of integers.
            k (int): Number of steps to rotate to the right.

        Returns:
            None: Modifies nums in-place.

        Example:
            >>> nums = [1,2,3,4,5,6,7]
            >>> Solution().rotate(nums, 3)
            >>> nums
            [5, 6, 7, 1, 2, 3, 4]
        """
        n = len(nums)
        if n == 0:
            return

        # Step 1: Handle k larger than n
        k = k % n
        if k == 0:
            return  # No rotation needed

        # Step 2: Reverse the entire array
        self._reverse(nums, 0, n - 1)

        # Step 3: Reverse the first k elements
        self._reverse(nums, 0, k - 1)

        # Step 4: Reverse the remaining n-k elements
        self._reverse(nums, k, n - 1)

    def _reverse(self, nums: List[int], left: int, right: int) -> None:
        """
        Helper function to reverse elements in nums between
        indices left and right (inclusive) using two pointers.
        """
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    arr1 = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(arr1, 3)
    print(arr1)  # [5, 6, 7, 1, 2, 3, 4]

    arr2 = [-1, -100, 3, 99]
    sol.rotate(arr2, 2)
    print(arr2)  # [3, 99, -1, -100]

    arr3 = [1, 2]
    sol.rotate(arr3, 5)  # k > n case
    print(arr3)  # [2, 1]
