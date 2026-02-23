#
# Greedy + Max-Heap (via negation) solution for:
# 1642. Furthest Building You Can Reach
#
# Idea:
#   - Spend bricks for every positive climb.
#   - Track all climbs in a max-heap (store as negative values).
#   - If we overspend bricks (bricks < 0), retroactively assign a ladder
#     to the largest climb so far (pop from heap) to refund bricks.
#   - If no ladders remain when overspending, we cannot reach the current building.
#
# Complexity:
#   - Time  : O(n log n) in worst case (each climb involves a heap push; some involve a pop)
#   - Space : O(n) for the heap (in the worst case of all positive climbs)

import heapq

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        maxHeap = []  # store negative diffs to simulate a max-heap

        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]

            # No cost if we don't need to climb up
            if diff <= 0:
                continue

            # Spend bricks first and record this climb
            bricks -= diff
            heapq.heappush(maxHeap, -diff)

            # If overspent, try to replace the largest previous brick usage with a ladder
            if bricks < 0:
                if ladders == 0:
                    # Can't climb to i; furthest reachable is i-1
                    return i - 1
                ladders -= 1
                # Refund bricks by assigning a ladder to the largest climb so far
                bricks += -heapq.heappop(maxHeap)

        # If we never failed, we've reached the last building
        return len(heights) - 1


if __name__ == "__main__":
    # Quick sanity checks
    sol = Solution()
    print(sol.furthestBuilding([4,2,7,6,9,14,12], 5, 1))  # Expected: 4
    print(sol.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2))  # Expected: 7
    print(sol.furthestBuilding([14,3,19,3], 17, 0))  # Expected: 3