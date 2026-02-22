"""
506. Relative Ranks

This module assigns ranks to athletes based on their scores.

Two approaches are included:

1. Heap-based:
    - Build max-heap with (negative score, index)
    - Pop elements in descending order
    - Assign medals/ranks

2. Sorting-based:
    - Sort scores descending
    - Map scores to ranks
    - Return result using original indices

Complexity:
    - Heap approach: Time O(n log n), Space O(n)
    - Sorting approach: Time O(n log n), Space O(n)
    - Heap is beneficial if only top k elements or streaming input needed
    - Sorting is simpler when full ranking is needed
"""

import heapq

class HeapSolution(object):
    """Heap-based DSA-style solution."""

    def findRelativeRanks(self, score):
        """
        Assign relative ranks using max heap.

        :type score: List[int]
        :rtype: List[str]
        """

        n = len(score)
        heap = [(-score[i], i) for i in range(n)]
        heapq.heapify(heap)

        result = [""] * n
        rank = 1

        while heap:
            _, index = heapq.heappop(heap)

            if rank == 1:
                result[index] = "Gold Medal"
            elif rank == 2:
                result[index] = "Silver Medal"
            elif rank == 3:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank)

            rank += 1

        return result


class SortSolution(object):
    """Sorting-based DSA-style solution."""

    def findRelativeRanks(self, score):
        """
        Assign relative ranks using sorting.

        :type score: List[int]
        :rtype: List[str]
        """

        sorted_scores = sorted(score, reverse=True)
        rank_map = {}

        for idx, val in enumerate(sorted_scores):
            if idx == 0:
                rank_map[val] = "Gold Medal"
            elif idx == 1:
                rank_map[val] = "Silver Medal"
            elif idx == 2:
                rank_map[val] = "Bronze Medal"
            else:
                rank_map[val] = str(idx + 1)

        return [rank_map[x] for x in score]


# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    score = [10, 3, 8, 9, 4]

    heap_sol = HeapSolution()
    sort_sol = SortSolution()

    print("Heap approach:", heap_sol.findRelativeRanks(score))
    print("Sort approach:", sort_sol.findRelativeRanks(score))