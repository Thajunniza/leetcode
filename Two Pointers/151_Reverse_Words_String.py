"""
===========================================================
151. Reverse Words in a String
===========================================================

🧩 Problem:
Given a string s, reverse the order of the words.
A word is defined as a sequence of non-space characters.

You must remove:
- Leading spaces
- Trailing spaces
- Extra spaces between words

🎯 Goal:
Return the reversed word order.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Example 1:
Input:   "the sky is blue"
Output:  "blue is sky the"

Example 2:
Input:   "  hello world  "
Output:  "world hello"

Example 3:
Input:   "a good   example"
Output:  "example good a"

-----------------------------------------------------------
Algorithm — Split + Two Pointers:
-----------------------------------------------------------
1. Use s.split() to extract words:
      - Removes extra spaces automatically
      - Produces a clean words array

2. Set two pointers:
      left  = 0
      right = len(words) - 1

3. While left < right:
      swap(words[left], words[right])
      left++, right--

4. Join reversed list using " ".join(words)

5. Return the final string.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(n)
-----------------------------------------------------------
"""


# ------------------------------------
# Reverse Words using Split + Two Pointers
# ------------------------------------
def reverse_words(s: str) -> str:
    # 1. Convert to list of words (clean)
    words = s.split()

    # 2. Two pointer swap
    left, right = 0, len(words) - 1

    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1

    # 3. Join into a sentence
    return " ".join(words)


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    s = "  hello   world  from   Thaj  "
    print("Input:  ", repr(s))
    print("Output: ", reverse_words(s))
