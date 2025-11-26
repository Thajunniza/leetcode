"""
===========================================================
1750. Minimum Length of String After Deleting Similar Ends
===========================================================

🧩 Problem:
You are given a string `s`.

Your task:
- Repeatedly delete characters from **both ends** of the string if:
    - The first and last characters are the same.
    - Remove all consecutive occurrences of that character from both ends.
- Stop when the first and last characters differ or the string becomes empty.

Return the **minimum length** of the string after performing these operations.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    s = "ca"
Process:
    - First and last characters differ → no deletion
Output:
    2

Example 2:
Input:
    s = "cabaabac"
Process:
    - Ends match: 'c'
        Remove all 'c' from both ends → "abaaba"
    - Ends match: 'a'
        Remove all 'a' from both ends → "baab"
    - Ends match: 'b'
        Remove all 'b' from both ends → "aa"
    - Ends match: 'a'
        Remove all 'a' → ""
Output:
    0

Example 3:
Input:
    s = "aabccabba"
Output:
    3

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Perform deletions until:
- Ends differ OR string is empty
Return remaining length.

Pattern / Folder:
    • Pattern: Two Pointers
    • Folder suggestion:
        /TwoPointers/1750-MinimumLengthString/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

- Use two pointers:
    - `left` at start, `right` at end
- While `left < right` and `s[left] == s[right]`:
    - Let `c = s[left]`
    - Move `left` forward while `s[left] == c`
    - Move `right` backward while `s[right] == c`
- Remaining length = `(right - left) + 1`

-----------------------------------------------------------
🧠 Algorithm (Two Pointers):
-----------------------------------------------------------

1. Initialize:
       left = 0
       right = len(s) - 1

2. While left < right and s[left] == s[right]:
       c = s[left]
       while left < right and s[left] == c:
           left += 1
       while left <= right and s[right] == c:
           right -= 1

3. Return (right - left) + 1

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time Complexity:
    • O(n) → each character visited at most once
- Space Complexity:
    • O(1)

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution:
    def minimumLength(self, s: str) -> int:
        """
        LeetCode 1750. Minimum Length of String After Deleting Similar Ends
        Two-pointer solution.

        Args:
            s (str): input string

        Returns:
            int: minimum length after deletions
        """
        left, right = 0, len(s) - 1

        while left < right and s[left] == s[right]:
            c = s[left]
            # Remove all occurrences of c from the left
            while left < right and s[left] == c:
                left += 1
            # Remove all occurrences of c from the right
            while left <= right and s[right] == c:
                right -= 1

        return (right - left) + 1


# ▶️ TEST CASES
if __name__ == "__main__":
    S = Solution()

    s1 = "ca"
    print(S.minimumLength(s1))  # Expected: 2

    s2 = "cabaabac"
    print(S.minimumLength(s2))  # Expected: 0

    s3 = "aabccabba"
    print(S.minimumLength(s3))  # Expected: 3
