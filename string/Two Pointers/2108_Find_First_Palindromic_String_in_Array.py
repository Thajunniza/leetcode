"""
===========================================================
2108. Find First Palindromic String in the Array
===========================================================

🧩 Problem:
You are given an array of strings `words`.

Your task:
Return the **first palindromic string** in the array.
If none of the strings are palindromes, return an empty string `""`.

A palindrome is a string that reads the same forward and backward.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    words = ["abc","car","ada","racecar","cool"]

Checking:
    "abc"      → not palindrome  
    "car"      → not palindrome  
    "ada"      → palindrome ✅ (first one)  

Output:
    "ada"


Example 2:
Input:
    words = ["notapalindrome","racecar"]

Output:
    "racecar"


Example 3:
Input:
    words = ["def","ghi"]

Output:
    ""

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

From the given list of strings:
- Find the **first** string which is a palindrome.
- Return that string.
- If no palindrome exists, return `""`.

Pattern / Folder:
    • Pattern: Two Pointers, String
    • Folder suggestion:
        /TwoPointers/2108-FirstPalindromicString/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

A palindrome can be checked using **two pointers**:
- `p` starts from the beginning
- `q` starts from the end

While `p < q`:
- If characters mismatch → not a palindrome
- If they match → move inward

Once a mismatch occurs, break early.
If no mismatch happens, the word is a palindrome.

Scan `words` from **left to right**.
The first palindrome found is the answer.

-----------------------------------------------------------
🧠 Algorithm (Two Pointer Palindrome Check):
-----------------------------------------------------------

1. Loop over each word `s` in `words`:
       p = 0  
       q = len(s) - 1  
       is_palindrome = True

2. While p < q:
       if s[p] != s[q]:
            is_palindrome = False
            break
       p += 1
       q -= 1

3. If is_palindrome is True:
       return s   # first palindromic string

4. After checking all strings:
       return ""  # no palindrome found

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

Let:
- `n` = number of words
- `L` = maximum length of each word

- Time Complexity: **O(n · L)**  
  (Checking each string for palindrome)

- Space Complexity: **O(1)**  
  (No extra structures; only pointers)

-----------------------------------------------------------
✅ Python Solution (Two Pointers – Best for Interviews):
-----------------------------------------------------------
"""
class Solution(object):
    def firstPalindrome(self, words):
        """
        LeetCode 2108: Find First Palindromic String in the Array

        Args:
            words (List[str]): list of input strings

        Returns:
            str: first palindrome, or "" if none exist
        """
        for s in words:
            p = 0
            q = len(s) - 1
            is_palindrome = True

            # Two-pointer palindrome check
            while p < q:
                if s[p] != s[q]:
                    is_palindrome = False
                    break
                p += 1
                q -= 1

            if is_palindrome:
                return s

        return ""


# ▶️ TEST HERE
if __name__ == "__main__":
    S = Solution()

    print(S.firstPalindrome(["abc","car","ada","racecar","cool"]))  # "ada"
    print(S.firstPalindrome(["notapalindrome","racecar"]))         # "racecar"
    print(S.firstPalindrome(["def","ghi"]))                        # ""

