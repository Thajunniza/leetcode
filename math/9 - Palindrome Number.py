"""
9 - Palindrome Number

Description:
Given an integer x, return true if x is a palindrome, and false otherwise.
An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is a palindrome while 123 is not.

Example:
Input: x = 121
Output: true

Approach:
Half-Number Reversal.
- Handle edge cases: negative numbers and numbers ending in zero (except 0 itself) cannot be palindromes.
- Reverse only the second half of the digits by popping the last digit of x and pushing it to a new variable 'r'.
- Stop when the original number x is no longer greater than the reversed half 'r'.
- Check if x equals r (for even length) or x equals r // 10 (for odd length to ignore the middle digit).

Time Complexity:
O(log10(n))

Space Complexity:
O(1)
"""

class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes.
        # Numbers ending in 0 (except 0) are not palindromes.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        r = 0
        # Build the reverse of the second half of x
        while x > r:
            mod = x % 10
            r = (r * 10) + mod
            x = x // 10
        
        # If length is odd, r // 10 removes the middle digit
        return x == r or x == r // 10


# -------------------- Test Cases --------------------

def test_is_palindrome():
    sol = Solution()

    # Test Case 1: Standard positive palindrome
    assert sol.isPalindrome(121) == True

    # Test Case 2: Negative number
    assert sol.isPalindrome(-121) == False

    # Test Case 3: Non-palindrome positive number
    assert sol.isPalindrome(10) == False

    # Test Case 4: Single digit
    assert sol.isPalindrome(0) == True

    # Test Case 5: Even length palindrome
    assert sol.isPalindrome(1221) == True

    print("All test cases passed.")


if __name__ == "__main__":
    test_is_palindrome()
