"""
===========================================================
727. Minimum Window Subsequence
===========================================================

🧩 Problem:
Given two strings `s1` and `s2`, return the **minimum contiguous substring**
of `s1` such that `s2` is a **subsequence** of that substring.

If no such substring exists, return an empty string.

🎯 Goal:
Return the **shortest substring** of `s1` that contains `s2` as a subsequence.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s1 = "abcdebdde", s2 = "bde"
Output: "bcde"

Example 2:
Input:  s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
Output: ""

-----------------------------------------------------------
Algorithm — Forward Scan + Backward Shrink:
-----------------------------------------------------------

1. Scan `s1` from left to right to match `s2` as a subsequence.
2. When all of `s2` is matched (reach the end index):
   - Move backward to shrink the window as much as possible
     while still matching `s2` as a subsequence.
3. Update the minimum window.
4. Restart scanning from just after the minimized start index.
5. Repeat until the end of `s1`.

Key idea:
Find a valid window first, then **shrink it from the left** to make it minimal.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n * m)  (worst case, n = len(s1), m = len(s2))

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1)

-----------------------------------------------------------
"""
# ------------------------------------
# 727. Minimum Window Subsequence
# Forward Scan + Backward Shrink
# ------------------------------------

def minWindow(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: str
    """
    l1 = len(s1)
    l2 = len(s2)

    right = 0
    minLen = float("inf")
    result = ""
    i = 0  # pointer for s2

    while right < l1:
        if i < l2 and s1[right] == s2[i]:
            if i == l2 - 1:
                # Full subsequence matched ending at `right`
                end = right
                left = right
                j = l2 - 1  # backward pointer for s2

                # Shrink window from the right to the left
                while j >= 0:
                    if s1[left] == s2[j]:
                        j -= 1
                    left -= 1

                left += 1  # move back to first valid index

                currLen = end - left + 1
                if currLen < minLen:
                    minLen = currLen
                    result = s1[left:end + 1]

                # Restart search after the minimized start
                right = left
                i = 0
            else:
                i += 1

        right += 1

    return result


# ------------------------------------
# Driver Test
# ------------------------------------

if __name__ == "__main__":
    print(minWindow("abcdebdde", "bde"))  # Expected: "bcde"
    print(minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u"))  # Expected: ""
    print(minWindow("fgrqsqsnodwmxzkzxwqegkndaa", "kzed"))  # Expected: "kzxwqegknd"
