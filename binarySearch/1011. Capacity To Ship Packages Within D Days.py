# ------------------------------------------------------------
# 1011: Capacity To Ship Packages Within D Days
# ------------------------------------------------------------
# Problem:
# You are given an array weights where weights[i] is the weight of the
# ith package, and an integer days representing the number of days.
# Each day, you load packages onto a ship with a fixed capacity.
# The ship loads packages in order and cannot exceed its capacity.
# Return the minimum ship capacity to ship all packages within days.
#
# Example:
# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
#
# ------------------------------------------------------------
# Algorithm:
# 1. The minimum capacity must be max(weights).
# 2. The maximum capacity can be sum(weights).
# 3. Use binary search on capacity.
# 4. For a given capacity, compute how many days (ships) are needed.
# 5. Minimize the capacity such that required days <= given days.
#
# ------------------------------------------------------------
# Time Complexity:
# O(n log S), where n = len(weights), S = sum(weights)
#
# Space Complexity:
# O(1)
#
# ------------------------------------------------------------
# Test Case:
# weights = [1,2,3,4,5,6,7,8,9,10]
# days = 5
# Expected Output: 15
# ------------------------------------------------------------

class Solution(object):
    def shipWithinDays(self, weights, days):
        def get_ships(capacity):
            curr = 0
            ships = 0
            for w in weights:
                curr += w
                if curr > capacity:
                    ships += 1
                    curr = w
            if curr > 0:
                ships += 1
            return ships

        # Search range
        left = max(weights)
        right = sum(weights)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if get_ships(mid) <= days:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


# ------------------- Test Run -------------------
if __name__ == "__main__":
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5

    sol = Solution()
    print(sol.shipWithinDays(weights, days))  # Expected: 15
