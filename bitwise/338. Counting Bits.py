"""
===========================================================
338. Counting Bits
===========================================================

Return array where ans[i] = number of 1 bits in i.

Dynamic Programming relation:
bits[i] = bits[i >> 1] + (i & 1)

Time Complexity:  O(n)
Space Complexity: O(n)
===========================================================
"""


class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp

    def countBits1(self, n):
        def count_ones(x):
            count = 0
            while x:
                x &= x - 1
                count += 1
            return count

        return [count_ones(i) for i in range(n + 1)]


# -----------------------------------------------------------
# Driver Test
# -----------------------------------------------------------
if __name__ == "__main__":

    sol = Solution()

    test_cases = [2, 5, 10]

    for num in test_cases:
        print("n =", num, "->", sol.countBits(num))
    
    for num in test_cases:
        print("n =", num, "->", sol.countBits1(num))