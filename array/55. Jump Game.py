
"""
55 - Jump Game 
=======================

Problem
-------
Given an integer array `nums` where each element represents your maximum jump length at that position, determine if you can reach the last index starting from index 0.

Example
-------
Input:  nums = [2, 3, 1, 1, 4]
Output: True
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Another example:
Input:  nums = [3, 2, 1, 0, 4]
Output: False
Explanation: You will always get stuck at index 3. Its maximum jump length is 0, which makes it impossible to reach the last index.

Algorithms
----------
1) Greedy from Right to Left (Iterative)
   - Maintain a `goal` (initially the last index). Scan indices from right to left.
   - If position `i` can reach `goal` (i + nums[i] >= goal), move `goal` to `i`.
   - At the end, return whether `goal == 0`.
   - Time: O(n), Space: O(1)

2) Greedy Goal-Shift (Recursive)
   - Recursive version that mirrors the right-to-left greedy logic.
   - `helper(i, goal)` scans from index `i` downwards. If `i + nums[i] >= goal`, shift `goal` to `i` and continue.
   - Base cases: `goal == 0` -> True, `i < 0` -> False.
   - Time: O(n), Space: O(n) due to recursion depth (call stack).

3) DFS with Memoization (Top-Down) [Optional]
   - Explore reachable next indices from the current position; cache results to avoid recomputation.
   - Worst-case Time: O(n^2), Space: O(n).

Time & Space Complexity Summary
-------------------------------
- Iterative Greedy (right-to-left):  Time O(n), Space O(1)
- Recursive Greedy (goal shift):     Time O(n), Space O(n) stack
- DFS + Memoization (optional):      Time O(n^2) worst-case, Space O(n)

"""
from typing import List
from functools import lru_cache


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Greedy from right to left (iterative). O(n) time, O(1) space.
        """
        n = len(nums)
        if n <= 1:
            return True
        goal = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
                if goal == 0:
                    return True
        return goal == 0

    def canJumpRec(self, nums: List[int]) -> bool:
        """Recursive version that mirrors the right-to-left greedy logic.
        O(n) time, O(n) recursion stack.
        """
        n = len(nums)

        def helper(i: int, goal: int) -> bool:
            if goal == 0:
                return True
            if i < 0:
                return False
            # shift goal left if i can reach current goal
            if i + nums[i] >= goal:
                goal = i
            return helper(i - 1, goal)

        return helper(n - 2, n - 1)

    def canJumpMemo(self, nums: List[int]) -> bool:
        """Top-down DFS with memoization. O(n^2) worst-case time, O(n) space.
        Included as an alternative recursive approach.
        """
        n = len(nums)

        @lru_cache(maxsize=None)
        def dfs(i: int) -> bool:
            if i >= n - 1:
                return True
            max_reach = min(n - 1, i + nums[i])
            # Try longer jumps first (a heuristic that often finishes earlier)
            for nxt in range(max_reach, i, -1):
                if dfs(nxt):
                    return True
            return False

        return dfs(0)


# -----------------------------
# Test Run
# -----------------------------

def run_tests():
    sol = Solution()
    tests = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([2, 0], True),
        ([0, 1], False),
        ([1, 1, 1, 1], True),
        ([2, 5, 0, 0], True),
        ([1, 0, 1, 0], False),
        ([4, 0, 0, 0, 0], True),
        ([1, 2, 0, 1, 0, 0], False),
    ]

    print("Iterative greedy (canJump):")
    for nums, expected in tests:
        got = sol.canJump(nums)
        print(f"  nums={str(nums):<22} -> {got} (expected {expected})")

    print("\nRecursive greedy (canJumpRec):")
    for nums, expected in tests:
        got = sol.canJumpRec(nums)
        print(f"  nums={str(nums):<22} -> {got} (expected {expected})")

    print("\nMemoized DFS (canJumpMemo):")
    for nums, expected in tests:
        got = sol.canJumpMemo(nums)
        print(f"  nums={str(nums):<22} -> {got} (expected {expected})")


if __name__ == "__main__":
    # Basic examples from the prompt
    s = Solution()
    print(s.canJump([0, 1]))        # False
    print(s.canJump([2, 3, 1, 1, 4]))  # True
    print(s.canJumpRec([0, 1]))     # False
    print(s.canJumpRec([2, 3, 1, 1, 4]))  # True

    print("\n--- Full test suite ---\n")
    run_tests()