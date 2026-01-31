"""
744. Find Smallest Letter Greater Than Target

Given a sorted list of characters `letters` containing only lowercase letters,
and a character `target`, find the smallest character in the list that is
strictly greater than `target`.

Letters wrap around circularly. For example, if `target` is 'z' and
`letters = ['a', 'b']`, the answer is 'a'.

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"

Example 3:
Input: letters = ["c","f","j"], target = "d"
Output: "f"

Example 4:
Input: letters = ["c","f","j"], target = "z"
Output: "c"

Algorithm:
- Use binary search since the array is sorted.
- Initialize answer as letters[0] to handle wrap-around case.
- If letters[mid] > target:
    - update answer
    - search left to find a smaller valid character
- Else:
    - search right
- Return answer after binary search completes.

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        l = 0
        r = len(letters) - 1
        ans = letters[0]

        while l <= r:
            mid = l + (r - l) // 2

            if letters[mid] > target:
                ans = letters[mid]
                r = mid - 1
            else:
                l = mid + 1

        return ans


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    print(sol.nextGreatestLetter(["c","f","j"], "a"))  # Expected: "c"
    print(sol.nextGreatestLetter(["c","f","j"], "c"))  # Expected: "f"
    print(sol.nextGreatestLetter(["c","f","j"], "d"))  # Expected: "f"
    print(sol.nextGreatestLetter(["c","f","j"], "z"))  # Expected: "c"
    print(sol.nextGreatestLetter(["a","b"], "z"))      # Expected: "a"
