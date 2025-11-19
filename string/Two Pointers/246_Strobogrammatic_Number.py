"""
===========================================================
246. Strobogrammatic Number (Two Pointers + Mapping)
===========================================================

🧩 Problem:
A **strobogrammatic number** is a number that looks the same when rotated
180 degrees (turned upside down).

Given a string `num` representing a non-negative integer, determine if
`num` is strobogrammatic.

Valid strobogrammatic digit pairs under rotation:
- 0 ↔ 0
- 1 ↔ 1
- 6 ↔ 9
- 8 ↔ 8
- 9 ↔ 6

🎯 Goal:
Return **True** if `num` is a strobogrammatic number, otherwise **False**.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Input:  num = "69"  
Output: True  
Explanation: 6 ↔ 9 → looks the same when rotated.

Input:  num = "88"  
Output: True  
Explanation: 8 ↔ 8 → symmetric.

Input:  num = "962"  
Output: False  
Explanation: 2 is invalid under 180° rotation.

Input:  num = "1"  
Output: True

Input:  num = "2"  
Output: False

-----------------------------------------------------------
Algorithm — Two Pointers + Rotation Map:
-----------------------------------------------------------
1. Create a map for valid rotations:
       '0' → '0'
       '1' → '1'
       '6' → '9'
       '8' → '8'
       '9' → '6'

2. Use two pointers:
       left  = 0
       right = len(num) - 1

3. While left <= right:
   a. Let `a = num[left]`, `b = num[right]`.
   b. If `a` is not in the map → return False.
   c. If `map[a] != b` → return False.
   d. Move pointers:
          left  += 1
          right -= 1

4. If the loop finishes without mismatch → return True.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)      (scan each character once)
💾 Space Complexity:  O(1)      (fixed-size map)
-----------------------------------------------------------
 
"""

# ------------------------------------
# Solution: Strobogrammatic Number
# ------------------------------------
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # Map of valid rotations
        rotation = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }

        left, right = 0, len(num) - 1

        while left <= right:
            a = num[left]
            b = num[right]

            # a must be a valid strobogrammatic digit
            if a not in rotation:
                return False

            # rotation of a must match b
            if rotation[a] != b:
                return False

            left += 1
            right -= 1

            # continue until pointers cross

        return True


# ------------------------------------
# Driver Tests
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.isStrobogrammatic("69"))   # True
    print(sol.isStrobogrammatic("88"))   # True
    print(sol.isStrobogrammatic("962"))  # False
    print(sol.isStrobogrammatic("1"))    # True
    print(sol.isStrobogrammatic("2"))    # False
