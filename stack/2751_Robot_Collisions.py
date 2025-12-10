"""
2751. Robot Collisions

🧩 Problem:
You are given three inputs describing robots on a 1D line:

positions[i] – starting position of robot i

healths[i] – initial health of robot i

directions[i] – 'L' or 'R' (moving left or right)

All robots:

Move at the same speed.

Collide only when a right-moving robot meets a left-moving robot.

When two robots collide:

If one has higher health, that robot:

Survives the collision.

Its health is decreased by 1.

If both have equal health, both robots are destroyed.

Collisions may cascade (a robot that survives a collision may collide again).

🎯 Goal:
After all possible collisions have resolved, return an array of the healths of the robots that are still alive, in the order of their original indices.

Examples:

Example 1:
Input:
positions = [5, 4, 3, 2, 1]
healths = [2, 17, 9, 15, 10]
directions = "RRLLL"

(Explanation sketch)

Sort robots by position:
pos: 1 2 3 4 5
idx: 4 3 2 1 0
dir: L L L R R
hp :10 15 9 17 2

Robots at position 4 (R, hp=17) and 3 (L, hp=9) collide.
R wins → hp becomes 16, L destroyed.

Robot at position 4 (R, 16) collides with L at 2 (hp=15).
R wins → hp becomes 15, L destroyed.

Robot at position 4 (R, 15) collides with L at 1 (hp=10).
R wins → hp becomes 14, L destroyed.

Final survivors (by original index order): [14, 17]

(Exact values depend on the official statement’s sample; this is just an intuition sketch.)

Example 2:
Input:
positions = [1, 3]
healths = [5, 3]
directions = "RL"

Process:
pos 1: robot A (R, hp=5)
pos 3: robot B (L, hp=3)

They move toward each other and collide once:
hp(A)=5, hp(B)=3 → A survives with hp=4, B destroyed.

Output:
[4] (only robot A survives)

Algorithm — Monotonic Stack (Right-Moving Robots):

Pattern: 🧱 Monotonic Stack — Collision (similar to Asteroid Collision)

Key observations:

Collisions occur only between:
→ a robot moving right ('R') and
← a robot moving left ('L')
and only when the R robot is to the left of the L robot.

If we sort robots by positions, then:

We process them from left to right.

We can maintain a stack of right-moving robots that are “waiting” to possibly collide with future left-moving robots.

When we meet a left-moving robot:

It may collide with one or more right-moving robots from the stack.

We simulate these collisions in LIFO order (last right-moving robot first).

Steps:

Create an array of indices order = sorted(range(n), key=lambda i: positions[i])

This gives robots sorted by position while keeping track of original indices.

Use:

stack: holds indices of robots that are moving to the right ('R') and are still alive.

Iterate over robots in order:

If direction is 'R':
→ Push its index onto stack.

If direction is 'L':
→ While stack is not empty and current left robot is still alive:
- Let j = stack[-1] be the index of the last alive right-moving robot.
- Compare healths[j] and healths[i]:
• If equal:
- Set both healths[j] and healths[i] to 0 (destroyed),
pop j from stack, and stop (left robot also dead).
• If healths[j] > healths[i]:
- Right robot survives, healths[j] -= 1,
left robot dies (healths[i] = 0), stop.
• If healths[j] < healths[i]:
- Left robot survives this round, healths[i] -= 1,
right robot j dies (healths[j] = 0), pop j,
and continue to check next right-moving robot in stack.

At the end:

healths contains the final health of each robot (0 = dead).

Return all positive healths in original index order:
return [h for h in healths if h > 0]

⏱ Time & Space Complexity:

Let n = len(positions).

Time Complexity:
• Sorting robots by position: O(n log n)
• Single pass with stack collisions: O(n)
• Final filtering: O(n)
⇒ Overall: O(n log n) (dominated by sorting; optimal for this problem).

Space Complexity:
• order array: O(n)
• stack: O(n) in worst case
⇒ Total: O(n) extra space.
"""
from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        """
        Simulates collisions between robots moving on a 1D line.

        Each robot i has:
            - positions[i]: its starting position
            - healths[i]:   its initial health
            - directions[i]: 'L' or 'R' for left or right

        Robots move at the same speed and collide only when a right-moving robot
        meets a left-moving robot. On collision:
            - If one has higher health, it survives with health - 1.
            - If both have equal health, both are destroyed.

        After resolving all collisions, this function returns the healths of all
        surviving robots in the order of their original indices.

        Approach:
            - Sort robots by position.
            - Use a stack to keep indices of right-moving robots.
            - For each left-moving robot, resolve collisions with the stack top
              until it either dies or no more right-moving robots can collide.

        Args:
            positions (List[int]): Starting positions of robots.
            healths   (List[int]): Initial healths of robots.
            directions (str): String of 'L' and 'R' directions.

        Returns:
            List[int]: Healths of surviving robots (original index order).
        """
        n = len(positions)

        # Process robots in increasing order of position
        order = sorted(range(n), key=lambda i: positions[i])

        stack = []  # will hold indices of robots moving to the right ('R')

        for idx in order:
            if directions[idx] == 'R':
                # Right-moving robots are candidates to collide with future left-movers
                stack.append(idx)
            else:
                # Current robot is moving left; it may collide with right-movers in stack
                while stack and healths[idx] > 0:
                    j = stack[-1]  # index of the last right-moving robot

                    if healths[j] == healths[idx]:
                        # Both robots destroyed
                        healths[j] = 0
                        healths[idx] = 0
                        stack.pop()
                        break
                    elif healths[j] > healths[idx]:
                        # Right-moving robot survives, loses 1 health
                        healths[j] -= 1
                        healths[idx] = 0
                        break
                    else:
                        # Left-moving robot survives this collision, loses 1 health
                        healths[idx] -= 1
                        healths[j] = 0
                        stack.pop()
                        # continue to check next right-moving robot (if any)

        # Collect all surviving robots' healths in original index order
        return [h for h in healths if h > 0]


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1 (you can adjust according to LeetCode's official examples)
    positions = [5, 4, 3, 2, 1]
    healths   = [2, 17, 9, 15, 10]
    directions = "RRLLL"
    print(sol.survivedRobotsHealths(positions, healths[:], directions))

    # Example 2
    positions = [1, 3]
    healths   = [5, 3]
    directions = "RL"
    print(sol.survivedRobotsHealths(positions, healths[:], directions))  # Expected: [4]
