"""
7 - Reverse Integer

Description:
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Example:
Input: x = 123
Output: 321

Approach:
Digit Extraction with Boundary Validation.
- Extract the sign of x and work with its absolute value.
- Reconstruct the number by repeatedly taking the last digit (n % 10) and shifting the result (ans * 10).
- Apply the original sign to the reversed result.
- Use a chained comparison to verify the result is within the 32-bit signed range [-2147483648, 2147483647].

Time Complexity:
O(log10(n)) - The loop runs once for each digit in the number.

Space Complexity:
O(1) - Only a few integer variables are used.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x > 0 else -1
        n = abs(x)
        ans = 0
        while n > 0 :
            mod = n % 10
            ans = (ans * 10) + mod
            n = n // 10
            
        ans = ans * sign
        
        # Chained comparison for 32-bit signed integer boundaries
        if (-(2 ** 31)) <= ans < (2 ** 31):
            return ans
        else:
            return 0

# -------------------- Test Cases --------------------

def test_reverse():
    sol = Solution()

    # Case 1: Standard positive
    assert sol.reverse(123) == 321
    # Case 2: Standard negative
    assert sol.reverse(-123) == -321
    # Case 3: Ends in zero
    assert sol.reverse(120) == 21
    # Case 4: Overflow (returns 0)
    assert sol.reverse(1534236469) == 0
    # Case 5: Zero
    assert sol.reverse(0) == 0

    print("All test cases passed.")

if __name__ == "__main__":
    test_reverse()
