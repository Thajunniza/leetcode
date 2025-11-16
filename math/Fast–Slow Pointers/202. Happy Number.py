"""
===========================================================
202. Happy Number (Floyd's Cycle Detection)
===========================================================

🧩 Problem:
A number is called "happy" if repeatedly replacing the number 
by the sum of the squares of its digits eventually leads to 1.

If the process enters a cycle (never reaches 1), the number is unhappy.

🎯 Goal:
Return True if n is a happy number, otherwise False.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Input:  n = 19
Output: True
Explanation:
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0 + 0 = 1 → happy number

Input: n = 2
Output: False
Explanation: Falls into cycle → not a happy number

-----------------------------------------------------------
Approach — Floyd’s Fast & Slow Pointers:
-----------------------------------------------------------
We treat the number transformation sequence like a linked list.

If there is a cycle (other than reaching 1), fast and slow will meet.

- slow = one transformation step at a time
- fast = two transformation steps at a time
- if both meet at 1 → happy
- if both meet at another number → cycle → unhappy

-----------------------------------------------------------
⏱ Time Complexity:   O(log n)  
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""
class Solution(object):
    def sumOfSquares(self, n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

    def isHappy(self, n):
        slow = n
        fast = self.sumOfSquares(n)

        while fast != 1 and slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))

        return fast == 1

solu = Solution()
print(solu.isHappy(81))
print(solu.isHappy(19))