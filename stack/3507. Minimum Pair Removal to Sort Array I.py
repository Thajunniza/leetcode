"""
3507. Minimum Pair Removal to Sort Array I
Author: Thajunniza
Description:
    Given an array nums, repeatedly perform the following operation:
    - Select the adjacent pair with the minimum sum (leftmost if multiple)
    - Replace the pair with their sum
    Return the minimum number of operations to make the array non-decreasing.

Algorithm:
    - Simulation-based approach:
        1. While the array is not non-decreasing:
            a. Find the leftmost adjacent pair with minimum sum
            b. Merge the pair (replace first element with sum, remove second element)
            c. Increment operation count
        2. Return total operations

Time Complexity:
    - O(n^2) worst case
      (For each operation, scanning the array for min pair can take O(n), and up to n operations)
Space Complexity:
    - O(1) (in-place array manipulation)
"""

from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        """
        Returns the minimum number of pair merge operations to make the array non-decreasing.
        """
        def is_non_decreasing():
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    return False
            return True
        
        def get_min_index():
            min_sum = float("inf")
            min_index = 0
            for i in range(len(nums)-1):
                total = nums[i] + nums[i+1]
                if total < min_sum:
                    min_sum = total
                    min_index = i
            return min_index
        
        count = 0
        if len(nums) <= 1:
            return count
        
        # Simulation loop
        while not is_non_decreasing():
            min_index = get_min_index()
            nums[min_index] += nums[min_index+1]
            nums.pop(min_index+1)
            count += 1
        
        return count


# --------------------- Test Run ---------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    nums1 = [5,2,3,1]
    print(f"Input: {nums1} → Operations: {sol.minimumPairRemoval(nums1[:])}")  # 2

    # Test case 2
    nums2 = [1,2,2]
    print(f"Input: {nums2} → Operations: {sol.minimumPairRemoval(nums2[:])}")  # 0

    # Test case 3 (complex)
    nums3 = [2,2,-1,3,-2,2,1,1,1,0,-1]
    print(f"Input: {nums3} → Operations: {sol.minimumPairRemoval(nums3[:])}")  # 9
