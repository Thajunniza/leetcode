
"""
278 – First Bad Version

You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. Since 
each version is developed based on the previous version, all the versions after a 
bad version are also bad.

Suppose you have an API: 
    bool isBadVersion(version)
that returns whether version is bad.

Your task is to implement a function to find the first bad version. You should 
minimize the number of calls to the API.

Example:
    Input: n = 5, first bad = 4
           isBadVersion(1) -> False
           isBadVersion(2) -> False
           isBadVersion(3) -> False
           isBadVersion(4) -> True
           isBadVersion(5) -> True
    Output: 4

Algorithm (Binary Search):
    1) Maintain two pointers l and r representing the current search range [l, r].
       Initialize l = 1, r = n.
    2) While l <= r:
         - Let m = (l + r) // 2 be the mid version.
         - If isBadVersion(m) is True, the first bad version is at m or to its left,
           so move the right bound: r = m - 1.
         - Otherwise, the first bad version is to the right of m, so move left bound:
           l = m + 1.
    3) When the loop ends, l points to the first index where versions become bad.

Correctness Intuition:
    - The predicate "isBadVersion(v)" is monotonic: once it becomes True, it stays True
      for all larger versions. Binary search over a monotonic predicate returns the
      smallest index that satisfies the predicate, which is exactly the first bad version.

Time Complexity:
    - O(log n) API calls, as we halve the search space each iteration.

Space Complexity:
    - O(1) extra space.

Notes:
    - This pattern is often called "lower_bound" on a boolean monotonic predicate.
"""

# The isBadVersion API is already defined for you in the judge.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int

        Binary search to find the first index where isBadVersion turns True.
        """
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m - 1    # first bad is at m or to the left
            else:
                l = m + 1    # first bad is to the right of m
        # l is the smallest index with isBadVersion(l) == True
        return l


# ---------------------------------------------------------------------
# Local test harness (only for running this file directly).
# In the online judge, the "isBadVersion" API is provided by the system.
# ---------------------------------------------------------------------
def _make_is_bad_version(first_bad):
    """
    Returns a closure emulating the isBadVersion API:
    - isBadVersion(v) -> (v >= first_bad)
    """
    def _api(v):
        return v >= first_bad
    return _api


def _run_tests():
    global isBadVersion

    tests = [
        # (n, first_bad, expected_first_bad)
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 2),
        (5, 4, 4),
        (10, 7, 7),
        (100, 100, 100),
        (100, 1, 1),
    ]

    sol = Solution()
    for n, fb, expected in tests:
        isBadVersion = _make_is_bad_version(fb)  # inject mock
        got = sol.firstBadVersion(n)
        print(f"n={n}, first_bad={fb} -> got={got}, expected={expected}")
        assert got == expected

    print("All tests passed.")


if __name__ == "__main__":
    _run_tests()