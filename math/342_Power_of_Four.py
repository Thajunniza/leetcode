"""
===========================================================
342 - Power of Four
===========================================================

🧩 Problem:
Given an integer n, return true if it is a power of four. 
Otherwise, return false.

An integer n is a power of four if there exists an integer x 
such that n == 4^x.

Example 1:
Input: n = 16
Output: true
Explanation: 4^2 = 16

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true
Explanation: 4^0 = 1

-----------------------------------------------------------
Approach 1 — Iterative Division:
-----------------------------------------------------------
1. If n <= 0, return False
2. While n is divisible by 4:
   - Divide n by 4
3. If n becomes 1, it was a power of 4
4. Otherwise, return False

Time: O(log n), Space: O(1)

-----------------------------------------------------------
Approach 2 — Logarithm (with precision check):
-----------------------------------------------------------
1. If n <= 0, return False
2. Calculate log4(n) = log(n) / log(4)
3. Check if result is an integer

Time: O(1), Space: O(1)
Note: Beware of floating point precision issues

-----------------------------------------------------------
Approach 3 — Bit Manipulation (Optimal):
-----------------------------------------------------------
Powers of 4 have special bit patterns:
- 4^0 = 1    = 0b1
- 4^1 = 4    = 0b100
- 4^2 = 16   = 0b10000
- 4^3 = 64   = 0b1000000
- 4^4 = 256  = 0b100000000

Pattern: Exactly one bit set, and it's at an EVEN position (0, 2, 4, 6, ...)

Conditions to check:
1. n > 0
2. n is a power of 2: (n & (n-1)) == 0
3. The single bit is at even position: (n & 0x55555555) == n
   - 0x55555555 = 0b01010101010101010101010101010101
   - This masks all odd bit positions

Time: O(1), Space: O(1)

-----------------------------------------------------------
⏱ Time Complexity:   O(1)       # bit manipulation approach
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

class Solution(object):
    # Approach 1: Iterative Division
    def isPowerOfFour_iterative(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        while n % 4 == 0:
            n //= 4
        
        return n == 1
    
    
    # Approach 2: Logarithm
    def isPowerOfFour_log(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        import math
        log_result = math.log(n, 4)
        return log_result == int(log_result)
    
    
    # Approach 3: Bit Manipulation (OPTIMAL)
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Check three conditions:
        # 1. n > 0
        # 2. n is power of 2: only one bit is set
        # 3. that bit is at an even position (0, 2, 4, 6, ...)
        
        # 0x55555555 in binary: 01010101010101010101010101010101
        # This masks odd positions, keeping only even positions
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) == n


# -----------------------------------------------------------
# Driver Examples
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.isPowerOfFour(16))
    # Expected Output: True
    # 16 = 4^2 = 0b10000 (bit at position 4, which is even)
    
    # Example 2
    print(sol.isPowerOfFour(5))
    # Expected Output: False
    
    # Example 3
    print(sol.isPowerOfFour(1))
    # Expected Output: True
    # 1 = 4^0 = 0b1 (bit at position 0, which is even)
    
    # Additional tests
    print(sol.isPowerOfFour(8))
    # Expected Output: False
    # 8 = 2^3 = 0b1000 (power of 2 but not 4, bit at position 3, which is odd)
    
    print(sol.isPowerOfFour(64))
    # Expected Output: True
    # 64 = 4^3 = 0b1000000 (bit at position 6, which is even)
    
    print(sol.isPowerOfFour(0))
    # Expected Output: False
    
    print(sol.isPowerOfFour(-4))
    # Expected Output: False