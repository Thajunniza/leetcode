"""
===========================================================
857. Minimum Cost to Hire K Workers
===========================================================

Problem:
You are given n workers, each with a quality and minimum wage.
Hire exactly k workers such that:
1. Every worker is paid at least their minimum wage.
2. Payment is proportional to quality.

Return the minimum total cost to hire k workers.
"""

import heapq


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """

        # Step 1: Compute wage-to-quality ratio for each worker
        workers = []
        for i in range(len(quality)):
            ratio = wage[i] / float(quality[i])
            workers.append((ratio, quality[i]))

        # Step 2: Sort workers by ratio ascending
        workers.sort()

        maxH = []         # max heap to track largest qualities
        quality_sum = 0
        res = float('inf')

        # Step 3: Iterate through sorted workers
        for ratio, q in workers:
            heapq.heappush(maxH, -q)
            quality_sum += q

            # Keep heap size <= k
            if len(maxH) > k:
                quality_sum += heapq.heappop(maxH)  # remove largest quality

            # When we have exactly k workers, compute total cost
            if len(maxH) == k:
                res = min(res, ratio * quality_sum)

        return res


"""
-----------------------------------------------------------
Algorithm
-----------------------------------------------------------

1. Compute ratio = wage[i]/quality[i] for every worker.
2. Sort workers by ratio ascending.
3. Use a max heap to keep track of k smallest qualities.
4. Maintain the sum of selected qualities.
5. For each worker, if heap size == k:
      cost = ratio * sum_of_qualities
6. Track the minimum cost.

-----------------------------------------------------------
Time Complexity
-----------------------------------------------------------

O(n log n) for sorting + O(n log k) for heap operations.

-----------------------------------------------------------
Space Complexity
-----------------------------------------------------------

O(k) for the heap.
"""

# Test Runs for 857. Minimum Cost to Hire K Workers

def run_tests():
    sol = Solution()

    tests = [
        # Example 1
        (
            [10,20,5],   # quality
            [70,50,30],  # wage
            2,           # k
            105.0        # expected
        ),
        # Example 2: all same ratio
        (
            [3,1,10], 
            [30,10,100], 
            2, 
            40.0
        ),
        # Example 3: k = 1
        (
            [10,20,5], 
            [70,50,30], 
            1, 
            30.0
        ),
        # Example 4: multiple small ratios
        (
            [1,2,3,4], 
            [1,2,1,2], 
            2, 
            2.5
        ),
        # Edge case: single worker
        (
            [5], 
            [10], 
            1, 
            10.0
        )
    ]

    for i, (quality, wage, k, expected) in enumerate(tests, 1):
        result = sol.mincostToHireWorkers(quality, wage, k)
        print(f"Test {i}")
        print("Quality:", quality)
        print("Wage:", wage)
        print("K:", k)
        print("Output:", result)
        print("Expected:", expected)
        print("Pass:", abs(result - expected) < 1e-5)
        print("-"*40)


run_tests()