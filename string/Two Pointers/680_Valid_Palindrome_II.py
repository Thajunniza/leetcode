"""
===========================================================
680. Valid Palindrome II
===========================================================

🧩 Problem:
Given a string s, return True if the string can become a 
palindrome after deleting **at most one character**.
Otherwise, return False.

🎯 Goal:
Allow ONE mistake in the string. If removing one character
makes it a palindrome → return True.
If no deletion helps → return False.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  "aba"
Output: True
Explanation: Already a palindrome. No deletion required.

Example 2:
Input:  "abca"
Output: True
Explanation: Remove 'b' → "aca" or remove 'c' → "aba"

Example 3:
Input:  "abc"
Output: False
Explanation: Even after deleting one character, it cannot 
             be made into a palindrome.

Example 4:
Input:  "deeee"
Output: True
Explanation: Remove 'd' → "eeee"

-----------------------------------------------------------
Algorithm — Two Pointers + One Skip:
-----------------------------------------------------------
1. Use two pointers:
       left  = 0
       right = len(s) - 1

2. While left < right:
       - If characters match → move inward.
       - If mismatch:
            → Option A: skip left char (left+1, right)
            → Option B: skip right char (left, right-1)
         Check if EITHER remaining substring is palindrome.

3. If both options fail → return False.

4. If no mismatches or fixable by one delete → return True.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""


# ------------------------------------
# Valid Palindrome II (Two Pointers)
# ------------------------------------
def is_palindrome_after_one_delete(s: str) -> bool:

    def is_pal(i: int, j: int) -> bool:
        """Check if s[i..j] is a palindrome."""
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # Try skipping left or skipping right
            return is_pal(left + 1, right) or is_pal(left, right - 1)

    return True


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":

    print(is_palindrome_after_one_delete("aba"))     # True
    print(is_palindrome_after_one_delete("abca"))    # True
    print(is_palindrome_after_one_delete("abc"))     # False
    print(is_palindrome_after_one_delete("deeee"))   # True
