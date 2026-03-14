"""
===========================================================
786. K-th Smallest Prime Fraction (Optimized for Small k)
===========================================================

Problem:
Given a sorted array arr containing 1 and prime numbers,
find the k-th smallest fraction arr[i]/arr[j] for i < j.

Optimization:
If k is much smaller than the length of the array,
we only need to push at most k fractions into the heap initially,
reducing heap size and improving efficiency.
"""

import heapq

class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(arr)
        minH = []

        # Only push at most k largest denominators initially
        for j in range(n-1, max(0, n-k-1), -1):
            heapq.heappush(minH, (arr[0] / float(arr[j]), 0, j))

        # Pop k smallest fractions
        for _ in range(k):
            val, i, j = heapq.heappop(minH)

            # Push next fraction in the same column (next numerator)
            if i + 1 < j:
                heapq.heappush(minH, (arr[i+1] / float(arr[j]), i+1, j))

        return [arr[i], arr[j]]


"""
-----------------------------------------------------------
Test Cases
-----------------------------------------------------------
"""

if __name__ == "__main__":
    s = Solution()

    arr = [1,2,3,5]
    k = 3
    print(s.kthSmallestPrimeFraction(arr,k))
    # Expected: [2,5]

    arr = [1,2,3,5,7,11]
    k = 2
    print(s.kthSmallestPrimeFraction(arr,k))
    # Expected: [1,7]

    arr = [1,3,5,7]
    k = 4
    print(s.kthSmallestPrimeFraction(arr,k))
    # Expected output depends on sorted fractions