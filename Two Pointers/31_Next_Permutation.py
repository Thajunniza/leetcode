"""
31\. Next Permutation

🧩 Problem:
Given an array of integers `nums`, rearrange the numbers to obtain the **next lexicographically greater permutation** of the given sequence. If such arrangement is **not possible** (i.e., the array is in non-increasing order), rearrange it to the **lowest possible order** (sorted ascending).

The rearrangement must be done **in-place**, and you must not allocate extra memory.

🎯 Goal:
Transform the array into the next permutation in lexicographic order, or the smallest permutation if the next one doesn't exist.

***

## Examples:

Example 1:
Input:  `nums = [1, 2, 3]`  
Output: `[1, 3, 2]`  
Explanation: The next permutation after `[1, 2, 3]` is `[1, 3, 2]`.

Example 2:
Input:  `nums = [3, 2, 1]`  
Output: `[1, 2, 3]`  
Explanation: No larger permutation exists; return the smallest (ascending).

Example 3:
Input:  `nums = [1, 1, 5]`  
Output: `[1, 5, 1]`  
Explanation: Swap the pivot `1` with `5`, then reverse the suffix.

Example 4:
Input:  `nums = [1, 3, 2]`  
Output: `[2, 1, 3]`  
Explanation: Pivot at `1` (index 0), successor `2`, swap and reverse suffix.

***

## Algorithm — Right-to-left scan + swap + reverse:

1.  **Find the pivot**:
    *   Scan from right to left to find the first index `i` such that `nums[i] < nums[i + 1]`.
    *   If no such `i` exists (array is non-increasing), reverse the entire array and return.

2.  **Find the rightmost successor to pivot**:
    *   From the end of the array, find the first index `j` such that `nums[j] > nums[i]`.

3.  **Swap pivot and successor**:
    *   Swap `nums[i]` and `nums[j]`.

4.  **Reverse the suffix**:
    *   Reverse the subarray from `i + 1` to the end to get the smallest order for the suffix, ensuring the next lexicographic permutation.

***

⏱ Time Complexity:

*   Single pass to find pivot + single pass to find successor + suffix reversal → **O(n)**

💾 Space Complexity:

*   **O(1)** extra space (in-place)

***

"""

# ------------------------------------

# Next Permutation — In-place

# ------------------------------------

class Solution(object):
    def nextPermutation(self, nums):

        n = len(nums)
        i = n - 2

        # 1) Find pivot: first index i from the right such that nums[i] < nums[i + 1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # If no pivot, reverse entire array to get the smallest permutation
        if i == -1:
            nums.reverse()
            return
        
        # 2) Find rightmost element greater than nums[i]
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        
        # 3) Swap pivot with successor
        nums[i], nums[j] = nums[j], nums[i]
        
        # 4) Reverse the suffix (from i+1 to end) to get the next lexicographic permutation
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# ------------------------------------
# Driver Tests
# ------------------------------------

def run_tests():
    cases = [
        [1, 2, 3],        # Expected: [1, 3, 2]
        [3, 2, 1],        # Expected: [1, 2, 3]
        [1, 1, 5],        # Expected: [1, 5, 1]
        [1, 3, 2],        # Expected: [2, 1, 3]
        [2, 3, 1],        # Expected: [3, 1, 2]
        [1],              # Expected: [1]
        [1, 5, 1],        # Expected: [5, 1, 1]
        [1, 2, 4, 3, 1],  # Expected: [1, 3, 1, 2, 4]
    ]
    
    s = Solution()
    for nums in cases:
        original = nums[:]
        s.nextPermutation(nums)
        print(f"Input:  {original}\nOutput: {nums}\n")

if __name__ == "__main__":
   run_tests()
