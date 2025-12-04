"""
===========================================================
853. Car Fleet
===========================================================

🧩 Problem:
There are `n` cars traveling towards the same destination.

    • Destination is at position `target` on a 1D road.
    • The i-th car starts at position `position[i]` with speed `speed[i]`.
    • All cars move **in the same direction** towards `target`.
    • A car can **never pass** another car in front of it.
    • If a faster car catches up to a slower car, they become a **fleet** and share the same speed.
    • A car fleet is a group of cars that travel together at the same speed.

🎯 Goal:
Return the **number of car fleets** that will arrive at the destination.

Each car is either:
    • alone as a fleet, or
    • part of a larger fleet formed by catching up to others.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:
    target   = 12
    position = [10, 8,  0, 5, 3]
    speed    = [ 2, 4,  1, 1, 3]

Step 1: Pair and sort by starting position (descending):
    Cars as (position, speed):
        (10, 2), (8, 4), (5, 1), (3, 3), (0, 1)

Step 2: Compute time to reach target for each (from closest to farthest):
    time = (target - position) / speed

    (10, 2) → time = (12 - 10) / 2 = 1.0
    (8, 4)  → time = (12 - 8)  / 4 = 1.0
    (5, 1)  → time = (12 - 5)  / 1 = 7.0
    (3, 3)  → time = (12 - 3)  / 3 = 3.0
    (0, 1)  → time = (12 - 0)  / 1 = 12.0

Process from right to left in terms of **road** (we already reversed sort):
    - Start with (10,2): fleet time = 1.0
    - (8,4): time = 1.0
        → since 1.0 ≤ 1.0, it catches the first car → same fleet
    - (5,1): time = 7.0
        → 7.0 > 1.0 → cannot catch previous fleet → new fleet
    - (3,3): time = 3.0
        → 3.0 ≤ 7.0 → joins fleet with time 7.0
    - (0,1): time = 12.0
        → 12.0 > 7.0 → new fleet

Fleets:
    • Fleet 1: cars at pos 10 & 8 (time 1.0)
    • Fleet 2: cars at pos 5 & 3 (time 7.0)
    • Fleet 3: car at pos 0      (time 12.0)

Output:
    3


Example 2:
Input:
    target   = 10
    position = [3]
    speed    = [3]

Only one car → one fleet.

Output:
    1


Example 3:
Input:
    target   = 10
    position = [6, 8]
    speed    = [3, 2]

Times:
    (8,2) → (10-8)/2 = 1.0
    (6,3) → (10-6)/3 = 1.333...

Car at 6 is behind and slower in arrival time (1.333 > 1.0) but *starts behind*,
so it never catches up → 2 separate fleets.

Output:
    2

-----------------------------------------------------------
Algorithm — Sort + Monotonic Stack (by Time)
-----------------------------------------------------------

Key idea:
    • Cars can only interact **forward** (a car behind may catch up to the one ahead).
    • After sorting by position **descending**:
          → We process cars from closest to the target to farthest.

Steps:

1) Zip `position` and `speed` into pairs `(pos, spd)`.
2) Sort pairs in **descending** order of `pos`
       (from closest to target to farthest).
3) For each car in that order:
       time = (target - pos) / spd     # time to reach target

   Maintain a stack (or just a list) of **fleet times**:

       • If the stack is empty, push time (new fleet).
       • Else:
            - If current time > last fleet time:
                  → This car cannot catch the fleet ahead → new fleet → push time.
            - Else:
                  → current car arrives earlier or same time, so it catches up
                    and merges into the fleet of the car in front → do NOT push.

4) At the end:
       Number of fleets = len(stack)

Why?
    • A "later" car (farther from target) with smaller or equal time will catch up
      to the one ahead and form/merge into a fleet.
    • Only when its time is strictly greater than the previous fleet time does it
      remain a separate fleet.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n log n)
    • Sorting the cars by position dominates.

Space Complexity:  O(n)
    • For storing pairs and the fleet times stack.

"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up positions and speeds
        cars = [(p, s) for p, s in zip(position, speed)]
        # Sort by position descending (closest to target first)
        cars.sort(reverse=True)

        stack = []  # will store times (monotonic non-increasing)

        for p, s in cars:
            time = (target - p) / s  # time to reach target from this position

            # If this car takes more time than the fleet in front,
            # it can't catch up → forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
            # else: it joins the fleet ahead (do nothing)

        return len(stack)


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    # Expected: 3

    print(sol.carFleet(10, [3], [3]))
    # Expected: 1

    print(sol.carFleet(10, [6, 8], [3, 2]))
    # Expected: 2

    print(sol.carFleet(100, [0, 2, 4], [4, 2, 1]))
    # Additional check
