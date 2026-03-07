"""
===========================================================
260. Single Number III
===========================================================

🧩 Problem:
Given an integer array `nums` where exactly two elements appear
only once and all the others appear exactly twice, find the two
elements that appear only once.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Input:  nums = [1,2,1,3,2,5]
Output: [3,5]

Input:  nums = [-1,0]
Output: [-1,0]

-----------------------------------------------------------
Algorithm — XOR + Bit Separation
-----------------------------------------------------------
Idea:

1. XOR all numbers → result is XOR of the two unique numbers.
2. Find the first set bit in the XOR result:
   - This bit differs between the two unique numbers.
3. Use this bit as a mask to separate numbers into two groups:
   - Numbers with this bit set.
   - Numbers with this bit unset.
4. XOR each group to isolate the unique numbers.

Key Operations:
- `^`  → XOR
- `&`  → bit check
- `<<` → shift mask

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

# ------------------------------------
# Solution
# ------------------------------------
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Step 1: XOR all numbers
        xor_all = 0
        for val in nums:
            xor_all ^= val

        # Step 2: Find first set bit (mask)
        mask = 1
        while not (xor_all & mask):
            mask <<= 1

        # Step 3: Split numbers into two groups and XOR each group
        first = 0
        second = 0
        for val in nums:
            if val & mask:
                first ^= val
            else:
                second ^= val

        return [first, second]


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":

    sol = Solution()

    print(sol.singleNumber([1,2,1,3,2,5]))       # Expected: [3,5]
    print(sol.singleNumber([-1,0]))              # Expected: [-1,0]
    print(sol.singleNumber([2,1,2,3]))           # Expected: [1,3]

    ums = [43772400,1674008457,1779561093,744132272,1674008457,448610617,
           1779561093,124075538,-1034600064,49040018,612881857,390719949,
           -359290212,-812493625,124732,-1361696369,49040018,-145417756,
           -812493625,2078552599,1568689850,865876872,865876872,-1471385435,
           1816352571,1793963758,2078552599,-1034600064,1475115274,-119634980,
           124732,661111294,-1813882010,1568689850,448610617,1347212898,
           -1293494866,612881857,661111294,-1361696369,1816352571,-1813882010,
           -359290212,1475115274,1793963758,1347212898,43772400,-1471385435,
           124075538,-1293494866,-119634980,390719949]

    print(sol.singleNumber(ums))  # Expected: two unique numbers