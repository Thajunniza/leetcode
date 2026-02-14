"""
===========================================================
Count Subarrays with XOR = K
===========================================================

🧩 Problem:
Given an integer array `nums` and integer `k`, return the
number of subarrays whose **bitwise XOR** equals `k`.

-----------------------------------------------------------
Algorithm — Prefix XOR + HashMap:
-----------------------------------------------------------
1. Initialize:
   - prefixXOR = 0
   - seen = {0: 1}  # count of XORs seen so far
   - res = 0

2. Iterate through nums:
   a. prefixXOR ^= val
   b. If (prefixXOR ^ k) exists in seen → add seen[prefixXOR ^ k] to res
      (because prefixXOR ^ prevXOR = k → valid subarray)
   c. Update seen[prefixXOR] count

3. Return res

⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(n)
"""
# ------------------------------------
# Solution — Prefix XOR
# ------------------------------------
class Solution:
    def subarraysWithXorK(self, nums, k):
        seen = {0: 1}  # prefixXOR counts
        prefixXOR = 0
        res = 0

        for val in nums:
            prefixXOR ^= val

            # check if there exists a previous prefixXOR that satisfies prefixXOR ^ prevXOR = k
            diff = prefixXOR ^ k
            if diff in seen:
                res += seen[diff]

            # update seen
            seen[prefixXOR] = seen.get(prefixXOR, 0) + 1

        return res


# --------------------------
# Driver Tests
# --------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.subarraysWithXorK([4,2,2,6,4], 6))  # 4
    print(sol.subarraysWithXorK([5,6,7,8,9], 5))  # 2
    print(sol.subarraysWithXorK([1,2,3,4,5], 4))  # 2
