"""
33 .Search in Rotated Sorted Array (no duplicates).

Run:
    python search_rotated.py

This will execute a few sanity tests and print results.
"""
from typing import List


class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        """
        Modified binary search for rotated sorted array without duplicates.
        Time: O(log n). Space: O(1).
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


def _run_tests():
    s = Solution()
    cases = [
        (([4,5,6,7,0,1,2], 0), 4),
        (([4,5,6,7,0,1,2], 3), -1),
        (([1], 0), -1),
        (([1], 1), 0),
        (([5,1,3], 3), 2),
        (([6,7,0,1,2,4,5], 6), 0),
        (([6,7,0,1,2,4,5], 5), 6),
        (([3,4,5,6,7,8,1,2], 1), 6),
    ]
    for (arr, target), expected in cases:
        got = s.search(arr, target)
        print(f"nums={arr}, target={target} -> {got} (expected {expected})")


if __name__ == "__main__":
    _run_tests()