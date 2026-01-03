"""
===========================================================
231 - Power of Two
===========================================================

🧩 Problem:
Given an integer n, return true if it is a power of two. 
Otherwise, return false.

An integer n is a power of two if there exists an integer x 
such that n == 2^x.

Example 1:
Input: n = 1
Output: true
Explanation: 2^0 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 2^4 = 16

Example 3:
Input: n = 3
Output: false

Example 4:
Input: n = 0
Output: false

-----------------------------------------------------------
Approach 1 — Iterative Division:
-----------------------------------------------------------
1. If n <= 0, return False
2. While n is divisible by 2:
   - Divide n by 2
3. If n becomes 1, it was a power of 2
4. Otherwise, return False

Time: O(log n), Space: O(1)

-----------------------------------------------------------
Approach 2 — Bit Manipulation (OPTIMAL):
-----------------------------------------------------------
Powers of 2 have exactly ONE bit set in their binary representation:
- 2^0 = 1   = 0b1
- 2^1 = 2   = 0b10
- 2^2 = 4   = 0b100
- 2^3 = 8   = 0b1000
- 2^4 = 16  = 0b10000

Key insight: n & (n-1) removes the rightmost set bit.
If n is a power of 2, it has only one bit set, so n & (n-1) == 0.

Example:
n = 8 = 0b1000
n-1 = 7 = 0b0111
n & (n-1) = 0b0000 = 0 ✓

n = 6 = 0b110
n-1 = 5 = 0b101
n & (n-1) = 0b100 ≠ 0 ✗

Conditions:
1. n > 0 (to exclude 0 and negative numbers)
2. (n & (n-1)) == 0 (only one bit is set)

Time: O(1), Space: O(1)

-----------------------------------------------------------
Approach 3 — Count Set Bits:
-----------------------------------------------------------
Check if n > 0 and has exactly one bit set.
Use bin(n).count('1') == 1

Time: O(log n), Space: O(1)

-----------------------------------------------------------
Approach 4 — Maximum Power of 2:
-----------------------------------------------------------
For 32-bit signed integer, max power of 2 is 2^30 = 1073741824
If n is a power of 2, then max_power % n == 0

Time: O(1), Space: O(1)

-----------------------------------------------------------
⏱ Time Complexity:   O(1)       # bit manipulation approach
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

class Solution(object):
    # Approach 1: Iterative Division
    def isPowerOfTwo_iterative(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        while n % 2 == 0:
            n //= 2
        
        return n == 1
    
    
    # Approach 2: Bit Manipulation (OPTIMAL)
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Check if n > 0 and has exactly one bit set
        # n & (n-1) removes the rightmost set bit
        return n > 0 and (n & (n - 1)) == 0
    
    
    # Approach 3: Count Set Bits
    def isPowerOfTwo_count_bits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and bin(n).count('1') == 1
    
    
    # Approach 4: Maximum Power of 2
    def isPowerOfTwo_max_power(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Maximum power of 2 in 32-bit signed integer: 2^30 = 1073741824
        return n > 0 and 1073741824 % n == 0
    
    
    # Approach 5: Alternative Bit Trick (n & -n)
    def isPowerOfTwo_negative(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # n & -n isolates the rightmost set bit
        # If n is a power of 2, this equals n itself
        return n > 0 and (n & -n) == n


# -----------------------------------------------------------
# Driver Examples
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.isPowerOfTwo(1))
    # Expected Output: True
    # 1 = 2^0 = 0b1
    
    # Example 2
    print(sol.isPowerOfTwo(16))
    # Expected Output: True
    # 16 = 2^4 = 0b10000
    
    # Example 3
    print(sol.isPowerOfTwo(3))
    # Expected Output: False
    # 3 = 0b11 (two bits set)
    
    # Example 4
    print(sol.isPowerOfTwo(0))
    # Expected Output: False
    
    # Additional tests
    print(sol.isPowerOfTwo(2))
    # Expected Output: True
    # 2 = 2^1 = 0b10
    
    print(sol.isPowerOfTwo(4))
    # Expected Output: True
    # 4 = 2^2 = 0b100
    
    print(sol.isPowerOfTwo(5))
    # Expected Output: False
    # 5 = 0b101 (two bits set)
    
    print(sol.isPowerOfTwo(8))
    # Expected Output: True
    # 8 = 2^3 = 0b1000
    
    print(sol.isPowerOfTwo(-16))
    # Expected Output: False
    # Negative numbers cannot be powers of 2
    
    # Demonstrate the bit manipulation trick
    print("\nBit manipulation examples:")
    for n in [1, 2, 3, 4, 5, 8, 16]:
        binary = bin(n)
        n_minus_1 = bin(n - 1)
        result = n & (n - 1)
        print(f"n={n:2d} ({binary:>7s}), n-1={n-1:2d} ({n_minus_1:>7s}), n&(n-1)={result:2d}, isPower2={result == 0}")