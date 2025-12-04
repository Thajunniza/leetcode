"""
===========================================================
901. Online Stock Span
===========================================================

🧩 Problem:
You are designing an algorithm to calculate the **span** of stock prices.

For each day's price, the **stock span** is defined as:

    The number of consecutive days (including today)
    where the stock price was <= today's price.

You will receive prices one by one using calls to:

        obj.next(price)

🎯 Goal:
Implement the class `StockSpanner` so that:

    • Each call to next(price) returns the stock span for that price.
    • The solution must be efficient for up to 10⁵ calls.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example:
Input:
    ["StockSpanner","next","next","next","next","next","next","next"]
    [[],[100],[80],[60],[70],[60],[75],[85]]

Process:
    next(100) → span = 1
        stack = [(100, 1)]

    next(80) → span = 1
        stack = [(100,1), (80,1)]

    next(60) → span = 1
        stack = [(100,1), (80,1), (60,1)]

    next(70) → price 70 >= 60 → absorb span of 60
        span = 1 + 1 = 2
        stack = [(100,1), (80,1), (70,2)]

    next(60) → span = 1  
        stack = [(100,1), (80,1), (70,2), (60,1)]

    next(75) → absorb 60 → span = 1 + 1 = 2  
              absorb 70 → span = 2 + 2 = 4  
        stack = [(100,1), (80,1), (75,4)]

    next(85) → absorb 75 → span = 1 + 4 = 5  
              absorb 80 → span = 5 + 1 = 6  
        stack = [(100,1), (85,6)]

Output:
    [1, 1, 1, 2, 1, 4, 6]

-----------------------------------------------------------
Algorithm — Monotonic Decreasing Stack:
-----------------------------------------------------------

To avoid scanning backward every time (O(n²)),  
use a **monotonic decreasing stack** storing pairs:

        (price, span)

For each incoming price:
    1) Set span = 1
    2) While stack.top.price <= current price:
            pop the top and add its span to current span
    3) Push (price, span)
    4) Return span

Why this works:
    • Each price is pushed and popped at most once.
    → Total work O(n) over all calls.
    • The stack always remains in strictly decreasing order of prices.
    • This ensures amortized O(1) time per `next()` call.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(1) amortized per next()
    • Each element gets pushed & popped once → O(n) total.

Space Complexity:  O(n)
    • Stack stores pairs of (price, span).

-----------------------------------------------------------
"""

class StockSpanner:

    def __init__(self):
        # stack will store pairs (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        """
        Returns the stock span for the given price.
        """
        span = 1

        # Merge spans from previous days with smaller or equal prices
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span

        # Push the current price and its span
        self.stack.append((price, span))

        return span


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    obj = StockSpanner()

    print(obj.next(100))  # Expected: 1
    print(obj.next(80))   # Expected: 1
    print(obj.next(60))   # Expected: 1
    print(obj.next(70))   # Expected: 2
    print(obj.next(60))   # Expected: 1
    print(obj.next(75))   # Expected: 4
    print(obj.next(85))   # Expected: 6
