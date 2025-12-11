"""
===========================================================
125. Valid Palindrome
===========================================================

🧩 Problem:
Given a string s, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

🎯 Goal:
Return True if s is a valid palindrome, False otherwise.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Example 1:
Input:  "A man, a plan, a canal: Panama"
Output: True
Explanation: After removing non-alphanumeric characters,
             it becomes "amanaplanacanalpanama"

Example 2:
Input:  "race a car"
Output: False

Example 3:
Input:  " "
Output: True
Explanation: Empty or spaces-only string is considered valid.

-----------------------------------------------------------
Algorithm — Two Pointers:
-----------------------------------------------------------
1. Use two pointers:
     left  = 0
     right = len(s) - 1

2. Move left forward until it points to an alphanumeric character.
3. Move right backward until it points to an alphanumeric character.

4. Compare lowercase characters:
       if s[left] != s[right] → return False

5. Move both pointers toward the center.

6. If pointers cross, the string is a valid palindrome.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""


# ------------------------------------
# Valid Palindrome (Two Pointers)
# ------------------------------------
def is_palindrome(s: str) -> bool:

    left, right = 0, len(s) - 1

    while left < right:

        # skip non-alphanumeric characters on left
        while left < right and not s[left].isalnum():
            left += 1

        # skip non-alphanumeric characters on right
        while left < right and not s[right].isalnum():
            right -= 1

        # compare characters in lowercase
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    s3 = "   "

    print(is_palindrome(s1))  # True
    print(is_palindrome(s2))  # False
    print(is_palindrome(s3))  # True
