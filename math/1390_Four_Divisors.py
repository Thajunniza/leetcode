"""
===========================================================
1390. Four Divisors
===========================================================

🧩 Problem:
Given an integer array nums, return the sum of divisors of the integers in that array 
that have exactly four divisors. If there is no such integer in the array, return 0.

-----------------------------------------------------------
Example :
-----------------------------------------------------------
Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only: 1 + 3 + 7 + 21 = 32

Example 2:

Input: nums = [21,21]
Output: 64

Example 3:

Input: nums = [1,2,3,4,5]
Output: 0

-----------------------------------------------------------
Brute Force Approach: Check all divisors up to n
-----------------------------------------------------------
1. For each number in nums, iterate from 1 to n
2. Count divisors and sum them
3. If count == 4, add sum to result
-----------------------------------------------------------
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  O(n * m) where n = length of nums, m = max value in nums
Space: O(1)

-----------------------------------------------------------
🧠 Better Approach: Iterate up to sqrt(n)
-----------------------------------------------------------
Key Insight: Divisors come in pairs (i, n/i)

Algorithm:
1. For each number n in nums:
   - Initialize count = 0, total = 0
   - Iterate i from 1 while i*i <= n
   - If i divides n:
     * If i*i == n: count i once (perfect square case)
     * Otherwise: count both i and n//i
     * Add to total accordingly
   - Check if count > 4 immediately for early termination
   - After loop, if count == 4, add total to result
   
2. Return the final result

Edge Cases:
- Perfect squares (i*i == n): count divisor only once
- Early termination: stop as soon as count > 4
-----------------------------------------------------------
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  O(n * sqrt(m)) where n = length of nums, m = max value in nums
Space: O(1)

"""

class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findFourDivisor(n):
            count = 0
            total = 0
            i = 1
            while (i * i) <= n:
                if n % i == 0:
                    if i * i == n:
                        # Perfect square: count i only once
                        count += 1
                        total += i
                    else:
                        # Count both i and n//i
                        count += 2
                        total += i + (n // i)
                    
                    # Early termination: check immediately after updating count
                    if count > 4:
                        return 0
                
                i += 1
            
            return total if count == 4 else 0
        
        result = 0
        for n in nums:
            result += findFourDivisor(n)
        return result

# -----------------------------------------------------------
# Driver Examples
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    print(f"[21,4,7] => {sol.sumFourDivisors([21,4,7])}")  # 32
    # 21: 1,3,7,21 (sum=32) ✓
    # 4: 1,2,4 (3 divisors) ✗
    # 7: 1,7 (2 divisors) ✗
    
    print(f"[21,21] => {sol.sumFourDivisors([21,21])}")  # 64
    # Each 21 contributes 32
    
    print(f"[1,2,3,4,5] => {sol.sumFourDivisors([1,2,3,4,5])}")  # 0
    # None have exactly 4 divisors
    
    print(f"[6] => {sol.sumFourDivisors([6])}")  # 12
    # 6: 1,2,3,6 (sum=12) ✓
    
    print(f"[10] => {sol.sumFourDivisors([10])}")  # 18
    # 10: 1,2,5,10 (sum=18) ✓
    
    print(f"[12] => {sol.sumFourDivisors([12])}")  # 0
    # 12: 1,2,3,4,6,12 (6 divisors) ✗
    
    print(f"[15] => {sol.sumFourDivisors([15])}")  # 24
    # 15: 1,3,5,15 (sum=24) ✓