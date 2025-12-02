"""
===========================================================
556. Next Greater Element III
===========================================================

🧩 Problem:
You are given a **positive integer** `n`.

You need to find the **smallest integer** that is:
    • strictly greater than `n`
    • can be formed by **rearranging the digits** of `n`
    • and fits in a **32-bit signed integer** range:
          -2^31 to 2^31 - 1  (here we only care about upper bound)

If no such integer exists, return -1.

🎯 Goal:
Return the **next greater permutation** of the digits of `n`,
or -1 if it does not exist or overflows 32-bit signed integer.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  n = 12
Digits: "1", "2"

Permutations in increasing order:
    12, 21
Next greater than 12 is 21

Output: 21


Example 2:
Input:  n = 21
Digits: "2", "1"

Permutations:
    12, 21
There is no permutation greater than 21 using the same digits.

Output: -1


Example 3:
Input:  n = 12443322

Next greater permutation (by rearranging digits) is:
    13222344

Output: 13222344


Example 4 (overflow case):
Suppose the next permutation is > 2^31 - 1 (2147483647),
then we must return -1.

-----------------------------------------------------------
Algorithm — Next Permutation on Digits:
-----------------------------------------------------------

Pattern: 🔢 Next Lexicographical Permutation

We treat the integer n as a sequence of digits and apply
the standard "next permutation" algorithm:

Steps:

1️⃣ Convert n to a list of characters (digits):
       s = list(str(n))

2️⃣ Find the first index `i` from the RIGHT where:
       s[i] < s[i + 1]
   - This is the "pivot" where we can still make a bigger number.
   - If no such i exists, digits are in descending order (e.g., 4321):
         → no greater permutation → return -1.

3️⃣ From the RIGHT side again, find the first index `j` > i such that:
       s[j] > s[i]
   - Because we scan from right, `s[j]` will be the **smallest digit
     greater than s[i]** in the suffix.

4️⃣ Swap s[i] and s[j].

5️⃣ Reverse the suffix starting at i + 1:
       s[i+1:] = reversed(s[i+1:])
   - This makes the suffix as small as possible while still being
     greater than the original → gives the **next** greater permutation.

6️⃣ Convert s back to integer:
       result = int("".join(s))

7️⃣ Check 32-bit signed integer overflow:
       if result > 2^31 - 1:
           return -1

8️⃣ Return result.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Let d = number of digits in n.

Time Complexity:   O(d)
    - Single pass from right to left + suffix reverse.

Space Complexity:  O(d)
    - For the digit array.

-----------------------------------------------------------
"""

class Solution(object):
    def nextGreaterElement(self, n):
        """
        Finds the next greater integer using the same digits as n.

        Uses the classic "next permutation" algorithm on the digits of n.
        If the next permutation exceeds 32-bit signed integer range or
        doesn't exist, returns -1.

        Args:
            n (int): Input positive integer.

        Returns:
            int: The next greater integer using the same digits,
                 or -1 if not possible.

        Example:
            >>> Solution().nextGreaterElement(12)
            21

            >>> Solution().nextGreaterElement(21)
            -1
        """
        # Convert integer to list of characters (digits)
        s = list(str(n))
        length = len(s)

        # 1️⃣ Find the pivot index `i` from the right
        # such that s[i] < s[i + 1]
        i = length - 2
        while i >= 0 and s[i] >= s[i + 1]:
            i -= 1

        # If no such i, digits are in non-increasing order → no next greater
        if i < 0:
            return -1

        # 2️⃣ Find index `j` (rightmost) such that s[j] > s[i]
        j = length - 1
        while j > i and s[j] <= s[i]:
            j -= 1

        # 3️⃣ Swap pivot s[i] and s[j]
        s[i], s[j] = s[j], s[i]

        # 4️⃣ Reverse suffix s[i+1:] to make it as small as possible
        s[i + 1:] = reversed(s[i + 1:])

        # 5️⃣ Convert back to integer
        result = int("".join(s))

        # 6️⃣ Check 32-bit signed integer limit
        if result > 2**31 - 1:
            return -1

        return result


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElement(12))        # Expected: 21
    print(sol.nextGreaterElement(21))        # Expected: -1
    print(sol.nextGreaterElement(12443322))  # Example: 13222344
    print(sol.nextGreaterElement(230241))    # Example: 230412
