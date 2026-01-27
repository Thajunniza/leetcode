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
Algorithm — Recursion:
-----------------------------------------------------------


-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""


# ------------------------------------
# Valid Palindrome (Recursion)
# ------------------------------------
def is_palindrome(s: str) -> bool:

    def is_pal(l,r):
        if l > r:
            return True
        if not s[l].isalnum():
            return is_pal(l+1,r)
        if not s[r].isalnum():
            return is_pal(l,r-1)
        if s[l].lower() != s[r].lower():
            return False
        return is_pal(l+1,r-1)

    return is_pal(0,len(s)-1)


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
