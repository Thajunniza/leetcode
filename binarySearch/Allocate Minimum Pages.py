# ------------------------------------------------------------
# Allocate Minimum Pages
# ------------------------------------------------------------
# Problem:
# Given an array arr[] of n integers representing number of pages in books
# and an integer k (number of students), allocate books to students
# such that:
# 1. Each student gets at least one book.
# 2. Books are allocated contiguously.
# 3. The maximum number of pages assigned to a student is minimized.
#
# Feasibility Rule:
# If allocating a candidate maximum pages requires more than k students,
# the allocation is invalid.
#
# Example:
# Input: arr = [12, 34, 67, 90], k = 2
# Output: 113
# Explanation:
# Student 1: [12, 34, 67] = 113
# Student 2: [90] = 90
# Maximum pages = 113 (minimized)
#
# ------------------------------------------------------------
# Algorithm:
# 1. Set low = max(arr), high = sum(arr)
# 2. Binary search on possible maximum pages (mid):
#    - Use a greedy allocation to check feasibility:
#        * Add books to current student until adding next book exceeds mid
#        * Start a new student with the current book if exceeded
#        * If students > k → allocation not feasible
# 3. If feasible, try smaller mid (high = mid - 1)
#    Else, try larger mid (low = mid + 1)
# 4. Return the minimum feasible maximum pages
#
# ------------------------------------------------------------
# Time Complexity: O(n log(sum(arr)))
# Space Complexity: O(1)
# ------------------------------------------------------------
# Test Case:
# arr = [12, 34, 67, 90], k = 2
# Expected Output: 113
# ------------------------------------------------------------

from typing import List

class Solution:
    def findPages(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if n == 0 or k > n:
            return -1  # Not enough books for each student
        
        low = max(arr)
        high = sum(arr)
        ans = high
        
        # Check if candidate maximum pages is feasible
        def can_allocate(max_pages: int) -> bool:
            students = 1
            total = 0
            for pages in arr:
                if total + pages <= max_pages:
                    total += pages
                else:
                    students += 1
                    total = pages
                    if students > k:
                        return False  # Exceeds allowed students → invalid
            return True
        
        # Binary search to minimize maximum pages
        while low <= high:
            mid = (low + high) // 2
            if can_allocate(mid):
                ans = mid
                high = mid - 1  # Try smaller maximum
            else:
                low = mid + 1   # Need larger maximum
        
        return ans

# ------------------- Test Run -------------------
if __name__ == "__main__":
    test_cases = [
        ([12, 34, 67, 90], 2),
        ([10, 20, 30, 40], 2),
        ([10, 20, 30, 40], 3),
        ([5, 5, 5, 5], 2)
    ]
    
    sol = Solution()
    for arr, k in test_cases:
        result = sol.findPages(arr, k)
        print("Input: arr =", arr, ", k =", k)
        print("Output:", result)
