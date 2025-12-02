"""
===========================================================
735. Asteroid Collision
===========================================================

🧩 Problem:
We are given an array `asteroids` of integers representing asteroids in a row.

Each asteroid has:
    • Magnitude → size  (abs(value))
    • Sign      → direction:
          > 0  → moving right
          < 0  → moving left

All asteroids move at the same speed.

When two asteroids meet:
    • The smaller one explodes.
    • If both are the same size, both explode.
    • Asteroids moving in the same direction never meet.

🎯 Goal:
Return the state of the asteroids after all collisions.  
The answer should be the final list of asteroids that remain in order.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  [5, 10, -5]

Process:
    5   → [5]
    10  → [5, 10]
    -5  → collision with 10:
              10 vs -5 → |10| > | -5 | → -5 explodes
Final: [5, 10]

Output: [5, 10]


Example 2:
Input: [8, -8]

Process:
    8   → [8]
    -8  → collision:
              8 vs -8 → equal size → both explode
Final: []

Output: []


Example 3:
Input: [10, 2, -5]

Process:
    10  → [10]
    2   → [10, 2]
    -5  → collide with 2:
              2 vs -5 → |2| < 5 → 2 explodes → [10]
           now collide with 10:
              10 vs -5 → |10| > 5 → -5 explodes
Final: [10]

Output: [10]

-----------------------------------------------------------
Algorithm — Stack Simulation:
-----------------------------------------------------------

Use a stack to represent the "current stable" asteroid state from left to right.

For each asteroid `a` in input:
    • While there is a possible collision:
          - top of stack > 0  (moving right)
          - current asteroid a < 0 (moving left)
      Compare sizes:
          1) If |top| < |a|:
                 → top explodes (pop from stack), continue checking with new top
          2) If |top| == |a|:
                 → both explode (pop top, do NOT push a), stop processing this a
          3) If |top| > |a|:
                 → a explodes (DO NOT push a), stop processing this a

    • If a survives all collisions, push it onto the stack.

At the end, stack represents the final asteroid state.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    - Each asteroid is pushed and popped at most once.

Space Complexity:  O(n)
    - In the worst case (no collisions), all asteroids remain in the stack.

-----------------------------------------------------------
"""

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        Simulates asteroid collisions and returns the final state.

        Args:
            asteroids (List[int]): List of integers representing asteroids.
                                   Positive → moving right, Negative → moving left.

        Returns:
            List[int]: Final configuration of asteroids after all collisions.
        """
        stack = []

        for a in asteroids:
            # Assume current asteroid is alive initially
            alive = True

            # Collision can only happen if:
            #   - previous asteroid is moving right (>0)
            #   - current asteroid is moving left (<0)
            while stack and stack[-1] > 0 and a < 0:
                top = stack[-1]

                if top < -a:
                    # Top asteroid is smaller → it explodes
                    stack.pop()
                    # Continue to check with new top of stack
                    continue

                elif top == -a:
                    # Both asteroids same size → both explode
                    stack.pop()
                    alive = False  # current asteroid also destroyed
                    break

                else:
                    # Top asteroid is larger → current asteroid is destroyed
                    alive = False
                    break

            # If current asteroid survived all collisions, push it to stack
            if alive:
                stack.append(a)

        return stack


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.asteroidCollision([5, 10, -5]))     # Expected: [5, 10]
    print(sol.asteroidCollision([8, -8]))         # Expected: []
    print(sol.asteroidCollision([10, 2, -5]))     # Expected: [10]
    print(sol.asteroidCollision([-2, -1, 1, 2]))  # Expected: [-2, -1, 1, 2]
