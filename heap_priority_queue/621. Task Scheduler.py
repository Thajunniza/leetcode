# 621. Task Scheduler — Heap Simulation
#
# This module computes the least number of intervals needed to finish all tasks with a cooldown,
# using a max-heap + cooldown queue simulation.
#
# Problem:
#     - You are given tasks as uppercase letters A–Z.
#     - Each task takes exactly 1 time unit.
#     - Two identical tasks must be separated by at least `n` intervals (idle or other tasks).
#     - Return the minimum total time (intervals) to finish all tasks.
#
# Core Idea (Heap Simulation):
#     - Count each task’s frequency.
#     - Use a max-heap (simulated with negative counts) to always pick the task with highest
#       remaining frequency.
#     - After executing a task, if it still has remaining occurrences, put it in a cooldown queue
#       with the time when it becomes available again.
#     - If multiple tasks become available at the same time, reactivate all of them immediately.
#
# Why a Heap?
#     - Efficiently retrieves the current most-needed task (highest remaining count).
#     - Greedy choice (always pick the largest remaining count) tends to minimize future idle time.
#
# Cooldown Handling:
#     - If a task is executed at time `t`, it can be scheduled again from time `t + n + 1`.
#     - In this implementation, we enqueue with a ready_time of `t + n` and reinsert tasks
#       when `ready_time <= current_time`, which is equivalent given the loop increments per unit.
#
# Constraints:
#     - 1 <= len(tasks) <= 10^5 (typical)
#     - 0 <= n
#     - Tasks are uppercase 'A'–'Z'
#
# Complexity:
#     - Time  : O(T log U), where T is total tasks and U is number of distinct tasks (<= 26),
#               practically close to O(T).
#     - Space : O(U) for heap + cooldown queue.

import heapq
from collections import deque

class Solution(object):
    """DSA-style solution using max-heap (via negative counts) + cooldown queue."""

    def leastInterval(self, tasks, n):
        """
        Return the least number of intervals to finish all tasks, including idles.

        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks:
            return 0
        if n == 0:
            return len(tasks)

        # 1) Count frequencies
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1

        # 2) Build max-heap of remaining counts (store negatives)
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)

        # 3) Simulation with time and cooldown queue
        time = 0
        # Queue holds (neg_remaining_count, ready_time)
        q = deque()

        while maxHeap or q:
            time += 1

            # Run one task (highest remaining count), if any
            if maxHeap:
                neg_cnt = heapq.heappop(maxHeap)  # neg_cnt <= -1
                neg_cnt += 1                      # we executed one instance; closer to zero
                if neg_cnt != 0:
                    # Put into cooldown; it becomes ready again after n intervals
                    # We reinsert when ready_time <= current time
                    q.append((neg_cnt, time + n))

            # Reactivate all tasks whose cooldown has expired by now
            while q and q[0][1] <= time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time


# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    sol = Solution()
    assert sol.leastInterval(["A","A","A","B","B","B"], 2) == 8
    assert sol.leastInterval(["A","A","A","B","B","B"], 0) == 6
    assert sol.leastInterval(["A","A","A","A"], 3) == 13
    assert sol.leastInterval(["A","B","C","A","B","C"], 2) == 6
    print("All tests passed.")