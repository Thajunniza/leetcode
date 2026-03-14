"""
===========================================================
378. Kth Smallest Element in a Sorted Matrix
===========================================================

Problem:
Given an n x n matrix where each of the rows and columns
is sorted in ascending order, return the kth smallest
element in the matrix.

Note: It is the kth smallest element in the sorted order,
not the kth distinct element.

-----------------------------------------------------------
Example
-----------------------------------------------------------
Input:
matrix = [
 [1, 5, 9],
 [10,11,13],
 [12,13,15]
]
k = 8

Output: 13

Explanation:
The sorted elements are:
[1,5,9,10,11,12,13,13,15]
The 8th smallest element is 13.

-----------------------------------------------------------
Approach 1: Min Heap (Priority Queue)
-----------------------------------------------------------
Idea:
- Since rows and columns are sorted, the smallest element
  of each row can be pushed into a min heap.
- Pop the smallest element k times.
- Push the next element from the same row.

Time Complexity:
O(k log n)

Space Complexity:
O(n)

-----------------------------------------------------------
Python Implementation
-----------------------------------------------------------
"""

import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)

        heap = []
        
        # push first element of each row
        for r in range(min(n, k)):
            heapq.heappush(heap, (matrix[r][0], r, 0))

        for _ in range(k - 1):
            val, r, c = heapq.heappop(heap)

            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

        return heapq.heappop(heap)[0]


"""
-----------------------------------------------------------
Approach 2: Binary Search (Optimal)
-----------------------------------------------------------
Idea:
- The matrix is sorted row-wise and column-wise.
- The smallest value is matrix[0][0]
- The largest value is matrix[n-1][n-1]
- Perform binary search on this value range.

Steps:
1. Pick mid value.
2. Count how many numbers in matrix <= mid.
3. If count < k → move left to mid+1
4. Otherwise move right to mid

Time Complexity:
O(n log(max-min))

Space Complexity:
O(1)

-----------------------------------------------------------
Python Implementation
-----------------------------------------------------------
"""

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)

        def countLessEqual(x):
            count = 0
            col = n - 1

            for row in range(n):
                while col >= 0 and matrix[row][col] > x:
                    col -= 1
                count += (col + 1)

            return count

        left = matrix[0][0]
        right = matrix[n-1][n-1]

        while left < right:
            mid = (left + right) // 2

            if countLessEqual(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left


matrix = [
    [1,5,9],
    [10,11,13],
    [12,13,15]
]
k = 8

print(Solution().kthSmallest(matrix, k))