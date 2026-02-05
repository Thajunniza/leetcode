# ===========================================================
# 128. Longest Consecutive Sequence
# ===========================================================

# 🧩 Problem:
# Given an unsorted array of integers nums, return the length
# of the longest consecutive elements sequence.

# The algorithm must run in O(n) time.

# Example:
# Input: [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive sequence is [1,2,3,4]

# Input: [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# -----------------------------------------------------------
# Approach — Hash Set + Sequence Start Detection:
# -----------------------------------------------------------
# 1. Insert all numbers into a hash set for O(1) lookup.
# 2. Iterate through each number in the set.
# 3. A number is considered the start of a sequence if
#    (number - 1) does NOT exist in the set.
# 4. From this starting number, expand forward while
#    consecutive numbers exist.
# 5. Track the maximum length found.

# This approach ensures each number is processed only once,
# achieving linear time complexity.

# -----------------------------------------------------------
# ⏱ Time Complexity:   O(n)
# 💾 Space Complexity:  O(n)
# -----------------------------------------------------------

class Solution(object):
    def longestConsecutive(self, nums):
        have = set(nums)
        res = 0

        for n in have:
            # start counting only if n is the beginning of a sequence
            if n - 1 not in have:
                length = 0
                while n + length in have:
                    length += 1
                res = max(res, length)

        return res


# -----------------------------------------------------------
# Driver Example
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))          # Expected Output: 4
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))      # Expected Output: 9

