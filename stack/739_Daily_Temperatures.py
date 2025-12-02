"""
===========================================================
739. Daily Temperatures
===========================================================

🧩 Problem:
You are given a list of daily temperatures `temperatures`, where `temperatures[i]` 
is the temperature on day i.

For each day, you need to find:
    ➜ How many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

🎯 Goal:
Return an array `answer` such that `answer[i]` is the number of days you must wait 
after day i to get a warmer temperature. If no warmer day exists, answer[i] = 0.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]

Explanation:
    - Day 0: 73 → next warmer is 74 on day 1 → wait 1 day
    - Day 1: 74 → next warmer is 75 on day 2 → wait 1 day
    - Day 2: 75 → next warmer is 76 on day 6 → wait 4 days
    - Day 3: 71 → next warmer is 72 on day 5 → wait 2 days
    - Day 4: 69 → next warmer is 72 on day 5 → wait 1 day
    - Day 5: 72 → next warmer is 76 on day 6 → wait 1 day
    - Day 6: 76 → no warmer day → 0
    - Day 7: 73 → no warmer day → 0


Example 2:
Input:  temperatures = [30, 40, 50, 60]
Output: [1, 1, 1, 0]

Example 3:
Input:  temperatures = [30, 60, 90]
Output: [1, 1, 0]

-----------------------------------------------------------
Algorithm — Monotonic Stack (Decreasing):
-----------------------------------------------------------

Pattern: 🧱 Monotonic Stack (Next Greater Element to the Right)

Idea:
- We want, for each day i, the **next day j > i where temperatures[j] > temperatures[i]**.
- We use a **monotonic decreasing stack** that stores indices of days.
    • Stack maintains temperatures in decreasing order: temperatures[stack[-1]] ≥ temperatures[stack[-2]].

Steps:
1. Initialize:
       answer = [0] * n
       stack = []  # will store indices of days

2. Iterate i from 0 to n-1:
       While stack is not empty AND current temp > temp at stack top:
            - Let prev = stack.pop()
            - We found the next warmer day for prev → answer[prev] = i - prev
       Push current index i onto stack.

3. Any index left in stack has no warmer future day → answer already 0.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    - Each index is pushed and popped at most once.

Space Complexity:  O(n)
    - Stack can hold up to n indices in the worst case.

-----------------------------------------------------------
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        Returns the number of days to wait for a warmer temperature for each day.

        Uses a monotonic decreasing stack of indices to find, for each day i,
        the next day j > i where temperatures[j] > temperatures[i].

        Args:
            temperatures (List[int]): List of daily temperatures.

        Returns:
            List[int]: List where result[i] is number of days until a warmer temp.
                       0 if no warmer future day exists.

        Example:
            >>> Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
            [1, 1, 4, 2, 1, 1, 0, 0]
        """
        n = len(temperatures)
        answer = [0] * n          # Default 0: assume no warmer day
        stack = []                # Stack of indices, temps in decreasing order

        for i, temp in enumerate(temperatures):
            # While current temperature is warmer than the temperature at
            # the index on top of the stack → we found the next warmer day
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index

            # Push current index onto stack
            stack.append(i)

        return answer


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))  # Expected: [1,1,4,2,1,1,0,0]
    print(sol.dailyTemperatures([30,40,50,60]))              # Expected: [1,1,1,0]
    print(sol.dailyTemperatures([30,60,90]))                 # Expected: [1,1,0]
