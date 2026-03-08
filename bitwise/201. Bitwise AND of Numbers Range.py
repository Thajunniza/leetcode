"""
===========================================================
201. Bitwise AND of Numbers Range
===========================================================

Problem:
Given two integers left and right that represent the range
[left, right], return the bitwise AND of all numbers in
this range (inclusive).

-----------------------------------------------------------
Example
-----------------------------------------------------------
Input:  left = 5, right = 7
Output: 4

Explanation:
5 = 101
6 = 110
7 = 111
--------------
AND = 100 = 4

Input:  left = 0, right = 0
Output: 0

-----------------------------------------------------------
Approach 1 — Common Prefix via Bit Shifting

Idea:
1. Continuously right shift both left and right
   until they become equal.
2. Count how many shifts were performed.
3. The remaining number is the common prefix.
4. Left shift back to restore the result.

This works because lower bits change across the range,
while only the common prefix remains stable.

Time Complexity:  O(log n)
Space Complexity: O(1)
-----------------------------------------------------------
"""

class SolutionShift(object):

    def rangeBitwiseAnd(self, left, right):

        shift = 0

        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        return left << shift


"""
-----------------------------------------------------------
Approach 2 — Brian Kernighan Bit Trick

Idea:
Remove the rightmost set bit of 'right' repeatedly until
right becomes less than or equal to left.

Operation:
    right = right & (right - 1)

This clears the lowest set bit each time.

Time Complexity:  O(number of set bits)
Space Complexity: O(1)
-----------------------------------------------------------
"""

class SolutionBitTrick(object):

    def rangeBitwiseAnd(self, left, right):

        while right > left:
            right = right & (right - 1)

        return right


# -----------------------------------------------------------
# Driver Code
# -----------------------------------------------------------

if __name__ == "__main__":

    left1, right1 = 5, 7
    left2, right2 = 0, 0

    shift = SolutionShift()
    trick = SolutionBitTrick()

    print("Shift Method:")
    print(shift.rangeBitwiseAnd(left1, right1))
    print(shift.rangeBitwiseAnd(left2, right2))

    print("\nBit Trick Method:")
    print(trick.rangeBitwiseAnd(left1, right1))
    print(trick.rangeBitwiseAnd(left2, right2))