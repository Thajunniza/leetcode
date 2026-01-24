"""
1877. Minimize Maximum Pair Sum in Array

Problem:
    Given an array nums of even length n, pair up the elements into n/2 pairs such that:
        1. Each element is in exactly one pair.
        2. The maximum pair sum is minimized.
    Return the minimized maximum pair sum after optimal pairing.

Example:
    Input: nums = [3,5,2,3]
    Output: 7
    Explanation: Pairs (3,3) and (5,2), max pair sum = 7

Algorithm:
    Approach 1 - Sorting:
        1. Sort the array.
        2. Pair the smallest and largest numbers using two pointers.
        3. Track the maximum sum among pairs.
        4. Return the maximum pair sum.

    Approach 2 - Counting/Frequency Array:
        1. Create a frequency array to track occurrences of each number.
        2. Use two pointers at smallest and largest available numbers.
        3. Pair numbers while decreasing their frequency.
        4. Track the maximum sum among all pairs.

Time Complexity:
    - Sorting Approach: O(n log n)
    - Counting Approach: O(n + max(nums))

Space Complexity:
    - Sorting Approach: O(1) (in-place)
    - Counting Approach: O(max(nums)) for frequency array
"""

from typing import List

# ------------------- Approach 1: Sorting -------------------
class SolutionSort:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        max_sum = 0
        while l < r:
            max_sum = max(max_sum, nums[l] + nums[r])
            l += 1
            r -= 1
        return max_sum

# ------------------- Approach 2: Counting -------------------
class SolutionCount:
    def minPairSum(self, nums: List[int]) -> int:
        max_num = max(nums)
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1
        
        i, j = 0, max_num
        max_sum = 0
        
        while i <= j:
            while i <= j and freq[i] == 0:
                i += 1
            while i <= j and freq[j] == 0:
                j -= 1
            if i > j:
                break
            
            pair_count = min(freq[i], freq[j])
            if i == j:
                pair_count = freq[i] // 2
            
            if pair_count > 0:
                max_sum = max(max_sum, i + j)
                freq[i] -= pair_count
                freq[j] -= pair_count
        
        return max_sum

# ------------------ Test Cases ------------------
if __name__ == "__main__":
    test_cases = [
        [3,5,2,3],
        [3,5,4,2,4,6],
        [1,2,3,9],
        [1,1,1,1,1,1]
    ]
    
    print("---- Testing Sorting Approach ----")
    sol_sort = SolutionSort()
    for i, nums in enumerate(test_cases, 1):
        print(f"Test Case {i}: {sol_sort.minPairSum(nums)}")
    
    print("\n---- Testing Counting Approach ----")
    sol_count = SolutionCount()
    for i, nums in enumerate(test_cases, 1):
        print(f"Test Case {i}: {sol_count.minPairSum(nums)}")