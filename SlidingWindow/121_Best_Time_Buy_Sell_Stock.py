"""
===========================================================
121. Best Time to Buy and Sell Stock
===========================================================

🧩 Problem:
You are given an array `prices` where `prices[i]` is the price of a stock
on day `i`.

You want to maximize your profit by choosing:
- **one day to buy**
- **a later day to sell**

You may complete **only one transaction**.

🎯 Goal:
Return the **maximum profit** you can achieve.
If no profit is possible, return `0`.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy at 1 and sell at 6 → profit = 5

Example 2:
Input:  prices = [7,6,4,3,1]
Output: 0
Explanation: Prices only decrease → no profit possible

-----------------------------------------------------------
Algorithm — One Pass Scan (Min So Far):
-----------------------------------------------------------

Track the minimum price seen so far and compute profit for each day.

1. Initialize:
   - minPrice = infinity
   - maxProfit = 0
2. Traverse prices from left to right:
   - Update minPrice = min(minPrice, current price)
   - Calculate profit = current price − minPrice
   - Update maxProfit = max(maxProfit, profit)
3. Return maxProfit

Key idea:
Always buy at the **lowest price before today**, and sell **today**.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)  
(single pass through the array)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1)  
(constant extra space)

-----------------------------------------------------------
"""
# ------------------------------------
# 121. Best Time to Buy and Sell Stock
# One Pass / Min So Far
# ------------------------------------

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float('inf')
        maxProfit = 0

        for val in prices:
            minPrice = min(minPrice, val)
            maxProfit = max(maxProfit, val - minPrice)

        return maxProfit


# ------------------------------------
# Driver Test
# ------------------------------------

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))  # Expected: 5
print(sol.maxProfit([7,6,4,3,1]))    # Expected: 0
