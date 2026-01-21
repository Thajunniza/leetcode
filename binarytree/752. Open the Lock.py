"""
LeetCode 752: Open the Lock

Algorithm:
-----------
We model the lock as an unweighted graph where:
- Each node is a 4-digit lock state (e.g., "0000")
- Each edge represents rotating one wheel up or down by 1

We use Breadth-First Search (BFS) because:
- All moves have equal cost
- BFS guarantees the shortest path (minimum turns)

Approach:
---------
1. Store all deadends in a set called `blocked`
2. Use the same set to also track visited states
3. Start BFS from "0000"
4. For each state, generate all 8 possible next states
5. Stop when the target is reached

Example:
--------
deadends = ["0201","0101","0102","1212","2002"]
target   = "0202"

Shortest path:
0000 → 1000 → 1100 → 1200 → 1201 → 1202 → 0202
Output: 6

Time Complexity:
----------------
O(10^4)
- There are at most 10,000 possible lock states
- Each state generates 8 neighbors

Space Complexity:
-----------------
O(10^4)
- Queue + visited (blocked) set

"""

from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        blocked = set(deadends)
        initial = "0000"

        # Edge cases
        if initial in blocked or target in blocked:
            return -1
        if target == initial:
            return 0

        # BFS initialization
        q = deque()
        q.append((initial, 0))
        blocked.add(initial)  # mark start as visited

        while q:
            lock, turns = q.popleft()

            if lock == target:
                return turns

            # Generate neighbors
            for i, c in enumerate(lock):
                num = int(c)

                # Rotate wheel up
                up = (num + 1) % 10
                nxt = lock[:i] + str(up) + lock[i + 1:]
                if nxt not in blocked:
                    blocked.add(nxt)
                    q.append((nxt, turns + 1))

                # Rotate wheel down
                down = (num - 1) % 10
                nxt = lock[:i] + str(down) + lock[i + 1:]
                if nxt not in blocked:
                    blocked.add(nxt)
                    q.append((nxt, turns + 1))

        return -1


# -------------------
# Test Run
# -------------------
if __name__ == "__main__":
    sol = Solution()

    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    print(sol.openLock(deadends, target))  # Expected: 6

    deadends = ["8888"]
    target = "0009"
    print(sol.openLock(deadends, target))  # Expected: 1

    deadends = ["0000"]
    target = "8888"
    print(sol.openLock(deadends, target))  # Expected: -1
