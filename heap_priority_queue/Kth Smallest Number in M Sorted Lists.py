"""
===========================================================
K-th Smallest Number in Multiple Sorted Lists
===========================================================

Problem:
Given multiple sorted lists of integers, find the k-th
smallest number across all lists.

Approach:
Use a Min Heap:
1. Push the first element of each list into the heap.
2. Pop the smallest element from the heap k times.
3. After popping an element, push the next element from
   the same list into the heap if it exists.
4. The last popped element is the k-th smallest number.

Time Complexity: O(k log n), where n = number of lists
Space Complexity: O(n)
"""

import heapq

def k_smallest_number(lists, k):
    """
    Find the k-th smallest number from a list of sorted lists.

    :param lists: List[List[int]] - each sublist is sorted ascending
    :param k: int - the k-th smallest element to find
    :return: int - the k-th smallest element
    """
    minH = []

    # Push first element of each list into the heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(minH, (lst[0], i, 0))

    val = 0
    for _ in range(k):
        if not minH:
            raise ValueError("k is larger than total number of elements.")
        val, i, j = heapq.heappop(minH)
        j += 1
        if j < len(lists[i]):
            heapq.heappush(minH, (lists[i][j], i, j))

    return val


"""
-----------------------------------------------------------
Test Cases
-----------------------------------------------------------
"""

if __name__ == "__main__":
    lists = [
        [1, 5, 9],
        [2, 6, 8],
        [3, 7, 10]
    ]
    k = 5
    print(k_smallest_number(lists, k))  # Expected: 5

    lists = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    k = 7
    print(k_smallest_number(lists, k))  # Expected: 7

    lists = [
        [1, 3, 5],
        [2, 4, 6]
    ]
    k = 4
    print(k_smallest_number(lists, k))  # Expected: 4