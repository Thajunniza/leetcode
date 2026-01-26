"""
169 - Majority Element

Description:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example:
Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2

Approach:
Boyer-Moore Voting Algorithm.
- Maintain a candidate and a counter.
- When counter is 0, pick the current element as candidate.
- Increment counter if current element equals candidate, else decrement.
- Since the majority element appears more than n/2 times, it will remain as the final candidate.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for n in nums:
            if count == 0:
                candidate = n
            if n == candidate:
                count += 1
            else:
                count -= 1

        return candidate


# -------------------- Test Cases --------------------

def test_majority_element():
    sol = Solution()

    nums1 = [3, 2, 3]
    assert sol.majorityElement(nums1) == 3

    nums2 = [2, 2, 1, 1, 1, 2, 2]
    assert sol.majorityElement(nums2) == 2

    nums3 = [1]
    assert sol.majorityElement(nums3) == 1

    nums4 = [6, 6, 6, 7, 7]
    assert sol.majorityElement(nums4) == 6

    print("All test cases passed.")


if __name__ == "__main__":
    test_majority_element()