"""
81 .Search in Rotated Sorted Array II (with duplicates).

Run:
    python search_rotated.py

This will execute a few sanity tests and print results.
"""

from typing import List

class Solution(object):
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # Found target
            if nums[mid] == target:
                return True

            # If left half is strictly sorted
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # If right half is strictly sorted
            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

            # nums[l] == nums[mid], duplicate → shrink left pointer
            else:
                l += 1

        return False


# --------------------------
# Simple test runner
# --------------------------

def _run_tests():
    s = Solution()
    tests = [
        (([2,5,6,0,0,1,2], 0), True),
        (([2,5,6,0,0,1,2], 3), False),
        (([1,1,1,1,3,1], 3), True),
        (([1,0,1,1,1], 0), True),
        (([1], 1), True),
        (([1], 0), False),
    ]

    for (arr, target), expected in tests:
        got = s.search(arr, target)
        print(f"nums={arr}, target={target} -> {got} (expected {expected})")


if __name__ == "__main__":
    _run_tests()