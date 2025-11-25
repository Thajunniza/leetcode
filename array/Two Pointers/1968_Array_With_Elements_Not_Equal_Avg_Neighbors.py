"""
===========================================================
1968. Array With Elements Not Equal to Average of Neighbors
===========================================================

🧩 Problem:
You are given a 0-indexed integer array `nums`.

Rearrange the array such that for **every** index `i` with `1 <= i <= n-2`:

        nums[i] != (nums[i-1] + nums[i+1]) / 2

In simple terms:
    • The middle number must *not* be exactly the average of its neighbors.

Return **any** valid rearrangement.


-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    nums = [1,2,3,4,5]

Output (one valid):
    [2,1,4,3,5]

Example 2:
Input:
    nums = [6,2,0,9,7]

Output (one valid):
    [2,0,7,6,9]


-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Ensure:
        nums[i] != (nums[i-1] + nums[i+1]) / 2
for all middle indices.

Pattern / Folder:
    • Pattern: Sorting + Wiggle Swap
    • Folder:
        /Arrays/1968-ArrayNotEqualToAverageOfNeighbors/


-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

If the array is sorted, middle elements can easily become the *average*
of their neighbors (especially in arithmetic progression).

To prevent this, create a **wiggle pattern**:

    peak > valley < peak > valley < peak

A number in a wiggle pattern is **never** equal to the average of its neighbors, because:

- Peak: neighbors are smaller → average < peak
- Valley: neighbors are larger → average > valley

✔ Simple way to create wiggle:
    1. Sort the array
    2. Swap adjacent pairs: (0,1), (2,3), (4,5)...


-----------------------------------------------------------
🧠 Algorithm (Sort + Swap Adjacent):
-----------------------------------------------------------

1. Sort `nums`
2. Loop with step 2:
        swap(nums[i], nums[i+1])
3. Return modified `nums`


-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time Complexity:
        O(n log n)
- Space Complexity:
        O(1) (in-place swapping)


-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------

"""
class Solution(object):
    def rearrangeArray(self, nums):
        """
        LeetCode 1968.
        Rearranges nums so no middle element equals the average
        of its neighbors.

        Approach:
            1. Sort the array.
            2. Swap adjacent pairs (0 with 1, 2 with 3, ...)
               → Creates a wiggle pattern (peak-valley-peak),
                 preventing any element from being the exact average.
        """

        nums.sort()

        i = 0
        while i < len(nums) - 1:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i += 2

        return nums


# ▶️ TEST CASES
if __name__ == "__main__":
    S = Solution()

    nums1 = [1,2,3,4,5]
    print(S.rearrangeArray(nums1))  # Expected wiggle pattern

    nums2 = [6,2,0,9,7]
    print(S.rearrangeArray(nums2))  # Any valid pattern

    nums3 = [1,3,2,5,4]
    print(S.rearrangeArray(nums3))  # Valid

    nums4 = [10,20,30,40,50]
    print(S.rearrangeArray(nums4))  # Wiggle pattern
