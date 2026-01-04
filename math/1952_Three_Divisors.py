"""
===========================================================
1952. Three Divisors
===========================================================

🧩 Problem:
Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.
-----------------------------------------------------------
Example :
-----------------------------------------------------------
Example 1:

Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.
Example 2:

Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.

-----------------------------------------------------------
Brute Force Approach 1: loop all till n
-----------------------------------------------------------
1. i cant be greater than n 
2. so loop it n and check if n % i == 0
3. if yes add it to the result
-----------------------------------------------------------
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  O(n)  
Space: O(1)
-----------------------------------------------------------
🧠 Better Approach: iterate up to sqrt of n
-----------------------------------------------------------
1. If you look at the pattern the divisors come in pairs
Example

For n = 36:
    1 × 36
    2 × 18
    3 × 12
    4 × 9
    6 × 6
so If a number i divides n, then:
    n = i * (n/i)
    
2. So Iterate till sqrt of n which means i * i <= n
3. For each i that divides n:
   - If i * i == n: count it once (perfect square)
   - Otherwise: count both i and n//i
4. After counting all divisors, check if count == 3
-----------------------------------------------------------
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  O(sqrt(n))  
Space: O(1)
-----------------------------------------------------------
🎯 Best Approach: Mathematical Insight (Prime Square Check)
-----------------------------------------------------------
Key Insight: A number has exactly 3 divisors if and only if 
it's the square of a prime number.

Why?
- For n = p² (where p is prime):
  Divisors are: 1, p, p² (exactly 3 divisors)
- For any other number:
  Either < 3 divisors or > 3 divisors

Algorithm:
1. Check if n is a perfect square
   - Calculate sqrt_n = √n
   - If sqrt_n * sqrt_n != n, return False
   
2. Check if sqrt_n is prime
   - If sqrt_n < 2, return False
   - Check divisibility from 2 to √(sqrt_n)
   - If any number divides sqrt_n, it's not prime
   
3. If both conditions pass, return True

Examples:
- n = 4 = 2²: √4 = 2 (prime) → True
- n = 9 = 3²: √9 = 3 (prime) → True
- n = 25 = 5²: √25 = 5 (prime) → True
- n = 6: √6 ≈ 2.45 (not perfect square) → False
- n = 36 = 6²: √36 = 6 (not prime, 6=2×3) → False
-----------------------------------------------------------
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  O(n^(1/4))  - Check primality of √n takes O(√√n)
Space: O(1)

"""

class Solution:
    # Brute Force Approach
    def isThree_bruteforce(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
            if count > 3:  # Early termination
                return False
        return count == 3
    
    # Better Approach - Iterate up to sqrt(n)
    def isThree_sqrt(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        i = 1
        while (i * i) <= n:
            if n % i == 0:
                if i * i == n:
                    # i is the square root, count it once
                    count += 1
                else:
                    # Count both i and n//i
                    count += 2
            
            # Early termination if count exceeds 3
            if count > 3:
                return False
            i += 1
        
        return count == 3
    
    # Best Approach - Prime Square Check
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Check if n is a perfect square
        sqrt_n = int(n ** 0.5)
        if sqrt_n * sqrt_n != n:
            return False
        
        # Check if sqrt_n is prime
        if sqrt_n < 2:
            return False
        
        # Check divisibility from 2 to sqrt(sqrt_n)
        for i in range(2, int(sqrt_n ** 0.5) + 1):
            if sqrt_n % i == 0:
                return False
        
        return True

# -----------------------------------------------------------
# Driver Examples
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    print("=== Testing Brute Force ===")
    print(f"4 has three divisors: {sol.isThree_bruteforce(4)}")    # True
    print(f"6 has three divisors: {sol.isThree_bruteforce(6)}")    # False
    print(f"9 has three divisors: {sol.isThree_bruteforce(9)}")    # True
    print(f"36 has three divisors: {sol.isThree_bruteforce(36)}")  # False
    
    print("\n=== Testing Sqrt Approach ===")
    print(f"4 has three divisors: {sol.isThree_sqrt(4)}")    # True
    print(f"6 has three divisors: {sol.isThree_sqrt(6)}")    # False
    print(f"9 has three divisors: {sol.isThree_sqrt(9)}")    # True
    print(f"36 has three divisors: {sol.isThree_sqrt(36)}")  # False
    
    print("\n=== Testing Best Approach (Prime Square) ===")
    print(f"4 has three divisors: {sol.isThree(4)}")    # True
    print(f"6 has three divisors: {sol.isThree(6)}")    # False
    print(f"9 has three divisors: {sol.isThree(9)}")    # True
    print(f"25 has three divisors: {sol.isThree(25)}")  # True
    print(f"36 has three divisors: {sol.isThree(36)}")  # False