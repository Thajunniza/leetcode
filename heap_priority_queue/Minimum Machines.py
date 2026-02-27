"""
Minimum Machines (Interval Scheduling / Meeting Rooms II)

This module calculates the minimum number of machines required
to execute all tasks without overlap.

Problem:
    - Given a list of tasks where each task is represented as:
        [start, end]
    - A machine can handle only one task at a time.
    - Return the minimum number of machines required.

Core Idea:
    - Sort tasks by start time.
    - Use a min-heap to track end times of active tasks.
    - If the earliest ending task finishes before the current task starts,
      reuse that machine.
    - Track the maximum heap size during processing.

Time Complexity:
    O(n log n)

Space Complexity:
    O(n)
"""

import heapq


def minimum_machines(tasks):
    """
    :type tasks: List[List[int]]
    :rtype: int
    """
    if not tasks:
        return 0

    # Sort tasks by start time
    tasks.sort(key=lambda x: x[0])

    end_heap = []
    max_machines = 0

    for start, end in tasks:

        # Free machines that finished before current task
        while end_heap and end_heap[0] <= start:
            heapq.heappop(end_heap)

        # Allocate machine for current task
        heapq.heappush(end_heap, end)

        # Track peak usage
        max_machines = max(max_machines, len(end_heap))

    return max_machines


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    print(minimum_machines([[1,4],[2,5],[7,9]]))      # Expected: 2
    print(minimum_machines([[6,7],[2,4],[8,12]]))     # Expected: 1
    print(minimum_machines([[1,5],[2,6],[3,7],[4,8]])) # Expected: 4