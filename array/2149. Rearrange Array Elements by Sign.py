"""
2149 - Rearrange Array Elements by Sign

Description:
Given a 0-indexed integer array nums of even length, consisting of an equal number of
positive and negative integers, rearrange the elements such that:
- Positive integers appear at even indices
- Negative integers appear at odd indices
- The relative order of positive and negative integers is preserved

Return the rearranged array.

Example:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]

Approach:
Two-Pointer Placement.
- Create a result array of the same size.
- Use two pointers:
  - p for even indices (positives)
  - q for odd indices (negatives)
- Traverse the input array:
  - Place positive numbers at index p and increment p by 2.
  - Place negative numbers at index q and increment q by 2.

Time Complexity:
O(n) - Each element is processed once.

Space Complexity:
O(n) - A new array is used to store the rearranged result.
"""

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        p = 0  # even index for positive numbers
        q = 1  # odd index for negative numbers

        for c in nums:
            if c > 0:
                res[p] = c
                p += 2
            else:
                res[q] = c
                q += 2

        return res


# -------------------- Test Cases --------------------

def test_rearrangeArray():
    sol = Solution()

    assert sol.rearrangeArray([3,1,-2,-5,2,-4]) == [3,-2,1,-5,2,-4]
    assert sol.rearrangeArray([-1,1]) == [1,-1]
    assert sol.rearrangeArray([1,-1,2,-2]) == [1,-1,2,-2]
    assert sol.rearrangeArray([5,-3,4,-2]) == [5,-3,4,-2]

    print("All test cases passed.")

if __name__ == "__main__":
    test_rearrangeArray()
