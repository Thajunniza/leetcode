"""
373. Find K Pairs with Smallest Sums

This module finds the k pairs (u, v), where:
    - u is from nums1
    - v is from nums2
such that their sum is among the k smallest possible sums.

Problem:
    - Given two sorted arrays nums1 and nums2,
      return the k pairs with the smallest sums.
    - Each pair consists of one element from each array.

Core Idea:
    - Use a min-heap to always extract the smallest sum pair.
    - Start from (0, 0).
    - From each popped pair (i, j), push:
        * (i+1, j)
        * (i, j+1)
      if not already visited.
    - Use a visited set to avoid duplicate states.

Why Visited Set?
    - Prevents pushing the same (i, j) pair multiple times.
    - Ensures correctness and avoids redundant heap entries.

Constraints:
    - nums1 and nums2 are sorted in ascending order.
    - 1 <= k <= len(nums1) * len(nums2)

Complexity:
    - Time  : O(k log k)
              * Each pop/push operation costs O(log k)
              * At most k elements are processed
    - Space : O(k) (heap + visited set)
"""

import heapq


class Solution(object):
    """DSA-style solution using min-heap + visited set."""

    def kSmallestPairs(self, nums1, nums2, k):
        """
        Return k pairs with smallest sums.

        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        if not nums1 or not nums2 or k == 0:
            return []

        res = []
        heap = []
        visited = set()

        m = len(nums1)
        n = len(nums2)

        # Start from (0, 0)
        heapq.heappush(heap, (nums1[0] + nums2[0], (0, 0)))
        visited.add((0, 0))

        while len(res) < k and heap:
            val, (i, j) = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            # Push next in nums1 direction
            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))

            # Push next in nums2 direction
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))

        return res


# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    print(f"{k} smallest pairs: {sol.kSmallestPairs(nums1, nums2, k)}")