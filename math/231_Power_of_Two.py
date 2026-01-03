"""
===========================================================
231 - Power of Two
===========================================================

🧩 Problem:
Given an integer `n`, return `true` if it is a power of two.
Otherwise, return `false`.

An integer `n` is a power of two if there exists an integer `x`
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

-----------------------------------------------------------
Approach — Bit Manipulation (Optimal):
-----------------------------------------------------------
Key observation:
A power of two has **exactly one set bit (1)** in its binary representation.

Examples:
1   -> 0001
2   -> 0010
4   -> 0100
8   -> 1000

For any number `n`:
- `n - 1` flips the rightmost set bit to 0
- ANDing `n` with `n - 1` clears that rightmost set bit

If `n` has only ONE set bit:
    n & (n - 1) == 0

-----------------------------------------------------------
Conditions to check:
-----------------------------------------------------------
1. `n > 0`
   - Powers of two are always positive
   - Avoids edge case n = 0

2. `(n & (n - 1)) == 0`
   - Ensures exactly one set bit

-----------------------------------------------------------
Key Insight:
-----------------------------------------------------------
If a number has:
- one `1` bit  → power of two
- more than one `1` bit → NOT a power of two

This approach:
- Uses no loops
- Runs in constant time
- Is highly preferred in interviews

-----------------------------------------------------------
⏱ Time Complexity:   O(1)
💾 Space Complexity: O(1)
-----------------------------------------------------------
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0


# -----------------------------------------------------------
# Driver Examples
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.isPowerOfTwo(1))   # True
    print(sol.isPowerOfTwo(16))  # True
    print(sol.isPowerOfTwo(3))   # False
    print(sol.isPowerOfTwo(0))   # False
