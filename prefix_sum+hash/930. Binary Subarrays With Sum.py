"""
===========================================================
930. Binary Subarrays With Sum
===========================================================

Problem:
--------
Given a binary array nums and an integer goal,
return the number of non-empty subarrays with sum equal to goal.

-----------------------------------------------------------
Approach 1: Prefix Sum + HashMap
-----------------------------------------------------------

Key Idea:
---------
Let prefix sum at index i be:
    total = nums[0] + ... + nums[i]

We want:
    total - previous_prefix = goal
=>  previous_prefix = total - goal

Store frequency of prefix sums.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class SolutionPrefix(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefix_freq = {0: 1}   # base case
        total = 0
        count = 0

        for num in nums:
            total += num

            if total - goal in prefix_freq:
                count += prefix_freq[total - goal]

            prefix_freq[total] = prefix_freq.get(total, 0) + 1

        return count


"""
-----------------------------------------------------------
Approach 2: Sliding Window (AtMost Trick)
-----------------------------------------------------------

Exactly(goal) = AtMost(goal) - AtMost(goal - 1)

Works because nums contains only 0 and 1 (non-negative).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class SolutionSliding(object):
    def numSubarraysWithSum(self, nums, goal):
        return self._atMost(nums, goal) - self._atMost(nums, goal - 1)

    def _atMost(self, nums, k):
        if k < 0:
            return 0

        left = 0
        total = 0
        count = 0

        for right in range(len(nums)):
            total += nums[right]

            while total > k:
                total -= nums[left]
                left += 1

            count += right - left + 1

        return count


# -----------------------------
# Test Case
# -----------------------------
if __name__ == "__main__":
    nums = [1, 0, 1, 0, 1]
    goal = 2

    sol_prefix = SolutionPrefix()
    sol_sliding = SolutionSliding()

    print("Prefix Sum:", sol_prefix.numSubarraysWithSum(nums, goal))   # Expected: 4
    print("Sliding Window:", sol_sliding.numSubarraysWithSum(nums, goal))  # Expected: 4
