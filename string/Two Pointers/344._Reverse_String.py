""" 
===========================================================
344. Reverse String
===========================================================

🧩 Problem:
Write a function that reverses a string **in-place**.
You must modify the input array directly using O(1) extra space.

The input string is given as an array of characters `s`.

🎯 Goal:
Swap characters from both ends using TWO POINTERS until the center.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input:  s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

-----------------------------------------------------------
Algorithm — Two Pointers:
-----------------------------------------------------------
1. Set two pointers:
       left  = 0
       right = len(s) - 1

2. While left < right:
       - Swap s[left] and s[right]
       - Move pointers inward:
            left  += 1
            right -= 1

3. Modifies the input list in-place.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------

"""

# ------------------------------------
# 344. Reverse String (Two Pointers)
# ------------------------------------
from typing import List


def reverse_string(s: List[str]) -> None:
    """
    Reverse the input list of characters in-place.

    Args:
        s (List[str]): List of characters.

    Returns:
        None: The input list is modified in-place.

    Example:
        >>> arr = ["h","e","l","l","o"]
        >>> reverse_string(arr)
        >>> arr
        ['o', 'l', 'l', 'e', 'h']
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]

        # Move pointers inward
        left += 1
        right -= 1


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":

    arr1 = ["h","e","l","l","o"]
    reverse_string(arr1)
    print(arr1)     # ['o','l','l','e','h']

    arr2 = ["H","a","n","n","a","h"]
    reverse_string(arr2)
    print(arr2)     # ['h','a','n','n','a','H']
