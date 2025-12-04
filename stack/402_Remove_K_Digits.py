"""===========================================================
402. Remove K Digits
===========================================================

🧩 Problem:
You are given a numeric string `num` and an integer `k`.

You must remove **exactly k digits** from the string **so that** the resulting number
is the **smallest possible** (in normal integer comparison).

Rules:
    • The digits must remain in their original order.
    • Leading zeros are allowed temporarily, but the final number must not contain them.
    • If the final number becomes empty → return "0".

🎯 Goal:
Return the smallest possible number as a string after removing exactly `k` digits.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  num = "1432219", k = 3

Process (best choice):
    Remove '4' (index 1)
    Remove '3' (index 2)
    Remove '2' (first occurrence among remaining)
    Final number = "1219"

Output: "1219"


Example 2:
Input:  num = "10200", k = 1

Process:
    Removing '1' is bad → "0200" (→ 200)
    Removing '0' (the 2nd digit) is optimal:
         "100" → 100
    Removing '2' gives "100" too.

Output: "200"


Example 3:
Input:  num = "10", k = 2

Removing all digits results in an empty string → return "0".

Output: "0"

-----------------------------------------------------------
Why This Is a Greedy + Monotonic Stack Problem:
-----------------------------------------------------------

Consider making the number as small as possible:

If a digit is **bigger** than the next digit, keeping it will produce a larger number.  
So we prefer to **remove previous larger digits** when we encounter a smaller one.

This is a classic pattern:

        Maintain digits in a monotonic **increasing** stack.

For each digit `d` in `num`:
    • While `k > 0` AND stack is not empty AND stack[-1] > d:
          → pop stack[-1] (remove the bigger digit)
          → k -= 1
    • Push the current digit `d`.

After processing all digits:
    • If k > 0, remove digits from the **end** (these are the largest remaining).

Finally strip leading zeros.

This guarantees the **lexicographically smallest** valid number.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    • Each digit is pushed and popped at most once.

Space Complexity:  O(n)
    • Stack may hold all digits in the worst case.

-----------------------------------------------------------
Optimal Python Solution (Monotonic Stack)
-----------------------------------------------------------
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Edge case: remove all digits
        if k >= len(num):
            return "0"

        stack = []

        for d in num:
            # Remove left-side larger digits when possible
            while k > 0 and stack and stack[-1] > d:
                stack.pop()
                k -= 1

            stack.append(d)

        # If k still remains, remove from end (these are largest)
        while k > 0:
            stack.pop()
            k -= 1

        # Remove leading zeros
        result = "".join(stack).lstrip("0")

        # If empty, return "0"
        return result if result else "0"


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.removeKdigits("1432219", 3))
    # Expected: "1219"

    print(sol.removeKdigits("10200", 1))
    # Expected: "200"

    print(sol.removeKdigits("10", 2))
    # Expected: "0"

    print(sol.removeKdigits("112", 1))
    # Possible removals:
    # Remove 1 → "12"
    # Remove 1 (second) → "12"
    # Remove 2 → "11" (smallest!)
    # Expected: "11"

    print(sol.removeKdigits("123456", 3))
    # Expected: "123"

    print(sol.removeKdigits("765028321", 5))
    # Expected: "0221" → "221"
