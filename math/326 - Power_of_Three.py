"""
===========================================================
326 - Power of Three
===========================================================

🧩 Problem:
Given an integer n, return true if it is a power of three. 
Otherwise, return false.

An integer n is a power of three if there exists an integer x 
such that n == 3^x.

Example 1:
Input: n = 27
Output: true
Explanation: 3^3 = 27

Example 2:
Input: n = 0
Output: false
Explanation: There is no x where 3^x = 0

Example 3:
Input: n = 9
Output: true
Explanation: 3^2 = 9

Example 4:
Input: n = 45
Output: false

-----------------------------------------------------------
Approach 1 — Iterative Division:
-----------------------------------------------------------
1. If n <= 0, return False
2. While n is divisible by 3:
   - Divide n by 3
3. If n becomes 1, it was a power of 3
4. Otherwise, return False

Time: O(log n), Space: O(1)

-----------------------------------------------------------
Approach 2 — Logarithm (with precision check):
-----------------------------------------------------------
1. If n <= 0, return False
2. Calculate log3(n) = log(n) / log(3)
3. Check if result is an integer

Time: O(1), Space: O(1)
Note: Beware of floating point precision issues

-----------------------------------------------------------
Approach 3 — Maximum Power of 3 (Mathematical Trick):
-----------------------------------------------------------
Since n is a 32-bit signed integer, the maximum power of 3 
that fits is 3^19 = 1162261467.

If n is a power of 3, then the maximum power of 3 must be 
divisible by n (since all powers of 3 only have 3 as a 
prime factor).

Conditions:
1. n > 0
2. 1162261467 % n == 0

Time: O(1), Space: O(1)

-----------------------------------------------------------
Approach 4 — Recursion:
-----------------------------------------------------------
1. Base case: if n == 1, return True
2. If n <= 0 or n % 3 != 0, return False
3. Recursively check n // 3

Time: O(log n), Space: O(log n) for recursion stack

-----------------------------------------------------------
⏱ Time Complexity:   O(1)       # maximum power approach
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

class Solution(object):
    # Approach 1: Iterative Division (Most Intuitive)
    def isPowerOfThree_iterative(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        while n % 3 == 0:
            n //= 3
        
        return n == 1
    
    
    # Approach 2: Logarithm
    def isPowerOfThree_log(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        import math
        # Use epsilon for floating point comparison
        log_result = math.log10(n) / math.log10(3)
        return abs(log_result - round(log_result)) < 1e-10
    
    
    # Approach 3: Maximum Power of 3 (OPTIMAL - O(1))
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Maximum power of 3 in 32-bit signed integer: 3^19 = 1162261467
        # If n is a power of 3, then max_power_of_3 % n == 0
        return n > 0 and 1162261467 % n == 0
    
    
    # Approach 4: Recursion
    def isPowerOfThree_recursive(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n <= 0 or n % 3 != 0:
            return False
        return self.isPowerOfThree_recursive(n // 3)


# -----------------------------------------------------------
# Driver Examples
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.isPowerOfThree(27))
    # Expected Output: True
    # 27 = 3^3
    
    # Example 2
    print(sol.isPowerOfThree(0))
    # Expected Output: False
    
    # Example 3
    print(sol.isPowerOfThree(9))
    # Expected Output: True
    # 9 = 3^2
    
    # Example 4
    print(sol.isPowerOfThree(45))
    # Expected Output: False
    # 45 = 3^2 * 5
    
    # Additional tests
    print(sol.isPowerOfThree(1))
    # Expected Output: True
    # 1 = 3^0
    
    print(sol.isPowerOfThree(3))
    # Expected Output: True
    # 3 = 3^1
    
    print(sol.isPowerOfThree(81))
    # Expected Output: True
    # 81 = 3^4
    
    print(sol.isPowerOfThree(243))
    # Expected Output: True
    # 243 = 3^5
    
    print(sol.isPowerOfThree(-3))
    # Expected Output: False
    
    # Verify the maximum power of 3 approach
    print("\nPowers of 3 up to 3^19:")
    power = 1
    for i in range(20):
        print(f"3^{i} = {power}")
        power *= 3