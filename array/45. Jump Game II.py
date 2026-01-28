"""
45 . Jump Game II 

Usage:
    python jump_game_ii.py

This will run a few sanity tests and print results.
"""

from typing import List


class Solution(object):
    def jump(self, nums: List[int]) -> int:
        """
        Iterative greedy solution (O(n) time, O(1) space)
        Counts the minimum number of jumps to reach the last index.
        """
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        cur_end = 0
        farthest = 0

        # We don't need to step onto the last index; reaching/passing it is enough
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = farthest
        return jumps

    def jump_rec(self, nums: List[int]) -> int:
        """
        Recursive greedy-by-level solution (O(n) time), using call stack depth ~ number of jumps.
        Returns float('inf') if an unreachable situation is detected (defensive; LeetCode 45 guarantees reachability).
        """
        n = len(nums)
        if n <= 1:
            return 0

        def helper(l: int, r: int) -> int:
            # If current window already reaches/passes the end, no more jumps needed
            if r >= n - 1:
                return 0

            farthest = r
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            # If we cannot move further, it's unreachable
            if farthest == r:
                return float('inf')

            # Take one jump and recurse to the next window
            return 1 + helper(r + 1, farthest)

        return helper(0, 0)


def _run_tests():
    sol = Solution()

    cases = [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([1, 1, 1, 1], 3),
        ([0], 0),
    ]

    print("Iterative greedy results:")
    for arr, expected in cases:
        got = sol.jump(arr)
        print(f"  nums={arr} -> {got} (expected {expected})")

    print("\nRecursive greedy-by-level results:")
    for arr, expected in cases:
        got = sol.jump_rec(arr)
        # expected may be inf for unreachable, but our cases are reachable
        print(f"  nums={arr} -> {got} (expected {expected})")


if __name__ == "__main__":
    _run_tests()