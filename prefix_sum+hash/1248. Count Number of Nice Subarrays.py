"""
===========================================================
1248. Count Number of Nice Subarrays
===========================================================

Problem:
--------
Given an integer array nums and an integer k,
return the number of subarrays with exactly k odd numbers.

Approach 1:
-----------
Sliding Window (Optimal Space O(1))

Key Idea:
---------
Maintain a window with at most k odd numbers.
When window has exactly k odds, count valid starting positions
by compressing leading even numbers.

Time Complexity:
----------------
O(n)

Space Complexity:
-----------------
O(1)

Author:
-------
Thajunniza M A
"""

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        odd_count = 0
        result = 0
        temp = 0   # counts valid starting positions

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1
                temp = 0  # reset when new odd appears

            while odd_count == k:
                temp += 1
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1

            result += temp

        return result


"""
===========================================================
Alternative Approach
===========================================================

Approach 2:
-----------
Prefix Sum + HashMap

Key Idea:
---------
Transform:
odd -> 1
even -> 0

Now problem becomes:
Count subarrays with sum == k

Time Complexity:
----------------
O(n)

Space Complexity:
-----------------
O(n)
"""

class SolutionPrefix(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_count = {0: 1}
        total = 0
        result = 0

        for num in nums:
            total += num % 2

            if total - k in prefix_count:
                result += prefix_count[total - k]

            prefix_count[total] = prefix_count.get(total, 0) + 1

        return result


# -----------------------------
# Test Cases
# -----------------------------
if __name__ == "__main__":
    nums = [1,1,2,1,1]
    k = 3

    sol1 = Solution()
    sol2 = SolutionPrefix()

    print("Sliding Window:", sol1.numberOfSubarrays(nums, k))  # Expected: 2
    print("Prefix Sum:", sol2.numberOfSubarrays(nums, k))      # Expected: 2
