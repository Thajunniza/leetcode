"""
===========================================================
2193. Minimum Number of Moves to Make Palindrome
===========================================================

🧩 Problem:
You are given a string `s`.

In **one move**, you may swap **two adjacent characters**  
(i.e., swap `s[i]` and `s[i+1]` for some index `i`).

Your task:
    ➤ Return the **minimum number of moves** required to make `s` a **palindrome**.

Assumption:
    • It is always possible to rearrange `s` into a palindrome
      (i.e., at most one character has an odd frequency).

🎯 Goal:
Given a string `s`, compute the **minimum number of adjacent swaps**
needed so that the resulting string is a palindrome.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:
    s = "aabb"

Possible steps:
    "aabb"
    swap s[1] and s[2]  → "abab"
    swap s[2] and s[3]  → "abba"

Output:
    2

Explanation:
    The minimum number of moves is 2.

-----------------------------------------------------------

Example 2:
Input:
    s = "mamad"

One optimal sequence:
    "mamad"
    swap s[2] and s[3]  → "maamd"
    swap s[3] and s[4]  → "maadm"
    swap s[1] and s[2]  → "ammad"

Output:
    3

-----------------------------------------------------------

Example 3:
Input:
    s = "ntiin"

One optimal sequence:
    "ntiin"
    swap s[1] and s[2]  → "nitin"

Output:
    1

-----------------------------------------------------------
Algorithm — Two Pointers + Greedy Adjacent Swaps
-----------------------------------------------------------

We use a **greedy two-pointer** strategy with indices:

    i → starts at the left  (0)
    j → starts at the right (n - 1)

We work on a list representation of the string so that swaps are easier.

High-level idea:
    • Try to match characters from the **outside in**.
    • At each step, we want to match `l[i]` with a character on the
      right side, ideally `l[j]`.
    • If `l[i]` already equals `l[j]`, great — just move both pointers inward.
    • Otherwise, search from `j` downward to find a matching character
      for `l[i]`.

-----------------------------------------------------------
Phase 1 — Handle Already-Matching Ends
-----------------------------------------------------------
1. While `i < j`:
       • If `l[i] == l[j]`:
             -> We already have a matching pair at the boundaries.
             -> Move both inward:
                    i += 1
                    j -= 1
             -> Continue to next iteration.

-----------------------------------------------------------
Phase 2 — Search for a Match on the Right
-----------------------------------------------------------
2. If `l[i] != l[j]`, we search for a match for `l[i]`:

       k = j
       while k > i and l[k] != l[i]:
           k -= 1

   Cases:

   🔹 Case A: Match found (`k > i`)
       • We found `l[k] == l[i]` somewhere between `i+1` and `j`.
       • We want this matching character to be at index `j`.
       • Use adjacent swaps to "bubble" `l[k]` to position `j`:

             while k < j:
                 swap l[k] and l[k+1]
                 k += 1
                 moves += 1

       • Now `l[i]` and `l[j]` form a pair.
       • Move both pointers inward:
             i += 1
             j -= 1

   🔹 Case B: No match on the right (`k == i`)
       • This means `l[i]` appears an odd number of times and is the
         **unique middle character** of the palindrome.
       • It should end up at the middle index: `mid = n // 2`.
       • To move it from index `i` to `mid` using adjacent swaps,
         we need exactly:
                mid - i
         swaps.

       • So we add:
                moves += (n // 2) - i

       • Conceptually, we've "pushed" this char towards the center.
         We then advance only the left pointer:
                i += 1
         (We do NOT decrement `j` here, because we didn't form a pair.)

-----------------------------------------------------------
Key Details / Edge Cases
-----------------------------------------------------------
• We must distinguish between:
      - Pair formed (match found at k > i)  → move both i and j.
      - Middle char (k == i)                → move only i.

• When `l[i] == l[j]` at the start of the loop, we simply shrink
  the window since the pair is already in place.

• The algorithm relies on the fact that at most one character has
  an odd count; otherwise, forming a palindrome is impossible.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
Worst case:
    • For each i (left pointer), we may scan from j down to i → O(n)
    • Also, bubbling the matching character to j costs up to O(n)
Overall:
    ➤ O(n²)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
We store the string as a list for easier swapping:
    ➤ O(n) additional space

===========================================================
"""

# ------------------------------------
# Minimum Number of Moves to Make Palindrome
# ------------------------------------
def min_moves_to_make_palindrome(s: str) -> int:
    """
    Calculate the minimum number of adjacent swaps required
    to rearrange the string into a palindrome.

    Uses a greedy two-pointer strategy:
    - Match characters from the left and right ends.
    - If a matching character is found on the right, bubble it
      towards the right end using adjacent swaps.
    - If no match is found, then the left character is the unique
      middle character; count how many swaps it would take to move
      it to the middle.

    Args:
        s (str): Input string.

    Returns:
        int: Minimum number of adjacent swaps needed to make `s`
             a palindrome.
    """
    l = list(s)
    i = 0
    j = len(l) - 1
    moves = 0
    n = len(l)

    while i < j:
        # Case 1: ends already match → move inward
        if l[i] == l[j]:
            i += 1
            j -= 1
            continue

        # Case 2: search for a match for l[i] from the right side
        k = j
        while k > i and l[k] != l[i]:
            k -= 1

        if k == i:
            # Case B: no match on the right → this is the middle char
            l[i], l[i + 1] = l[i + 1], l[i]
            count += 1
        else:
            # Case A: found a match → bubble it to position j
            while k < j:
                l[k], l[k + 1] = l[k + 1], l[k]
                k += 1
                moves += 1
            # Now l[i] and l[j] are a pair; move both pointers
            i += 1
            j -= 1

    return moves


# ------------------------------------
# Driver Code (Optional)
# ------------------------------------
if __name__ == "__main__":
    tests = ["aabb", "mamad", "ntiin", "a", "racecar"]
    for t in tests:
        print(f"{t!r} -> {min_moves_to_make_palindrome(t)} moves")
