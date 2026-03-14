"""
===========================================================
373. Find K Pairs with Smallest Sums
===========================================================

Problem:
You are given two integer arrays nums1 and nums2 sorted in
ascending order and an integer k.

Return the k pairs (u, v) such that:
- u ∈ nums1
- v ∈ nums2

with the smallest sums.

Return the answer as a list of pairs.

-----------------------------------------------------------
Example
-----------------------------------------------------------
Input:
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

Output:
[[1,2],[1,4],[1,6]]

-----------------------------------------------------------
Approach
-----------------------------------------------------------
Use a Min Heap.

1. Push pairs (nums1[i] + nums2[0], i, 0) for first k rows.
2. Pop smallest pair.
3. Add the pair to result.
4. Push next pair in same row (i, j+1).
5. Continue until k pairs are collected.

-----------------------------------------------------------
Time Complexity
-----------------------------------------------------------
O(k log min(m, k))

-----------------------------------------------------------
Space Complexity
-----------------------------------------------------------
O(min(m, k))
"""

import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        if not nums1 or not nums2 or k == 0:
            return []

        res = []
        minH = []

        m = len(nums1)
        n = len(nums2)

        # Initialize heap with first column
        for i in range(min(m, k)):
            total = nums1[i] + nums2[0]
            heapq.heappush(minH, (total, i, 0))

        # Extract k smallest pairs
        while minH and len(res) < k:
            total, i, j = heapq.heappop(minH)

            res.append([nums1[i], nums2[j]])

            if j + 1 < n:
                heapq.heappush(minH, (nums1[i] + nums2[j+1], i, j+1))

        return res


"""
-----------------------------------------------------------
Test Cases
-----------------------------------------------------------
"""

if __name__ == "__main__":

    s = Solution()

    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    print(s.kSmallestPairs(nums1, nums2, k))
    # Expected: [[1,2],[1,4],[1,6]]

    nums1 = [1,1,2]
    nums2 = [1,2,3]
    k = 2
    print(s.kSmallestPairs(nums1, nums2, k))
    # Expected: [[1,1],[1,1]]

    nums1 = [1,2]
    nums2 = [3]
    k = 3
    print(s.kSmallestPairs(nums1, nums2, k))
    # Expected: [[1,3],[2,3]]