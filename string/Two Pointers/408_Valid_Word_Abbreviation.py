"""
===========================================================
408. Valid Word Abbreviation
===========================================================

🧩 Problem:
Given a string `word` and an abbreviation string `abbr`,
return True if `abbr` is a **valid abbreviation** of `word`.

An abbreviation replaces **non-empty**, **non-adjacent** 
substrings of the word with their **lengths**.

❗ Rules:
- Numbers cannot have **leading zeros**
- Zero-length replacement (like "0") is invalid
- Abbreviation must match the entire word exactly

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  word = "internationalization", abbr = "i18n"
Output: True
Explanation: Skip 18 characters between i and n.

Example 2:
Input:  word = "calendar", abbr = "cal3ar"
Output: True
Explanation: Skip "end" of length 3.

Example 3:
Input:  word = "calendar", abbr = "c06r"
Output: False
Explanation: Leading zero is not allowed.

Example 4:
Input:  word = "calendar", abbr = "cale0ndar"
Output: False
Explanation: Cannot replace an empty substring.

Example 5:
Input:  word = "calendar", abbr = "c24r"
Output: False
Explanation: Skip count exceeds remaining characters.

-----------------------------------------------------------
Algorithm — Two Pointers:
-----------------------------------------------------------
1. Maintain two pointers:
       p → index in `word`
       q → index in `abbr`

2. While both pointers are in range:
       - If abbr[q] is a **letter**:
            → It must match word[p]
            → Move both pointers

       - If abbr[q] is a **digit**:
            → If it's '0' → invalid (leading zero)
            → Build the full number (skip count)
            → Move p forward by `num`

3. After loop:
       - Both pointers must reach the end
         → p == len(word) and q == len(abbr)

-----------------------------------------------------------
⏱ Time Complexity:   O(n + m)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

# -----------------------------------------------
# 408. Valid Word Abbreviation (Two Pointers)
# -----------------------------------------------
def valid_word_abbreviation(word: str, abbr: str) -> bool:
    p = 0  # pointer for word
    q = 0  # pointer for abbr
    a = len(word)
    b = len(abbr)

    while p < a and q < b:

        # Case 1: abbr has a letter
        if abbr[q].isalpha():
            if word[p] != abbr[q]:
                return False
            p += 1
            q += 1

        # Case 2: abbr has digits
        else:
            # Leading zero is invalid
            if abbr[q] == "0":
                return False

            num = 0
            # Read the full number
            while q < b and abbr[q].isdigit():
                num = num * 10 + int(abbr[q])
                q += 1

            # Skip characters in `word`
            p += num

    # Both must reach the end
    return p == a and q == b


# -----------------------------------------------
# Driver Test
# -----------------------------------------------
if __name__ == "__main__":

    print(valid_word_abbreviation("internationalization", "i18n"))  # True
    print(valid_word_abbreviation("calendar", "cal3ar"))            # True
    print(valid_word_abbreviation("calendar", "c6r"))               # True
    print(valid_word_abbreviation("calendar", "c06r"))              # False
    print(valid_word_abbreviation("calendar", "cale0ndar"))         # False
    print(valid_word_abbreviation("calendar", "c24r"))              # False
