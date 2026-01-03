"""
===========================================================
326 - Power of Three
===========================================================

🧩 Problem:
Given an integer `n`, return `true` if it is a power of three.
Otherwise, return `false`.

An integer `n` is a power of three if there exists an integer `x`
such that n == 3^x.

Example 1:
Input: n = 27
Output: true
Explanation: 3^3 = 27

Example 2:
Input: n = 0
Output: false

Example 3:
Input: n = 45
Output: false

-----------------------------------------------------------
Approach — Math + Divisibility Trick (No Loops):
-----------------------------------------------------------
Key observation:
- 3 is a **prime number**
- Any power of 3 can divide only another power of 3

The largest power of 3 that fits in a 32-bit signed integer is:
3^19 = 1162261467
If `n` is a power of 3, then:
1162261467 % n == 0


-----------------------------------------------------------
Conditions to check:
-----------------------------------------------------------
1. `n > 0`
   - Powers of three are always positive
   - Handles edge case n = 0 and negatives

2. `largest_power_of_3 % n == 0`
   - Ensures `n` contains only factor 3

-----------------------------------------------------------
Key Insight:
-----------------------------------------------------------
Instead of repeatedly dividing `n` by 3 (loop),
we reverse the logic:
- Check whether `n` divides the largest possible power of 3

This gives:
- Constant time
- Cleaner logic
- Interview-preferred solution

-----------------------------------------------------------
⏱ Time Complexity:   O(1)
💾 Space Complexity: O(1)
-----------------------------------------------------------
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 3 ** 19
        return n > 0 and x % n == 0


# -----------------------------------------------------------
# Driver Examples
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.isPowerOfThree(27))   # True
    print(sol.isPowerOfThree(9))    # True
    print(sol.isPowerOfThree(1))    # True
    print(sol.isPowerOfThree(45))   # False
    print(sol.isPowerOfThree(0))    # False
