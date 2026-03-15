"""
===========================================================
K Maximum Sum Combinations From Two Arrays
===========================================================

Problem:
Given two arrays A and B of size n, return the k maximum
sum combinations from the possible pairs.

Each pair is formed by selecting one element from A
and one element from B.

Return the k largest sums possible.

-----------------------------------------------------------
Example
-----------------------------------------------------------
Input:
A = [3,2]
B = [1,4]
k = 2

Possible sums:
3 + 1 = 4
3 + 4 = 7
2 + 1 = 3
2 + 4 = 6

Output:
[7,6]
"""

import heapq


def max_combinations(arr1, arr2, k):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :type k: int
    :rtype: List[int]
    """

    # Step 1: sort both arrays in descending order
    arr1.sort(reverse=True)
    arr2.sort(reverse=True)

    n = len(arr1)

    maxH = []
    visited = set()
    res = []

    # Step 2: push the largest possible sum
    heapq.heappush(maxH, (-(arr1[0] + arr2[0]), 0, 0))
    visited.add((0, 0))

    # Step 3: extract k maximum sums
    for _ in range(k):

        val, i, j = heapq.heappop(maxH)
        res.append(-val)

        # Next combination from arr1
        if i + 1 < n and (i + 1, j) not in visited:
            heapq.heappush(maxH, (-(arr1[i+1] + arr2[j]), i+1, j))
            visited.add((i+1, j))

        # Next combination from arr2
        if j + 1 < n and (i, j + 1) not in visited:
            heapq.heappush(maxH, (-(arr1[i] + arr2[j+1]), i, j+1))
            visited.add((i, j+1))

    return res


"""
-----------------------------------------------------------
Algorithm
-----------------------------------------------------------

1. Sort both arrays in descending order.
2. The largest possible sum is arr1[0] + arr2[0].
3. Use a max heap to always get the next largest sum.
4. Store index pairs (i, j) representing arr1[i] + arr2[j].
5. When popping (i, j), generate neighbors:
      (i+1, j)
      (i, j+1)
6. Use a visited set to avoid pushing the same pair twice.
7. Repeat until k sums are extracted.

-----------------------------------------------------------
Time Complexity
-----------------------------------------------------------

Sorting arrays:
O(n log n)

Heap operations:
O(k log k)

Total:
O(n log n + k log k)

-----------------------------------------------------------
Space Complexity
-----------------------------------------------------------

Heap + visited set:

O(k)
"""

# -----------------------------
# Test Runs
# -----------------------------

if __name__ == "__main__":

    tests = [
        ([3,2], [1,4], 2),
        ([4,2,5,1], [8,0,3,5], 3),
        ([1,2], [3,4], 3),
        ([10,9,8], [7,6,5], 4)
    ]

    for i, (a, b, k) in enumerate(tests, 1):
        print(f"Test Case {i}")
        print("Array1:", a)
        print("Array2:", b)
        print("k:", k)
        print("Output:", max_combinations(a[:], b[:], k))  # copy arrays
        print("-"*40)