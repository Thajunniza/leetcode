"""
===========================================================
541. Reverse String II
===========================================================

🧩 Problem:
Given a string `s` and an integer `k`, you must modify the string using the
following rules applied to every consecutive block of **2k** characters:

1. Reverse the **first k** characters.
2. Leave the **next k** characters unchanged.
3. Move to the next 2k block and repeat until the end of the string.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "abcdefg", k = 2
Output: "bacdfeg"

Explanation:
Block 1: "abcd" → reverse first 2 → "bacd"
Block 2: "efg"  → reverse first 2 → "fe" + "g"
Final Result → "bacdfeg"

Example 2:
Input:  s = "abcd", k = 3
Output: "cbad"

Explanation:
Only one block:
"abcd" → reverse first 3 → "cba" + "d"

-----------------------------------------------------------
🎯 Core Logic (Most Important):
-----------------------------------------------------------

For every **2k block** in the string:

1️⃣ If fewer than **k** characters remain →  
    🔁 Reverse **all** remaining characters.

2️⃣ If at least **k** but fewer than **2k** characters remain →  
    🔁 Reverse **only the first k** characters.  
    ⏩ Leave the rest unchanged.

3️⃣ If **2k or more** characters remain →  
    🔁 Reverse the first k characters.  
    ⏩ Skip the next k characters.  
    ➡️ Move to next 2k block and repeat.

-----------------------------------------------------------
🧠 Approach:
-----------------------------------------------------------

We iterate over the string in jumps of **2k**:

s[i : i+k]

Python slicing handles all edge cases automatically:
- If less than k left → reverse all
- If between k and 2k → reverse first k
- If 2k → normal pattern

-----------------------------------------------------------
💡 Code (Cleanest Python Solution):
-----------------------------------------------------------

```python
"""
class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)

        for i in range(0, len(s), 2 * k):
            s[i:i+k] = s[i:i+k][::-1]

        return "".join(s)


if __name__ == "__main__":
    sol = Solution()

    # Testcase 1
    s1 = "abcdefg"
    k1 = 2
    print("Input:", s1, "k =", k1)
    print("Output:", sol.reverseStr(s1, k1))   # Expected: bacdfeg

    print("-----")

    # Testcase 2
    s2 = "abcd"
    k2 = 3
    print("Input:", s2, "k =", k2)
    print("Output:", sol.reverseStr(s2, k2))   # Expected: cbad

    print("-----")

    # You can add your own tests here
    s3 = "abcdefghijk"
    k3 = 4
    print("Input:", s3, "k =", k3)
    print("Output:", sol.reverseStr(s3, k3))