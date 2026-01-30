# ------------------------------------------------------------
# Aggressive Cows Problem
# ------------------------------------------------------------
# Problem:
# You are given an array of unique stall positions `stalls[]` and an integer `k`,
# representing the number of aggressive cows. Place the cows in stalls such that
# the minimum distance between any two cows is maximized.
#
# Example:
# Input: stalls = [1, 2, 4, 8, 9], k = 3
# Output: 3
#
# Explanation:
# Place cows at positions [1, 4, 8]. The minimum distance between cows is 3,
# which is the largest possible.
#
# ------------------------------------------------------------
# Algorithm:
# 1. Sort the stalls array.
# 2. Use binary search on the possible minimum distance:
#    - low = 1, high = max(stalls) - min(stalls)
# 3. For each candidate distance `mid`, check if it's possible to place all k cows:
#    - Place the first cow at the first stall.
#    - For each subsequent stall, place a cow only if distance from last placed cow >= mid.
#    - If all k cows are placed, mid is possible.
# 4. Adjust binary search boundaries:
#    - If mid is possible, try a larger distance (low = mid + 1)
#    - Otherwise, try smaller distance (high = mid - 1)
# 5. Return the largest feasible minimum distance.
#
# ------------------------------------------------------------
# Time Complexity: O(n log(max_distance))
#   - Sorting stalls: O(n log n)
#   - Binary search over distance: O(log(max_distance))
#   - Greedy check: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------
# Test Case:
# stalls = [1, 2, 4, 8, 9], k = 3
# Expected Output: 3
# ------------------------------------------------------------

from typing import List

class Solution:
    def aggressiveCows(self, stalls: List[int], k: int) -> int:
        # Sort stalls
        stalls.sort()
        
        # Helper function: can we place k cows with at least distance 'dist'?
        def canPlaceCows(dist: int) -> bool:
            count = 1
            last_pos = stalls[0]
            
            for i in range(1, len(stalls)):
                if stalls[i] - last_pos >= dist:
                    count += 1
                    last_pos = stalls[i]
                if count == k:
                    return True
            return False
        
        # Binary search for largest minimum distance
        low, high = 1, stalls[-1] - stalls[0]
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlaceCows(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result

# ------------------- Test Run -------------------
if __name__ == "__main__":
    stalls_list = [
        ([1, 2, 4, 8, 9], 3),
        ([10, 1, 2, 7, 5], 3),
        ([2, 12, 11, 3, 26, 7], 5)
    ]

    sol = Solution()
    for stalls, k in stalls_list:
        result = sol.aggressiveCows(stalls, k)
        print("Input: stalls =", stalls, ", k =", k)
        print("Output:", result)
