# ===========================================================
# 190 - Reverse Bits
# ===========================================================

# 🧩 Problem:
# Reverse the bits of a 32-bit unsigned integer and return the result.

# 🎯 Goal:
# Given an integer n, return an integer representing its 32-bit binary reversal.

# -----------------------------------------------------------
# Examples:
# -----------------------------------------------------------

# Input:  n = 43261596  (Binary: 00000010100101000001111010011100)
# Output: 964176192     (Binary: 00111001011110000010100101000000)

# Input:  n = 4294967293 (Binary: 11111111111111111111111111111101)
# Output: 3221225471    (Binary: 10111111111111111111111111111111)

# -----------------------------------------------------------
# Algorithm — Convert to Array (Based on Original Code):
# -----------------------------------------------------------
# 1. Convert n to a binary array of 32 bits (pad with zeros).
# 2. Reverse the bits logically by treating the first array element as MSB.
# 3. Convert the array back to integer.

# ⏱ Time Complexity:   O(32) → O(1)
# 💾 Space Complexity:  O(32) → O(1)
# -----------------------------------------------------------


# ------------------------------------
# Solution: Array-based (Fixed Original)
# ------------------------------------
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Convert integer to 32-bit binary array
        def inttobin(n):
            res = []
            while n > 0:
                res.append(n % 2)
                n //= 2
            # Pad with zeros to ensure 32 bits
            while len(res) < 32:
                res.append(0)
            return res

        # Convert binary array back to integer (reversed)
        def bintoint(arr):
            ans = 0
            for i in range(32):
                ans += arr[i] * (2 ** (31 - i))
            return ans

        arr = inttobin(n)
        res = bintoint(arr)
        return res


# ------------------------------------
# Driver Tests
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()
    n1 = 43261596
    n2 = 4294967293

    print(sol.reverseBits(n1))  # Output: 964176192
    print(sol.reverseBits(n2))  # Output: 3221225471
