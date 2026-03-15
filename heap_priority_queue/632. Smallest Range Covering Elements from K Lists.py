"""
===========================================================
632. Smallest Range Covering Elements from K Lists
===========================================================

Problem:
You are given k sorted lists of integers. Find the smallest
range [a, b] such that at least one number from each of the
k lists lies inside the range.

If multiple ranges have the same length, return the one
with the smallest starting value.

-----------------------------------------------------------
Example
-----------------------------------------------------------
Input:
nums = [
 [4,10,15,24,26],
 [0,9,12,20],
 [5,18,22,30]
]

Output:
[20,24]

Explanation:
20 comes from list 2
24 comes from list 1
22 comes from list 3
So the range [20,24] covers at least one number from
each list.
"""

import heapq


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        n = len(nums)
        min_heap = []
        right = float("-inf")

        # Step 1: Insert first element of each list
        for i in range(n):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            right = max(right, nums[i][0])

        result = [float("-inf"), float("inf")]

        # Step 2: Process heap
        while True:

            left, list_idx, elem_idx = heapq.heappop(min_heap)

            old_range = result[1] - result[0]
            new_range = right - left

            # Update result if better range found
            if new_range < old_range or (new_range == old_range and left < result[0]):
                result = [left, right]

            elem_idx += 1

            # If this list is exhausted we stop
            if elem_idx >= len(nums[list_idx]):
                break

            next_val = nums[list_idx][elem_idx]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx))

            right = max(right, next_val)

        return result


"""
-----------------------------------------------------------
Algorithm
-----------------------------------------------------------

1. Insert the first element from each list into a min heap.
   Heap stores: (value, list_index, element_index)

2. Track the maximum value among the inserted elements.

3. Pop the smallest element from the heap. This becomes
   the left boundary of the current range.

4. The right boundary is the current maximum element.

5. Update the best range if:
      - new range is smaller
      - OR same size but smaller starting value

6. Push the next element from the same list into the heap.

7. Update the maximum value if necessary.

8. Stop when any list runs out of elements.

-----------------------------------------------------------
Time Complexity
-----------------------------------------------------------

O(N log K)

N = total number of elements across all lists
K = number of lists

Each heap operation costs log K.

-----------------------------------------------------------
Space Complexity
-----------------------------------------------------------

O(K)

The heap stores at most one element from each list.
"""

# Test Runs for 632. Smallest Range Covering Elements from K Lists

def run_tests():
    sol = Solution()

    tests = [
        (
            [[4,10,15,24,26],
             [0,9,12,20],
             [5,18,22,30]],
            [20,24]
        ),
        (
            [[1,2,3],
             [1,2,3],
             [1,2,3]],
            [1,1]
        ),
        (
            [[1],
             [2],
             [3]],
            [1,3]
        ),
        (
            [[10,10],
             [11,11]],
            [10,11]
        ),
        (
            [[1,5,8],
             [4,12],
             [7,8,10]],
            [4,7]
        )
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.smallestRange(nums)
        print("Test", i)
        print("Input:", nums)
        print("Output:", result)
        print("Expected:", expected)
        print("Pass:", result == expected)
        print("-"*40)


run_tests()