"""
===========================================================
904. Fruit Into Baskets
===========================================================

🧩 Problem:
You are given an integer array `fruits` where `fruits[i]` represents
the type of fruit produced by the i-th tree.

You have **two baskets**, and each basket can hold **only one type of fruit**.
You can pick **exactly one fruit from each tree**, moving from left to right,
but you must stop when you cannot pick a fruit.

🎯 Goal:
Return the **maximum number of fruits** you can collect.

(Equivalent to: longest subarray with at most **2 distinct values**.)

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  fruits = [1,2,1]
Output: 3
Explanation: Collect all fruits [1,2,1]

Example 2:
Input:  fruits = [0,1,2,2]
Output: 3
Explanation: Longest valid subarray is [1,2,2]

Example 3:
Input:  fruits = [1,2,3,2,2]
Output: 4
Explanation: Longest valid subarray is [2,3,2,2]

-----------------------------------------------------------
Algorithm — Sliding Window (At Most K = 2 Distinct):
-----------------------------------------------------------

Maintain a sliding window [left .. right] with at most 2 fruit types.

1. Use a dictionary `freq` to store counts of fruit types in the window
2. Expand `right` and add fruits[right] to freq
3. If distinct types > 2:
   - Shrink window from the left
   - Decrease count of fruits[left]
   - Remove fruit type when count reaches 0
4. Track the maximum window size

Key idea:
This is a classic **“longest subarray with at most K distinct elements”**
problem where K = 2.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)  
(each index moves at most once)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1)  
(at most 2 keys in the map)

-----------------------------------------------------------
"""
# ------------------------------------
# 904. Fruit Into Baskets
# Sliding Window (At Most 2 Distinct)
# ------------------------------------

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0
        freq = {}
        best = 0

        for right, fruit in enumerate(fruits):
            freq[fruit] = freq.get(fruit, 0) + 1

            while len(freq) > 2:
                lf = fruits[left]
                freq[lf] -= 1
                if freq[lf] == 0:
                    del freq[lf]
                left += 1

            best = max(best, right - left + 1)

        return best


# ------------------------------------
# Driver Test
# ------------------------------------

if __name__ == "__main__":
    sol = Solution()
    print(sol.totalFruit([1,2,1]))        # Expected: 3
    print(sol.totalFruit([0,1,2,2]))      # Expected: 3
    print(sol.totalFruit([1,2,3,2,2]))    # Expected: 4
    print(sol.totalFruit([3,3,3,1,2,1]))  # Expected: 5
