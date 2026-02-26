"""
===========================================================
1792. Maximum Average Pass Ratio
===========================================================

🧩 Problem:
There is a school with several classes. Each class has:
    - pass_i students who passed
    - total_i total students

You are given:
    classes = [[pass1, total1], [pass2, total2], ...]
    extraStudents = k

Each extra student is guaranteed to pass.

You must assign the k extra students to classes such that
the average pass ratio across all classes is maximized.

Return the maximum possible average pass ratio.

-----------------------------------------------------------
Example :
-----------------------------------------------------------
Example 1:
Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333

Explanation:
Initial ratios:
1/2 = 0.5
3/5 = 0.6
2/2 = 1.0

After optimal assignment:
3/4 = 0.75
3/5 = 0.6
2/2 = 1.0

Average = (0.75 + 0.6 + 1.0) / 3 = 0.78333

-----------------------------------------------------------
Brute Force Approach:
-----------------------------------------------------------
Try assigning each extra student to every class recursively
and compute the final average.

Problems:
- Exponential combinations
- Completely infeasible for constraints
-----------------------------------------------------------
⏱️ Time & Space Complexity (Brute Force)
-----------------------------------------------------------
Time:  O(n^k)
Space: O(k)

-----------------------------------------------------------
🧠 Optimal Approach: Greedy + Max Heap
-----------------------------------------------------------

Key Insight:
At every step, assign the extra student to the class that
gives the maximum marginal improvement.

Marginal Gain Formula:

Gain = (p + 1)/(t + 1) - p/t

We always choose the class with maximum gain.

Algorithm:
1. Compute current total pass ratio.
2. Push (-gain, p, t) into a max heap.
3. While extraStudents > 0:
   - Pop class with highest gain.
   - Add gain to total.
   - Increment p and t.
   - Recalculate gain and push back.
4. Return total / number_of_classes.

Why Greedy Works:
Each assignment is independent and always improves the
global average optimally due to diminishing returns.

-----------------------------------------------------------
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  O(n + k log n)
Space: O(n)

n = number of classes
k = extraStudents
"""

import heapq


class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """

        def get_gain(p, t):
            # Important: use float division for Python 2 safety
            return (p + 1) / float(t + 1) - p / float(t)

        max_heap = []
        total = 0.0

        # Build initial heap and compute total ratio
        for p, t in classes:
            total += p / float(t)
            gain = get_gain(p, t)
            heapq.heappush(max_heap, (-gain, p, t))

        # Assign extra students greedily
        while extraStudents:
            gain, p, t = heapq.heappop(max_heap)

            # Apply improvement
            total += -gain

            # Update class
            p += 1
            t += 1

            # Push updated class back
            heapq.heappush(max_heap, (-get_gain(p, t), p, t))

            extraStudents -= 1

        return total / float(len(classes))


# -----------------------------------------------------------
# Driver Examples
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print("=== Example 1 ===")
    classes = [[1, 2], [3, 5], [2, 2]]
    extra = 2
    result = sol.maxAverageRatio(classes, extra)
    print(f"Input: classes = {classes}, extraStudents = {extra}")
    print(f"Output: {round(result, 5)}")
    print("Expected: 0.78333")

    print("=== Example 2 ===")
    classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extra = 4
    result = sol.maxAverageRatio(classes, extra)
    print(f"Input: classes = {classes}, extraStudents = {extra}")
    print(f"Output: {round(result, 5)}")

    print("=== Example 3 (Single Class) ===")
    classes = [[5, 10]]
    extra = 3
    result = sol.maxAverageRatio(classes, extra)
    print(f"Input: classes = {classes}, extraStudents = {extra}")
    print(f"Output: {round(result, 5)}")