# ===========================================================
# 16 - 3Sum Closest
# ===========================================================

# 🧩 Problem:
# Given an integer array nums of length n and an integer target, find three integers
# at distinct indices such that their sum is closest to target. Return the sum.
# You may assume exactly one solution exists.

# 🎯 Goal:
# Return the sum of the three integers whose total is closest to target.

# -----------------------------------------------------------
# Examples:
# -----------------------------------------------------------
# Input:  nums = [-1, 2, 1, -4], target = 1
# Output: 2
# Explanation: The sum that is closest to target is 2 (-1 + 1 + 2).

# -----------------------------------------------------------
# Approach — Sort + Two Pointers (Standard & Correct)
# -----------------------------------------------------------
# 1) Sort the array.
# 2) Fix one index i (0 .. n-3). For the remaining subarray (i+1 .. n-1),
#    use two pointers l and r to probe sums:
#       s = nums[i] + nums[l] + nums[r]
#    - If |s - target| is smaller than the best so far, update result.
#    - If s == target, return immediately (can't get closer).
#    - If s < target, move l++ to increase the sum.
#    - Else move r-- to decrease the sum.
#
# This ensures O(n^2) time after sorting and O(1) extra space.
#
# ⏱ Time Complexity:   O(n^2)
# 💾 Space Complexity:  O(1)  (ignoring sort in-place)
# -----------------------------------------------------------

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        # Optional guard if not using LeetCode constraints:
        if n < 3:
            # Depending on platform requirements, you could raise or return None.
            # Here, we return the sum of what's available for robustness.
            return sum(nums)

        nums.sort()
        # Initialize with the first valid triplet
        res = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            # Optional micro-optimization to skip duplicate anchors:
            # if i > 0 and nums[i] == nums[i - 1]:
            #     continue

            l, r = i + 1, n - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                # Update the closest sum if current is better
                if abs(curr_sum - target) < abs(res - target):
                    res = curr_sum

                if curr_sum == target:
                    # Exact match is the closest possible
                    return curr_sum
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1

        return res


# ------------------------------------
# Driver Tests
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums1 = [-1, 2, 1, -4]
    target1 = 1
    print(sol.threeSumClosest(nums1, target1))  # Expected: 2

    # Additional quick checks
    nums2 = [0, 0, 0]
    target2 = 1
    print(sol.threeSumClosest(nums2, target2))  # Expected: 0

    nums3 = [1, 1, 1, 0]
    target3 = -100
    print(sol.threeSumClosest(nums3, target3))  # Expected: 2 (1+1+0)

    nums4 = [4, -1, -4, 2, 9, 7]
    target4 = 5
    print(sol.threeSumClosest(nums4, target4))  # One valid closest sum (varies by set)