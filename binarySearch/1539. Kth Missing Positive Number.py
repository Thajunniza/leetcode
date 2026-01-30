# ------------------------------------------------------------
# 1539: Kth Missing Positive Number
# ------------------------------------------------------------
# Problem:
# Given a sorted array arr of positive integers and an integer k,
# return the kth positive integer that is missing from this array.
#
# Example:
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
#
# Explanation:
# The missing numbers are [1,5,6,8,9,...], the 5th missing is 9.
#
# ------------------------------------------------------------
# Algorithm:
# 1. Use binary search on array indices.
# 2. Define missing_count(i) = arr[i] - (i + 1)
#    → Number of missing numbers before arr[i].
# 3. Find the smallest index l where missing_count(l) >= k.
# 4. The kth missing number = l + k
#
# ------------------------------------------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)
# ------------------------------------------------------------
# Test Case:
# arr = [2,3,4,7,11], k = 5
# Expected Output: 9
# ------------------------------------------------------------

class Solution(object):
    def findKthPositive(self, arr, k):
        if not arr:
            return k

        n = len(arr)
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2
            missing = arr[mid] - (mid + 1)

            if missing < k:
                l = mid + 1
            else:
                r = mid - 1

        return l + k


# ------------------- Test Run -------------------
if __name__ == "__main__":
    arr = [2,3,4,7,11]
    k = 5

    sol = Solution()
    result = sol.findKthPositive(arr, k)
    print("Input: arr =", arr, ", k =", k)
    print("Output:", result)  # Expected: 9
