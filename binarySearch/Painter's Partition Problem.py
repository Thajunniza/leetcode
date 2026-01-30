# ------------------------------------------------------------
# Painter's Partition Problem
# ------------------------------------------------------------
# Problem:
# Given an array arr[] of board lengths and k painters:
# 1. Each painter paints contiguous boards.
# 2. Total time taken by a painter = sum of boards assigned.
# 3. Minimize the time taken to paint all boards (maximum among painters).
#
# Example:
# Input: arr = [10, 20, 30, 40], k = 2
# Output: 60
# Explanation:
# Painter 1: [10, 20, 30] → 60
# Painter 2: [40] → 40
# Maximum time among painters = 60 (minimized)
#
# ------------------------------------------------------------
# Algorithm:
# 1. Set low = max(arr), high = sum(arr)
# 2. Binary search on possible maximum time (mid):
#    - Use greedy allocation:
#        * Add boards to current painter until total > mid
#        * Start new painter with current board
#        * If painters used <= k → feasible
# 3. If feasible → try smaller mid (r = mid - 1)
#    Else → try larger mid (l = mid + 1)
# 4. Return minimum feasible maximum time
#
# ------------------------------------------------------------
# Time Complexity: O(n log(sum(arr)))
# Space Complexity: O(1)
# ------------------------------------------------------------
# Test Case:
# arr = [10, 20, 30, 40], k = 2
# Expected Output: 60
# ------------------------------------------------------------

from typing import List

class Solution:
    def minTime(self, arr: List[int], k: int) -> int:
        def can_paint(time: int) -> bool:
            count = 0  # number of additional painters
            total = 0
            for n in arr:
                total += n
                if total > time:
                    count += 1
                    total = n
            return count + 1 <= k  # +1 accounts for first painter
        
        n = len(arr)
        if n < k:
            return -1
        
        l = max(arr)
        r = sum(arr)
        ans = r
        
        while l <= r:
            mid = (l + r) // 2
            if can_paint(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans

# ------------------- Test Run -------------------
if __name__ == "__main__":
    test_cases = [
        ([10, 20, 30, 40], 2),
        ([10, 20, 30, 40], 3),
        ([10, 20, 30, 40, 50], 2),
        ([5, 5, 5, 5], 2)
    ]
    
    sol = Solution()
    for arr, k in test_cases:
        result = sol.minTime(arr, k)
        print("Input: arr =", arr, ", k =", k)
        print("Output:", result)
