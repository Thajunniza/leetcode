"""
===========================================================
1475. Final Prices With a Special Discount in a Shop
===========================================================

🧩 Problem:
You are given an array `prices` where:

    prices[i] = price of the i-th item in a shop.

There is a **special discount rule**:

For each item `i`, you look at the items **to its right** (indices j > i) and find the
**first** item `j` such that:

    prices[j] <= prices[i]

If such an item exists, then `prices[j]` is the **discount** for item `i`.

If no such item exists, the discount is 0.

🎯 Goal:
Return an array `result` where:

    result[i] = prices[i] - discount_for_item_i

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  prices = [8, 4, 6, 2, 3]

Step-by-step:

    i = 0, price = 8
        Right side → [4, 6, 2, 3]
        First j where prices[j] <= 8 is 4
        Discount = 4 → final price = 8 - 4 = 4

    i = 1, price = 4
        Right side → [6, 2, 3]
        6 > 4, skip
        Next is 2 <= 4 → discount = 2
        Final price = 4 - 2 = 2

    i = 2, price = 6
        Right side → [2, 3]
        2 <= 6 → discount = 2
        Final price = 6 - 2 = 4

    i = 3, price = 2
        Right side → [3]
        3 > 2, no price <= 2 → discount = 0
        Final price = 2

    i = 4, price = 3
        No elements to the right → discount = 0
        Final price = 3

Output:
    [4, 2, 4, 2, 3]


Example 2:
Input:  prices = [1, 2, 3, 4, 5]

Right side for each price always has larger numbers only → no discounts.

Output:
    [1, 2, 3, 4, 5]


Example 3:
Input:  prices = [10, 1, 1, 6]

    i = 0, price = 10 → first right <= 10 is 1 → 10 - 1 = 9
    i = 1, price = 1  → first right <= 1 is 1 → 1 - 1 = 0
    i = 2, price = 1  → right side is [6], no <= 1 → 1 - 0 = 1
    i = 3, price = 6  → no right side → 6 - 0 = 6

Output:
    [9, 0, 1, 6]

-----------------------------------------------------------
Algorithm — Monotonic Stack (Next Smaller or Equal to the Right)
-----------------------------------------------------------

Naive approach:
    For each index i, scan all elements j > i to find the first prices[j] <= prices[i].
    → This is O(n²) in the worst case.

Optimized approach using a stack (O(n)):

We want the **first price to the right** that is **<= current price**.

Use a stack that stores **indices** of prices in a way that helps us find discounts quickly.

Idea:
    • Iterate from left to right over indexes i.
    • Maintain a stack of indices whose discount has not been found yet.
    • For each new index i:
        - While stack is not empty AND current price <= price at stack top:
              → We found the discount for index stack[-1].
              → Pop j = stack.pop()
              → result[j] = prices[j] - prices[i]
        - Then push i onto the stack.

Why it works:
    • The stack keeps indices whose final discount is not yet determined.
    • As soon as we see a future price that is <= some previous price, we know it's
      the **first such price to the right** for that previous index.
    • This is exactly the "Next Smaller Element to the Right (<=)" pattern.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    • Each index is pushed to the stack once and popped at most once.

Space Complexity:  O(n)
    • Stack can hold up to n indices in the worst case (strictly increasing prices).

-----------------------------------------------------------
"""

class Solution(object):
    def finalPrices(self, prices):
        """
        Computes final prices after applying the special discount rule.

        For each item i, the discount is the price of the first item j > i
        such that prices[j] <= prices[i]. If no such j exists, discount is 0.

        Args:
            prices (List[int]): List of item prices.

        Returns:
            List[int]: Final prices after discount.
        """
        n = len(prices)
        result = prices[:]   # Copy original prices
        stack = []           # Monotonic stack storing indices

        for i in range(n):
            # While current price can be a discount for previous indices
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                result[j] = prices[j] - prices[i]
            stack.append(i)

        return result


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.finalPrices([8, 4, 6, 2, 3]))
    # Expected: [4, 2, 4, 2, 3]

    print(sol.finalPrices([1, 2, 3, 4, 5]))
    # Expected: [1, 2, 3, 4, 5]

    print(sol.finalPrices([10, 1, 1, 6]))
    # Expected: [9, 0, 1, 6]

    print(sol.finalPrices([5]))
    # Expected: [5]

    print(sol.finalPrices([4, 4, 4, 4]))
    # First right <= itself for each:
    # [4-4, 4-4, 4-4, 4] = [0, 0, 0, 4]
    # Expected: [0, 0, 0, 4]
