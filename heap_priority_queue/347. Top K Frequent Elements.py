"""
347. Top K Frequent Elements

This module finds the k most frequent elements in an integer array.

Problem:
    - Given an integer array nums and an integer k,
      return the k most frequent elements.
    - You may return the answer in any order.

Core Idea:
    - Count frequency using a hash map (dictionary).
    - Maintain a min-heap of size k based on frequency.
    - If heap size exceeds k, remove the smallest frequency.
    - The heap finally contains the k most frequent elements.

Why Min-Heap?
    - Keeps only top k frequent elements.
    - Root always holds the smallest frequency among top k.
    - Efficient removal when heap exceeds size k.

Constraints:
    - 1 <= nums.length <= large constraints
    - 1 <= k <= number of unique elements

Complexity:
    - Time  : O(n log k)
              * Frequency count → O(n)
              * Heap operations → O(n log k)
    - Space : O(n) (frequency map + heap)
"""

import heapq


class Solution(object):
    """DSA-style solution using frequency map + size-k min-heap."""

    def topKFrequent(self, nums, k):
        """
        Return k most frequent elements.

        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Step 1: Count frequencies
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Maintain min-heap of size k
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        # Step 3: Extract results
        result = []
        for count, num in heap:
            result.append(num)

        return result


# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f"Top {k} frequent elements: {sol.topKFrequent(nums, k)}")