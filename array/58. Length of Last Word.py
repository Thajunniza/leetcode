# length_of_last_word.py

"""
58: Length of Last Word
-------------------------------
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: "Hello World"
Output: 5

Example 2:
Input: "   fly me   to   the moon  "
Output: 4

Constraints:
- 1 <= s.length <= 10^4
- s consists of only English letters and spaces ' '.
- There will be at least one word in s.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        r = len(s) - 1
        while r >= 0 :
            if s[r] != " ":
                res += 1
            elif res > 0:
                return res
            r -= 1
        return res


# ===============================
# Example Test Cases
# ===============================

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.lengthOfLastWord("Hello World"))  # Output: 5

    # Test case 2
    print(solution.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4

    # Test case 3
    print(solution.lengthOfLastWord("single"))  # Output: 6

    # Test case 4
    print(solution.lengthOfLastWord("a "))  # Output: 1
