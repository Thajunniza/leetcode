
"""
509: Fibonacci Number (F(n))
--------------------------------
Given an integer n (n >= 0), compute the n-th Fibonacci number using the
convention F(0) = 0 and F(1) = 1.

Examples
--------
Input: 2  -> Output: 1
Input: 3  -> Output: 2
Input: 4  -> Output: 3

Approach
--------
This file includes:
1) A direct recursive solution (matches the mathematical definition).
2) A memoized recursive solution (O(n) time).
3) An iterative O(n) / O(1) space solution (idiomatic and fast for typical n).
4) A fast-doubling O(log n) solution (best for very large n).

Run the file directly to see sample test runs for all approaches.
"""

from __future__ import annotations
from functools import lru_cache
from typing import Tuple


class SolutionRecursive:
    """Plain recursive solution (exponential time).

    Suitable only for small n (e.g., n <= 30) due to repeated subproblems.
    """

    def fib(self, n: int) -> int:
        if n < 0:
            raise ValueError("n must be non-negative")
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


class SolutionMemoized:
    """Top-down memoized recursion using lru_cache (O(n) time, O(n) space)."""

    @lru_cache(maxsize=None)
    def fib(self, n: int) -> int:
        if n < 0:
            raise ValueError("n must be non-negative")
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


class SolutionIterative:
    """Iterative bottom-up solution (O(n) time, O(1) space)."""

    def fib(self, n: int) -> int:
        if n < 0:
            raise ValueError("n must be non-negative")
        a, b = 0, 1  # a = F(k), b = F(k+1)
        for _ in range(n):
            a, b = b, a + b
        return a  # F(n)


class SolutionFastDoubling:
    """Fast-doubling solution (O(log n) time).

    Returns F(n) using identities:
      F(2k)   = F(k) * [2*F(k+1) – F(k)]
      F(2k+1) = F(k+1)^2 + F(k)^2
    """

    def fib(self, n: int) -> int:
        if n < 0:
            raise ValueError("n must be non-negative")
        return self._fib_pair(n)[0]

    def _fib_pair(self, n: int) -> Tuple[int, int]:
        # Returns (F(n), F(n+1))
        if n == 0:
            return (0, 1)
        a, b = self._fib_pair(n // 2)  # a=F(k), b=F(k+1)
        c = a * (2 * b - a)            # F(2k)
        d = a * a + b * b              # F(2k+1)
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


# -------------------------
# Test runs / Demonstration
# -------------------------

def _run_basic_tests():
    print("Basic checks (n = 0..10) for Iterative:")
    it = SolutionIterative()
    seq = [it.fib(i) for i in range(11)]
    print(seq)
    assert seq == [0,1,1,2,3,5,8,13,21,34,55]

    print("\nFastDoubling spot checks:")
    fd = SolutionFastDoubling()
    for n, expected in [(2,1),(3,2),(4,3),(10,55),(20,6765)]:
        val = fd.fib(n)
        print(f"F({n}) = {val}")
        assert val == expected

    print("\nMemoized recursion spot checks:")
    memo = SolutionMemoized()
    for n in range(11):
        print(f"F({n}) = {memo.fib(n)}")

    print("\nPlain recursion small n (n=2..6):")
    rec = SolutionRecursive()
    for n in range(2, 7):
        print(f"F({n}) = {rec.fib(n)}")

    print("\nAll assertions passed!")


if __name__ == "__main__":
    # Problem examples (from the prompt-like examples):
    print("Example outputs (should be 1, 2, 3):")
    it = SolutionIterative()
    print(it.fib(2))
    print(it.fib(3))
    print(it.fib(4))

    # Run a broader set of tests/demos
    print("\nRunning basic test suite...\n")
    _run_basic_tests()
