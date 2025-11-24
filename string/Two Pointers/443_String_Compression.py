""" 
===========================================================
443. String Compression
===========================================================

🧩 Problem:
You are given an array of characters `chars`.

Your task:
- Compress the array **in-place** using the following rules:
    - For each group of consecutive repeating characters:
        - Keep the character
        - Append the count of repetitions (only if count > 1)
- The compressed array should be stored in the same `chars` array.
- Return the **new length** of the array after compression.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    chars = ["a","a","b","b","c","c","c"]

Process:
    - Groups:
        "aa" → "a2"
        "bb" → "b2"
        "ccc" → "c3"

    Compressed array:
        ["a","2","b","2","c","3"]

Output:
    6


Example 2:
Input:
    chars = ["a"]

Process:
    - Only one character, no compression needed.

Output:
    1

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Perform **in-place compression**:
- Use O(1) extra space
- Return the new length after compression

Pattern / Folder:
    • Pattern: Two Pointers
    • Folder suggestion:
        /TwoPointers/443-StringCompression/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

We need to:
- Traverse the array
- Identify consecutive groups of the same character
- Write the character and its count (if > 1) back into the array

Steps:
1. Use two pointers:
    - `read` → scans through the array
    - `write` → writes compressed characters back into the array

2. For each group:
    - Write the character at `write`
    - If count > 1, write each digit of count

3. Return `write` as the new length.

-----------------------------------------------------------
🧠 Algorithm (Two Pointers):
-----------------------------------------------------------

1. Initialize:
       n = len(chars)
       read = 0
       write = 0

2. While read < n:
       group_start = read
       while read < n and chars[group_start] == chars[read]:
           read += 1

       chars[write] = chars[group_start]
       write += 1

       count = read - group_start
       if count > 1:
           for digit in str(count):
               chars[write] = digit
               write += 1

3. Return write.

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time Complexity:
    • O(n) → single pass through array
- Space Complexity:
    • O(1) → in-place compression

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution:
    def compress(self, chars: list[str]) -> int:
        """
        LeetCode 443. String Compression
        In-place two-pointer solution.

        Args:
            chars (List[str]): list of characters

        Returns:
            int: new length after compression
        """
        n = len(chars)
        read = 0
        write = 0

        while read < n:
            group_start = read
            while read < n and chars[group_start] == chars[read]:
                read += 1

            chars[write] = chars[group_start]
            write += 1

            count = read - group_start
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


# ▶️ TEST HERE
if __name__ == "__main__":
    S = Solution()

    chars1 = ["a","a","b","b","c","c","c"]
    print(S.compress(chars1), chars1[:S.compress(chars1)])  # Expected: 6, ['a','2','b','2','c','3']

    chars2 = ["a"]
    print(S.compress(chars2), chars2[:S.compress(chars2)])  # Expected: 1, ['a']
