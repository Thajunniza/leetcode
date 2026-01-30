# ------------------------------------------------------------
# 1482: Minimum Number of Days to Make m Bouquets
# ------------------------------------------------------------
# Problem:
# You are given an integer array bloomDay where bloomDay[i] is the day
# the ith flower blooms. You need to make m bouquets.
# To make one bouquet, you need k adjacent flowers that have bloomed.
# Return the minimum number of days needed to make m bouquets.
# If it is impossible, return -1.
#
# Example:
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
#
# Explanation:
# Day 3: Flowers at indices 0, 2, and 4 have bloomed.
# We can make 3 bouquets of size 1.
#
# ------------------------------------------------------------
# Algorithm:
# 1. If m * k > len(bloomDay), return -1 (impossible case).
# 2. Use binary search on the answer (days).
# 3. For a given day `d`, check how many bouquets can be formed
#    by counting consecutive flowers with bloomDay <= d.
# 4. If bouquets >= m, try a smaller day; otherwise, try a larger day.
#
# ------------------------------------------------------------
# Time Complexity:
# O(n log D), where n = len(bloomDay) and D = max(bloomDay)
#
# Space Complexity:
# O(1)
#
# ------------------------------------------------------------
# Test Case:
# bloomDay = [1,10,3,10,2]
# m = 3
# k = 1
# Expected Output = 3
# ------------------------------------------------------------

class Solution(object):
    def minDays(self, bloomDay, m, k):
        # Edge case: not enough flowers
        if m * k > len(bloomDay):
            return -1

        def get_bouquet(day):
            count = 0
            bouquets = 0
            for b in bloomDay:
                if b <= day:
                    count += 1
                else:
                    count = 0
                if count == k:
                    bouquets += 1
                    count = 0
            return bouquets

        left, right = 1, max(bloomDay)
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if get_bouquet(mid) >= m:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

# ------------------- Test Run -------------------
if __name__ == "__main__":
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1

    sol = Solution()
    result = sol.minDays(bloomDay, m, k)

    print("Input:")
    print("bloomDay =", bloomDay)
    print("m =", m, ", k =", k)
    print("Output:")
    print(result)  # Expected: 3
