"""
===========================================================
1700. Number of Students Unable to Eat Lunch
===========================================================

Approach: Counting (Optimal)

We count how many students prefer:
    0 → circular sandwich
    1 → square sandwich

Then iterate through sandwiches:
    • If at least one student wants the current sandwich → one eats
    • Otherwise → stop (deadlock)

Return the number of remaining students.
===========================================================
"""


class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        circleCount = 0
        squareCount = 0

        # Count student preferences
        for c in students:
            if c == 0:
                circleCount += 1
            else:
                squareCount += 1

        # Process sandwiches
        for s in sandwiches:
            if s == 0:
                if circleCount == 0:
                    break
                circleCount -= 1
            else:
                if squareCount == 0:
                    break
                squareCount -= 1

        return circleCount + squareCount


# ---------------------------------------------------------
# Test Cases
# ---------------------------------------------------------
def test_countStudents():
    sol = Solution()

    # Given examples
    assert sol.countStudents([1, 1, 0, 0], [0, 1, 0, 1]) == 0
    assert sol.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]) == 3

    # All students can eat
    assert sol.countStudents([0, 0, 0, 1], [0, 0, 0, 1]) == 0
    assert sol.countStudents([1, 1, 1], [1, 1, 1]) == 0

    # None can eat after some point
    assert sol.countStudents([0, 0, 0], [1, 1, 1]) == 3
    assert sol.countStudents([1, 1, 1], [0, 0, 0]) == 3

    # Mixed deadlock cases
    assert sol.countStudents([0, 1, 0, 1], [0, 0, 0, 0]) == 2
    assert sol.countStudents([1, 0, 1, 0], [1, 1, 1, 1]) == 2

    # Edge cases
    assert sol.countStudents([], []) == 0
    assert sol.countStudents([0], [0]) == 0
    assert sol.countStudents([1], [0]) == 1

    print("All test cases passed!")


# ---------------------------------------------------------
# Driver
# ---------------------------------------------------------
if __name__ == "__main__":
    test_countStudents()
