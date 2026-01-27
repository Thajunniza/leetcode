"""
--------------------------------------------------
122: Best Time to Buy and Sell Stock II
--------------------------------------------------

You are given an array prices where prices[i] is the price
of a given stock on the i-th day.

You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).
However, you must sell the stock before you buy again.

Return the maximum profit you can achieve.

--------------------------------------------------
Example:
Input:
    prices = [7, 1, 5, 3, 6, 4]
Output:
    7

Explanation:
Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 4
Buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 3
Total profit = 4 + 3 = 7
--------------------------------------------------
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Greedy approach:
        Add profit for every increasing pair of days.
        """
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit


# --------------------------------------------------
# Algorithm Explanation:
# --------------------------------------------------
# 1. Traverse the price list from day 1 to day n.
# 2. Whenever today's price is higher than yesterday's,
#    add the difference to total profit.
# 3. This captures all profitable upward movements.
#
# --------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# --------------------------------------------------


# --------------------------------------------------
# Test Cases
# --------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected: 7
    print(sol.maxProfit([1, 2, 3, 4, 5]))     # Expected: 4
    print(sol.maxProfit([7, 6, 4, 3, 1]))     # Expected: 0
    print(sol.maxProfit([1]))                 # Expected: 0
    print(sol.maxProfit([]))                  # Expected: 0