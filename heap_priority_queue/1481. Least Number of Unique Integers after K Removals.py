"""
===========================================================
1481. Least Number of Unique Integers after K Removals
===========================================================

Problem:
Given an integer array arr and an integer k, remove exactly
k elements from the array. Find the least number of unique
integers left.

-----------------------------------------------------------
Example
-----------------------------------------------------------
Input:  arr = [5,5,4], k = 1
Output: 1

Explanation:
Remove one occurrence of 4 → remaining array [5,5]
Unique numbers left = 1


===========================================================
Approach (Greedy + Min Heap)
===========================================================

Idea:
To minimize the number of unique integers left, we should
remove numbers with the smallest frequency first.

Steps:
1. Count the frequency of each number.
2. Store frequencies in a min heap.
3. Always remove the smallest frequency group first.
4. If k is enough to remove that group, subtract it from k.
5. Continue until k becomes 0.


===========================================================
Code
===========================================================
"""
import heapq

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):

        # Step 1: Count frequencies
        have = {}
        for val in arr:
            have[val] = have.get(val, 0) + 1

        # Step 2: Build min heap of frequencies
        minH = []
        for val, count in have.items():
            minH.append(count)

        heapq.heapify(minH)

        # Step 3: Remove smallest frequency groups
        while k > 0 and minH:
            count = heapq.heappop(minH)

            if k >= count:
                k -= count
            else:
                heapq.heappush(minH, count)
                break

        return len(minH)

"""
===========================================================
Time Complexity Analysis
===========================================================

Let:
n = length of array
u = number of unique elements

1. Frequency Counting
   We traverse the array once.

   Time = O(n)

2. Building the Heap
   We insert frequencies of unique elements.

   Time = O(u)

3. Heapify
   Python heapify builds heap in linear time.

   Time = O(u)

4. Heap Pop Operations
   Each heap pop costs O(log u).

   In the worst case we pop all unique elements.

   Time = O(u log u)

Total Time Complexity:

O(n + u log u)

Since u ≤ n

Worst case:

O(n log n)


===========================================================
Space Complexity Analysis
===========================================================

1. Frequency Dictionary
   Stores frequency for each unique number.

   Space = O(u)

2. Min Heap
   Stores u frequency values.

   Space = O(u)

Total Space Complexity:

O(u)

Worst Case:

O(n)


===========================================================
Key Intuition
===========================================================

Removing elements with the smallest frequency first ensures
that we eliminate entire numbers from the array using the
least amount of k, minimizing the number of unique integers
remaining.

"""
# ===================== Test Cases =====================
def run_tests():
    sol = Solution()
    test_cases = [
        ([5,5,4], 1, 1),
        ([4,3,1,1,3,3,2], 3, 2),
        ([2,2,2,2], 2, 1),
        ([1,2,3], 3, 0),
        ([1,2,2,3], 0, 3),
        ([1,1,1,2,2,3], 2, 2),
        ([1], 1, 0),
        ([1,2,3,4], 2, 2),
    ]

    for i, (arr, k, expected) in enumerate(test_cases, 1):
        result = sol.findLeastNumOfUniqueInts(arr, k)
        print(f"Test Case {i}: arr={arr}, k={k} → Output: {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")

if __name__ == "__main__":
    run_tests()