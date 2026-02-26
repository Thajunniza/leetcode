# --------------------------------------------------
# 1942: The Smallest Number of Unoccupied Chair
# --------------------------------------------------

# There is a party where friends will arrive and leave at specific times.
# Each chair has a non-negative integer index starting from 0 and is initially unoccupied.

# - When a friend arrives, they take the **smallest-indexed** unoccupied chair available.
# - When a friend leaves, their chair becomes available immediately at that leave time.

# You are given `times` where `times[i] = [arrival_i, leave_i]` for the i-th friend,
# and an integer `targetFriend`. Return the **chair index** that `targetFriend` will sit on.

# --------------------------------------------------
# Example:
# Input:
#     times = [[1,4],[2,3],[4,6]], targetFriend = 1
# Output:
#     1

# Explanation:
# - Friend 0 arrives at 1 → takes chair 0.
# - Friend 1 arrives at 2 → chair 0 is occupied, so takes chair 1.
# - Friend 1 leaves at 3 → chair 1 becomes free.
# - Friend 2 arrives at 4 → friend 0 leaves at 4, chair 0 becomes free first.
#   Friend 2 takes chair 0.
# Target is friend 1 → sat on chair 1.
# --------------------------------------------------

import heapq
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        """
        Greedy with two min-heaps:
        - Sort friends by arrival time (keeping original indices).
        - Maintain a min-heap of free chair indices.
        - Maintain a min-heap of occupied chairs ordered by leave time (leave, chair).
        - For each arrival:
            * Free all chairs whose leave time <= arrival.
            * Assign the smallest free chair.
            * If this is the target friend, return that chair.
            * Otherwise, push (leave, chair) to occupied.
        """
        # Pair each friend with their original index and sort by arrival time
        arrivals = sorted(enumerate(times), key=lambda x: x[1][0])

        n = len(arrivals)
        # All chair indices start free; managed as a min-heap
        free_chairs = list(range(n))
        heapq.heapify(free_chairs)

        # Occupied chairs: (leave_time, chair_index)
        occupied = []

        for idx, (arrive, leave) in arrivals:
            # Free chairs from friends who have already left
            while occupied and occupied[0][0] <= arrive:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(free_chairs, chair)

            # Assign the smallest available chair
            chair = heapq.heappop(free_chairs)

            # If this is the target friend, return immediately
            if idx == targetFriend:
                return chair

            # Otherwise, mark the chair as occupied until 'leave'
            heapq.heappush(occupied, (leave, chair))

        # Problem guarantees a return before this point
        return -1


# --------------------------------------------------
# Algorithm Explanation:
# --------------------------------------------------
# 1) Sort all friends by arrival time so we process events chronologically.
# 2) Before seating the next arriving friend, pop from the 'occupied' heap
#    while the smallest leave_time <= current arrival; each pop frees a chair
#    that we push back into the 'free_chairs' heap.
# 3) Pop the smallest-indexed chair from 'free_chairs' and:
#       - If this is the target friend, return it.
#       - Else, push (leave_time, chair_index) into 'occupied'.
# 4) Using a min-heap for 'free_chairs' ensures we always pick the smallest index.
#    Using a min-heap for 'occupied' ensures we free chairs in correct time order,
#    and arrivals at time t can use chairs from friends leaving at time t.
#
# --------------------------------------------------
# Time Complexity: O(n log n)  from sorting and heap operations
# Space Complexity: O(n)       for the heaps
# --------------------------------------------------


# --------------------------------------------------
# Test Cases
# --------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.smallestChair([[1,4],[2,3],[4,6]], 1))  # Expected: 1
    print(sol.smallestChair([[3,10],[1,5],[2,6]], 0)) # Expected: chair for friend 0 -> 2
    print(sol.smallestChair([[1,2],[2,3],[3,4],[4,5]], 3))  # Expected: 0
    print(sol.smallestChair([[1,4],[2,3],[3,5],[4,6]], 2))  # Expected: 1
    print(sol.smallestChair([[1,10],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]], 0))  # Expected: 0
