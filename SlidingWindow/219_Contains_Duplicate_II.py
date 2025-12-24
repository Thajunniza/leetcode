"""
===========================================================
219. Contains Duplicate II
===========================================================

🧩 Problem:
Given an integer array `nums` and an integer `k`,
return `True` if there are **two distinct indices** `i` and `j`
such that:

    nums[i] == nums[j]
    |i - j| ≤ k

Otherwise, return `False`.

🎯 Goal:
Detect duplicates that appear **within a distance of k**.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  nums = [1,2,3,1], k = 3
Output: True

Example 2:
Input:  nums = [1,0,1,1], k = 1
Output: True

Example 3:
Input:  nums = [1,2,3,1,2,3], k = 2
Output: False

-----------------------------------------------------------
Algorithm — Fixed Size Sliding Window + Hash Set:
-----------------------------------------------------------

Maintain a sliding window of size at most `k`.

1. Use a set `seen` to store elements in the current window
2. Iterate through the array:
   - If nums[i] is already in `seen`, return True
   - Add nums[i] to `seen`
   - If window size exceeds `k`, remove nums[i - k] from `seen`
3. If no duplicates are found, return False

Key idea:
We only care about duplicates within the last `k` indices.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(k)

-----------------------------------------------------------
"""
# ------------------------------------
# 219. Contains Duplicate II
# Sliding Window (Fixed Size) + Set
# ------------------------------------

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = set()

        for i, val in enumerate(nums):
            if val in seen:
                return True

            seen.add(val)

            if i >= k:
                seen.remove(nums[i - k])

        return False


# ------------------------------------
# Driver Test
# ------------------------------------

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2,3,1], 3))     # Expected: True
    print(sol.containsNearbyDuplicate([1,0,1,1], 1))     # Expected: True
    print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2)) # Expected: False
    print(sol.containsNearbyDuplicate([1,1], 0))         # Expected: False
