"""
===========================================================
1980. Find Unique Binary String
===========================================================

Problem:
Given an array of n unique binary strings nums,
where each string has length n, return a binary string
of length n that does not appear in nums.

You may return any valid answer.

-----------------------------------------------------------
Example
-----------------------------------------------------------
Input:  nums = ["01","10"]
Output: "11"

Input:  nums = ["00","01"]
Output: "10"

-----------------------------------------------------------
Approach 1 — Brute Force (Binary ↔ Integer Conversion)

Idea:
1. Convert all binary strings to integers.
2. Store them in a set.
3. Check numbers from 0 → 2^n - 1
4. Return the first missing number converted back to binary.

Time Complexity:  O(n²)
Space Complexity: O(n)
-----------------------------------------------------------
"""

class SolutionBruteForce(object):

    def to_bin(self, val, n):
        ans = []

        for _ in range(n):
            bit = val & 1
            val >>= 1
            ans.append(str(bit))

        return "".join(ans[::-1])

    def to_int(self, b):
        ans = 0

        for bit in b:
            ans <<= 1
            if bit == "1":
                ans |= 1

        return ans

    def findDifferentBinaryString(self, nums):

        have = set()

        for val in nums:
            have.add(self.to_int(val))

        n = len(nums)

        for i in range(1 << n):
            if i not in have:
                return self.to_bin(i, n)

        return ""


"""
-----------------------------------------------------------
Approach 2 — Cantor Diagonal Trick (Optimal)

Idea:
Flip the diagonal bits.

For each i:
    nums[i][i]
    0 → 1
    1 → 0

This guarantees the result differs from every string
in at least one position.

Time Complexity:  O(n)
Space Complexity: O(n)
-----------------------------------------------------------
"""

class SolutionDiagonal(object):

    def findDifferentBinaryString(self, nums):

        n = len(nums)
        res = []

        for i in range(n):
            if nums[i][i] == "0":
                res.append("1")
            else:
                res.append("0")

        return "".join(res)


# -----------------------------------------------------------
# Driver Code
# -----------------------------------------------------------

if __name__ == "__main__":

    nums1 = ["01","10"]
    nums2 = ["00","01"]

    brute = SolutionBruteForce()
    diag = SolutionDiagonal()

    print("Brute Force:")
    print(brute.findDifferentBinaryString(nums1))
    print(brute.findDifferentBinaryString(nums2))

    print("\nDiagonal Trick:")
    print(diag.findDifferentBinaryString(nums1))
    print(diag.findDifferentBinaryString(nums2))