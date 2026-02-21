"""
762. Prime Number of Set Bits in Binary Representation

This module solves the problem of counting numbers in a range [left, right]
whose number of set bits in binary representation is prime.

Core functions:
    - is_prime(n)       : Checks if n is prime using 6k ± 1 optimization.
    - get_set_bits(n)   : Counts number of 1s using Brian Kernighan's algorithm.

Constraints:
    - No precomputed arrays or hash tables.
    - Pure computation on the fly.
    - Efficient for Google-level interviews.
"""

class Solution(object):
    """DSA-style solution for counting numbers with prime set bits."""

    def countPrimeSetBits(self, left, right):
        """
        Count numbers with prime number of set bits in [left, right].

        :type left: int
        :type right: int
        :rtype: int
        """

        def is_prime(n):
            """Check if n is prime using 6k ± 1 optimization."""
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            sq = int(n ** 0.5)
            while i <= sq:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        def get_set_bits(n):
            """Count number of 1s using Brian Kernighan's method."""
            count = 0
            while n:
                n &= (n - 1)  # remove lowest set bit
                count += 1
            return count

        res = 0
        for num in range(left, right + 1):
            bits = get_set_bits(num)
            if is_prime(bits):
                res += 1

        return res


# ----------- Example usage / quick sanity run -----------
if __name__ == "__main__":
    sol = Solution()
    left, right = 6, 10
    print(f"Count of numbers with prime set bits in [{left},{right}]: {sol.countPrimeSetBits(left, right)}")