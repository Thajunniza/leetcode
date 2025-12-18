
"""
18. Reverse Vowels of a String

🧩 Problem:
Given a string `s`, reverse only the vowels in the string and return the resulting string.
Vowels are: a, e, i, o, u (both lowercase and uppercase).

🎯 Goal:
Swap the vowels so that their order is reversed, while all non-vowel characters remain in their original positions.

---

## Examples:

Example 1:
Input:  s = "hello"
Output: "holle"
Explanation:
Vowels are 'e' and 'o'. Reversing them yields "holle".

Example 2:
Input:  s = "leetcode"
Output: "leotcede"

Example 3:
Input:  s = "aA"
Output: "Aa"
Explanation:
Uppercase and lowercase are both treated as vowels.

Example 4:
Input:  s = ""
Output: ""

---

## Algorithm — Two Pointers:

1. Convert the string s to a list (s_list) to allow in-place swaps.

2. Maintain two pointers:
   left  = 0
   right = len(s_list) - 1

3. While left < right:
   - Move left to the right until it points at a vowel.
   - Move right to the left until it points at a vowel.
   - If left < right:
       → Swap s_list[left] and s_list[right]
       → Move both pointers inward.

4. Join the list back into a string and return.

---

⏱ Time Complexity:
* O(n) — Each character is visited at most once.

💾 Space Complexity:
* O(n) — Due to converting the string to a list (strings are immutable in Python).
* O(1) auxiliary structures.
"""

# ------------------------------------
# Reverse Vowels of a String — Two Pointers
# ------------------------------------

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")
        s_list = list(s)
        left, right = 0, len(s_list) - 1

        while left < right:
            # Move left until it hits a vowel
            while left < right and s_list[left] not in vowels:
                left += 1
            # Move right until it hits a vowel
            while left < right and s_list[right] not in vowels:
                right -= 1
            # Swap vowels
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

        return "".join(s_list)


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    s = Solution()
    print(s.reverseVowels("hello"))        # Expected: "holle"
    print(s.reverseVowels("leetcode"))     # Expected: "leotcede"
    print(s.reverseVowels("aA"))           # Expected: "Aa"
    print(s.reverseVowels(""))             # Expected: ""
    print(s.reverseVowels("bcdfg"))        # Expected: "bcdfg" (no vowels)
    print(s.reverseVowels("AEIOU"))        # Expected: "UOIEA"
    print(s.reverseVowels("Programming"))  # Expected: "Prigrammong"
    print(s.reverseVowels("Dublin"))       # Expected: "Dublin" (only one vowel 'u', no swap
